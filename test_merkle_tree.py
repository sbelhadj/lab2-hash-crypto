import pytest
from merkle_tree import MerkleTree

def test_merkle_root():
    leaves = ["A", "B", "C", "D"]
    tree = MerkleTree(leaves)
    assert len(tree.tree) == 3  # Il doit y avoir 3 niveaux dans l'arbre
    assert tree.get_merkle_root() == "81fc7ee8bc37735a3948584fe6b68b95e0182b927ba4a685ae96bc5a39e039e0"  # Exemple de racine attendue

def test_merkle_proof():
    leaves = ["A", "B", "C", "D"]
    tree = MerkleTree(leaves)
    proof = tree.get_merkle_proof(0)
    assert len(proof) == 2  # Il doit y avoir 2 éléments dans la preuve
    assert tree.verify_merkle_proof(proof, "A", tree.get_merkle_root()) is True

def test_invalid_proof():
    leaves = ["A", "B", "C", "D"]
    tree = MerkleTree(leaves)
    proof = tree.get_merkle_proof(0)
    assert tree.verify_merkle_proof(proof, "A", "invalid_root") is False

if __name__ == "__main__":
    pytest.main()
