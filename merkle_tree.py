import hashlib

# Fonction pour calculer le hachage Keccak-256 (SHA3-256)
def keccak256(data):
    """Retourne le hachage Keccak-256 (SHA3-256)"""
    return hashlib.sha3_256(data.encode('utf-8')).hexdigest()

# Fonction pour construire un Arbre de Merkle
class MerkleTree:
    def __init__(self, leaves):
        self.leaves = [keccak256(leaf) for leaf in leaves]  # Calculer les hachages des feuilles
        self.tree = self.build_tree(self.leaves)

    def build_tree(self, leaves):
        """Construit l'Arbre de Merkle à partir des feuilles"""
        tree = [leaves]
        while len(leaves) > 1:
            leaves = [keccak256(leaves[i] + leaves[i + 1]) for i in range(0, len(leaves), 2)]
            tree.append(leaves)
        return tree

    def get_merkle_root(self):
        """Retourne la racine de l'Arbre de Merkle"""
        return self.tree[-1][0]

    def get_merkle_proof(self, index):
        """Retourne une preuve de Merkle pour le nœud à l'index donné"""
        proof = []
        for level in self.tree[:-1]:
            pair_index = index ^ 1  # Obtenir l'index de l'autre nœud
            if pair_index < len(level):
                proof.append(level[pair_index])
            index //= 2
        return proof

    def verify_merkle_proof(self, proof, leaf, root):
        """Vérifie la validité d'une preuve de Merkle"""
        current_hash = keccak256(leaf)
        for p in proof:
            current_hash = keccak256(current_hash + p)
        return current_hash == root

# Exemple d'utilisation
if __name__ == "__main__":
    leaves = ["A", "B", "C", "D"]
    tree = MerkleTree(leaves)
    root = tree.get_merkle_root()
    print(f"Merkle Root: {root}")
    
    # Test de la preuve de Merkle pour le premier élément
    proof = tree.get_merkle_proof(0)
    print(f"Proof for leaf 'A': {proof}")
    
    # Vérification de la preuve
    is_valid = tree.verify_merkle_proof(proof, "A", root)
    print(f"Merkle Proof valid: {is_valid}")
