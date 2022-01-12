from mstrio.connection import Connection
from mstrio.project_objects.datasets import OlapCube, load_cube
from mstrio.project_objects.datasets import SuperCube

import pandas as pd

class mstr:
    base_url = "http://localhost:8080/MicroStrategyLibrary/api"
    mstr_username = "Administrator"
    mstr_password =""
    project_name = "MicroStrategy Tutorial"
    conn=""

    def conectar (self):
        self.conn = Connection(self.base_url, self.mstr_username, self.mstr_password, self.project_name)

    def LeerDataset(self, report):
        self.conectar()
        my_cube = OlapCube(connection=self.conn, id="107425DA11E5CC7C00000080EFB57A54")
        my_cube = load_cube(connection=self.conn, cube_id="107425DA11E5CC7C00000080EFB57A54")
        df = my_cube.to_dataframe()
        print(df["Brand"])

    def CargaCubo(self, datos):
        self.conectar()

        # Add tables to the super cube and create it. By default 'create()' will
        # additionally upload data to the I-Server and publish it. You can manipulate it
        # by setting parameters `auto_upload` and `auto_publish`
        try:
            stores_df = datos
            ds = SuperCube(connection=self.conn, name="Store Analysis x")
            ds.add_table(name="Stores", data_frame=stores_df, update_policy="replace")
            ds.create('FBD29C1C41405F2ACC37AE9C987C74E8')
        except :
            print ("Error")


        else:
            print("ok")



