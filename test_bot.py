#!/usr/bin/env python3
"""
Script de test local - Utile pour vérifier que le bot fonctionne avant GitHub Actions
Utilisation:
    python test_bot.py
    
Vous pouvez aussi définir les variables d'environnement:
    set EMAIL_USER=votre_email@gmail.com
    set EMAIL_PASSWORD=votre_app_password
    set RECEIVER_EMAIL=votre_email@gmail.com
    python test_bot.py
"""

import os
import sys

def main():
    print("\n" + "="*60)
    print("🧪 TEST DU BOT CROUS MENDE")
    print("="*60 + "\n")
    
    # Vérifier les dépendances
    print("1️⃣  Vérification des dépendances...")
    try:
        import selenium
        import webdriver_manager
        print("   ✅ Selenium et webdriver-manager importés")
    except ImportError as e:
        print(f"   ❌ Erreur: {e}")
        print("\n   Solution: Installez les dépendances")
        print("   >> pip install -r requirements.txt\n")
        sys.exit(1)
    
    # Vérifier les variables d'environnement
    print("\n2️⃣  Vérification des variables d'environnement...")
    email_user = os.getenv("EMAIL_USER", "")
    email_password = os.getenv("EMAIL_PASSWORD", "")
    receiver_email = os.getenv("RECEIVER_EMAIL", "")
    
    if email_user:
        print(f"   ✅ EMAIL_USER défini: {email_user}")
    else:
        print("   ⚠️  EMAIL_USER non défini (emails ne seront pas envoyés)")
    
    if email_password:
        print(f"   ✅ EMAIL_PASSWORD défini: {'*' * 16}")
    else:
        print("   ⚠️  EMAIL_PASSWORD non défini (emails ne seront pas envoyés)")
    
    if receiver_email:
        print(f"   ✅ RECEIVER_EMAIL défini: {receiver_email}")
    else:
        print("   ⚠️  RECEIVER_EMAIL non défini (emails ne seront pas envoyés)")
    
    # Lancer le bot
    print("\n3️⃣  Exécution du bot...")
    print("   Patience, cela peut prendre 10-20 secondes...\n")
    
    try:
        # Importer et lancer le bot
        from mende_bot import main
        main()
    except Exception as e:
        print(f"\n   ❌ Erreur lors de l'exécution: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n" + "="*60)
    print("✅ TEST TERMINÉ")
    print("="*60 + "\n")
    
    print("📊 Vérifiez state.json pour voir l'état actuel:")
    try:
        import json
        with open("state.json", "r") as f:
            state = json.load(f)
        print(f"   - Logements détectés: {state.get('count', 0)}")
        print(f"   - Dernière mise à jour: {state.get('last_update', 'N/A')}")
        print(f"   - Dernier texte: {state.get('last_line', 'N/A')}")
    except:
        print("   ❌ state.json non trouvé")
    
    print("\n💡 Prochain pas:")
    print("   1. Consultez le README.md pour la configuration complète")
    print("   2. Mettez à jour les secrets GitHub")
    print("   3. Le bot s'exécutera ensuite toutes les 5 minutes\n")

if __name__ == "__main__":
    main()
