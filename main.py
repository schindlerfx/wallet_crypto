from wallet.wallet import CryptoWallet
from wallet.backup import BackupManager
from wallet.scheduler import BackupScheduler


def main():
    # Configurações
    backup_interval_hours = 1
    print("Configuração: Intervalo de backups definido para 1 hora.")
    backup_retention_days = 7
    print("Configuração: Retenção de backups definida para 7 dias.")

    # Inicializa a carteira
    print("Inicializando a carteira...")
    wallet = CryptoWallet()
    print("Carteira criada com sucesso.")

    # Gera as chaves
    print("Gerando chaves...")
    wallet.generate_keys()
    print("Chaves geradas com sucesso.")

    # Inicializa o gerenciador de backups
    print("Inicializando o gerenciador de backups...")
    backup_manager = BackupManager(wallet, backup_retention_days=backup_retention_days)
    print("Gerenciador de backups inicializado com sucesso.")

    # Inicializa o agendador de backups com tratamento de erros
    try:
        print("Inicializando o agendador de backups...")
        BackupScheduler(backup_manager, backup_interval_hours=backup_interval_hours)
        print("Agendador de backups inicializado com sucesso.")
    except Exception as e:
        print(f"Erro ao inicializar o agendador de backups: {e}")

    # Exibe informações da carteira
    print("\n=== Informações da Carteira ===")
    print(f"Endereço: {wallet.address}")
    print(f"Chave Pública: {wallet.public_key.decode()}")
    print(f"Chave Privada: {wallet.private_key.decode()}")

    # Menu interativo
    print("Entrando no loop do menu...")
    while True:
        print("\n=== Menu ===")
        print("1. Criar transação")
        print("2. Verificar assinatura")
        print("3. Restaurar backup")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            # Criar transação
            transaction = input("Digite a transação: ")
            signature = wallet.sign_transaction(transaction)
            print(f"\nTransação: {transaction}")
            print(f"Assinatura: {signature}")
            input("\nPressione Enter para continuar...")

        elif choice == "2":
            # Verificar assinatura
            transaction = input("Digite a transação: ")
            signature = input("Digite a assinatura: ")
            is_valid = wallet.verify_signature(transaction, signature, wallet.public_key)
            print(f"\nAssinatura válida? {is_valid}")
            input("\nPressione Enter para continuar...")

        elif choice == "3":
            # Restaurar backup
            backup_file = input("Digite o caminho do backup (ex: backups/wallet_backup_20231025-153045.json): ")
            backup_manager.restore_backup(backup_file)
            print("\n=== Informações da Carteira após restauração ===")
            print(f"Endereço: {wallet.address}")
            print(f"Chave Pública: {wallet.public_key.decode()}")
            print(f"Chave Privada: {wallet.private_key.decode()}")
            input("\nPressione Enter para continuar...")

        elif choice == "4":
            # Sair
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()