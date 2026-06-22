# ⚡ DEMARRER MAINTENANT (5 minutes)

Si tu es VRAIMENT pressé, suis EXACTEMENT ceci:

---

## ⏱️ 5 MINUTES POUR UN BOT FONCTIONNEL

### ✅ ÉTAPE 1: Gmail (2 min)

1. Va sur: https://myaccount.google.com/apppasswords
2. Sélecte: Mail + appareil
3. **Copie l'App Password** (16 caractères)

❌ Ça ne fonctionne pas?
- Va sur https://myaccount.google.com/security
- Active "Vérification en deux étapes"
- Réessaye

---

### ✅ ÉTAPE 2: GitHub (1 min)

1. Va sur: https://github.com/new
2. Crée un dépôt: `crous-mende-bot`
3. Clone-le: `git clone https://github.com/TON_USERNAME/crous-mende-bot.git && cd crous-mende-bot`

---

### ✅ ÉTAPE 3: Code (1 min)

**Copie tous les fichiers du dossier actuel vers ton dépôt:**

```bash
# Tu as tous les fichiers dans le dossier
# Assure-toi qu'ils sont là:
# - mende_bot.py
# - requirements.txt
# - state.json
# - .github/workflows/crous.yml
# - Et tous les fichiers README

git add .
git commit -m "🤖 Bot CROUS"
git push
```

---

### ✅ ÉTAPE 4: Secrets (1 min)

1. Va sur: https://github.com/TON_USERNAME/crous-mende-bot/settings/secrets/actions
2. Crée 3 secrets:
   - `EMAIL_USER` = ton_email@gmail.com
   - `EMAIL_PASSWORD` = (Paste l'App Password)
   - `RECEIVER_EMAIL` = ton_email@gmail.com

---

### ✅ ÉTAPE 5: Test (0 min - Automatique!)

1. Va sur: https://github.com/TON_USERNAME/crous-mende-bot/actions
2. Clique "Surveillance CROUS Mende"
3. Clique "Run workflow"
4. **Attend que ce soit vert ✅**
5. **Regarde tes emails** 📧

---

## 🎉 C'EST FINI!

Le bot s'exécute maintenant automatiquement toutes les 5 minutes.

---

## ❌ Problème?

| Erreur | Solution |
|---|---|
| "Paramètres email manquants" | Vérifiez les 3 secrets |
| "Authentication failed" | Générez un nouvel App Password |
| Workflow échoue | Lisez les logs d'erreur |

**Plus d'aide?** Consultez `COMMENCER.md` ou `README.md`

---

**Voilà! Ton bot fonctionne! 🚀**
