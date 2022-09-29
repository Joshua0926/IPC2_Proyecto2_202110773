from nodo import nodo
import numpy as np
import xml.etree.cElementTree as ET


class listaempresa():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        


    # def siginsert(self, idE, nombre, abreviatura, lista_puntosa, lista_escritorio, lista_trans):
    #     global empresa_data
    #     empresa_data= nodo(dato=[idE, nombre, abreviatura, lista_puntosa, lista_escritorio, lista_trans])
    #     self.size += 1
    #     if self.primero is None:
    #         self.primero = empresa_data
    #         self.ultimo= empresa_data
    #     else:
    #         tmp = self.primero
    #         while tmp.getsiguiente() is not None:
    #             tmp=tmp.getsiguiente()
    #         tmp.setsiguiente(empresa_data)

    def insertar_empresa(self, idE, nombre, abreviatura, lista_puntosa, lista_escritorio):
        global empresa_data
        empresa_data= nodo(dato=[idE, nombre, abreviatura, lista_puntosa, lista_escritorio])
        self.size += 1
        if self.primero is None:
            self.primero = empresa_data
            self.ultimo= empresa_data
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(empresa_data)
    

    def mostrar_empresa(self):
        tmp = self.primero
        while tmp is not None:
            print("--EMPRESA--")
            print("ID: ", tmp.dato[0])
            print("Nombre: ", tmp.dato[1])
            print("Abreviación: ", tmp.dato[2])
            numeracion_puntoa=0
            for i in tmp.dato[3]:
                print("--PUNTO DE ATENCION--")
                print("ID: ", tmp.dato[3][numeracion_puntoa][0])
                print("Nombre: ", tmp.dato[3][numeracion_puntoa][1])
                print("Direccion: ", tmp.dato[3][numeracion_puntoa][2])
                print("--ESCRITORIOS--")
                numeracion_esc=0
                for i in tmp.dato[4]:
                    if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa][0]:
                        numeracion_esc+=1
                    else:
                        while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa][0]:
                            print("ID: ", tmp.dato[4][numeracion_esc][1])
                            print("Código: ", tmp.dato[4][numeracion_esc][2])
                            print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                            numeracion_esc+=1
                            break
                numeracion_puntoa+=1
            print("-------------------------")
            tmp=tmp.getsiguiente()