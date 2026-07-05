class nodo():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class linkedList():
    def __init__(self):
        self.head = None
        
    def AddFirst(self, valor):
        nuevo = nodo(valor)
        nuevo.next = self.head
        self.head = nuevo
        
    def AddLast(self, valor):
        nuevo = nodo(valor)
        if self.head == None:
            self.head = nuevo
            
        if self.head is not None:
            puntero = self.head
            while puntero != None:
                puntero = puntero.next
            if puntero == None:
                self.head.next = nuevo
                
    def valueInPosition(self, position):
        indice = 1
        puntero = self.head
        while puntero != None:
            valor = puntero.value
            if position == indice:
                return "el valor en la posicion ", position, "es: ", valor
            puntero = puntero.next
            indice += 1
        if puntero == None: 
            return "indice no encontrado"
        
    def positionInvalue(self, valor):
        indice = 1
        puntero = self.head
        while puntero != None:
            if puntero.value == valor:
                return valor,  "se encuentra en el lugar", indice 
                break
            puntero = puntero.next
            indice += 1
            
    def insertInPosition(self, valor, position):
        nuevo = nodo(valor)
        indice = 1
        puntero = self.head
        
        if position == 1:
            nuevo.next = self.head
            self.head = nuevo
        
        while puntero != None:
            if position - 1 == indice:
                nuevo.next = puntero.next
                puntero.next = nuevo
            puntero = puntero.next
            indice += 1 
            
    def lenght(self):
        numero = 0
        puntero = self.head
        while puntero != None:
            puntero = puntero.next
            numero += 1
        return numero
    
    def deletefirst(self):
        self.head = self.head.next
        
    def deleteLast(self):
        puntero = self.head
        while puntero.next.next != None:
            puntero = puntero.next
        puntero.next = None
        
    def deleteinposition(self, position):
        if self.head == None:
            print("lista vacia")
            return
        
        if position == 1:
            self.head = self.head.next
            return
        
        indice = 1
        puntero = self.head
        encontrado = False
        
        while puntero != None and puntero.next != None:
            
            if indice == position - 1:
                puntero.next = puntero.next.next
                encontrado = True
                
            puntero = puntero.next
            indice += 1
            
        if encontrado == False:
            print("no hay nodos ahi ")
        
        
        
    

        
    def recorrer(self):
        puntero = self.head
        while puntero != None:
            print(puntero.value)
            puntero = puntero.next
            
            
mylist = linkedList()

mylist.AddFirst(30)
mylist.AddFirst(20)
mylist.AddFirst(10)
mylist.insertInPosition(5,1)
mylist.recorrer()
mylist.deleteinposition(9999)
print("despues")
mylist.recorrer()


