import hashlib

def calculate_hash(file_path):
    with open(file_path, 'rb') as file:
        file_hash = hashlib.sha256()
        while chunk := file.read(4096):
            file_hash.update(chunk)
    return file_hash.hexdigest()

file1_hash = calculate_hash('file1.txt')
file2_hash = calculate_hash('file1_backup.txt')

if file1_hash == file2_hash:
    print("File integrity verified.")
else:
    print("File integrity check failed!")