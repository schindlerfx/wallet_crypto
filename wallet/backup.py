import os
import json
from datetime import datetime, timedelta
from .encryption import EncryptionManager


class BackupManager:
    def __init__(self, wallet, backup_dir="backups", backup_retention_days=7):
        print("[BackupManager] Inicializando BackupManager...")
        self.wallet = wallet
        self.backup_dir = backup_dir
        self.backup_retention_days = backup_retention_days
        print(f"[BackupManager] Diretório de backups: {self.backup_dir}")
        print(f"[BackupManager] Retenção de backups: {self.backup_retention_days} dias")

        # Inicializa o gerenciador de criptografia
        print("[BackupManager] Inicializando EncryptionManager...")
        try:
            self.encryption_manager = EncryptionManager()
            print("[BackupManager] EncryptionManager inicializado com sucesso.")
        except Exception as e:
            print(f"[BackupManager] Erro ao inicializar EncryptionManager: {e}")
            raise  # Re-lança a exceção para que o programa pare com uma mensagem clara

        # Configura o diretório de backups
        print("[BackupManager] Configurando diretório de backups...")
        self.setup_backup_dir()
        print("[BackupManager] BackupManager inicializado com sucesso.")

    def setup_backup_dir(self):
        """Cria o diretório de backups se não existir."""
        print(f"[BackupManager] Verificando diretório de backups: {self.backup_dir}")
        if not os.path.exists(self.backup_dir):
            print(f"[BackupManager] Diretório de backups não encontrado. Criando: {self.backup_dir}")
            try:
                os.makedirs(self.backup_dir)
                print(f"[BackupManager] Diretório de backups criado com sucesso.")
            except Exception as e:
                print(f"[BackupManager] Erro ao criar diretório de backups: {e}")
                raise
        else:
            print(f"[BackupManager] Diretório de backups já existe: {self.backup_dir}")

    def create_backup(self):
        """Cria um backup criptografado da carteira."""
        print("[BackupManager] Criando backup...")
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_file = os.path.join(self.backup_dir, f"wallet_backup_{timestamp}.json")
        print(f"[BackupManager] Nome do arquivo de backup: {backup_file}")

        # Prepara os dados da carteira
        wallet_data = {
            "address": self.wallet.address,
            "public_key": self.wallet.public_key.decode(),
            "private_key": self.wallet.private_key.decode()
        }
        print("[BackupManager] Dados da carteira preparados.")

        # Criptografa os dados
        print("[BackupManager] Criptografando dados...")
        encrypted_backup = self.encryption_manager.encrypt_data(json.dumps(wallet_data))
        print("[BackupManager] Dados criptografados com sucesso.")

        # Salva o backup
        with open(backup_file, "wb") as f:
            f.write(encrypted_backup)
        print(f"[BackupManager] Backup criado com sucesso: {backup_file}")

        # Limpa backups antigos
        self.clean_old_backups()

    def clean_old_backups(self):
        """Remove backups mais antigos que o número de dias configurado."""
        print("[BackupManager] Verificando backups antigos...")
        now = datetime.now()
        for filename in os.listdir(self.backup_dir):
            file_path = os.path.join(self.backup_dir, filename)
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if now - file_creation_time > timedelta(days=self.backup_retention_days):
                print(f"[BackupManager] Removendo backup antigo: {filename}")
                os.remove(file_path)
                print(f"[BackupManager] Backup removido: {filename}")
        print("[BackupManager] Verificação de backups antigos concluída.")

    def restore_backup(self, backup_file):
        """Restaura a carteira a partir de um backup criptografado."""
        print(f"[BackupManager] Restaurando backup: {backup_file}")
        if not os.path.exists(backup_file):
            print("[BackupManager] Arquivo de backup não encontrado.")
            return

        # Lê o backup criptografado
        with open(backup_file, "rb") as f:
            encrypted_backup = f.read()
            print("[BackupManager] Backup criptografado lido com sucesso.")

            # Descriptografa os dados
            print("[BackupManager] Descriptografando dados...")
            wallet_data = json.loads(self.encryption_manager.decrypt_data(encrypted_backup))
            print("[BackupManager] Dados descriptografados com sucesso.")

            # Restaura os dados da carteira
            self.wallet.address = wallet_data["address"]
            self.wallet.public_key = wallet_data["public_key"].encode()
            self.wallet.private_key = wallet_data["private_key"].encode()
            print("[BackupManager] Carteira restaurada com sucesso.")
        print(f"[BackupManager] Backup restaurado com sucesso: {backup_file}")