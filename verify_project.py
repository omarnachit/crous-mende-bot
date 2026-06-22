#!/usr/bin/env python3
"""
Verification Script - Vérifie que tous les fichiers sont présents et valides
Exécutez avec: python verify_project.py
"""

import os
import sys
import json
from pathlib import Path

def check_file(filepath, file_type="unknown"):
    """Vérifie qu'un fichier existe"""
    if Path(filepath).exists():
        size = os.path.getsize(filepath)
        print(f"  ✅ {filepath} ({size} bytes)")
        return True
    else:
        print(f"  ❌ {filepath} - MANQUANT!")
        return False

def check_json(filepath):
    """Vérifie qu'un fichier JSON est valide"""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        print(f"  ✅ {filepath} (JSON valide)")
        return True
    except Exception as e:
        print(f"  ❌ {filepath} - ERREUR JSON: {e}")
        return False

def check_python(filepath):
    """Vérifie qu'un fichier Python est syntactiquement valide"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            compile(f.read(), filepath, 'exec')
        print(f"  ✅ {filepath} (Python valide)")
        return True
    except SyntaxError as e:
        print(f"  ❌ {filepath} - ERREUR SYNTAXE: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("🔍 VÉRIFICATION DU PROJET CROUS")
    print("="*60 + "\n")
    
    all_good = True
    
    # 1. Fichiers essentiels
    print("1️⃣  Fichiers Essentiels:")
    essential_files = {
        "mende_bot.py": "python",
        "test_bot.py": "python",
        "requirements.txt": "text",
        "state.json": "json",
        ".gitignore": "text",
        ".github/workflows/crous.yml": "text",
    }
    
    for filename, ftype in essential_files.items():
        if ftype == "python":
            if not check_python(filename):
                all_good = False
        elif ftype == "json":
            if not check_json(filename):
                all_good = False
        else:
            if not check_file(filename, ftype):
                all_good = False
    
    # 2. Fichiers de documentation
    print("\n2️⃣  Fichiers de Documentation:")
    doc_files = [
        "00_LIRE_EN_PREMIER.md",
        "COMMENCER.md",
        "DEMARRER.md",
        "QUICKSTART.md",
        "DEPLOYMENT_GUIDE.md",
        "GITHUB_SECRETS_SETUP.md",
        "FINAL_CHECKLIST.md",
        "README.md",
        "PROJECT_STRUCTURE.md",
        "LOCAL_TESTING.md",
        "IMPROVEMENTS.md",
        "INDEX.md",
        "FICHIERS_EXPLIQUES.md",
        "RESUME_FINAL.md",
        "LIRE_MOI.txt",
    ]
    
    for doc in doc_files:
        if not check_file(doc, "doc"):
            all_good = False
    
    # 3. Contenu des fichiers clés
    print("\n3️⃣  Vérification du Contenu:")
    
    # Vérifier mende_bot.py contient les fonctions essentielles
    with open("mende_bot.py", "r", encoding='utf-8') as f:
        bot_content = f.read()
        
    required_functions = [
        "def main()",
        "save_state",
        "send_email",
        "check_apartments",
    ]
    
    for func in required_functions:
        if func in bot_content:
            print(f"  ✅ mende_bot.py contient '{func}'")
        else:
            print(f"  ⚠️  mende_bot.py pourrait ne pas contenir '{func}'")
    
    # Vérifier requirements.txt
    with open("requirements.txt", "r") as f:
        req_content = f.read()
    
    if "selenium" in req_content.lower() and "webdriver-manager" in req_content.lower():
        print(f"  ✅ requirements.txt contient selenium et webdriver-manager")
    else:
        print(f"  ❌ requirements.txt manque des dépendances")
        all_good = False
    
    # 4. Vérifier le workflow GitHub Actions
    print("\n4️⃣  GitHub Actions Workflow:")
    if Path(".github/workflows/crous.yml").exists():
        with open(".github/workflows/crous.yml", "r") as f:
            workflow_content = f.read()
        
        if "*/5 * * * *" in workflow_content:
            print(f"  ✅ Cron configuré (toutes les 5 minutes)")
        else:
            print(f"  ⚠️  Attention: Cron peut ne pas être correctement configuré")
        
        if "python mende_bot.py" in workflow_content:
            print(f"  ✅ Script lanché dans le workflow")
        else:
            print(f"  ❌ Script ne semble pas être lancé")
            all_good = False
    
    # 5. Résumé
    print("\n" + "="*60)
    
    if all_good:
        print("✅ TOUS LES FICHIERS SONT PRÉSENTS ET VALIDES!")
        print("\n🚀 Vous pouvez déployer le projet!")
        print("\nProchaines étapes:")
        print("  1. Lisez DEMARRER.md")
        print("  2. Créez un dépôt GitHub")
        print("  3. Configurez les secrets")
        print("  4. Testez le workflow")
        return 0
    else:
        print("❌ CERTAINS FICHIERS SONT MANQUANTS OU INVALIDES!")
        print("\nVérifiez les ❌ ci-dessus et réessayez.")
        return 1
    
    print("="*60 + "\n")

if __name__ == "__main__":
    sys.exit(main())
