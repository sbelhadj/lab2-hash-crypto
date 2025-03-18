from eth_hash.auto import keccak

"""" if needed pip install eth-hash[pycryptodome]""""
def ethereum_hash(data):
    """Hache les données en utilisant la fonction Keccak-256 d'Ethereum."""
    # Convertir les données en bytes si c'est une chaîne de caractères
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Calculer le hachage Keccak-256
    hashed_data = keccak(data)
    return hashed_data.hex()

def main():
    print("Hachage Keccak-256 d'Ethereum")
    # Exemple 1 : Hachage d'une chaîne
    string_data = "Bonjour, Ethereum!"
    string_hash = ethereum_hash(string_data)
    print(f"Hachage de '{string_data}': {string_hash}")
    
    # Exemple 2 : Hachage d'un nombre (converti en chaîne)
    number_data = "1234567890"
    number_hash = ethereum_hash(number_data)
    print(f"Hachage de '{number_data}': {number_hash}")
    
    # Exemple 3 : Hachage d'une transaction simulée
    tx_data = '{"from": "0xabc123", "to": "0xdef456", "value": "100"}'
    tx_hash = ethereum_hash(tx_data)
    print(f"Hachage de la transaction : {tx_hash}")

if __name__ == "__main__":
    main()
