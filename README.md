# 🏠 Bot de Surveillance CROUS Mende

Script Python automatisé pour surveiller les logements CROUS à Mende (48000) et recevoir une alerte email lorsqu'un nouveau logement devient disponible.

## 📋 Fonctionnalités

✅ Surveille automatiquement la page CROUS toutes les 5 minutes  
✅ Exécution entièrement sur GitHub Actions (PC peut être éteint)  
✅ Envoie un email Gmail lors de la détection d'un nouveau logement  
✅ Sauvegarde l'état dans un fichier JSON  
✅ Gestion robuste des erreurs  
✅ Mode headless compatible avec GitHub Actions  

## 🛠️ Prérequis

- ✅ Compte GitHub avec dépôt
- ✅ Compte Gmail avec **App Password** généré
- ✅ Python 3.12+ (local) ou GitHub Actions (cloud)

## 📁 Structure du Projet

```
bot/
├── mende_bot.py              # Script principal
├── requirements.txt          # Dépendances Python
├── state.json               # État persistant des logements
├── .github/
│   └── workflows/
│       └── crous.yml        # Workflow GitHub Actions
└── README.md               # Ce fichier
```

## 🚀 Installation et Déploiement

### Étape 1: Cloner ou créer le dépôt GitHub

```bash
# Option A: Créer un nouveau dépôt (via GitHub web)
# 1. Allez sur https://github.com/new
# 2. Nommez-le "crous-mende-bot" (ou autre)
# 3. Créez le dépôt

# Option B: Cloner un dépôt existant
git clone https://github.com/VotreUsername/crous-mende-bot.git
cd crous-mende-bot
```

### Étape 2: Obtenir un Gmail App Password

Gmail n'accepte plus les mots de passe simples pour les applications tiers. Vous devez créer un "App Password":

1. **Allez sur**: https://myaccount.google.com/apppasswords
   - Si ce lien ne fonctionne pas, il faut d'abord activer la **Vérification en deux étapes**
   
2. **Créer une vérification en deux étapes** (si nécessaire):
   - Allez sur: https://myaccount.google.com/security
   - Cliquez sur "Vérification en deux étapes"
   - Suivez les instructions

3. **Créer un App Password**:
   - Retournez sur https://myaccount.google.com/apppasswords
   - Sélectionnez: App = "Courrier" | Appareil = "Windows (ou autre)"
   - Google génère un mot de passe de 16 caractères
   - **Copiez-le quelque part** (vous en aurez besoin)

### Étape 3: Configurer les GitHub Secrets

Les secrets sont des variables chiffrées stockées de manière sécurisée sur GitHub.

1. **Allez sur votre dépôt GitHub**: https://github.com/VotreUsername/crous-mende-bot
2. **Cliquez sur**: Settings → Secrets and variables → Actions
3. **Créez 3 secrets**:

| Nom du Secret | Valeur | Exemple |
|---|---|---|
| `EMAIL_USER` | Votre adresse Gmail | `votremail@gmail.com` |
| `EMAIL_PASSWORD` | App Password généré (pas le mot de passe Gmail) | `abcd efgh ijkl mnop` |
| `RECEIVER_EMAIL` | Email où recevoir les alertes | `votremail@gmail.com` |

**Comment créer un secret:**
- Cliquez sur "New repository secret"
- Nom: `EMAIL_USER`
- Valeur: `votremail@gmail.com`
- Cliquez "Add secret"
- Répétez pour les 2 autres

### Étape 4: Pousser le code sur GitHub

```bash
# Depuis le dossier du projet
git add .
git commit -m "🤖 Initial commit: Bot CROUS"
git push origin main
```

### Étape 5: Activer GitHub Actions

1. Allez sur votre dépôt
2. Cliquez sur l'onglet "Actions"
3. Cliquez sur "Surveillance CROUS Mende"
4. Cliquez "Enable workflow" (si nécessaire)

## 🧪 Test Local

Pour tester le script avant de le mettre sur GitHub Actions:

```bash
# 1. Installez les dépendances
pip install -r requirements.txt

# 2. Exécutez le script
python mende_bot.py

# 3. Vérifiez que state.json a été créé/mis à jour
cat state.json
```

### Test avec des emails

Pour tester l'envoi d'emails en local:

```bash
# Exécutez avec les variables d'environnement
set EMAIL_USER=votre_email@gmail.com
set EMAIL_PASSWORD=votre_app_password
set RECEIVER_EMAIL=votre_email@gmail.com
python mende_bot.py
```

## 📊 Comment ça fonctionne

### Workflow GitHub Actions

1. **Planification**: Le workflow s'exécute toutes les 5 minutes (cron)
2. **Récupération**: GitHub Actions clone votre dépôt
3. **Installation**: Les dépendances Python sont installées
4. **Exécution**: Le script `mende_bot.py` démarre
5. **Détection**: Le script visite la page CROUS et compte les logements
6. **Comparaison**: Compare avec l'état précédent (state.json)
7. **Email**: Si le nombre augmente, envoie un email
8. **Sauvegarde**: Mets à jour state.json dans le dépôt

### Fichier state.json

```json
{
  "count": 5,
  "last_update": "2024-06-22T14:30:45.123456",
  "last_line": "5 logements trouvés"
}
```

## 🔍 Surveillance de l'exécution

1. Allez sur votre dépôt GitHub
2. Cliquez sur "Actions"
3. Vous verrez les exécutions listées
4. Cliquez sur une exécution pour voir les logs

**Logs utiles à chercher**:
- ✅ `Email envoyé à` = Email envoyé avec succès
- ⚠️ `Changement détecté` = Nouveau logement trouvé
- ❌ `Erreur lors de l'envoi de l'email` = Problème avec les identifiants

## 🐛 Dépannage

### "Paramètres email manquants"

**Cause**: Les secrets GitHub ne sont pas configurés correctement

**Solution**:
1. Allez sur Settings → Secrets and variables → Actions
2. Vérifiez que vous avez exactement:
   - `EMAIL_USER`
   - `EMAIL_PASSWORD`
   - `RECEIVER_EMAIL`
3. Vérifiez la valeur du `EMAIL_PASSWORD` (App Password, pas le mot de passe Gmail)

### "Authentication failed for SMTP"

**Cause**: App Password incorrect ou Gmail pas bien configuré

**Solution**:
1. Générez un nouveau App Password sur https://myaccount.google.com/apppasswords
2. Copiez le nouveau mot de passe (16 caractères)
3. Mettez à jour le secret `EMAIL_PASSWORD` sur GitHub
4. Re-testez

### Le workflow n'exécute pas automatiquement

**Cause**: Les workflows GitHub Actions peuvent être désactivés

**Solution**:
1. Allez sur Settings → Actions → General
2. Vérifiez que "Allow all actions and reusable workflows" est sélectionné
3. Allez sur l'onglet "Actions" et vérifiez le workflow

### Pas de changements détectés même avec de nouveaux logements

**Cause**: La sélection du texte sur la page pourrait être différente

**Solution**:
1. Exécutez le script localement: `python mende_bot.py`
2. Ouvrez `state.json` et vérifiez la valeur de `last_line`
3. Consultez la page CROUS pour voir le texte exact
4. Modifiez la fonction `extract_count()` si nécessaire

## 📧 Format de l'Email

Quand un nouveau logement est détecté, vous recevez un email comme celui-ci:

```
Sujet: 🏠 Nouveau logement CROUS détecté à Mende! (5 disponible(s))

Corps:
- Alerte Logement CROUS
- Nombre actuel: 5
- Heure: 2024-06-22 14:30:45
- Localisation: Mende (48000)
- Lien direct vers la page CROUS
```

## ⏰ Fréquence de vérification

Par défaut, le script vérifie **toutes les 5 minutes**. Pour changer cela:

1. Ouvrez `.github/workflows/crous.yml`
2. Trouvez la ligne: `- cron: '*/5 * * * *'`
3. Modifiez le nombre (en minutes):
   - `*/5` = Toutes les 5 minutes
   - `*/10` = Toutes les 10 minutes
   - `0 */1 * * *` = Toutes les heures
4. Commitez et poussez les changements

## 📝 Variables d'Environnement

| Variable | Description | Défaut |
|---|---|---|
| `EMAIL_USER` | Adresse Gmail (secret) | Vide |
| `EMAIL_PASSWORD` | App Password (secret) | Vide |
| `RECEIVER_EMAIL` | Email destinataire (secret) | Vide |
| `DEBUG` | Affiche les logs détaillés | `false` |

## 🔒 Sécurité

- ✅ Les mots de passe sont stockés dans GitHub Secrets (chiffrés)
- ✅ Les App Passwords de Gmail peuvent être révoqués à tout moment
- ✅ Le code source ne contient aucun secret en dur
- ✅ Les logs GitHub ne contiennent pas les secrets

## 📄 Licence

Ce projet est fourni tel quel. Libre d'utilisation.

## 💡 Améliorations Possibles

- Ajouter des alertes Telegram/Discord
- Envoyer un email résumé quotidien
- Sauvegarder l'historique des logements
- Intégrer avec d'autres sites CROUS
- Créer une interface web de monitoring

---

**Besoin d'aide?** Consultez les logs GitHub Actions ou les erreurs affichées lors de l'exécution locale.

**Bon courage dans ta recherche de logement! 🏠**
