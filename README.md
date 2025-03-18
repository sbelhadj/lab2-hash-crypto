# 🔐 Lab 1 : Comprendre le Hashing et la Cryptographie

## 🎯 Objectif  
Ce Lab vous permettra de comprendre le rôle du **hashing cryptographique** et de l’expérimenter en Python.  

### 📌 **Concepts clés**  
✅ SHA-256 et l’immutabilité des données  
✅ Intégrité et sécurité en blockchain  
✅ Propriétés des fonctions de hash  

---

## 🛠️ **1. Installation des outils**  

Avant de commencer, assurez-vous d’avoir **Python 3+** installé. Pour vérifier :  

```bash
python --version
```


📝 2. Expérience avec le Hashing
Ouvrez le fichier hash_exercise.py et exécutez-le :
```bash
python hash_exercise.py
```

Analysez la sortie et modifiez le script pour :

Accepter une phrase en entrée et générer son hash SHA-256.
Comparer le hash de deux phrases similaires.

Complétez le fichier student_submission.md avec vos observations.



# Laboratoire Blockchain: Cryptographie, Hashing et ECDSA

## Objectif:
Ce laboratoire a pour objectif de vous faire découvrir les concepts clés de la cryptographie utilisés dans les blockchains, en particulier **Ethereum**. À la fin de ce laboratoire, vous serez capables de :
- Utiliser la fonction de **haching Ethereum (Keccak-256)**.
- Implémenter **ECDSA (Elliptic Curve Digital Signature Algorithm)** pour générer des clés, signer et vérifier des messages.
  
Le laboratoire est divisé en **deux activités** :
1. **Activité 1 : Fonction de Hachage Ethereum** (Keccak-256)
2. **Activité 2 : Cryptographie avec ECDSA**

## Prérequis:
Vous aurez besoin de **Python** installé sur votre machine, ainsi que des bibliothèques suivantes :
- **ecdsa** : Pour les fonctions de cryptographie utilisant ECDSA.
- **eth-hash** : Pour l'implémentation du hachage Ethereum (Keccak-256).

Installez les dépendances en utilisant la commande suivante :
```bash
pip install -r requirements.txt
```




