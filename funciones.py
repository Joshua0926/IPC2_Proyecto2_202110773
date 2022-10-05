from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
from lista_empresa import ListaEmpresa
from lista_transacciones import listatrans
from lista_empresa import Business
from lista_empresa import Attention
from lista_empresa import Desktop
from lista_empresa import Transaction
from lista_empresa import Stack
listaempresa = ListaEmpresa()
listatransac = listatrans()




def pedirOpcion():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opción: "))
            correcto=True
        except ValueError:
            print('¡Error, introduce un numero entero!')
    return num  

def systemConfiguration(lista_empresas:ListaEmpresa, configuracion_inicial):
    end = False
    selection = 0

    while not end:
        print("""
        \n---------- Configuración de empresas ----------\n 1. Limpiar sistema\n 2. Cargar archivo (Configuracion sistema)\n 3. Crear nueva empresa\n 4. Cargar archivo (Configuración inicial)\n 5. Regresar \n 6.Opcion""")
        selection = pedirOpcion()
        
        # VACIA LA LISTA DE LOS DATOS
        if selection == 1:
            listaempresa.eliminardatos()
          
            
            
            
            # configuracion_inicial.eliminardatos()
            print("¡Datos eliminados")

        elif selection == 2:
            subirArchivo()

        elif selection == 3:
            end_1 = False

            while(not end_1):
                correct = False
                CrearEmpresas()
                # empresa = CrearEmpresa()
                # lista_empresas.append(empresa)

                print("\n¡Empresa creada!\n¿Desea agregar otra empresa?\n 1. Si\n 2. No")
                
                while(not correct):
                    selection = pedirOpcion()
        
                    if selection == 1:
                        correct = True

                    elif selection == 2:
                        correct = True
                        end_1 = True
                    else:
                        print("Intente de nuevo") 

        elif selection == 4:
            CargarTrans()

        elif selection == 5:
            end = True

        elif selection == 6:
            listaempresa.SeleccionarEmpresa(config_idE, config_idP)
        else:
            print("Intente de nuevo") 





def ManejoPuntosA(lista_empresas:ListaEmpresa, configuracion_inicial):
    end = False
    selection = 0

    while not end:
        print("""
        \n---------- Manejo de Puntos de Atención ----------\n 1. Ver Estado Punto de Atención\n 2. Avtivar Escritorio de Servicio\n 3. Desactivar Escritorio\n 4. Atener Cliente\n 5. Solicitud de Atención \n 6.Simular Actividad""")
        selection = pedirOpcion()
        
        # VACIA LA LISTA DE LOS DATOS
        if selection == 1:
            listadopuntosa()

        elif selection == 2:
            print("HOla")

        elif selection == 3:
            end_1 = False

            while(not end_1):
                correct = False
                CrearEmpresas()
                # empresa = CrearEmpresa()
                # lista_empresas.append(empresa)

                print("\n¡Empresa creada!\n¿Desea agregar otra empresa?\n 1. Si\n 2. No")
                
                while(not correct):
                    selection = pedirOpcion()
        
                    if selection == 1:
                        correct = True

                    elif selection == 2:
                        correct = True
                        end_1 = True
                    else:
                        print("Intente de nuevo") 

        elif selection == 4:
            CargarTrans()

        elif selection == 5:
            end = True

        elif selection == 6:
            listaempresa.SeleccionarEmpresa(config_idE, config_idP)
        else:
            print("Intente de nuevo") 

def subirArchivo():
    cont =0
    filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", ".xml"), ("Todos los archivos",".*")))
    docxml = ET.parse(filename)
    root = docxml.getroot()

    global listaIDCliente
    listaIDCliente=[]
    global listaempresas
    listaempresas =[]
    


    for x in root.findall('empresa'):
        # print("ID: "+ x.attrib.get('id'))
        # print("Nombre: "+ x.find('nombre').text)
        # print("Abreviatura: "+ x.find('abreviatura').text)
        listaIDCliente.append(x.attrib.get('id'))



    for x in root.findall('empresa'):
        IdEmpresa=x.attrib.get('id')
        NombreEmpresa=x.find('nombre').text
        AbrevEmpresa=x.find('abreviatura').text
        listaempresas.append([IdEmpresa,NombreEmpresa,AbrevEmpresa])

        PuntosAtencion = x.find('listaPuntosAtencion')
        global listapuntos
        listapuntos =[]
        global listaescritorios
        listaescritorios=[]

        for y in PuntosAtencion.findall('puntoAtencion'):
            IdPuntos=y.attrib.get('id')
            NombrePunto=y.find('nombre').text 
            DireccionPunto=y.find('direccion').text
            listapuntos.append([IdPuntos,NombrePunto,DireccionPunto])

            escritorios = y.find('listaEscritorios')

            for z in escritorios.findall('escritorio'):
                IdEscritorio=z.attrib.get('id') 
                IdentificacionEscritorio=z.find('identificacion').text 
                EncargadoEscritorio=z.find('encargado').text
                Activacion=False
                listaescritorios.append([IdPuntos,IdEscritorio,IdentificacionEscritorio,EncargadoEscritorio, Activacion])

        transacciones = x.find('listaTransacciones') #lista de transacciones
        listatransacciones=[]
        for a in transacciones.findall('transaccion'):

            Id_transaccion = a.attrib.get('id') #id transaccion
            Nombre_transaccion = a.find('nombre').text #nombre transaccion
            Tiempo = a.find('tiempoAtencion').text #tiempo transaccion
            listatransacciones.append([Id_transaccion,Nombre_transaccion,Tiempo])



            # transacciones = a.find('listaTransacciones')

            # for a in transacciones.findall('transaccion'):
            #     print('ID Transaccion: '+a.attrib.get('id')) 
            #     print('Nombre Transaccion: '+a.find('nombre').text) 
            #     print('Tiempo Atencion: '+a.find('tiempoAtencion').text)
            #     listatransacciones.append([a.attrib.get('id'),a.find('nombre').text,a.find('tiempoAtencion').text])
            #     print("-----------------------------------------")
        
        listaempresa.insertar_empresa(IdEmpresa,NombreEmpresa,AbrevEmpresa,listapuntos,listaescritorios, listatransacciones)
    listaempresa.mostrar_empresa()
    # print("***********************************")
    # print(listaempresas)
    # print(listapuntos)
    # print(listaescritorios)
    # print(listatransacciones)


def CrearEmpresas():
    listanuevaempresa=[]
    print(" Crear Nueva Empresa")
    print("Ingrese el ID")
    idcreate=input()
    print("Ingrese el Nombre")
    namecreate=input()
    print("Ingrese la Abreviatura")
    abrevcreate=input()
    listanuevaempresa.append([idcreate,namecreate,abrevcreate])
    listanuevopunto=[]
    deskcreate=[]
    print("Ingrese el número de puntos de atención")
    natecreate=input()
    puntcreate=0
    for nat in range(int(natecreate)):
        puntcreate+=1
        print("Ingrese el Id punto ",puntcreate)
        idcreateate=input()
        print("Ingrese el Nombre punto ",puntcreate)
        namecreateate=input()
        print("Ingrese la dirección punto ",puntcreate)
        direccreateate=input()
        print("Ingrese el número de escritorios que desea para el punto ",puntcreate)
        listanuevopunto.append([idcreateate,namecreateate,direccreateate])
        numdcreate=input()
        contdeskcreate=0
        for numc in range(int(numdcreate)):
            contdeskcreate+=1
            print("Ingrese el Id escritorio ",contdeskcreate)
            iddeskcreate=input()
            print("Ingrese el identificador escritorio ",contdeskcreate)
            identicreate=input()
            print("Ingrese el encargado escritorio ",contdeskcreate)
            encarcreate=input()
            deskcreate.append([idcreateate,iddeskcreate,identicreate,encarcreate])
        #atencreate.append([idcreateate,namecreateate,direccreateate,deskcreate])
    #hola    
    print("Ingrese el número de transacciones")
    numtracreate=input()
    trancreate=[]
    transaccreatecont=0
    for numt in range(int(numtracreate)):
        transaccreatecont+=1
        print("Ingrese el Id transacción ",transaccreatecont)
        idtrancreate=input()
        print("Ingrese el nombre de la transacción ",transaccreatecont)
        identicreate=input()
        print("Ingrese el tiempo de atención de la transacción ",transaccreatecont)
        timecreate=input()
        trancreate.append([idtrancreate,identicreate,timecreate])
        listaempresa.insertar_empresa(idcreate,namecreate,abrevcreate,listanuevopunto, deskcreate, trancreate)
    listaempresa.mostrar_empresa()


def CargarTrans(): 
    #Abrir archivos (XML y todos los archivos) 
    global archivo2
    archivo2 = fd.askopenfilename(initialdir="C:/", title="abrir", filetypes=(("XML files",".XML"),("Todos los archivos",".*"))) 
    datos = ET.parse(archivo2) 
    ruta = datos.getroot()

    listaconfi=[]
    global config_id
    global config_idE
    global config_idP

    for k in datos.findall('configInicial'): 
        config_id=(k.attrib.get('id')) 
        config_idE=(k.attrib.get('idEmpresa')) 
        config_idP=(k.attrib.get('idPunto')) 
        # idconfi.append([config_id])
        # idEmpresaconfi.append([config_idE])
        # idPuntoconfi.append([config_idP])
        #listaconfi.append([config_id, config_idE, config_idP])
        escritorio_act=k.find('escritoriosActivos') 
        #global escritorio
        escritorio=[] 
        
        
        for m in escritorio_act.findall('escritorio'): 
            escritorio_id=m.attrib.get('idEscritorio') 
            escritorio.append([escritorio_id]) 
        clientes_list=k.find('listadoClientes') 

        listaclientes=[]
        nombreclientes=[]
        transaccion=[] 
        #cantidad=[] 
        for n in clientes_list.findall('cliente'): 
            cliente_dpi=n.attrib.get('dpi') 
            cliente_nombre=n.find('nombre').text 
            listaclientes.append([cliente_dpi,cliente_nombre])
            #nombreclientes.append([cliente_nombre])
            trans_list=n.find('listadoTransacciones') 
        
            for l in trans_list.findall('transaccion'): 
                trans_id=l.attrib.get('idTransaccion') 
                trans_cantidad=l.attrib.get('cantidad') 
                transaccion.append([cliente_dpi,trans_id,trans_cantidad]) 
                #cantidad.append([trans_cantidad]) 

        #Agregar datos al nodo a través de la lista 
        listatransac.insertar_trans(config_id, config_idE,config_idP, escritorio, listaclientes, transaccion)
    listatransac.mostrar_transac()

def listadopuntosa():
    datos = ET.parse(archivo2)
      
    for k in datos.findall('configInicial'):
        trans_id=(k.attrib.get('id'))
    
        trans_idE=(k.attrib.get('idEmpresa'))
        
        trans_idP=(k.attrib.get('idPunto'))
        escritorio_act=k.find('escritoriosActivos')
        
        escritorio=[]
        transaccion=[]
        cantidad=[]
        clientes=[]
        for m in escritorio_act.findall('escritorio'):
            
            escritorio_id=(m.attrib.get('idEscritorio'))
            escritorio.append([escritorio_id])
        clientes_list=k.find('listadoClientes')
        for n in clientes_list.findall('cliente'):
            cliente_dpi=(n.attrib.get('dpi'))
            cliente_nombre=(n.find('nombre').text)
            clientes.append([cliente_dpi, cliente_nombre])
            trans_list=n.find('listadoTransacciones')
            for l in trans_list.findall('transaccion'):
                trans_id=l.attrib.get('idTransaccion')
                trans_cantidad=l.attrib.get('cantidad')
                transaccion.append([cliente_dpi, trans_id, trans_cantidad])

        for i in escritorio:
            listaempresa.activarescritorios(trans_idE,trans_idP,*i)                    
        listaempresa.SeleccionarEmpresa(trans_idE,trans_idP)



# def CrearEmpresa():
#     end = False
#     id_empresa = ""
#     name = ""
#     abrev = ""
#     lista_puntos_atencion = ListaEmpresa()
#     lista_transacciones = ListaEmpresa()
#     print("\n---------- Crear nueva empresas ----------")
#     while(not end):
#         if not(id_empresa):
#             id_empresa = input("Ingrese el ID: ")
#         if not(name):
#             name = input("Ingrese el Nombre: ")
#         if not(abrev):
#             abrev = input("Ingrese abreviatura: ")
        
#         if id_empresa and name and abrev:
            
#             listaempresas.append([id_empresa,name,abrev])
#             #empresa = ListaEmpresa(id_empresa, name, abrev)
            
#             end_1 = False
#             while(not end_1):
#                 punto_atencion = createNewAttention()
#                 lista_puntos_atencion.append(punto_atencion)

#                 print("\n¡Punto de atención añadido!\n¿Desea agregar otro punto de atención?\n 1. Si\n 2. No")
#                 end_2 = False
#                 while(not end_2):
#                     selection = pedirOpcion()
        
#                     if selection == 1:
#                         end_2 = True

#                     elif selection == 2:
#                         #empresa.setPuntosAtencion(lista_puntos_atencion)
#                         end_1 = True
#                         end_2 = True
#                     else:
#                         print("Intente de nuevo")
            
#             end_1 = False
#             while(not end_1):
#                 transaccion = createNewTransaction()
#                 lista_transacciones.append(transaccion)

#                 print("\n¡Transacción creada!\n¿Desea crear una nueva transaccion?\n 1. Si\n 2. No")
#                 end_2 = False
#                 while(not end_2):
#                     selection = pedirOpcion()
        
#                     if selection == 1:
#                         end_2 = True

#                     # elif selection == 2:
#                     #     empresa.setTransacciones(lista_transacciones)
#                     #     end_1 = True
#                     #     end_2 = True
#                     else:
#                         print("Intente de nuevo")
#             return listaempresas

#         else:
#             print("\n¡Ingrese todos los datos requeridos!")
#     listaempresa.insertar_empresa(id_empresa,name,abrev,listapuntos,listaescritorios)
# def createNewAttention():
#     global id_punto
#     id_punto = ""
#     name = ""
#     direccion = ""
#     lista_escritorio = LinkedList()
#     print("\n---------- Crear Punto de atención ----------")
#     while True:
#         if not(id_punto):
#             id_punto = input("Ingrese el ID: ")
#         if not(name):
#             name = input("Ingrese el Nombre: ")
#         if not(direccion):
#             direccion = input("Ingrese direccion: ")
        
#         if id_punto and name and direccion:
#             listapuntos.append([id_punto,name,direccion])
#             #punto_atencion = Attention(id_punto, name, direccion)

#             while True:
#                 escritorio = createNewDesktop()
#                 lista_escritorio.append(escritorio)
#                 print("\n¡Escritorio de atención añadido!\n¿Desea agregar otro Escritorio de atención?\n 1. Si\n 2. No")
                
#                 end_2 = False
#                 while(not end_2):
#                     selection = pedirOpcion()

#                     if selection == 1:
#                         end_2 = True

#                     # elif selection == 2:
#                     #     # punto_atencion.setListaEscritorio(lista_escritorio)
#                     #     # return punto_atencion
#                     # else:
#                     #     print("Intente de nuevo")
                

#         else:
#             print("¡Ingrese todos los datos requeridos!")

# def createNewDesktop():
#     id = ""
#     identificacion = ""
#     encargado = ""
#     print("\n---------- Crear escritorio de servicio ----------")
#     while True:
#         if not(id):
#             id = input("Ingrese el ID: ")
#         if not(identificacion):
#             identificacion = input("Ingrese la identificación: ")
#         if not(encargado):
#             encargado = input("Ingrese el nombre del encargado: ")
        
#         if id and identificacion and encargado:
#             listaescritorios.append([id_punto,id,identificacion,encargado])
#             #escritorio = Desktop(id, identificacion, encargado)
#             return listaescritorios
#         else:
#             print("¡Ingrese todos los datos requeridos!")

# def createNewTransaction():
#     id = ""
#     name = ""
#     tiempoAtencion = ""
#     print("\n---------- Crear nueva transaccion ----------")
#     while True:
#         if not(id):
#             id = input("Ingrese el ID: ")
#         if not(name):
#             name = input("Ingrese la identificación: ")
#         if not(tiempoAtencion):
#             tiempoAtencion = input("Ingrese el tiempo de atencion: ")
        
#         if id and name and tiempoAtencion:
#             transaccion = Transaction(id, name, tiempoAtencion)
#             return transaccion
#         else:
#             print("¡Ingrese todos los datos requeridos!")

# a=input("¿Cargar un Archivo? Y/N")
# if a == "Y":
#     filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", "*.xml*"), ("Todos los archivos",".*")))
#     docxml = minidom.parse(filename)
#     empresa = docxml.getElementsByTagName('empresa')
#     for i in empresa:
#         nombre = i.getElementsByTagName('nombre')
#         abreviatura = i.getElementsByTagName('abreviatura')
#         nombre1=i.getElementsByTagName('nombre')

#         print(nombre[0].firstChild.data)  
#         print(abreviatura[0].firstChild.data)
#         print(nombre1[1].firstChild.data) 
        # puntoatencion=docxml.getElementsByTagName('puntoAtencion')
        # for j in puntoatencion:
        #     nombrepunto = j.getElementsByTagName('nombre')
        #     direccionpunto = j.getElementsByTagName('direccion')
        #     print(nombrepunto[0].firstChild.data)  
        #     print(direccionpunto[0].firstChild.data) 
        #     escritorio=docxml.getElementsByTagName('escritorio')
        #     for k in escritorio:
        #         identificacion = k.getElementsByTagName('indentificacion')
        #         encargado = k.getElementsByTagName('encargado') 
        #         print(identificacion[0].firstChild.data)  
        #         print(encargado[0].firstChild.data)
        #         break
    # puntoatencion=docxml.getElementsByTagName('puntoAtencion')
    # for i in puntoatencion:
    #     nombrepunto = i.getElementsByTagName('nombre')
    #     direccionpunto = i.getElementsByTagName('direccion')
    #     print(nombrepunto[0].firstChild.data)  
    #     print(direccionpunto[0].firstChild.data)
    # escritorio=docxml.getElementsByTagName('escritorio')
    # for i in escritorio:
    #     identificacion = i.getElementsByTagName('indentificacion')
    #     encargado = i.getElementsByTagName('encargado') 
    #     print(identificacion[0].firstChild.data)  
    #     print(encargado[0].firstChild.data)
    # transaccion=docxml.getElementsByTagName('transaccion')    
    # for i in transaccion:
    #     nombretransac = i.getElementsByTagName('nombre')
    #     tiempoatencion = i.getElementsByTagName('tiempoAtencion')   

    
