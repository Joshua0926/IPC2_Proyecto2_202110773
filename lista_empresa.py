from nodo import Nodo
import numpy as np
import xml.etree.cElementTree as ET
import graphviz


class ListaEmpresa():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        



    def insertar_empresa(self, idE, nombre, abreviatura, lista_puntosa, lista_escritorio, lista_transacciones):
        global empresa_data
        empresa_data= Nodo(dato=[idE, nombre, abreviatura, lista_puntosa, lista_escritorio, lista_transacciones])
        self.size += 1
        if self.primero is None:
            self.primero = empresa_data
            self.ultimo= empresa_data
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(empresa_data)
    
    def SeleccionarEmpresa(self, bus, punto):
        tmp = self.primero
        numeracion_puntoa2=0
        while tmp is not None:
            if bus != tmp.dato[0]:
                tmp=tmp.getsiguiente()
            else:
                print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                print("-- EMPRESA SELECCIONADA --")
                print("ID: ", tmp.dato[0])
                print("Nombre: ", tmp.dato[1])
                print("Abreviación: ", tmp.dato[2])
                print("--PUNTOS DE ATENCIÓN--")
                numeracion_puntoa=0
                while punto != tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[3] son los puntos de atención
                    numeracion_puntoa2+=1
                else:
                    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    print("-- PUNTO DE ATENCIÓN SELECCIONADO --")
                    print("ID: ", tmp.dato[3][numeracion_puntoa2][0])
                    print("Nombre: ", tmp.dato[3][numeracion_puntoa2][1])
                    print("Direccion: ", tmp.dato[3][numeracion_puntoa2][2])
                    print("-- ESCRITORIOS --")
                    numeracion_esc=0
                    for i in tmp.dato[4]:
                        if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                            numeracion_esc+=1
                        else:
                            #Comparo el id conectado de los escritorios con los id del punto de atención
                            while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[4] son los escritorios
                                print("ID: ", tmp.dato[4][numeracion_esc][1])
                                print("Código: ", tmp.dato[4][numeracion_esc][2])
                                print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                                if tmp.dato[4][numeracion_esc][4]==True:
                                    print("Estado de escritorio:  ACTIVO")
                                else:
                                    print("Estado de escritorio:  INACTIVO")
                                numeracion_esc+=1
                                break
                break
        
       

    def activarescritorios(self,bus,punto, escritorios):
        tmp = self.primero
        numeracion_puntoa2=0
        while tmp is not None:
            if bus != tmp.dato[0]:
                tmp=tmp.getsiguiente()
            else:
                while punto != tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[3] son los puntos de atención
                    numeracion_puntoa2+=1
                else:
                    numeracion_esc=0
                    for i in tmp.dato[4]:
                        if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                            numeracion_esc+=1
                        else:
                            #Comparo el id conectado de los escritorios con los id del punto de atención
                            while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[4] son los escritorios
                                while tmp.dato[4][numeracion_esc][1]==escritorios:
                                    tmp.dato[4][numeracion_esc][4]=True
                                    break
                                numeracion_esc+=1
                                break
                                
                break

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

            numeracion_trans=0
            for j in tmp.dato[5]:
                print("--TRANSACCIONES--")
                print("ID: ", tmp.dato[5][numeracion_trans][0])
                print("Nombre: ", tmp.dato[5][numeracion_trans][1])
                print("Tiempo de Atención: ", tmp.dato[5][numeracion_trans][2])
                numeracion_trans+=1
            
            print("-------------------------")
            tmp=tmp.getsiguiente()

    def emply(self):
        return self.primero

    def append(self, data):
        nodo = Nodo(data)
        if not self.emply():
            self.primero = nodo
            self.ultimo = nodo
        else:
            self.ultimo.siguiente = nodo
            nodo.anterior = self.ultimo
            self.ultimo = nodo

    def lengt(self):
        n = 0
        i = self.primero
        while i:
            i = i.siguiente
            n+=1
        return n

    def eliminardatos(self):
        temp = self.primero
        if temp is None:
            print("\n No es posible limpiar el sistema")
        while temp:
            self.primero = temp.getsiguiente()
            temp=None
            temp=self.primero
            self.size=0

    def dibujarGrafica(self):
        tmp = self.primero
        f = graphviz.Digraph(filename = "output/colorful organogram 1.gv")
        contesc=0
        for i in tmp.dato[4]:
            f.node("Escritorio: "+ tmp.dato[4][contesc][1]+"  "+ tmp.dato[4][contesc][2]+" "+tmp.dato[4][contesc][3], shape="box")
            contesc+=1
        f.render(filename='Escritorios', format="png", view=0, cleanup=1)    
        f
            





#***************************************************************************
