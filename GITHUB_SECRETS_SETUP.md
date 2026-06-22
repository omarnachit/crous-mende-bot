# 🚀 Guide de Configuration GitHub Secrets

Ce guide vous aide à configurer les secrets GitHub pour que le bot fonctionne correctement.

## ⚙️ Étapes Rapides

### 1️⃣ Accéder à la page des Secrets

1. Allez sur: **https://github.com/VotreUsername/crous-mende-bot/settings/secrets/actions**
   - Remplacez `VotreUsername` par votre nom d'utilisateur GitHub
   - Remplacez `crous-mende-bot` par le nom de votre dépôt

2. Vous devriez voir un bouton vert: **"New repository secret"**

### 2️⃣ Créer le premier secret: `EMAIL_USER`

1. Cliquez sur **"New repository secret"**
2. Dans le champ **"Name"**: Tapez `EMAIL_USER`
3. Dans le champ **"Secret"**: Tapez votre adresse Gmail complète
   - Exemple: `john.doe@gmail.com`
4. Cliquez **"Add secret"**

### 3️⃣ Créer le deuxième secret: `EMAIL_PASSWORD`

1. Cliquez sur **"New repository secret"**
2. Dans le champ **"Name"**: Tapez `EMAIL_PASSWORD`
3. Dans le champ **"Secret"**: Collez votre App Password (16 caractères)
   - ⚠️ **IMPORTANT**: C'est l'App Password généré sur https://myaccount.google.com/apppasswords
   - **NON** votre mot de passe Gmail normal!
   - Exemple: `abcd efgh ijkl mnop`
4. Cliquez **"Add secret"**

### 4️⃣ Créer le troisième secret: `RECEIVER_EMAIL`

1. Cliquez sur **"New repository secret"**
2. Dans le champ **"Name"**: Tapez `RECEIVER_EMAIL`
3. Dans le champ **"Secret"**: Tapez l'adresse email où vous voulez recevoir les alertes
   - Peut être identique à `EMAIL_USER`
   - Exemple: `john.doe@gmail.com`
4. Cliquez **"Add secret"**

## ✅ Vérifier la Configuration

Une fois les 3 secrets créés, la page des secrets devrait afficher:

```
📋 Repository secrets

✓ EMAIL_USER           (Updated X minutes ago)
✓ EMAIL_PASSWORD       (Updated X minutes ago)
✓ RECEIVER_EMAIL       (Updated X minutes ago)
```

## 🔑 Générer un App Password Gmail

Si vous n'avez pas encore d'App Password:

### Prérequis: Vérification en deux étapes activée

1. Allez sur: https://myaccount.google.com/security
2. Cherchez **"Vérification en deux étapes"**
3. Si elle n'est pas activée:
   - Cliquez dessus
   - Suivez les instructions (vous recevrez un code sur votre téléphone)
   - Complétez la configuration

### Générer l'App Password

1. Allez sur: https://myaccount.google.com/apppasswords
   - **Vous devez être connecté à Gmail**
   - **Vous devez avoir activé la vérification en deux étapes**

2. Sélectionnez:
   - **Sélectionnez l'app**: "Courrier" (Mail)
   - **Sélectionnez l'appareil**: "Windows" (ou votre OS)

3. Cliquez **"Générer"**

4. Google vous affiche un mot de passe de 16 caractères:
   ```
   abcd efgh ijkl mnop
   ```
   - **Copiez-le exactement** (y compris les espaces)
   - **C'est ce que vous colleriez dans le secret `EMAIL_PASSWORD`**

## ⚠️ Points Importants

1. **App Password vs Mot de Passe Gmail**
   - ❌ N'utilisez PAS votre mot de passe Gmail normal
   - ✅ Utilisez UNIQUEMENT l'App Password généré
   
2. **Les secrets sont privés**
   - ✅ Visibles que par vous
   - ✅ GitHub ne les affiche jamais en clair dans les logs
   - ✅ Les utiliser dans GitHub Actions est sûr

3. **Si vous avez des problèmes**
   - ❌ Ne postez PAS vos secrets sur internet
   - ✅ Générez un nouvel App Password
   - ✅ Mettez à jour le secret sur GitHub

## 🧪 Tester Localement

Pour vérifier que vos identifiants Gmail fonctionnent avant de les mettre sur GitHub:

```bash
# Sur Windows (PowerShell)
$env:EMAIL_USER = "votre_email@gmail.com"
$env:EMAIL_PASSWORD = "votre_app_password"
$env:RECEIVER_EMAIL = "votre_email@gmail.com"
python mende_bot.py

# Sur Mac/Linux (Bash)
export EMAIL_USER="votre_email@gmail.com"
export EMAIL_PASSWORD="votre_app_password"
export RECEIVER_EMAIL="votre_email@gmail.com"
python mende_bot.py
```

Si l'email est envoyé sans erreur, c'est bon! 🎉

## 🔄 Réinitialiser un Secret

Si vous avez fait une erreur:

1. Allez sur: https://github.com/VotreUsername/crous-mende-bot/settings/secrets/actions
2. Trouvez le secret à modifier
3. Cliquez sur le bouton **"🗑️ Delete"** (poubelle)
4. Créez un nouveau secret avec le bon nom et la bonne valeur

---

**Une fois cela fait, GitHub Actions pourra envoyer les emails automatiquement!** ✅
