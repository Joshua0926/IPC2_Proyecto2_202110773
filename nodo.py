class Nodo():
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

    def getsiguiente(self):
        return self .siguiente


    def setsiguiente(self, siguiente):
        self.siguiente=siguiente

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last = None

#     # VERIFICAMOS SI LA LISTA ESTA VACÍA
#     def emply(self):
#         return self.head
    
#     # AGREGAMOS LOS DATOS AL FINAL
#     def append(self, dato):
#         nodo = Nodo(dato)
#         if not self.emply():
#             self.head = nodo
#             self.last = nodo
#         else:
#             self.last.siguiente = nodo
#             nodo.anterior = self.last
#             self.last = nodo
    
#     # RETORNAR EL NÚMERO DE ELEMENTOS
#     def length(self):
#         n = 0
#         i = self.head
#         while i:
#             i = i.siguiente
#             n+=1
#         return n

#     # BUSCAMOS UN DATO EN ESPECIFICO POR SU POSICION
#     def searchDate(self, selection):
#         n = 1
#         i = self.head
#         while i:
#             if selection == n:
#                 return i.dato
#             else:
#                 n +=1 
#                 i = i.siguiente
#         return False
    
#     def eliminardatos(self):
#         if self.length() > 0:
#             self.head = None
#             self.last = None

