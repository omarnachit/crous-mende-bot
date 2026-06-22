# 📖 Guide Complet du Déploiement - Pas à Pas

Ce guide vous accompagne du début à la fin pour mettre en place le bot CROUS sur GitHub Actions.

## 🎯 Objectif Final

- ✅ Bot qui s'exécute automatiquement toutes les 5 minutes sur GitHub Actions
- ✅ Vous recevez un email quand un nouveau logement CROUS apparaît
- ✅ Votre ordinateur peut rester éteint

## ⏱️ Temps Estimé: 15 minutes

---

## 📝 Préparation (5 min)

### ✅ Liste de Contrôle

- [ ] J'ai un compte GitHub
- [ ] J'ai un compte Gmail
- [ ] J'ai accès à mon Gmail App Password (ou sais comment le générer)
- [ ] J'ai Git installé sur mon ordinateur

### 📋 Informations à Préparer

Avant de commencer, rassemblez ces informations:

1. **Adresse Gmail**: `votremail@gmail.com`
2. **App Password**: Copiez-le depuis https://myaccount.google.com/apppasswords
3. **URL du dépôt GitHub**: `https://github.com/votreusername/crous-mende-bot`

---

## 🚀 Déploiement Étape par Étape

### ÉTAPE 1: Créer ou Préparer le Dépôt GitHub (2 min)

#### Option A: Créer un NOUVEAU dépôt

1. Allez sur: **https://github.com/new**
2. Remplissez:
   - **Repository name**: `crous-mende-bot`
   - **Description**: `Bot de surveillance des logements CROUS Mende`
   - **Visibility**: `Public` (ou Private, comme vous préférez)
3. Cliquez **"Create repository"**
4. Vous êtes redirigé vers la page du dépôt vide

#### Option B: Utiliser un dépôt EXISTANT

- Allez juste sur votre dépôt existant

### ÉTAPE 2: Préparer les Fichiers Localement (3 min)

Créez un dossier sur votre ordinateur:

```bash
# Créez le dossier
mkdir crous-mende-bot
cd crous-mende-bot

# Initialisez Git
git init
git branch -M main
```

### ÉTAPE 3: Ajouter les Fichiers du Projet (1 min)

Créez ces fichiers dans le dossier:

**1. requirements.txt**
```
selenium==4.15.2
webdriver-manager==4.0.1
```

**2. state.json**
```json
{
  "count": 0,
  "last_update": null,
  "last_line": ""
}
```

**3. Créez le dossier** `.github/workflows/`

**4. Créez** `.github/workflows/crous.yml`
(Voir le contenu plus bas)

**5. mende_bot.py**
(Voir le contenu plus bas)

### ÉTAPE 4: Créer le Workflow GitHub Actions (2 min)

Créez le fichier `.github/workflows/crous.yml`:

```yaml
name: Surveillance CROUS Mende

on:
  schedule:
    - cron: '*/5 * * * *'
  workflow_dispatch:

jobs:
  check_apartments:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Récupérer le code
        uses: actions/checkout@v4

      - name: Configurer Python 3.12
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Installer les dépendances
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Vérifier les logements CROUS
        env:
          EMAIL_USER: ${{ secrets.EMAIL_USER }}
          EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
          RECEIVER_EMAIL: ${{ secrets.RECEIVER_EMAIL }}
          DEBUG: 'false'
        run: python mende_bot.py

      - name: Sauvegarder l'état
        if: always()
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "📊 Mise à jour de l'état CROUS"
          file_pattern: state.json
          commit_options: '--no-verify'
```

### ÉTAPE 5: Pousser le Code sur GitHub (2 min)

```bash
# Ajouter l'origin (remplacez par votre URL)
git remote add origin https://github.com/VotreUsername/crous-mende-bot.git

# Commiter et pousser
git add .
git commit -m "🤖 Initial: Bot CROUS Mende"
git push -u origin main
```

### ÉTAPE 6: Configurer les Secrets GitHub (3 min)

1. Allez sur: **https://github.com/VotreUsername/crous-mende-bot/settings/secrets/actions**

2. Créez 3 secrets:

   **Secret 1: EMAIL_USER**
   - Name: `EMAIL_USER`
   - Secret: `votremail@gmail.com`
   - Cliquez "Add secret"

   **Secret 2: EMAIL_PASSWORD**
   - Name: `EMAIL_PASSWORD`
   - Secret: Votre App Password Gmail (16 caractères avec espaces)
   - Cliquez "Add secret"

   **Secret 3: RECEIVER_EMAIL**
   - Name: `RECEIVER_EMAIL`
   - Secret: `votremail@gmail.com` (ou autre email)
   - Cliquez "Add secret"

### ÉTAPE 7: Tester le Workflow (2 min)

1. Allez sur votre dépôt GitHub
2. Cliquez sur l'onglet **"Actions"**
3. Sur la gauche, cliquez **"Surveillance CROUS Mende"**
4. Cliquez le bouton **"Run workflow"** → **"Run workflow"**
5. Attendez 30 secondes et actualisez la page

**Vous devriez voir**:
- ✅ Exécution en cours (ronde jaune puis verte)
- ✅ Aucune erreur rouge

Si tout est vert ✅, c'est bon! Le bot fonctionne!

### ÉTAPE 8: Vérifier les Logs (1 min)

1. Dans "Actions", cliquez sur l'exécution qui vient de se terminer
2. Cliquez sur **"Vérifier les logements CROUS"**
3. Vous verrez:
   ```
   [2024-06-22 14:30:45] [INFO] Début de la surveillance CROUS
   [2024-06-22 14:30:50] [INFO] Résultat trouvé: 3 logements trouvés
   [2024-06-22 14:30:50] [INFO] État sauvegardé...
   [2024-06-22 14:30:50] [SUCCESS] Email envoyé à votremail@gmail.com
   ```

---

## 🧪 Test Complet (Optionnel)

Pour tester localement avant GitHub Actions:

```bash
# Installez les dépendances
pip install -r requirements.txt

# Testez le script
python mende_bot.py

# Vérifiez que state.json a été créé/mis à jour
cat state.json
```

---

## 🔍 Maintenant Quoi?

### Les 5 Prochaines Minutes

Le bot va:
1. S'exécuter toutes les 5 minutes automatiquement
2. Vérifier la page CROUS
3. Vous envoyer un email si un nouveau logement apparaît
4. Mettre à jour `state.json` dans le dépôt

### Vérifier que Ça Fonctionne

1. Allez sur: https://github.com/VotreUsername/crous-mende-bot/actions
2. Vous verrez les exécutions s'ajouter toutes les 5 minutes
3. Les logs doivent être verts (✅)

### Si Vous Recevez un Email

🎉 **Félicitations!** Le bot fonctionne complètement!

---

## ⚠️ Troubleshooting

### Problème 1: "Paramètres email manquants"

**Cause**: Les secrets ne sont pas configurés

**Solution**:
1. Allez sur Settings → Secrets and variables → Actions
2. Vérifiez les 3 secrets existent
3. Attendez 1-2 minutes et relancez le workflow

### Problème 2: "Authentication failed for SMTP"

**Cause**: App Password invalide

**Solution**:
1. Allez sur https://myaccount.google.com/apppasswords
2. Générez un nouveau App Password
3. Mettez à jour le secret `EMAIL_PASSWORD`
4. Relancez le workflow

### Problème 3: Le workflow n'apparaît pas

**Cause**: Actions désactivées

**Solution**:
1. Allez sur Settings → Actions → General
2. Sélectionnez "Allow all actions and reusable workflows"
3. Allez sur l'onglet Actions et vérifiez

### Problème 4: Pas de changements détectés

**Cause**: La page CROUS change ou le texte est différent

**Solution**:
1. Consultez la page CROUS manuellement
2. Exécutez le script localement
3. Vérifiez `state.json` pour voir quel texte a été trouvé
4. Modifiez la fonction `extract_count()` si nécessaire

---

## 📊 Résumé Final

✅ **Structure créée**:
- `mende_bot.py` - Script principal
- `requirements.txt` - Dépendances
- `state.json` - État persistant
- `.github/workflows/crous.yml` - Workflow GitHub Actions

✅ **Configuration faite**:
- 3 secrets GitHub créés
- Workflow déployé
- Premier test réussi

✅ **Maintenant**:
- Le bot s'exécute toutes les 5 minutes
- Emails envoyés automatiquement
- Votre PC peut rester éteint

🎉 **Vous êtes prêt!**

---

## 📞 Besoin d'aide?

- Consultez le `README.md` pour plus de détails
- Vérifiez les logs GitHub Actions (onglet Actions)
- Testez localement avec `python mende_bot.py`

**Bon courage pour trouver un logement! 🏠**
