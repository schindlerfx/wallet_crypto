import os


class file_utils:

   def create_directory_if_not_exists(directory):
       """Cria um diretório se ele não existir."""
       if not os.path.exists(directory):
           os.makedirs(directory)