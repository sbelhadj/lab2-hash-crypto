from ethereum_hashing import ethereum_hash

def test_hashing():
    data1 = "Bonjour, Ethereum!"
    data2 = "Bonjour, Ethereum!!"  # Un point d'exclamation supplémentaire

    print("Hachages originaux :")
    hash1 = ethereum_hash(data1)
    hash2 = ethereum_hash(data2)
    
    print(f"Hachage de '{data1}': {hash1}")
    print(f"Hachage de '{data2}': {hash2}")
    
    # Comparer les deux hachages
    print("\nComparer les hachages :")
    if hash1 == hash2:
        print("Les hachages sont identiques.")
    else:
        print("Les hachages sont différents. Même un petit changement génère un hachage complètement différent !")

if __name__ == "__main__":
    test_hashing()
