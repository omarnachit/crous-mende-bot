# Exemple de Configuration Locale

Ce fichier montre comment configurer les variables d'environnement pour les tests locaux.

## 🪟 Sur Windows (PowerShell)

```powershell
# Définir les variables d'environnement temporairement

$env:EMAIL_USER = "votremail@gmail.com"
$env:EMAIL_PASSWORD = "abcd efgh ijkl mnop"
$env:RECEIVER_EMAIL = "votremail@gmail.com"
$env:DEBUG = "true"

# Exécuter le script
python mende_bot.py
```

### Ou créer un fichier setup_env.ps1

```powershell
# setup_env.ps1

# ⚠️ IMPORTANT: Modifiez ces valeurs!
$env:EMAIL_USER = "votremail@gmail.com"
$env:EMAIL_PASSWORD = "votre_app_password"
$env:RECEIVER_EMAIL = "votremail@gmail.com"
$env:DEBUG = "true"

Write-Host "✅ Variables d'environnement configurées"
Write-Host "   EMAIL_USER: $($env:EMAIL_USER)"
Write-Host "   EMAIL_PASSWORD: ***"
Write-Host "   RECEIVER_EMAIL: $($env:RECEIVER_EMAIL)"
```

Utilisation:
```powershell
.\setup_env.ps1
python mende_bot.py
```

---

## 🐧 Sur Mac/Linux (Bash)

```bash
# Définir les variables d'environnement temporairement

export EMAIL_USER="votremail@gmail.com"
export EMAIL_PASSWORD="abcd efgh ijkl mnop"
export RECEIVER_EMAIL="votremail@gmail.com"
export DEBUG="true"

# Exécuter le script
python mende_bot.py
```

### Ou créer un fichier setup_env.sh

```bash
#!/bin/bash

# setup_env.sh

# ⚠️ IMPORTANT: Modifiez ces valeurs!
export EMAIL_USER="votremail@gmail.com"
export EMAIL_PASSWORD="votre_app_password"
export RECEIVER_EMAIL="votremail@gmail.com"
export DEBUG="true"

echo "✅ Variables d'environnement configurées"
echo "   EMAIL_USER: $EMAIL_USER"
echo "   EMAIL_PASSWORD: ***"
echo "   RECEIVER_EMAIL: $RECEIVER_EMAIL"
```

Utilisation:
```bash
chmod +x setup_env.sh
./setup_env.sh
python mende_bot.py
```

---

## 🔒 Sécurité: Ne Commitez PAS Les Secrets!

**⚠️ IMPORTANT**: Ne commitez JAMAIS vos secrets sur GitHub!

Le fichier `.gitignore` contient:
```
# Fichiers d'environnement
.env
.env.local
setup_env.ps1
setup_env.sh
```

Cela signifie que même si vous créez des fichiers avec vos secrets localement, ils ne seront pas envoyés à GitHub. ✅

---

## ✅ Checklist pour les Tests Locaux

- [ ] J'ai créé un App Password Gmail
- [ ] Je sais mon adresse Gmail
- [ ] J'ai copié l'App Password (16 caractères)
- [ ] J'ai installé les dépendances: `pip install -r requirements.txt`
- [ ] J'ai configuré mes variables d'environnement
- [ ] J'ai exécuté: `python mende_bot.py`
- [ ] Je vérife les logs dans la console
- [ ] Je vérife que state.json a été créé/mis à jour

---

## 🧪 Exemple de Test Complet

### 1. Configurer les variables

```powershell
$env:EMAIL_USER = "john.doe@gmail.com"
$env:EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"
$env:RECEIVER_EMAIL = "john.doe@gmail.com"
$env:DEBUG = "true"
```

### 2. Exécuter le script

```powershell
python mende_bot.py
```

### 3. Vérifier les résultats

```powershell
# Voir le contenu de state.json
cat state.json

# Ou avec PowerShell:
Get-Content state.json | ConvertFrom-Json | Format-List
```

### 4. Vérifier les emails reçus

- Ouvrez Gmail
- Cherchez un email du bot
- Vérifiez la présence du lien CROUS

---

## 📝 Variables d'Environnement Disponibles

| Variable | Type | Défaut | Description |
|---|---|---|---|
| `EMAIL_USER` | string | Vide | Adresse Gmail |
| `EMAIL_PASSWORD` | string | Vide | App Password |
| `RECEIVER_EMAIL` | string | Vide | Email destinataire |
| `DEBUG` | boolean | false | Affiche logs détaillés |

---

## 🆘 Problèmes Courants

### "Authentication failed for SMTP"

**Cause**: App Password invalide

```bash
# Vérifiez votre App Password sur:
# https://myaccount.google.com/apppasswords
```

### "ModuleNotFoundError: No module named 'selenium'"

**Cause**: Dépendances non installées

```bash
pip install -r requirements.txt
```

### "Paramètres email manquants"

**Cause**: Variables d'environnement non définies

```powershell
# Vérifiez que les variables sont définies:
$env:EMAIL_USER
$env:EMAIL_PASSWORD
$env:RECEIVER_EMAIL
```

---

## 💡 Conseils

1. **Testez d'abord localement** avant GitHub Actions
2. **Activez DEBUG=true** pour voir les logs détaillés
3. **Gardez vos App Passwords secrets** (jamais sur GitHub)
4. **Testez sans email d'abord** (commentez la ligne send_email)
5. **Consultez state.json** pour déboguer

---

**Prêt à tester? Configurez vos variables et lancez le script!** 🚀
