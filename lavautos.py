#Daniel Esteban Alegría Zamora


import sys

from estructura.secuenciales.cola import Cola
from PyQt6.QtWidgets import (QApplication,QPushButton,
    QLabel, QMessageBox, QWidget,
    QLineEdit,QMainWindow, QComboBox)
from PyQt6.QtGui import *

class Vehiculo:
    def __init__(self,dueño,placa,tipo):
        self.dueño=dueño
        self.placa=placa
        self.tipo=tipo
    def __str__(self):
        return f"El usuario {self.dueño} con tipo de vehículo: {self.tipo}, de placa: {self.placa}"

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,450,450)
        self.setWindowTitle("LAVAUTOS")
        self.generar_formulario()
        self.show()
        self.car=Cola()
        self.mot=Cola()
        self.cam=Cola()

    def generar_formulario(self): 
        label = QLabel(self)
        label.setGeometry(0,0,450,450)
        label.setStyleSheet("background:QLinearGradient(x1:0,y1:0,x2:1,y2:0,stop: 0 #73c6b6,stop: 1 #f39c12)")

        imagen = QPixmap("imagenes/welcome.png").scaled(165, 125)
        label1 = QLabel(self)
        label1.setGeometry(160,0,450,52)
        label1.move(140,0)
        label1.setPixmap(imagen)
        
        imagen = QPixmap("imagenes/acqua.png").scaled(100,100)
        labela = QLabel(self)
        labela.move(350,360)
        labela.setPixmap(imagen)
        
        font=QFont('Algerian',8,5)
        labela1 = QLabel(self)
        labela1.move(370,400)
        labela1.setText("LAVAUTOS\n      DANY")
        labela1.setStyleSheet("color: white")
        labela1.setFont(font)
        
        
        user_label=QLabel(self)
        user_label.setText("Usuario:")
        user_label.move(65,55)
#-------ingreso datos----------------------------------------------------
        self.user_input=QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(120,54)
        self.user_input.setStyleSheet("background:QLinearGradient(x1:0,y1:0,x2:1,y2:0,stop: 0 #FFFFFF,stop: 1  #839192 )")

        placa_label=QLabel(self)
        placa_label.setText("Placa:")
        placa_label.move(78,90)

        self.placa_input=QLineEdit(self)
        self.placa_input.resize(250,24)
        self.placa_input.move(120,86)
        self.placa_input.setStyleSheet("background:QLinearGradient(x1:0,y1:0,x2:1,y2:0,stop: 0 #FFFFFF,stop: 1  #839192 )")

        tipo_label=QLabel(self)
        tipo_label.setText("Tipo de vehiculo:")
        tipo_label.move(20,122)

        self.tipo_input = QComboBox(self)
        self.tipo_input.addItems(["Carro", "Moto", "Camion"])
        self.tipo_input.resize(250, 24)
        self.tipo_input.move(120, 118)
        self.tipo_input.setStyleSheet("background: QLinearGradient(x1:0, y1:0, x2:1, y2:0, stop: 0 #FFFFFF, stop: 1 #839192);")
#-------Botones------------------------------------------------
        font=QFont('Arial Black',7,5)
        intro_label=QLabel(self)
        intro_label.setText("Seleccione una opción:")
        intro_label.resize(200,24)
        intro_label.move(175,154)
        intro_label.setFont(font)

        ingresar_label=QLabel(self)
        ingresar_label.setText("INGRESAR")
        ingresar_label.move(20,182)
        
        ingresar_button=QPushButton(self)
        ingresar_button.resize(50,50)
        ingresar_button.move(20,214)
        ingresar_button.clicked.connect(self.ingresar)
        

        imagen = QPixmap("imagenes/ingresar.png")
        scaled = imagen.scaled(60,60)
        icon = QIcon(scaled)
        ingresar_button=QPushButton('',self)
        ingresar_button.resize(50,50)
        ingresar_button.move(20,214)
        ingresar_button.setStyleSheet("background: #73c6b6")
        ingresar_button.clicked.connect(self.ingresar)
        ingresar_button.setIcon(icon)

        


        salida_label=QLabel(self)
        salida_label.setText("SALIDA")
        salida_label.move(105,182)

        imagen = QPixmap("imagenes/salida.png")
        scaled = imagen.scaled(70,70)
        icon = QIcon(scaled)
        salida_button=QPushButton(self)
        salida_button.resize(50,50)
        salida_button.move(100,214)
        salida_button.setStyleSheet("background: #73c6a4")
        salida_button.clicked.connect(self.salir)
        salida_button.setIcon(icon)

        primero_label=QLabel(self)
        primero_label.setText("COLA")
        primero_label.move(292,182)

        imagen = QPixmap("imagenes/cola.png")
        scaled = imagen.scaled(60,60)
        icon = QIcon(scaled)
        lista_button=QPushButton(self)
        lista_button.resize(50,50)
        lista_button.move(285,214)
        lista_button.setStyleSheet("background:  #f3ab12")
        lista_button.clicked.connect(self.lista)
        lista_button.setIcon(icon)

        faltan_label=QLabel(self)
        faltan_label.setText("TOTAL")
        faltan_label.move(372,182)

        imagen = QPixmap("imagenes/lista.png")
        scaled = imagen.scaled(60,60)
        icon = QIcon(scaled)
        faltan_button=QPushButton(self)
        faltan_button.resize(50,50)
        faltan_button.move(365,214)
        faltan_button.setStyleSheet("background: #f39c12")
        faltan_button.clicked.connect(self.todos)
        faltan_button.setIcon(icon)

        
        self.ver_label=QLabel(self)
        self.ver_label.move(20,280)
        self.ver_label.resize(450,100)
#-------operaciones--------------------------------------------------------------------------------------- 
    def ingresar(self):#Ingresa los vehiculos a su respectiva cola
        dueño=self.user_input.text()
        placa=self.placa_input.text()
        tipo=self.tipo_input.currentText()
        if dueño !="" and placa !="" and tipo !="":
            veh=Vehiculo(dueño,placa,tipo)
            if tipo.casefold()=="Carro".casefold():
                self.car.encolar(veh)
                QMessageBox.information(self,"ENHORABUENA" ,"Su carro esta en la cola, su turno es: "+str(len(self.car))+ "\nPor favor espere.",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok) 
                self.user_input.setText("")
                self.placa_input.setText("")
                
                self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))          
            elif tipo.casefold()=="Moto".casefold():
                self.mot.encolar(veh)
                QMessageBox.information(self,"ENHORABUENA" ,"Su moto esta en la cola, su turno es: "+str(len(self.mot))+ "\nPor favor espere.",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.user_input.setText("")
                self.placa_input.setText("")
                
                self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))         
            elif tipo.casefold()=="Camion".casefold():
                self.cam.encolar(veh)
                QMessageBox.information(self,"ENHORABUENA" ,"Su camion esta en la cola, su turno es: "+str(len(self.cam)) +"\nPor favor espere.",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.user_input.setText("")
                self.placa_input.setText("")
                
                self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))        
            else:
                QMessageBox.warning(self,"ADVERTENCIA" ,"Escriba un tipo de vehiculo valido (Moto, Carro, Camion), para ponerlo en la cola",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
                self.user_input.setText("")
                self.placa_input.setText("")
                
                self.ver_label.setText("Los primeros son"+
                                       "\nCarros: "+str(self.car.frente())+
                                       "\n"+str(self.mot.frente())+
                                       "\n"+str(self.cam.frente()))  
        else:
            QMessageBox.warning(self,"ADVERTENCIA" ,"Por favor llenar los datos",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
            self.user_input.setText("")
            self.placa_input.setText("")
            
            self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))
    def salir(self):#Saca los vehiculos de  la cola escogida
        placa=self.placa_input.text()
        tipo=self.tipo_input.currentText()
        if tipo !="":
            if tipo.casefold()=="Carro".casefold():
                if self.car.es_vacia():
                    QMessageBox.warning(self,"ADVERTENCIA" ,"No hay ningun carro en esta cola",
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                    self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))
                else:
                    QMessageBox.information(self,"ENHORABUENA" ,str(self.car.desencolar())+" esta listo para ser retirado.\nVuelva pronto. :)",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                    self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))
            elif tipo.casefold()=="moto".casefold():
                if self.mot.es_vacia():
                    QMessageBox.warning(self,"ADVERTENCIA" ,"No hay ninguna moto en esta cola",
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                    self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))
                else:
                    QMessageBox.information(self,"ENHORABUENA" ,str(self.car.desencolar())+" esta listo para ser retirado.\nVuelva pronto. :)",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                    self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))


            elif tipo.casefold()=="Camion".casefold():
                if self.cam.es_vacia():
                    QMessageBox.warning(self,"ADVERTENCIA" ,"No hay ningun camion en esta cola",
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                    self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))
                else:
                    QMessageBox.information(self,"ENHORABUENA" ,str(self.cam.desencolar())+" esta listo para ser retirado.\nVuelva pronto. :)",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                    self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente())) 
            else:
                QMessageBox.warning(self,"ADVERTENCIA" ,"Escriba la placa y el tipo de vehiculo valido (Moto, Carro, Camion)",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
                self.user_input.setText("")
                self.placa_input.setText("")
                
                self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))
        else:
            QMessageBox.warning(self,"ADVERTENCIA" ,"Por favor llenar el tipo de vehiculo (Moto, Carro, Camion)",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
            self.user_input.setText("")
            self.placa_input.setText("")
            
            self.ver_label.setText("<b>Encabezan la lista:</b>"+
                                       "<br><i>Carros:</i> " + str(self.car.frente()) +
                                       "<br><i>Motos:</i> " + str(self.mot.frente()) +
                                       "<br><i>Camiones:</i> " + str(self.cam.frente()))


    def lista(self):#muestre La lista del tipo escogido
        tipo=self.tipo_input.currentText()
        if tipo !="":
            if tipo.casefold()=="Carro".casefold():
                if self.car.es_vacia():
                    QMessageBox.information(self,"ENHORABUENA" ,"Aun no hay nadie en la cola, usted puede ser el primero",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                else:
                    cont=1
                    actual = self.car.inicio
                    datos = "La lista de "+str(tipo)+"s es: \n"
                    while actual:
                        dat=str(cont)+". "+str(actual)+"\n"
                        datos=datos + dat
                        actual = actual.sig
                        cont+=1
                    QMessageBox.information(self,"Lista de "+str(tipo) ,datos,
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                              
            elif tipo.casefold()=="moto".casefold():
                if self.mot.es_vacia():
                    QMessageBox.information(self,"ENHORABUENA" ,"Aun no hay nadie en la cola, usted puede ser el primero",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                else:
                    cont=1
                    actual = self.mot.inicio
                    datos = "La lista de "+str(tipo)+"s es: \n"
                    while actual:
                        dat=str(cont)+". "+str(actual)+"\n"
                        datos=datos + dat
                        actual = actual.sig
                        cont+=1
                    QMessageBox.information(self,"Lista de "+str(tipo) ,datos,
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
            elif tipo.casefold()=="Camion".casefold():
                if self.cam.es_vacia():
                    QMessageBox.information(self,"ENHORABUENA" ,"Aun no hay nadie en la cola, usted puede ser el primero",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                else:
                    cont=1
                    actual = self.cam.inicio
                    datos = "La lista de "+str(tipo)+"es es: \n"
                    while actual:
                        dat=str(cont)+". "+str(actual)+"\n"
                        datos=datos + dat
                        actual = actual.sig
                        cont+=1
                    QMessageBox.information(self,"Lista de "+str(tipo) ,datos,
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
            else:
                QMessageBox.warning(self,"ADVERTENCIA" ,"Escriba un tipo de vehiculo valido (Moto, Carro, Camion)",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
                self.user_input.setText("")
                self.placa_input.setText("")
                
        else:
            QMessageBox.warning(self,"ADVERTENCIA" ,"Por favor llenar el tipo de vehiculo (Moto, Carro, Camion), para consultar la fila que desea saber",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
            self.user_input.setText("")
            self.placa_input.setText("")
            
            
    def todos(self):#Cuenta los vehiculos de la cola escogida
        tipo=self.tipo_input.currentText()
        if tipo !="":
            if tipo.casefold()=="Carro".casefold():
                if self.car.es_vacia():
                    QMessageBox.information(self,"INFORMACION" ,"Aun no hay nadie en esta cola",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                                    
                else:
                    QMessageBox.information(self,"INFORMACION" ,"En la fila de los carros hay "+str(len(self.car))+" turnos",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    

            elif tipo.casefold()=="moto".casefold():
                if self.mot.es_vacia():
                    QMessageBox.information(self,"INFORMACION" ,"Aun no hay nadie en esta cola",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                else:
                    QMessageBox.information(self,"INFORMACION" ,"En la fila de los motos hay "+str(len(self.mot))+" turnos",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                       
            elif tipo.casefold()=="Camion".casefold():
                if self.cam.es_vacia():
                    QMessageBox.information(self,"INFORMACION" ,"Aun no hay nadie en esta cola",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
                else:
                    QMessageBox.information(self,"INFORMACION" ,"En la fila de los camiones hay "+str(len(self.cam))+" turnos",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                    self.user_input.setText("")
                    self.placa_input.setText("")
                    
            else:
                QMessageBox.warning(self,"ADVERTENCIA" ,"Escriba un tipo de vehiculo valido (Moto, Carro, Camion)",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
                self.user_input.setText("")
                self.placa_input.setText("")
                
        else:
            QMessageBox.warning(self,"ADVERTENCIA" ,"Por favor llenar el tipo de vehiculo (Moto, Carro, Camion), para consultar la fila que desea saber",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
            self.user_input.setText("")
            self.placa_input.setText("")
            
            
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
    