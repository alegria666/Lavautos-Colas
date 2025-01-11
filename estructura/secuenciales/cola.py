#Daniel Esteban Alegría Zamora

class NodoLSE:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
    
    def __str__(self):
        return(str(self.dato))
   
class Cola:
    # '''Clase que implementa el funcionamiento del TAD Cola.
    # '''
    def __init__(self):
        # '''Método que realiza la creación e inicialización de la cola.
        # '''
        self.inicio = None


    def es_vacia(self):
        # '''Método que verifica si la cola se encuentra vacía.
        # :returns: True si la cola es vacía. False en caso contrario.
        # :rtype: bool
        # '''
        if self.inicio is not None:
            return False
        return True

    def encolar(self, nuevo_dato):
        # '''Método que adiciona un nuevo nodo con su dato al final de la cola.
        # Realizar la validación de Homogeneidad para cada dato ingresado a la
        # cola.
        # :returns: True si nuevo_dato fue encolado. False en caso contrario.
        # :rtype: bool
        # '''
        if self.es_vacia():
            self.inicio= NodoLSE(nuevo_dato)
            return True
        elif isinstance(nuevo_dato, type(self.inicio.dato)):
            actual = self.inicio
                    
            while actual.sig:
                actual = actual.sig
            actual.sig= NodoLSE(nuevo_dato)
            return True
        else:
            return False

    def desencolar(self):
            # '''Método que saca/quita el primer nodo (elimina el nodo) de la cola y
            # retorna su dato.
            # :returns: El dato del primer nodo de la Cola y None en caso de que la
            # cola esté vacía.
            # :rtype: object
            # '''
        aux = None
        if self.es_vacia():
            return aux
        else:
            aux = self.inicio.dato
            self.inicio = self.inicio.sig
            return aux

    def frente(self):
        # '''Método que retorna el dato del primer nodo de la cola, sin quitarlo
        # de la misma.
        # :returns: El dato del primer nodo en la cola y None en caso de que la
        # cola esté vacía.
        # :rtype: object
        # '''
        if self.es_vacia():
            return None
        else:
            return self.inicio.dato

    def __len__(self):
        # '''Método que retorna del número de elementos que contiene la cola.
        # :returns: Tamaño de la cola
        # :rtype: int
        # '''
        tam=0
        actual = self.inicio
        while actual:
            actual = actual.sig
            tam+=1
        return tam

