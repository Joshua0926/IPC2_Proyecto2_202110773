from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
from lista_empresa import listaempresa
listaempresa = listaempresa()



cont =0
filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", ".xml"), ("Todos los archivos",".*")))
docxml = ET.parse(filename)
root = docxml.getroot()


listaIDCliente=[]
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
    listapuntos =[]
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

    listaempresa.insertar_empresa(IdEmpresa,NombreEmpresa,AbrevEmpresa,listapuntos,listaescritorios)
listaempresa.mostrar_empresa()
# print("***********************************")
# print(listaempresas)
# print(listapuntos)
# print(listaescritorios)
# print(listatransacciones)




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

    
