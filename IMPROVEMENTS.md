# 🚀 Améliorations et Bonnes Pratiques

Ce fichier explique comment améliorer le bot et les meilleures pratiques de sécurité.

---

## 🔒 Sécurité

### ✅ Déjà Implément

- ✅ Pas de secrets en dur dans le code
- ✅ Utilisation de GitHub Secrets (chiffré)
- ✅ App Password à la place du mot de passe Gmail
- ✅ Mode headless (pas de fenêtre)

### 🆙 À Ajouter (Optionnel)

#### 1. Utiliser un Fichier .env Local

Créez un fichier `.env` pour les tests locaux:

```env
EMAIL_USER=votremail@gmail.com
EMAIL_PASSWORD=votre_app_password
RECEIVER_EMAIL=votremail@gmail.com
DEBUG=true
```

Installation de python-dotenv:
```bash
pip install python-dotenv
```

Utilisation dans mende_bot.py:
```python
from dotenv import load_dotenv
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER", "")
```

#### 2. Rotation des App Passwords

- Générez un nouvel App Password tous les 3-6 mois
- Mettez à jour le secret GitHub
- Révoquedez l'ancien (optionnel)

#### 3. Validation des Entrées

Ajouter une validation avant d'envoyer les emails:
```python
if not validate_email(RECEIVER_EMAIL):
    print("Email invalide!")
    sys.exit(1)
```

---

## 📊 Améliorations Fonctionnelles

### 1. Historique des Logements

**Idée**: Garder un historique pour voir les tendances

```json
{
  "count": 5,
  "history": [
    {"count": 3, "timestamp": "2024-06-22T10:00:00"},
    {"count": 3, "timestamp": "2024-06-22T10:05:00"},
    {"count": 4, "timestamp": "2024-06-22T10:10:00"},
    {"count": 5, "timestamp": "2024-06-22T10:15:00"}
  ]
}
```

### 2. Email Résumé Quotidien

**Idée**: Recevoir un email résumé chaque matin

```yaml
# Ajouter au workflow crous.yml
- cron: '0 9 * * *'  # 9h du matin chaque jour
```

### 3. Alertes Multi-Canaux

**Ajouter Telegram, Discord, SMS**:

```bash
pip install python-telegram-bot
pip install discord.py
pip install twilio
```

### 4. Dashboard Web

**Idée**: Voir l'historique en ligne

```
https://votresite.com/crous
- Graphique du nombre de logements
- Historique complet
- Notifications reçues
```

### 5. Augmentation du Seuil d'Alerte

**Ne alerter que si +2 logements**:

```python
ALERT_THRESHOLD = 2

if count >= previous_count + ALERT_THRESHOLD:
    send_email(...)
```

---

## ⏱️ Optimisations de Performance

### 1. Réduire la Fréquence

**Actuellement**: Toutes les 5 minutes

**Options**:
- Toutes les 10 minutes (moins de requêtes)
- Toutes les heures (économise les ressources)
- Seulement les jours de classe (lun-ven 8h-18h)

**Modifier dans `.github/workflows/crous.yml`**:
```yaml
cron: '0 8-18 * * 1-5'  # Lun-ven, 8h-18h
```

### 2. Timeout Court

**Actuellement**: 15 minutes timeout

**Réduire à 5 minutes**:
```yaml
jobs:
  check_apartments:
    timeout-minutes: 5
```

### 3. Cache des Dépendances

**Déjà activé** dans le workflow:
```yaml
cache: 'pip'
```

---

## 🐛 Debugging Avancé

### 1. Logs Structurés

Utiliser JSON pour les logs:
```python
import json
log = {
    "timestamp": datetime.now().isoformat(),
    "level": "INFO",
    "message": "Script démarré",
    "count": 5
}
print(json.dumps(log))
```

### 2. Envoi des Erreurs par Email

```python
try:
    # Code principal
except Exception as e:
    send_error_email(e)
```

### 3. Monitoring Avancé

Ajouter un log centralisé:
```python
import logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

---

## 🔄 Versions Améliorées du Script

### Version 2: Avec Historique

```python
def load_state():
    state = load_state()
    if "history" not in state:
        state["history"] = []
    
    # Ajouter à l'historique
    state["history"].append({
        "count": count,
        "timestamp": datetime.now().isoformat()
    })
    
    # Garder seulement les 100 dernières entrées
    if len(state["history"]) > 100:
        state["history"] = state["history"][-100:]
    
    save_state(state)
```

### Version 3: Avec Retry Logic

```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def check_apartments():
    # Code principal avec retry automatique
    pass
```

---

## 🚀 Déploiements Avancés

### 1. Plusieurs Villes

```python
CITIES = [
    {"name": "Mende", "url": "https://..."},
    {"name": "Clermont", "url": "https://..."},
    {"name": "Le Puy", "url": "https://..."}
]

for city in CITIES:
    check_apartments(city)
```

### 2. Déploiement sur Heroku

```bash
# Créer une app Heroku
heroku create mon-crous-bot

# Ajouter les secrets
heroku config:set EMAIL_USER="..."
heroku config:set EMAIL_PASSWORD="..."

# Deployer
git push heroku main
```

### 3. Déploiement AWS Lambda

```python
def lambda_handler(event, context):
    main()
    return {"statusCode": 200}
```

---

## 📈 Métriques et Analytics

### 1. Compter les Notifications Envoyées

```python
def save_metric(metric_type, value):
    metrics = load_metrics()
    metrics.append({
        "type": metric_type,
        "value": value,
        "timestamp": datetime.now().isoformat()
    })
    save_metrics(metrics)
```

### 2. Analyser les Tendances

```python
# Quel jour/heure les logements apparaissent?
# Combien en moyenne par jour?
# Taux de turnover?
```

---

## 💰 Économies de Coûts

### GitHub Actions: Gratuit pour les Repos Publics ✅

- ✅ 2000 minutes/mois gratuit (perso)
- ✅ Exécutions illimitées pour repos publics
- ✅ Aucun coût si < 2000 min/mois

### Si Vous Dépassez

- Réduire la fréquence (moins souvent)
- Utiliser des conditions (if logements > 0)
- Archiver le projet (si pas utilisé)

**Calcul**: 5 min × 288/jour = 1440 min/mois ✅ Gratuit

---

## ✅ Checklist d'Optimisation

- [ ] Mon bot s'exécute correctement?
- [ ] Reçois-je les emails?
- [ ] Je veux ajouter un historique?
- [ ] Je veux réduire la fréquence?
- [ ] Je veux ajouter d'autres canaux (Telegram, Discord)?
- [ ] Je veux monitorer les performances?

---

## 📚 Ressources Supplémentaires

### Selenium
- https://www.selenium.dev/documentation/
- https://www.selenium.dev/webdriver/

### GitHub Actions
- https://docs.github.com/en/actions
- https://crontab.guru/ (Cron expressions)

### Email/SMTP
- https://support.google.com/accounts/answer/185833 (App Passwords)
- https://docs.python.org/3/library/smtplib.html

### Alerting
- https://telegram.org/blog/bot-revolution (Telegram)
- https://discord.com/developers (Discord)

---

## 🎓 Concepts À Apprendre

1. **Selenium**: Web scraping
2. **GitHub Actions**: CI/CD
3. **JSON**: Stockage de données
4. **SMTP**: Envoi d'emails
5. **Cron**: Scheduling
6. **Environment Variables**: Secrets

---

## 🎯 Prochaines Étapes

1. ✅ Faites fonctionner la version de base
2. 🔄 Testez pendant 1-2 semaines
3. 📈 Ajoutez l'historique
4. 📢 Ajoutez d'autres canaux
5. 📊 Analysez les données

---

**Continuez à améliorer votre bot! 🚀**
