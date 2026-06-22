# 📁 Structure du Projet - Vue d'Ensemble

```
crous-mende-bot/
│
├── 📄 mende_bot.py                    ⭐ SCRIPT PRINCIPAL
│   └── Script Python qui:
│       - Visite la page CROUS
│       - Détecte les logements
│       - Envoie les emails
│       - Sauvegarde l'état
│
├── 📄 requirements.txt                ⭐ DÉPENDANCES
│   └── Liste des packages Python
│       (selenium, webdriver-manager)
│
├── 📄 state.json                      ⭐ ÉTAT PERSISTANT
│   └── Conserve:
│       - Nombre de logements
│       - Dernière mise à jour
│       - Dernier texte détecté
│
├── .github/
│   └── workflows/
│       └── 📄 crous.yml               ⭐ WORKFLOW GITHUB ACTIONS
│           └── Configure:
│               - Exécution toutes les 5 min
│               - Installation Python
│               - Envoi des emails
│               - Sauvegarde de l'état
│
├── 📄 README.md                       📖 DOCUMENTATION COMPLÈTE
│   └── Guide complet du projet
│
├── 📄 DEPLOYMENT_GUIDE.md             🚀 GUIDE PAS À PAS
│   └── Instructions détaillées du déploiement
│
├── 📄 GITHUB_SECRETS_SETUP.md         🔐 CONFIG DES SECRETS
│   └── Comment configurer GitHub Secrets
│
├── 📄 QUICKSTART.md                   ⚡ DÉMARRAGE RAPIDE
│   └── Checklist 10 minutes
│
├── 📄 test_bot.py                     🧪 SCRIPT DE TEST
│   └── Pour tester localement
│
├── 📄 .gitignore                      🚫 EXCLUSIONS GIT
│   └── Fichiers à ignorer
│
└── 📄 PROJECT_STRUCTURE.md            📋 CE FICHIER
    └── Vue d'ensemble du projet
```

---

## 🎯 Fichiers Essentiels

### ⭐ À Créer/Configurer ABSOLUMENT

1. **mende_bot.py** - Le cœur du projet
2. **requirements.txt** - Dépendances
3. **.github/workflows/crous.yml** - Automation
4. **state.json** - État initial

### 📖 À Lire

1. **README.md** - Avant de commencer
2. **DEPLOYMENT_GUIDE.md** - Pour le déploiement
3. **GITHUB_SECRETS_SETUP.md** - Pour les secrets

### ⚡ Pour Aller Vite

- **QUICKSTART.md** - 10 minutes pour tout configurer

### 🧪 Pour Tester

- **test_bot.py** - Vérifiez que ça marche localement

---

## 🚀 Ordre des Étapes

### 1. **Préparation Locale** (5 min)
   - Clonez ou créez le dépôt
   - Copiez les fichiers essentiels
   - Testez localement: `python test_bot.py`

### 2. **Configuration GitHub** (3 min)
   - Poussez le code
   - Configurez les 3 secrets

### 3. **Déploiement** (1 min)
   - Lancez le workflow manuellement
   - Vérifiez que ça fonctionne

### 4. **Automatisation** (Ensuite)
   - Le workflow s'exécute toutes les 5 minutes
   - Vous recevez les emails

---

## 📊 Comment Ça Marche

```
┌─────────────────────────────────────────────────────────┐
│ GitHub Actions (toutes les 5 minutes)                  │
├─────────────────────────────────────────────────────────┤
│ 1. Clone le dépôt                                       │
│ 2. Installe les dépendances (pip install)              │
│ 3. Lance: python mende_bot.py                          │
│    ├─ Accès à la page CROUS                            │
│    ├─ Extrait le nombre de logements                   │
│    ├─ Compare avec state.json                          │
│    ├─ Si changement → Envoie email                     │
│    └─ Met à jour state.json                            │
│ 4. Commit state.json                                    │
│ 5. Fin                                                  │
└─────────────────────────────────────────────────────────┘
```

---

## 🔑 Variables Clés

### Variables d'Environnement (GitHub Secrets)
```
EMAIL_USER          → votremail@gmail.com
EMAIL_PASSWORD      → App Password de Gmail (16 caractères)
RECEIVER_EMAIL      → Email pour recevoir les alertes
```

### Données Persistantes (state.json)
```json
{
  "count": 5,                                    // Nombre actuel
  "last_update": "2024-06-22T14:30:45.123456",  // Dernière mise à jour
  "last_line": "5 logements trouvés"            // Texte détecté
}
```

---

## ⏱️ Cronométrage GitHub Actions

```yaml
cron: '*/5 * * * *'  # Toutes les 5 minutes

# D'autres options:
'*/10 * * * *'       # Toutes les 10 minutes
'0 * * * *'          # Toutes les heures
'0 9 * * *'          # Chaque jour à 9h00
```

---

## 🧪 Tests Recommandés

### Test 1: Local
```bash
python test_bot.py
```

### Test 2: Avec Emails
```bash
set EMAIL_USER=votremail@gmail.com
set EMAIL_PASSWORD=votre_app_password
set RECEIVER_EMAIL=votremail@gmail.com
python mende_bot.py
```

### Test 3: GitHub Actions
- Allez sur Actions
- Lancez le workflow manuellement
- Vérifiez que les logs sont verts

---

## 🐛 Fichiers de Débogage

Si quelque chose ne marche pas:

1. **Vérifiez les logs GitHub Actions**
   - Onglet "Actions" → Workflow → Cliquez sur l'exécution

2. **Testez localement**
   - `python test_bot.py`
   - `python mende_bot.py`

3. **Consultez state.json**
   - Vérifiez que le nombre augmente
   - Vérifiez la dernière mise à jour

4. **Vérifiez les secrets**
   - Settings → Secrets and variables → Actions

---

## 📞 Support

| Fichier | Pour Quoi? |
|---|---|
| README.md | Documentation générale |
| DEPLOYMENT_GUIDE.md | Déploiement étape par étape |
| GITHUB_SECRETS_SETUP.md | Configuration des secrets |
| QUICKSTART.md | Démarrage rapide |
| test_bot.py | Tests locaux |

---

## ✅ Checklist Finale

- [ ] J'ai cloné/créé le dépôt
- [ ] Les 4 fichiers essentiels sont en place
- [ ] Le code est poussé sur GitHub
- [ ] Les 3 secrets sont configurés
- [ ] Le test manuel a réussi (onglet Actions)
- [ ] state.json a été mis à jour
- [ ] Un email a été reçu (ou vous l'avez testé)

**Si tout est ✅, le bot fonctionne!** 🎉

---

**Besoin d'aide? Consultez les documents de guide ou les logs GitHub Actions.**
