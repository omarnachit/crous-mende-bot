#!/usr/bin/env python3

import json
import os
import sys
import time
import smtplib
from datetime import datetime
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://trouverunlogement.lescrous.fr/tools/45/search?bounds=3.4287318_44.5758211_3.5534049_44.4938499&locationName=Mende+%2848000%29"
STATE_FILE = "state.json"

EMAIL_USER = os.getenv("EMAIL_USER", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"


def log_message(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")


def load_state():
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        log_message(f"Erreur lors de la lecture de {STATE_FILE}: {e}", "WARNING")
    
    return {"count": 0, "last_update": None}


def save_state(state):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
        if DEBUG:
            log_message(f"État sauvegardé: {state}")
    except Exception as e:
        log_message(f"Erreur lors de la sauvegarde de l'état: {e}", "ERROR")


def send_email(subject, body):
    if not EMAIL_USER or not EMAIL_PASSWORD or not RECEIVER_EMAIL:
        log_message(
            "Paramètres email manquants. Vérifiez les variables d'environnement.",
            "ERROR"
        )
        return False

    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "html", "utf-8"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        log_message(f"Email envoyé à {RECEIVER_EMAIL}", "SUCCESS")
        return True

    except Exception as e:
        log_message(f"Erreur lors de l'envoi de l'email: {e}", "ERROR")
        return False


def extract_count(text):
    lines = text.split("\n")
    
    for line in lines:
        line_lower = line.lower()
        if "logement" in line_lower and ("trouvé" in line_lower or "disponible" in line_lower):
            words = line.split()
            for i, word in enumerate(words):
                try:
                    num = int(word)
                    if i + 1 < len(words) and "logement" in words[i + 1].lower():
                        return num, line.strip()
                except ValueError:
                    continue
    
    return 0, None


def setup_driver():
    try:
        options = Options()
        
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
        
        if chromedriver_path and os.path.exists(chromedriver_path):
            service = Service(chromedriver_path)
            if DEBUG:
                log_message(f"Utilisation du ChromeDriver: {chromedriver_path}", "INFO")
        else:
            service = Service(ChromeDriverManager().install())
        
        driver = webdriver.Chrome(service=service, options=options)
        
        return driver
    except Exception as e:
        log_message(f"Erreur lors de l'initialisation du driver: {e}", "ERROR")
        sys.exit(1)


def check_apartments():
    driver = None
    try:
        driver = setup_driver()
        
        log_message(f"Accès à la page CROUS: {URL}")
        driver.get(URL)
        
        time.sleep(5)
        
        page_text = driver.find_element(By.TAG_NAME, "body").text
        
        count, line = extract_count(page_text)
        
        if line:
            log_message(f"Résultat trouvé: {line}")
        
        previous_state = load_state()
        previous_count = previous_state.get("count", 0)
        
        change_detected = count != previous_count
        
        new_state = {
            "count": count,
            "last_update": datetime.now().isoformat(),
            "last_line": line or ""
        }
        save_state(new_state)
        
        message = f"Logements trouvés: {count} (précédent: {previous_count})"
        
        if change_detected:
            log_message(f"🚨 Changement détecté! {message}", "ALERT")
        else:
            log_message(f"✓ Pas de changement. {message}")
        
        return count, message, change_detected
    
    except Exception as e:
        log_message(f"Erreur lors de la vérification: {e}", "ERROR")
        return None, str(e), False
    
    finally:
        if driver:
            driver.quit()


def main():
    log_message("=== Début de la surveillance CROUS ===")
    
    count, message, change_detected = check_apartments()
    
    if change_detected and count is not None:
        subject = f"🏠 Nouveau logement CROUS détecté à Mende! ({count} disponible(s))"
        
        body = f"""
        <html>
            <body style="font-family: Arial, sans-serif;">
                <h2>🚨 Alerte Logement CROUS</h2>
                <p><strong>{message}</strong></p>
                <hr>
                <h3>Détails:</h3>
                <ul>
                    <li><strong>Nombre actuel:</strong> {count}</li>
                    <li><strong>Heure:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</li>
                    <li><strong>Localisation:</strong> Mende (48000)</li>
                </ul>
                <hr>
                <h3>Consulter les logements:</h3>
                <p><a href="{URL}">Cliquez ici pour voir les logements disponibles</a></p>
                <hr>
                <p style="color: #666; font-size: 12px;">
                    Email automatique - Bot CROUS Mende
                </p>
            </body>
        </html>
        """
        
        send_email(subject, body)
    
    log_message("=== Fin de la surveillance ===\n")


if __name__ == "__main__":
    main()
