from ecdsa import SigningKey
import hashlib
import binascii

def sign_message(message):
    # Charger la clé privée
    with open('private.pem', 'rb') as priv_file:
        sk = SigningKey.from_pem(priv_file.read())

    # Signer le message
    signature = sk.sign(message.encode())

    print(f"Message : {message}")
    print(f"Signature : {binascii.hexlify(signature)}")

if __name__ == '__main__':
    message = input("Entrez le message à signer : ")
    sign_message(message)
