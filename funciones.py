from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
from lista_empresa import ListaEmpresa
from lista_transacciones import listatrans
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
        \n---------- Configuración de empresas ----------\n 1. Limpiar sistema\n 2. Cargar archivo (Configuracion sistema)\n 3. Crear nueva empresa\n 4. Cargar archivo (Configuración inicial)\n 5. Regresar""")
        selection = pedirOpcion()
        
        # VACIA LA LISTA DE LOS DATOS
        if selection == 1:
            listaempresa.eliminardatos()
            listatransac.eliminardatos()
          
            
            
            
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
            CrearCliente()
            end = True

        elif selection == 6:
            listaempresa.dibujarGrafica()
            listatransac.dibujarGraficaClientes()
        elif selection == 7:
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



        
        listaempresa.insertar_empresa(IdEmpresa,NombreEmpresa,AbrevEmpresa,listapuntos,listaescritorios, listatransacciones)
    listaempresa.mostrar_empresa()
   





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

def CrearCliente():
    listanuevacliente=[]
    print(" Crear Nueva Cliente")
    print("Ingrese el ID de la Configuración a la que lo desea ingresar")
    idcreatecliente=input()
    print("Ingrese el Nombre")
    idcreateempresa=input()
    print("Ingrese la Abreviatura")
    idcreatepunto=input()
    #listanuevaempresa.append([idcreate,namecreate,abrevcreate])
    listanuevosclientes=[]
    listadonuevastransacciones=[]
    print("Ingrese id Escritorio")
    idEsc=input()
    print("Ingrese el número de Clientes")
    natecreate=input()
    puntcreate=0
    for nat in range(int(natecreate)):
        puntcreate+=1
        print("Ingrese el DPI del Cliente ",puntcreate)
        dpicreateate=input()
        print("Ingrese el Nombre del Cliente ",puntcreate)
        namecreatecliente=input()
        print("Ingrese el número de transacciones que desea para el cliente ",puntcreate)
        listanuevosclientes.append([dpicreateate,namecreatecliente])
        numdcreate=input()
        contdeskcreate=0
        for numc in range(int(numdcreate)):
            contdeskcreate+=1
            print("Ingrese el Id transaccion ",contdeskcreate)
            idtranscreate=input()
            print("Ingrese el cantidad de la transaccion ",contdeskcreate)
            cantidadcreate=input()
            listadonuevastransacciones.append([dpicreateate,idtranscreate,cantidadcreate])
           
        listatransac.insertar_trans(idcreatecliente,idcreateempresa,idcreatepunto,idEsc, listanuevosclientes, listadonuevastransacciones)
    listatransac.mostrar_transac()



def CargarTrans(): 
     
    global archivo2
    archivo2 = fd.askopenfilename(initialdir="C:/", title="abrir", filetypes=(("XML files",".XML"),("Todos los archivos",".*"))) 
    datos = ET.parse(archivo2) 
    ruta = datos.getroot()

    listaconfi=[]
    

    for k in datos.findall('configInicial'): 
        global config_id
        global config_idE
        global config_idP
        config_id=(k.attrib.get('id')) 
        config_idE=(k.attrib.get('idEmpresa')) 
        config_idP=(k.attrib.get('idPunto')) 
       
        escritorio_act=k.find('escritoriosActivos') 
      
        escritorio=[] 
        
        
        for m in escritorio_act.findall('escritorio'): 
            escritorio_id=m.attrib.get('idEscritorio') 
            escritorio.append([escritorio_id]) 
        clientes_list=k.find('listadoClientes') 

        listaclientes=[]
        nombreclientes=[]
        transaccion=[] 
        
        for n in clientes_list.findall('cliente'): 
            cliente_dpi=n.attrib.get('dpi') 
            cliente_nombre=n.find('nombre').text 
            listaclientes.append([cliente_dpi,cliente_nombre])
          
            trans_list=n.find('listadoTransacciones') 
        
            for l in trans_list.findall('transaccion'): 
                trans_id=l.attrib.get('idTransaccion') 
                trans_cantidad=l.attrib.get('cantidad') 
                transaccion.append([cliente_dpi,trans_id,trans_cantidad]) 
             

    
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


