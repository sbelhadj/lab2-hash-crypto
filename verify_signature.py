from ecdsa import VerifyingKey
import hashlib
import binascii

def verify_signature(message, signature):
    # Charger la clé publique
    with open('public.pem', 'rb') as pub_file:
        vk = VerifyingKey.from_pem(pub_file.read())

    # Vérifier la signature
    try:
        vk.verify(signature, message.encode())
        print("La signature est vérifiée avec succès !")
    except:
        print("La vérification de la signature a échoué.")

if __name__ == '__main__':
    message = input("Entrez le message à vérifier : ")
    signature_hex = input("Entrez la signature à vérifier (hex) : ")
    signature = binascii.unhexlify(signature_hex)

    verify_signature(message, signature)
