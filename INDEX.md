# 📇 Index Complet des Fichiers

## 🎯 Fichiers À LIRE EN PREMIER

| # | Fichier | Durée | Description |
|---|---|---|---|
| 1️⃣ | **COMMENCER.md** | 2 min | **COMMENÇE ICI!** Instructions d'installation rapide |
| 2️⃣ | **QUICKSTART.md** | 5 min | Checklist 10-15 minutes pour tout configurer |
| 3️⃣ | **DEPLOYMENT_GUIDE.md** | 10 min | Guide étape par étape complet |

---

## ⭐ Fichiers ESSENTIELS du Projet

### Code Python

| Fichier | Taille | Description |
|---|---|---|
| **mende_bot.py** | ~400 lignes | **Script principal** - Tout le logic du bot |
| **test_bot.py** | ~100 lignes | Script de test pour vérifier localement |

### Configuration

| Fichier | Description |
|---|---|
| **requirements.txt** | Dépendances Python (selenium, webdriver-manager) |
| **state.json** | État persistant des logements détectés |
| **.github/workflows/crous.yml** | Workflow GitHub Actions (exécution toutes 5 min) |

### Ignoré par Git

| Fichier | Description |
|---|---|
| **.gitignore** | Fichiers/dossiers à ignorer (venv, __pycache__, etc.) |

---

## 📖 Documentation et Guides

### Guides d'Installation

| Fichier | Pour Qui? | Durée |
|---|---|---|
| **COMMENCER.md** | 👶 Débutants complets | 10 min |
| **QUICKSTART.md** | ⚡ Gens pressés | 5 min |
| **DEPLOYMENT_GUIDE.md** | 📖 Préfère le détail | 20 min |

### Configuration

| Fichier | Pour Quoi? | Durée |
|---|---|---|
| **GITHUB_SECRETS_SETUP.md** | Configurer les secrets Gmail | 5 min |
| **PROJECT_STRUCTURE.md** | Comprendre la structure | 10 min |

### Documentation Générale

| Fichier | Pour Quoi? |
|---|---|
| **README.md** | Documentation générale complète |

---

## 🗂️ Structure Complète du Projet

```
crous-mende-bot/
│
├── 📌 COMMENCER.md                    ← COMMENCEZ ICI!
├── 📌 QUICKSTART.md                   ← Checklist 10 min
├── 📌 DEPLOYMENT_GUIDE.md             ← Guide complet
│
├── 📌 README.md                       ← Doc générale
├── 📌 GITHUB_SECRETS_SETUP.md         ← Config secrets
├── 📌 PROJECT_STRUCTURE.md            ← Structure du projet
│
├── 📄 mende_bot.py                    ← SCRIPT PRINCIPAL
├── 📄 test_bot.py                     ← Test local
├── 📄 requirements.txt                ← Dépendances
├── 📄 state.json                      ← État persistant
│
├── 📁 .github/workflows/
│   └── crous.yml                      ← GitHub Actions
│
├── .gitignore                         ← Fichiers ignorés
└── INDEX.md                           ← CE FICHIER
```

---

## 🚀 Par Cas d'Usage

### Je Suis Complètement Perdu

1. **COMMENCER.md** (5 min) - Instructions simples
2. **test_bot.py** - Teste localement
3. **QUICKSTART.md** - Checklist rapide

### Je Veux Juste le Faire Rapidement

1. **QUICKSTART.md** - Checklist 10 minutes
2. Copie les secrets GitHub
3. Teste avec le bouton "Run workflow"

### Je Veux Comprendre Complètement

1. **README.md** - Documentation générale
2. **DEPLOYMENT_GUIDE.md** - Étape par étape
3. **PROJECT_STRUCTURE.md** - Architecture
4. **mende_bot.py** - Lisez le code

### J'Ai un Problème

1. **COMMENCER.md** → Section "Ça ne fonctionne pas?"
2. **DEPLOYMENT_GUIDE.md** → Section "Troubleshooting"
3. **mende_bot.py** → Consultez les logs (print statements)
4. **test_bot.py** → Exécutez localement

---

## 📊 Flux de Travail Recommandé

### 1️⃣ LIRE (5 min)
```
COMMENCER.md
    ↓
QUICKSTART.md (optionnel)
```

### 2️⃣ TESTER (5 min)
```
python test_bot.py
```

### 3️⃣ CONFIGURER (5 min)
```
- GitHub Secrets
- GITHUB_SECRETS_SETUP.md
```

### 4️⃣ DÉPLOYER (2 min)
```
- git push
- GitHub Actions → Run workflow
```

### 5️⃣ VÉRIFIER (1 min)
```
- Vérifiez l'email
- Vérifiez state.json
- Vérifiez les logs
```

---

## 🔑 Points Clés par Fichier

### mende_bot.py
**Ce qu'il fait**:
- Accède la page CROUS
- Extrait le nombre de logements
- Compare avec l'état précédent
- Envoie un email si changement
- Sauvegarde l'état dans state.json

**Variables d'environnement utilisées**:
- `EMAIL_USER` - Votre email Gmail
- `EMAIL_PASSWORD` - App Password de Gmail
- `RECEIVER_EMAIL` - Email destinataire
- `DEBUG` - Mode verbose (optionnel)

### .github/workflows/crous.yml
**Ce qu'il fait**:
- S'exécute toutes les 5 minutes (`*/5 * * * *`)
- Configure Python 3.12
- Installe les dépendances
- Lance mende_bot.py
- Sauvegarde state.json dans le dépôt

**Vous pouvez modifier**:
- Fréquence (cron expression)
- Version Python
- Secrets utilisés

### state.json
**Format**:
```json
{
  "count": 5,                          // Nombre de logements
  "last_update": "ISO 8601 timestamp", // Quand
  "last_line": "5 logements trouvés"  // Texte trouvé
}
```

**Permet**:
- Sauvegarder l'état entre exécutions
- Détecter les changements
- Historique (optionnel)

---

## 🎯 Checklist de Vérification

Pour vérifier que tout est correctement configuré:

- [ ] Ai-je lu COMMENCER.md?
- [ ] Ai-je créé mon App Password Gmail?
- [ ] Ai-je configuré les 3 secrets GitHub?
- [ ] Ai-je testé le script localement (`python test_bot.py`)?
- [ ] Ai-je lancé le workflow depuis GitHub Actions?
- [ ] Ai-je reçu un email?

Si tout est ✅, vous êtes prêt!

---

## 📞 Ressources d'Aide

| Besoin | Fichier |
|---|---|
| Aide rapide | COMMENCER.md, QUICKSTART.md |
| Aide détaillée | DEPLOYMENT_GUIDE.md |
| Dépannage | Consultez les sections "Troubleshooting" |
| Code | Lisez mende_bot.py avec les commentaires |
| Tests | Exécutez test_bot.py |

---

## 🏁 Prêt à Commencer?

**Cliquez sur**: [COMMENCER.md](COMMENCER.md)

**Temps estimé**: 15-20 minutes pour un fonctionnement complet

**Résultat**: Bot qui s'exécute automatiquement, 24h/24, 7j/7! 🚀

---

**Bonne chance pour ton logement CROUS! 🏠**
