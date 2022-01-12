import os

from Clases import ConexionPostGreSQL
from Clases import microstrategy

# from Clases.Excel.ReadExcel import RadExcelFile
from Clases.Excel.ReadExcel import RadExcelFile

if __name__ == '__main__':

    # ConexionPostGreSQL.postgre().conectar()
    # microstrategy.mstr().conectar()
    # microstrategy.mstr().LeerDataset("601A954347DF09505572CC8F914CAEBD")
    loc = 'C:/Users/jaramos/PycharmProjects/pythonProject/Clases/Excel/Test.xlsx'
    datos = RadExcelFile(loc).Read()
    print(datos)
    microstrategy.mstr().CargaCubo(datos)

    from os import listdir
    from os.path import isfile, join

    mypath = "C:/Program Files (x86)/MicroStrategy/Developer"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles:
        if file.endswith('.DLL') or file.endswith('.OCX'):
            print(file)
            # os.system('Regsvr32  '+ file)
