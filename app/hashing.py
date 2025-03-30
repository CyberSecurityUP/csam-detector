from PIL import Image
import imagehash
import json
import os

HASH_DB_PATH = os.path.join("hash_db", "hashes.json")

def generate_hash(image_path):
    """
    Gera um hash perceptual (phash) da imagem.
    """
    img = Image.open(image_path)
    hash_val = imagehash.phash(img)
    return str(hash_val)  # continua retornando string para visualização

def compare_with_database(hash_val_str, threshold=10):
    """
    Compara o hash (string) com a base de hashes simulada.
    """
    hash_val = imagehash.hex_to_hash(hash_val_str)  # ✅ conversão de volta para ImageHash

    try:
        with open(HASH_DB_PATH, "r") as f:
            hash_list = json.load(f)
    except FileNotFoundError:
        return False, None

    for entry in hash_list:
        existing_hash = imagehash.hex_to_hash(entry["hash"])
        distance = hash_val - existing_hash
        if distance <= threshold:
            return True, entry.get("id", "UNKNOWN")

    return False, None
