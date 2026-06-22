# 📋 Checklist de Configuration - Quick Start

## ⚡ En 10 Minutes

### ✅ Avant de Commencer

- [ ] J'ai un compte GitHub
- [ ] J'ai Git installé
- [ ] J'ai mon Gmail App Password prêt (ou sais le générer)

### 🚀 Procédure

#### 1. Créer/Préparer le Dépôt (1 min)

```bash
# Créez un nouveau dépôt sur https://github.com/new
# OU clonez un existant
git clone https://github.com/VotreUsername/crous-mende-bot.git
cd crous-mende-bot
```

#### 2. Copier les Fichiers (2 min)

Assurez-vous que vous avez ces fichiers:

- ✅ `mende_bot.py` (script principal)
- ✅ `requirements.txt` (dépendances)
- ✅ `state.json` (état)
- ✅ `.github/workflows/crous.yml` (GitHub Actions)

#### 3. Pousser sur GitHub (2 min)

```bash
git add .
git commit -m "🤖 Bot CROUS Mende"
git push
```

#### 4. Configurer les Secrets (3 min)

Allez sur: `https://github.com/VotreUsername/crous-mende-bot/settings/secrets/actions`

Créez 3 secrets:
- `EMAIL_USER` = votremail@gmail.com
- `EMAIL_PASSWORD` = Votre App Password (16 caractères)
- `RECEIVER_EMAIL` = votremail@gmail.com

#### 5. Tester (2 min)

1. Allez sur l'onglet "Actions"
2. Cliquez "Surveillance CROUS Mende"
3. Cliquez "Run workflow"
4. Attendez que ce soit vert ✅

### 🎉 C'est Fini!

Le bot s'exécute maintenant toutes les 5 minutes automatiquement!

---

## 📚 Documentation Complète

- 📖 `README.md` - Documentation complète
- 🚀 `DEPLOYMENT_GUIDE.md` - Guide pas à pas
- 🔐 `GITHUB_SECRETS_SETUP.md` - Configuration des secrets

---

## 🆘 En Cas de Problème

### Erreur: "Paramètres email manquants"
→ Vérifiez les secrets GitHub

### Erreur: "Authentication failed"
→ Générez un nouvel App Password Gmail

### Pas d'exécution automatique
→ Allez sur Settings → Actions → General → Activez

### Aucun email reçu
→ Consultez les logs GitHub Actions (onglet Actions)

---

## 📞 Besoin d'Aide Rapide?

| Problème | Solution |
|---|---|
| Secrets mal configurés | Vérifiez les 3 secrets dans Settings → Secrets |
| App Password incorrect | Générez un nouveau sur myaccount.google.com/apppasswords |
| Workflow ne s'exécute pas | Attendez 5-10 min, relancez manuellement ou allez dans Settings → Actions |
| Pas de notification email | Consultez les logs GitHub Actions |

---

**À bientôt pour les notifications! 🏠📧**
