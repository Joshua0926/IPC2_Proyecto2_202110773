from nodo import Nodo
import numpy as np
import xml.etree.cElementTree as ET


class ListaEmpresa():
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
        empresa_data= Nodo(dato=[idE, nombre, abreviatura, lista_puntosa, lista_escritorio])
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

    def size(self):
        n = 0
        i = self.primero
        while i:
            i = i.siguiente
            n+=1
        return n

    def eliminardatos(self):
        if self.size() > 0:
            self.primero = None
            self.ultimo = None
            






#***************************************************************************


class Business:
    def __init__(self, id_empresa, nombre, abreviatura):
        self.id_empresa = id_empresa
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.puntosAtencion = ListaEmpresa()
        self.transacciones = ListaEmpresa()
    
    def getId(self):
        return self.id_empresa
    
    def getNombre(self):
        return self.nombre
    
    def getAbreviatura(self):
        return self.abreviatura

    def getPuntosAtencion(self):
        return self.puntosAtencion
    
    def getTransacciones(self):
        return self.transacciones

    def setId(self, id_empresa):
        self.id_empresa = id_empresa
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setAbreviatura(self, abreviatura):
        self.abreviatura = abreviatura
    
    def setPuntosAtencion(self, puntosAtencion):
        self.puntosAtencion = puntosAtencion
    
    def setTransacciones(self, transacciones):
        self.transacciones = transacciones
    
    def addPuntoAtencion(self, punto):
        self.puntosAtencion.append(punto)
    
    def addTransaccion(self, transaccion):
        self.transacciones.append(transaccion)


class Stack:
    def __init__(self):
        self.head = None

    # VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head
    
    # AGREGAMOS LOS DATOS AL FINAL
    def insert(self, data):
        nodo = Nodo(data)
        
        if not self.emply():
            self.head = nodo
        else:
            nodo.siguiente = self.head
            self.head = nodo
    
    # RETORNAR EL NÚMERO DE ELEMENTOS
    def length(self):
        n = 0
        i = self.head
        while i:
            i = i.siguiente
            n+=1
        return n

    # BUSCAMOS UN DATO EN ESPECIFICO POR SU POSICION
    def searchDate(self, selection):
        n = 1
        i = self.head
        while i:
            if selection == n:
                return i.dato
            else:
                n +=1 
                i = i.siguiente 
        return False
    
    def print(self):
        aux = self.head
        while aux:
            print(aux.dato)
            aux = aux.siguiente
    
    def pop(self):
        if not self.emply():
            return None
        else:
            aux = self.head
            self.head = self.head.siguiente
            return aux.dato





class Attention():
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.listaEscritorio = ListaEmpresa()
        self.escritoriosActivos = Stack()
    
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getListaEscritorio(self):
        return self.listaEscritorio

    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def setListaEscritorio(self, listaEscitorio):
        self.listaEscritorio = listaEscitorio   

    def addEscritorio(self, escritorio):
        self.listaEscritorio.append(escritorio)
    
    def addEscritorioActivo(self, activo):
        self.escritoriosActivos.insert(activo)   

class Desktop():
    def __init__(self, id, identificacion, encargado):
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = False
        self.cliente = None
    
    def getId(self):
        return self.id
    
    def getIdentificacion(self):
        return self.identificacion

    def getEncargado(self):
        return self.encargado
    
    def getEstado(self):
        return self.estado
    
    def getCliente(self):
        return self.cliente
    
    def setId(self, id):
        self.id = id
    
    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion
    
    def setEncargado(self, encargado):
        self.encargado = encargado
    
    def activar(self):
        self.estado = True
    
    def desactivar(self):
        self.estado = False
    
    def atenderCliente(self, cliente):
        self.cliente = cliente
    
    def clienteAtendido(self):
        self.cliente = None

class Transaction():
    def __init__(self, id, nombre, tiempoAtencion):
        self.id = id
        self.nombre = nombre
        self.tiempoAtencion = tiempoAtencion
    
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre

    def getTiempo(self):
        return self.tiempoAtencion

    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTiempo(self, tiempoAtencion):
        self.tiempoAtencion = tiempoAtencion
    
    def printDates(self):
        print(self.id, self.nombre, self.tiempoAtencion)