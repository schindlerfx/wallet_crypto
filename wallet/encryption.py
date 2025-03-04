import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


class EncryptionManager:
    def _init_(self, key_file="key.key"):
        print("[EncryptionManager] Inicializando EncryptionManager...")
        self.key_file = key_file
        self.encryption_key = self.load_or_generate_encryption_key()
        print("[EncryptionManager] EncryptionManager inicializado com sucesso.")

    def derive_key_from_password(self, password, salt):
        """Deriva uma chave de criptografia a partir de uma senha."""
        print("[EncryptionManager] Derivando chave da senha...")
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        print("[EncryptionManager] Chave derivada com sucesso.")
        return key

    def load_or_generate_encryption_key(self):
        """Carrega a chave de criptografia ou gera uma nova se não existir."""
        print("[EncryptionManager] Carregando ou gerando chave de criptografia...")
        if os.path.exists(self.key_file):
            print("[EncryptionManager] Arquivo de chave encontrado. Carregando chave...")
            password = input("Digite a senha para descriptografar a chave: ")  # Substitui getpass por input
            with open(self.key_file, "rb") as f:
                salt = f.read(16)
                encrypted_key = f.read()
            key = self.derive_key_from_password(password, salt)
            print("[EncryptionManager] Chave carregada com sucesso.")
            return Fernet(key)
        else:
            print("[EncryptionManager] Arquivo de chave não encontrado. Gerando nova chave...")
            password = input("Crie uma senha para proteger a chave: ")  # Substitui getpass por input
            salt = os.urandom(16)
            key = self.derive_key_from_password(password, salt)
            with open(self.key_file, "wb") as f:
                f.write(salt + key)
            print("[EncryptionManager] Nova chave gerada e salva com sucesso.")
            return Fernet(key)

    def encrypt_data(self, data):
        """Criptografa os dados usando a chave de criptografia."""
        print("[EncryptionManager] Criptografando dados...")
        encrypted_data = self.encryption_key.encrypt(data.encode())
        print("[EncryptionManager] Dados criptografados com sucesso.")
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Descriptografa os dados usando a chave de criptografia."""
        print("[EncryptionManager] Descriptografando dados...")
        decrypted_data = self.encryption_key.decrypt(encrypted_data).decode()
        print("[EncryptionManager] Dados descriptografados com sucesso.")
        return decrypted_data