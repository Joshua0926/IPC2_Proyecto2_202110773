from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
from lista_empresa import ListaEmpresa
from nodo import LinkedList
from lista_empresa import Business
from lista_empresa import Attention
from lista_empresa import Desktop
from lista_empresa import Transaction
from lista_empresa import Stack
listaempresa = ListaEmpresa()



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
        \n---------- Configuración de empresas ----------\n 1. Limpiar sistema\n 2. Cargar archivo (Configuracion sistema)\n 3. Crear nueva empresa\n 4. Cargar archivo (Configuración inicial)\n 5. Regresar""")
        selection = pedirOpcion()
        
        # VACIA LA LISTA DE LOS DATOS
        if selection == 1:
            ListaEmpresa().eliminardatos
            
            
            
            # configuracion_inicial.eliminardatos()
            print("¡Datos eliminados")

        elif selection == 2:
            subirArchivo()

        elif selection == 3:
            end_1 = False

            while(not end_1):
                correct = False
                empresa = CrearEmpresa()
                lista_empresas.append(empresa)

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

        
        elif selection == 5:
            end = True
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
    listatransacciones=[]


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
                listaescritorios.append([IdPuntos,IdEscritorio,IdentificacionEscritorio,EncargadoEscritorio])



            # transacciones = x.find('listaTransacciones')

            # for a in transacciones.findall('transaccion'):
            #     print('ID Transaccion: '+a.attrib.get('id')) 
            #     print('Nombre Transaccion: '+a.find('nombre').text) 
            #     print('Tiempo Atencion: '+a.find('tiempoAtencion').text)
            #     listatransacciones.append([a.attrib.get('id'),a.find('nombre').text,a.find('tiempoAtencion').text])
            #     print("-----------------------------------------")
        empresa = CrearEmpresa()
        listaempresa.append(empresa)
        #listaempresa.append(IdEmpresa,NombreEmpresa,AbrevEmpresa,listapuntos,listaescritorios)
    listaempresa.mostrar_empresa()
    # print("***********************************")
    # print(listaempresas)
    # print(listapuntos)
    # print(listaescritorios)
    # print(listatransacciones)

def CrearEmpresa():
    end = False
    id_empresa = ""
    name = ""
    abrev = ""
    lista_puntos_atencion = ListaEmpresa()
    lista_transacciones = ListaEmpresa()
    print("\n---------- Crear nueva empresas ----------")
    while(not end):
        if not(id_empresa):
            id_empresa = input("Ingrese el ID: ")
        if not(name):
            name = input("Ingrese el Nombre: ")
        if not(abrev):
            abrev = input("Ingrese abreviatura: ")
        
        if id_empresa and name and abrev:
            
            empresa = Business(id_empresa, name, abrev)
            
            end_1 = False
            while(not end_1):
                punto_atencion = createNewAttention()
                lista_puntos_atencion.append(punto_atencion)

                print("\n¡Punto de atención añadido!\n¿Desea agregar otro punto de atención?\n 1. Si\n 2. No")
                end_2 = False
                while(not end_2):
                    selection = pedirOpcion()
        
                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        empresa.setPuntosAtencion(lista_puntos_atencion)
                        end_1 = True
                        end_2 = True
                    else:
                        print("Intente de nuevo")
            
            end_1 = False
            while(not end_1):
                transaccion = createNewTransaction()
                lista_transacciones.append(transaccion)

                print("\n¡Transacción creada!\n¿Desea crear una nueva transaccion?\n 1. Si\n 2. No")
                end_2 = False
                while(not end_2):
                    selection = pedirOpcion()
        
                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        empresa.setTransacciones(lista_transacciones)
                        end_1 = True
                        end_2 = True
                    else:
                        print("Intente de nuevo")
            return empresa

        else:
            print("\n¡Ingrese todos los datos requeridos!")

def createNewAttention():
    id_punto = ""
    name = ""
    direccion = ""
    lista_escritorio = LinkedList()
    print("\n---------- Crear Punto de atención ----------")
    while True:
        if not(id_punto):
            id_punto = input("Ingrese el ID: ")
        if not(name):
            name = input("Ingrese el Nombre: ")
        if not(direccion):
            direccion = input("Ingrese direccion: ")
        
        if id_punto and name and direccion:
            punto_atencion = Attention(id_punto, name, direccion)

            while True:
                escritorio = createNewDesktop()
                lista_escritorio.append(escritorio)
                print("\n¡Escritorio de atención añadido!\n¿Desea agregar otro Escritorio de atención?\n 1. Si\n 2. No")
                
                end_2 = False
                while(not end_2):
                    selection = pedirOpcion()

                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        punto_atencion.setListaEscritorio(lista_escritorio)
                        return punto_atencion
                    else:
                        print("Intente de nuevo")
                

        else:
            print("¡Ingrese todos los datos requeridos!")

def createNewDesktop():
    id = ""
    identificacion = ""
    encargado = ""
    print("\n---------- Crear escritorio de servicio ----------")
    while True:
        if not(id):
            id = input("Ingrese el ID: ")
        if not(identificacion):
            identificacion = input("Ingrese la identificación: ")
        if not(encargado):
            encargado = input("Ingrese el nombre del encargado: ")
        
        if id and identificacion and encargado:
            escritorio = Desktop(id, identificacion, encargado)
            return escritorio
        else:
            print("¡Ingrese todos los datos requeridos!")

def createNewTransaction():
    id = ""
    name = ""
    tiempoAtencion = ""
    print("\n---------- Crear nueva transaccion ----------")
    while True:
        if not(id):
            id = input("Ingrese el ID: ")
        if not(name):
            name = input("Ingrese la identificación: ")
        if not(tiempoAtencion):
            tiempoAtencion = input("Ingrese el tiempo de atencion: ")
        
        if id and name and tiempoAtencion:
            transaccion = Transaction(id, name, tiempoAtencion)
            return transaccion
        else:
            print("¡Ingrese todos los datos requeridos!")

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

    
