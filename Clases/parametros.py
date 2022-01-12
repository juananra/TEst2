import configparser

class parametros:


    def __init__(self):

        self.database_host = ""
        self.database_user = ""
        self.database_name = ""
        self.database_password = ""

    def leerconexion(self, entorno="DEFAULT"):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.database_name = config[entorno]['DB_NAME']
        self.database_user = config[entorno]['DB_USER']
        self.database_password = config[entorno]['DB_PASSWORD']
        self.database_host = config[entorno]['DB_HOST']