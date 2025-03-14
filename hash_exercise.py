### 📜 **hash_exercise.py**  

```python
import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

if __name__ == "__main__":
    data = input("Entrez une phrase à hacher : ")
    print("Hash SHA-256 :", hash_data(data))
