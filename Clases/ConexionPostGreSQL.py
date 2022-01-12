import psycopg2
import configparser

from Clases.parametros import parametros


class postgre:

    def conectar(self):
        # Conecta a PostGreeSQL

        #Obtenemos parametros de conexion
        datos = parametros()
        datos.leerconexion("TESTING")

        self.host= datos.database_host
        self.database = datos.database_name
        self.user = datos.database_user
        self.password = datos.database_password

        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)

        # Creamos el cursor con el objeto conexion
        cur = conexion.cursor()

        # Ejecutamos una consulta
        cur.execute("SELECT tran_id FROM access_transactions")

        # Recorremos los resultados y los mostramos
        for trand_id in cur.fetchall():
            print(trand_id)

        # Cerramos la conexión
        conexion.close()
