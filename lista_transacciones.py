from nodo import Nodo
import numpy as np 
import xml.etree.cElementTree as ET 


class listatrans(): 
    def __init__(self): 
        self.primero=None 
        self.ultimo= None 
        self.size = 0 

    def insertar_trans(self, id, idE,idP, idEs, clientes, idT): 
        global empresa_trans 
        empresa_trans= Nodo(dato=[id, idE,idP, idEs, clientes, idT]) 
        self.size+=1
        if self.primero is None: 
            self.primero = empresa_trans 
            self.ultimo= empresa_trans 
        else: 
            tmp = self.primero 
            while tmp.getsiguiente() is not None: 
                tmp=tmp.getsiguiente() 
            tmp.setsiguiente(empresa_trans) 



    def mostrar_transac(self): 
        tmp = self.primero 
        while tmp is not None: 
            
            numeracion_trans=0 
            print("--TRANSACCIONES--") 
            print("ID: ", tmp.dato[0]) 
            print("ID Empresa: ", tmp.dato[1]) 
            print("ID Punto de Atención: ", tmp.dato[2]) 
            cont_trans=0 
            for i in tmp.dato[3]: 
                print("Escritorios activos: ", tmp.dato[3][cont_trans][0]) 
                cont_trans+=1 
            cont_cliente=0
            # print("prueba******")            
            # print(tmp.dato[0]) 
            for j in tmp.dato[4]:   
                print("--CLIENTE--") 
                print("DPI: ", tmp.dato[4][cont_cliente][0]) 
                print("Nombre del cliente: ", tmp.dato[4][cont_cliente][1]) 
                print("--TRANSACIONES--")
                cont_id=0 
                for l in tmp.dato[5]: 
                    if tmp.dato[5][cont_id][0]!=tmp.dato[4][cont_cliente][0]:
                        cont_id+=1
                    else:
                        while tmp.dato[5][cont_id][0]==tmp.dato[4][cont_cliente][0]:    
                            print("ID transacción: ", tmp.dato[5][cont_id][1]) 
                            print("Cantidad: ", tmp.dato[5][cont_id][2]) 
                            cont_id+=1 
                            break
                cont_cliente+=1
                        
                           
                       
                        
            numeracion_trans+=1 
            print("-------------------------")
            tmp=tmp.getsiguiente() 




    def eliminardatos(self): 
        if  self.size>0: 
            self.primero=None 
            self.ultimo= None 
            self.size=0 
            print(self.size)