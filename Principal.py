from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd


cont =0
filename = fd.askopenfilename(initialdir="C:/", title="Select a File", filetypes=(("Text files", ".xml"), ("Todos los archivos",".*")))
docxml = ET.parse(filename)
root = docxml.getroot()


listaIDCliente=[]
listaempresas =[]
listapuntos =[]
listaescritorios=[]
listatransacciones=[]


for x in root.findall('empresa'):
    # print("ID: "+ x.attrib.get('id'))
    # print("Nombre: "+ x.find('nombre').text)
    # print("Abreviatura: "+ x.find('abreviatura').text)
    listaIDCliente.append(x.attrib.get('id'))



for i in listaIDCliente:
    for x in root.findall('.//empresa[@id="'+i+'"]'):
        print("ID Empresa: "+ x.attrib.get('id'))
        print("Nombre Empresa: "+ x.find('nombre').text)
        print("Abreviatura Empresa: "+ x.find('abreviatura').text)
        listaempresas.append([x.attrib.get('id'),x.find('nombre').text,x.find('abreviatura').text])

        PuntosAtencion = x.find('listaPuntosAtencion')

        for y in PuntosAtencion.findall('puntoAtencion'):
            print('ID Punto de Atencion: '+y.attrib.get('id')) 
            print('NOMBRE Punto de Atencion: '+y.find('nombre').text) 
            print('Direccion Punto de Atencion: '+y.find('direccion').text)
            listapuntos.append([y.attrib.get('id'),y.find('nombre').text,y.find('direccion').text])

            escritorios = y.find('listaEscritorios')

            for z in escritorios.findall('escritorio'):
                print('ID Escritorio: '+z.attrib.get('id')) 
                print('Identificacion Escritorio: '+z.find('identificacion').text) 
                print('Encargado Escritorio: '+z.find('encargado').text)
                listaescritorios.append([z.attrib.get('id'),z.find('identificacion').text,z.find('encargado').text])



        transacciones = x.find('listaTransacciones')

        for a in transacciones.findall('transaccion'):
            print('ID Transaccion: '+a.attrib.get('id')) 
            print('Nombre Transaccion: '+a.find('nombre').text) 
            print('Tiempo Atencion: '+a.find('tiempoAtencion').text)
            listatransacciones.append([a.attrib.get('id'),a.find('nombre').text,a.find('tiempoAtencion').text])
            print("-----------------------------------------")

print("***********************************")
print(listaempresas)
print(listapuntos)
print(listaescritorios)
print(listatransacciones)




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

    
