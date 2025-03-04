import time
from threading import Thread
import schedule


class BackupScheduler:
    def _init_(self, backup_manager, backup_interval_hours=1):
        print("[BackupScheduler] Inicializando BackupScheduler...")
        self.backup_manager = backup_manager
        self.backup_interval_hours = backup_interval_hours
        self.running = True  # Controle para parar o agendador
        print(f"[BackupScheduler] Intervalo de backups: {self.backup_interval_hours} horas")
        self.start_backup_scheduler()
        print("[BackupScheduler] BackupScheduler inicializado com sucesso.")

    def start_backup_scheduler(self):
        """Inicia o agendamento de backups automáticos."""
        print("[BackupScheduler] Configurando agendamento de backups...")
        schedule.every(self.backup_interval_hours).hours.do(self.backup_manager.create_backup)
        print("[BackupScheduler] Agendamento configurado com sucesso.")

        def run_scheduler():
            print("[BackupScheduler] Iniciando thread do agendador...")
            while self.running:
                schedule.run_pending()
                time.sleep(1)
            print("[BackupScheduler] Agendador parado.")

        # Inicia o scheduler em uma thread separada
        self.scheduler_thread = Thread(target=run_scheduler)
        self.scheduler_thread.daemon = True  # Thread encerra quando o programa principal encerrar
        self.scheduler_thread.start()
        print("[BackupScheduler] Thread do agendador iniciada com sucesso.")

    def stop(self):
        """Para o agendador de backups."""
        #print("[BackupScheduler] Parando agendador...")
        self.running = False
        self.scheduler_thread.join()  # Espera a thread terminar
        print("[BackupScheduler] Agendador parado com sucesso.")