# 👋 COMMENCER ICI

Bienvenue! Ce fichier t'explique quoi faire en **première étape**.

---

## 🎯 Ton Objectif

**Automatiser la surveillance des logements CROUS Mende sur GitHub Actions**

- ✅ Bot s'exécute toutes les 5 minutes
- ✅ Vous recevez un email quand un logement apparaît
- ✅ Votre ordinateur peut rester éteint

---

## ⏱️ Temps: 15-20 minutes

---

## 📋 Checklist d'Installation Rapide

### ✅ ÉTAPE 1: Vérifier les Prérequis (2 min)

Assure-toi que tu as:
- [ ] Un compte GitHub
- [ ] Un compte Gmail
- [ ] Git installé sur ton ordinateur
- [ ] Python 3.8+ (ou GitHub fera tout)

### ✅ ÉTAPE 2: Préparer ton Gmail (3 min)

Tu dois créer un **App Password** pour que le bot puisse envoyer des emails.

**Pourquoi?** Gmail n'accepte plus les mots de passe simples pour les applis.

1. Allez sur: https://myaccount.google.com/apppasswords
2. Gmail te demandera de confirmer ton identité
3. Tu recevras un mot de passe de 16 caractères
4. **Copie-le quelque part** (tu en auras besoin)

⚠️ Si le lien ne fonctionne pas:
- Tu dois d'abord activer la "Vérification en deux étapes"
- Allez sur: https://myaccount.google.com/security

### ✅ ÉTAPE 3: Copier le Projet (2 min)

**Option A: Sur GitHub (Recommandé)**
1. Allez sur: https://github.com/new
2. Crée un dépôt nommé `crous-mende-bot`
3. Clone-le sur ton ordinateur: 
   ```bash
   git clone https://github.com/VotreUsername/crous-mende-bot.git
   cd crous-mende-bot
   ```

**Option B: Localement d'abord**
```bash
mkdir crous-mende-bot
cd crous-mende-bot
git init
```

### ✅ ÉTAPE 4: Copier les Fichiers (1 min)

Assure-toi que tu as ces fichiers dans ton dossier:

```
crous-mende-bot/
├── mende_bot.py              ← Script principal
├── requirements.txt          ← Dépendances
├── state.json               ← État
├── .github/
│   └── workflows/
│       └── crous.yml        ← Automation GitHub
└── [Autres fichiers README, etc]
```

**Tous ces fichiers sont déjà dans le dossier. Tu n'as rien à créer!** ✅

### ✅ ÉTAPE 5: Pousser sur GitHub (2 min)

```bash
git add .
git commit -m "🤖 Bot CROUS Mende"
git push -u origin main
```

**Important**: Si c'est la première fois, configure Git d'abord:
```bash
git config --global user.name "Ton Nom"
git config --global user.email "tonemail@gmail.com"
```

### ✅ ÉTAPE 6: Configurer les Secrets GitHub (5 min)

Les secrets sont des **variables chiffrées** que GitHub stocke de manière sûre.

1. Va sur ton dépôt: https://github.com/VotreUsername/crous-mende-bot
2. Clique sur **Settings** (Paramètres)
3. À gauche, clique sur **Secrets and variables** → **Actions**
4. Clique **New repository secret** (vert)

**Créé ces 3 secrets**:

#### Secret 1: EMAIL_USER
- Name: `EMAIL_USER`
- Secret: `votremail@gmail.com`
- Clique "Add secret"

#### Secret 2: EMAIL_PASSWORD
- Name: `EMAIL_PASSWORD`
- Secret: **Colle l'App Password de Gmail** (16 caractères)
- Clique "Add secret"

#### Secret 3: RECEIVER_EMAIL
- Name: `RECEIVER_EMAIL`
- Secret: `votremail@gmail.com` (ou autre email)
- Clique "Add secret"

### ✅ ÉTAPE 7: Tester (3 min)

1. Va sur ton dépôt GitHub
2. Clique sur l'onglet **"Actions"**
3. À gauche, clique **"Surveillance CROUS Mende"**
4. Clique le bouton **"Run workflow"** (vert)
5. Clique **"Run workflow"** (confirmez)
6. Attendez 30-60 secondes et actualise la page

**Quoi regarder**:
- 🟢 La barre devient **VERTE** = Succès! ✅
- 🔴 La barre devient **ROUGE** = Erreur ❌

**Si c'est vert**, clique pour voir les logs. Tu devrais voir:
```
[INFO] Début de la surveillance CROUS
[INFO] Résultat trouvé: 3 logements trouvés
[SUCCESS] Email envoyé à votremail@gmail.com
[INFO] Fin de la surveillance
```

### ✅ ÉTAPE 8: Vérifier les Emails (1 min)

- Regarde tes emails (y compris les spams)
- Tu devrais avoir reçu un email du bot
- Si oui: **Félicitations! Ça marche!** 🎉

---

## 🎯 Après la Configuration

Le bot:
- ✅ S'exécute **toutes les 5 minutes** automatiquement
- ✅ Envoie un **email** quand un logement apparaît
- ✅ Fonctionne même si ton PC est **éteint**
- ✅ Sauvegarde l'**état** automatiquement

---

## 📚 Documentation

Si tu besoin de plus de détails:

| Fichier | Pour Quoi? |
|---|---|
| **QUICKSTART.md** | Démarrage ultra-rapide (checklist) |
| **README.md** | Documentation complète |
| **DEPLOYMENT_GUIDE.md** | Guide détaillé pas à pas |
| **GITHUB_SECRETS_SETUP.md** | Comment configurer les secrets |
| **PROJECT_STRUCTURE.md** | Explication de la structure |

---

## 🆘 Ça ne Fonctionne Pas?

### Problème: "Paramètres email manquants"

**Cause**: Les secrets GitHub ne sont pas configurés

**Solution**:
1. Va sur: Settings → Secrets and variables → Actions
2. Vérifie que les 3 secrets existent
3. Relance le test

### Problème: "Authentication failed"

**Cause**: L'App Password est invalide

**Solution**:
1. Va sur: https://myaccount.google.com/apppasswords
2. Génère un NOUVEAU mot de passe
3. Mets à jour le secret `EMAIL_PASSWORD`
4. Re-teste

### Problème: Le workflow ne s'exécute pas

**Cause**: GitHub Actions peut être désactivé

**Solution**:
1. Va sur: Settings → Actions → General
2. Vérifie que "Allow all actions" est sélectionné
3. Attends 5-10 minutes
4. Re-teste

### Problème: Pas d'email reçu

**Cause**: Peut-être qu'aucun logement n'est apparu

**Solution**:
1. Consulte les **logs GitHub Actions**
2. Vérifie le fichier **state.json**
3. Regarde la page CROUS directement

---

## 💡 Astuce: Tester Localement

Pour vérifier que le bot fonctionne avant GitHub:

```bash
# Installe les dépendances
pip install -r requirements.txt

# Exécute le script
python test_bot.py
```

Tu devrais voir les logs s'afficher.

---

## 🎉 Félicitations!

Tu as mis en place un bot professionnel qui:
- Automatise la surveillance CROUS
- S'exécute sur le cloud (GitHub Actions)
- T'envoie des notifications par email
- Fonctionne 24h/24, 7j/7

**Prochaine étape**: Attendre les emails quand des logements apparaissent! 🏠

---

## 📞 Besoin d'Aide?

1. **Consulte les guides**: README.md, DEPLOYMENT_GUIDE.md, etc.
2. **Regarde les logs**: GitHub Actions → Actions → Cliquez sur le workflow
3. **Teste localement**: `python test_bot.py`
4. **Vérifie les secrets**: Settings → Secrets

---

## 🚀 Commencer!

Si tu es prêt(e), suis la **Checklist d'Installation Rapide** ci-dessus.

**Bon courage pour trouver un logement! 🏠**
