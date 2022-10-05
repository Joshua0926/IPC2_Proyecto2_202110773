from funciones import *
from lista_empresa import ListaEmpresa

def run():
    lista_empresas = ListaEmpresa()
    configuracion_inicial = ListaEmpresa()
    
    end = False
    selection = 0

    # VARIABLES
    empresa = None
    pto_atencion = None

    while not end:
        print("\n------------------ Menú ------------------\n  1. Configuración de empresas\n  2. Seleccionar Empresa y puntos de atención\n  3. Manejo de puntos de atención\n  4. Salir")

        selection = pedirOpcion()
        
        if selection == 1:
            systemConfiguration(lista_empresas, configuracion_inicial)

        # elif selection == 2:
        #     empresa = selectBussines(lista_empresas)
        #     pto_atencion = selectPoint(empresa)

        # elif selection == 3:
        #     if empresa !=None and pto_atencion != None:
        #         startTest(empresa, pto_atencion)
        #     else:
        #         print("Datos incorrectos")
        elif selection == 2:
            listaempresa.SeleccionarEmpresa(config_idE, config_idP)  

        elif selection == 3:
            ManejoPuntosA(lista_empresas, configuracion_inicial)

        elif selection == 4:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()

    