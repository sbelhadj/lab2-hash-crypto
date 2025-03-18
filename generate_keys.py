from ecdsa import NIST256p, SigningKey
import os

def generate_keys():
    # Générer une clé privée ECDSA
    sk = SigningKey.generate(curve=NIST256p)
    vk = sk.verifying_key  # Clé publique correspondante

    # Sauvegarder la clé privée dans un fichier
    with open('private.pem', 'wb') as priv_file:
        priv_file.write(sk.to_pem())

    # Sauvegarder la clé publique dans un fichier
    with open('public.pem', 'wb') as pub_file:
        pub_file.write(vk.to_pem())

    print("Clés ECDSA générées et sauvegardées dans 'private.pem' et 'public.pem'")

if __name__ == '__main__':
    generate_keys()
