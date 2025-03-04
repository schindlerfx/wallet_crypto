from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib


class CryptoWallet:
    def __init__(self):
        print("[CryptoWallet] Inicializando carteira...")
        self.private_key, self.public_key = self.generate_keys()  # Gera as chaves
        self.address = self.generate_address()  # Gera o endereço
        print("[CryptoWallet] Carteira inicializada com sucesso.")

    def generate_keys(self):
        """Gera um par de chaves pública e privada."""
        print("[CryptoWallet] Gerando chaves...")
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        print("[CryptoWallet] Chaves geradas com sucesso.")
        return private_key, public_key

    def generate_address(self):
        """Gera um endereço simplificado a partir da chave pública."""
        print("[CryptoWallet] Gerando endereço...")
        address = hashlib.sha256(self.public_key).hexdigest()[:40]
        print(f"[CryptoWallet] Endereço gerado: {address}")
        return address

    def sign_transaction(self, transaction):
        """Assina uma transação com a chave privada."""
        print("[CryptoWallet] Assinando transação...")
        key = RSA.import_key(self.private_key)
        h = SHA256.new(transaction.encode())
        signature = pkcs1_15.new(key).sign(h)
        print("[CryptoWallet] Transação assinada com sucesso.")
        return signature.hex()

    def verify_signature(self, transaction, signature, public_key):
        """Verifica a assinatura de uma transação."""
        print("[CryptoWallet] Verificando assinatura...")
        key = RSA.import_key(public_key)
        h = SHA256.new(transaction.encode())
        try:
            pkcs1_15.new(key).verify(h, bytes.fromhex(signature))
            print("[CryptoWallet] Assinatura válida.")
            return True
        except (ValueError, TypeError):
            print("[CryptoWallet] Assinatura inválida.")
            return False