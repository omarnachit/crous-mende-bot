# 📚 Guide Complet des Fichiers

Ce fichier explique chaque fichier du projet et ce qu'il contient.

---

## 🔴 À LIRE AVANT TOUT

### 📄 00_LIRE_EN_PREMIER.md (Ce fichier!)

**Quoi**: Vue d'ensemble du projet  
**Pour qui**: Tous  
**Durée**: 5 minutes  
**Contient**:
- Résumé du projet
- Checklist finale
- Comment démarrer

**Quand lire**: MAINTENANT!

---

### 📄 COMMENCER.md

**Quoi**: Instructions étape par étape pour démarrer  
**Pour qui**: Débutants complets  
**Durée**: 10 minutes  
**Contient**:
- Prérequis
- Comment préparer Gmail
- 8 étapes de configuration
- Section "Ça ne fonctionne pas?"

**Quand lire**: Après 00_LIRE_EN_PREMIER.md

---

### 📄 QUICKSTART.md

**Quoi**: Checklist ultra-rapide  
**Pour qui**: Gens pressés  
**Durée**: 5 minutes  
**Contient**:
- Checklist de 10 minutes
- Tableau de troubleshooting

**Quand lire**: Si tu veux faire ça rapidement

---

## 🟠 GUIDES DE DÉPLOIEMENT

### 📄 DEPLOYMENT_GUIDE.md

**Quoi**: Guide complet étape par étape  
**Pour qui**: Préfère le détail  
**Durée**: 20 minutes  
**Contient**:
- Préparation locale
- Création du dépôt
- Copie des fichiers
- Configuration des secrets
- Test et vérification
- Troubleshooting complet

**Quand lire**: Pour une compréhension approfondie

---

### 📄 GITHUB_SECRETS_SETUP.md

**Quoi**: Comment générer et configurer les secrets Gmail  
**Pour qui**: Tous (surtout si App Password est nouveau)  
**Durée**: 10 minutes  
**Contient**:
- Comment générer l'App Password Gmail
- Comment créer les secrets GitHub
- Importance des secrets
- Réinitialisation en cas d'erreur

**Quand lire**: Quand tu configures les secrets

---

### 📄 FINAL_CHECKLIST.md

**Quoi**: Vérification complète du projet  
**Pour qui**: Avant de mettre en production  
**Durée**: 10 minutes (pour vérifier)  
**Contient**:
- 7 parts de vérification
- Check par check
- Solutions aux problèmes
- Statut final

**Quand lire**: Après le déploiement

---

## 🟡 DOCUMENTATION

### 📄 README.md

**Quoi**: Documentation générale et complète  
**Pour qui**: Ceux qui veulent tout comprendre  
**Durée**: 30 minutes  
**Contient**:
- Fonctionnalités
- Prérequis
- Structure
- Installation
- Test
- Dépannage
- Format email
- FAQ

**Quand lire**: En parallèle du déploiement

---

### 📄 INDEX.md

**Quoi**: Index complet de tous les fichiers  
**Pour qui**: Pour naviguer le projet  
**Durée**: 5 minutes  
**Contient**:
- Liste de tous les fichiers
- Par cas d'usage
- Flux de travail recommandé
- Ressources d'aide

**Quand lire**: Quand tu cherches un fichier

---

### 📄 PROJECT_STRUCTURE.md

**Quoi**: Explication de la structure du projet  
**Pour qui**: Ceux qui veulent comprendre l'architecture  
**Durée**: 10 minutes  
**Contient**:
- Vue d'ensemble de la structure
- Explication de chaque fichier/dossier
- Comment ça marche
- Variables clés
- Fichiers de débogage

**Quand lire**: Pour comprendre l'organisation

---

### 📄 LOCAL_TESTING.md

**Quoi**: Comment tester localement avant GitHub  
**Pour qui**: Ceux qui veulent vérifier avant de pusher  
**Durée**: 10 minutes  
**Contient**:
- Configuration Windows (PowerShell)
- Configuration Mac/Linux (Bash)
- Fichiers de setup
- Test complet
- Troubleshooting

**Quand lire**: Avant de mettre sur GitHub

---

### 📄 IMPROVEMENTS.md

**Quoi**: Comment améliorer le bot  
**Pour qui**: Ceux qui veulent aller plus loin  
**Durée**: 30 minutes (lecture)  
**Contient**:
- Améliorations de sécurité
- Améliorations fonctionnelles
- Optimisations
- Versions améliorées du script
- Déploiements avancés
- Métriques

**Quand lire**: Après que le bot fonctionne bien

---

## 🟢 CODE PYTHON

### 📄 mende_bot.py (Le Script Principal!)

**Quoi**: Le script qui fait tout  
**Pour qui**: Tous (à comprendre)  
**Taille**: ~300 lignes  
**Contient**:

```python
# Imports et configuration
URL = "https://..."
EMAIL_USER = os.getenv("EMAIL_USER")  # Variables d'env
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# Fonctions principales:
def load_state()           # Charge l'état précédent
def save_state(state)      # Sauvegarde l'état
def send_email()           # Envoie un email Gmail
def extract_count()        # Extrait le nombre de logements
def setup_driver()         # Initialise Selenium
def check_apartments()     # Vérifie les logements
def main()                 # Fonction principale
```

**Fonctionnement**:
1. Charge l'état précédent
2. Lance un navigateur Selenium
3. Visite la page CROUS
4. Extrait le nombre de logements
5. Compare avec le précédent
6. Si changement → envoie email
7. Sauvegarde le nouvel état
8. Ferme le navigateur

**Modification possible**:
- Changer l'URL (pour d'autres villes)
- Modifier la fréquence d'exécution
- Ajouter d'autres canaux (Telegram, etc.)

---

### 📄 test_bot.py

**Quoi**: Script de test pour vérifier le bot localement  
**Pour qui**: Avant GitHub Actions  
**Taille**: ~100 lignes  
**Contient**:

```python
# Vérifie:
✓ Les dépendances sont installées
✓ Les variables d'environnement existent
✓ Le script s'exécute sans erreur
✓ state.json est créé
✓ Les emails peuvent être envoyés
```

**Usage**:
```bash
python test_bot.py
```

---

## 🔧 CONFIGURATION

### 📄 requirements.txt

**Quoi**: Liste des dépendances Python  
**Contient**:
```
selenium==4.15.2
webdriver-manager==4.0.1
```

**Usage**:
```bash
pip install -r requirements.txt
```

**Peut être modifié pour**:
- Ajouter des packages supplémentaires
- Utiliser des versions différentes

---

### 📄 state.json

**Quoi**: Fichier d'état persistant  
**Format**:
```json
{
  "count": 5,                          // Nombre actuel
  "last_update": "ISO timestamp",      // Quand?
  "last_line": "5 logements trouvés"  // Texte trouvé
}
```

**Créé automatiquement** par le bot  
**Mis à jour** à chaque exécution  
**Sauvegardé sur GitHub** automatiquement

**Important**: Ce fichier permet au bot de déterminer s'il y a du changement!

---

### 📄 .gitignore

**Quoi**: Fichiers/dossiers à ignorer par Git  
**Contient**:
```
__pycache__/     # Fichiers Python compilés
venv/            # Environnement virtuel
.vscode/         # Configuration VS Code
.wdm/            # ChromeDriver cache
.env             # Secrets locaux
setup_env.*      # Scripts de setup
```

**Importance**: Évite de pousser des secrets ou gros fichiers

---

## 🤖 GITHUB ACTIONS

### 📄 .github/workflows/crous.yml

**Quoi**: Workflow GitHub Actions  
**Exécution**: Toutes les 5 minutes  
**Contient**:

```yaml
name: Surveillance CROUS Mende

on:
  schedule:
    - cron: '*/5 * * * *'    # Toutes les 5 min
  workflow_dispatch:         # Lancé manuellement

jobs:
  check_apartments:
    runs-on: ubuntu-latest   # Sur serveur Ubuntu
    timeout-minutes: 15
    
    steps:
      1. Récupère le code (actions/checkout)
      2. Configure Python 3.12 (actions/setup-python)
      3. Installe les dépendances (pip install)
      4. Lance le bot (python mende_bot.py)
      5. Sauvegarde l'état (git-auto-commit-action)
```

**Variables utilisées**:
- `secrets.EMAIL_USER`
- `secrets.EMAIL_PASSWORD`
- `secrets.RECEIVER_EMAIL`

**Peut être modifié pour**:
- Changer la fréquence (cron)
- Ajouter d'autres étapes
- Utiliser d'autres secrets

---

## 📊 Résumé des Fichiers

| Fichier | Type | Taille | Description |
|---|---|---|---|
| 00_LIRE_EN_PREMIER.md | 📖 Doc | 1KB | Vue d'ensemble |
| COMMENCER.md | 📖 Guide | 5KB | Instructions rapides |
| QUICKSTART.md | ⚡ Checklist | 2KB | 10 minutes |
| DEPLOYMENT_GUIDE.md | 📖 Guide | 8KB | Détaillé |
| README.md | 📖 Doc | 10KB | Complète |
| GITHUB_SECRETS_SETUP.md | 📖 Guide | 4KB | Secrets |
| FINAL_CHECKLIST.md | ✅ Checklist | 8KB | Vérification |
| PROJECT_STRUCTURE.md | 📖 Guide | 5KB | Architecture |
| LOCAL_TESTING.md | 🧪 Guide | 3KB | Tests |
| INDEX.md | 📇 Index | 4KB | Navigation |
| IMPROVEMENTS.md | 🚀 Guide | 6KB | Améliorations |
| mende_bot.py | 🐍 Code | 12KB | Script principal |
| test_bot.py | 🧪 Code | 3KB | Tests |
| requirements.txt | 📝 Config | 1KB | Dépendances |
| state.json | 📊 Données | 1KB | État |
| .gitignore | 📝 Config | 1KB | Exclusions |
| .github/workflows/crous.yml | ⚙️ Config | 1KB | GitHub Actions |

**Total**: ~80KB de documentation et code! 📚

---

## 🎯 Par Cas d'Usage

### Je Suis Débutant et Perdu

Lis dans cet ordre:
1. 00_LIRE_EN_PREMIER.md
2. COMMENCER.md
3. FINAL_CHECKLIST.md

### Je Veux Faire Ça Rapidement

Lis dans cet ordre:
1. QUICKSTART.md
2. GITHUB_SECRETS_SETUP.md
3. Saute directement à GitHub

### Je Veux Tout Comprendre

Lis dans cet ordre:
1. README.md
2. DEPLOYMENT_GUIDE.md
3. PROJECT_STRUCTURE.md
4. mende_bot.py

### Je Veux Tester Localement

Lis dans cet ordre:
1. LOCAL_TESTING.md
2. Exécute: `python test_bot.py`
3. Exécute: `python mende_bot.py`

### J'Ai un Problème

1. FINAL_CHECKLIST.md (section "Si quelque chose...")
2. README.md (section "Dépannage")
3. IMPROVEMENTS.md (section "Debugging")

### Je Veux Améliorer le Bot

1. IMPROVEMENTS.md (toute la section)
2. README.md (section "Améliorations Possibles")
3. Modifiez mende_bot.py

---

## 📞 Navigation Rapide

**Je cherche...**

- **Comment démarrer?** → COMMENCER.md
- **Instructions rapides?** → QUICKSTART.md
- **Guide détaillé?** → DEPLOYMENT_GUIDE.md
- **Configuration des secrets?** → GITHUB_SECRETS_SETUP.md
- **Documentation générale?** → README.md
- **Tests locaux?** → LOCAL_TESTING.md
- **Structure du projet?** → PROJECT_STRUCTURE.md
- **Vérification finale?** → FINAL_CHECKLIST.md
- **Améliorations?** → IMPROVEMENTS.md
- **Index complet?** → INDEX.md
- **Liste des fichiers?** → Ce fichier! (FICHIERS_EXPLIQUES.md)

---

## ✅ Checklist d'Utilisation

- [ ] J'ai lu 00_LIRE_EN_PREMIER.md
- [ ] J'ai choisi mon guide (COMMENCER, QUICKSTART, ou DEPLOYMENT)
- [ ] J'ai suivi les étapes
- [ ] J'ai testé localement (optionnel)
- [ ] J'ai configuré les secrets GitHub
- [ ] J'ai lancé le workflow
- [ ] J'ai reçu un email
- [ ] J'ai coché la FINAL_CHECKLIST.md

**Si tous les ✅ sont cochés: BOT PRÊT!** 🎉

---

**Bonne chance avec ton bot! 🚀**
