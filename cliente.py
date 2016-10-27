from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import sys, time
from PyQt4 import QtCore, QtGui, uic


class Cliente(QtGui.QMainWindow):
    def __init__(self): 
        super(Cliente, self).__init__()
        uic.loadUi('cliente.ui', self)
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.clicked.connect(self.focus)
        self.pushButton.clicked.connect(self.ping)
        self.pushButton_2.clicked.connect(self.participar)
        self.cliente = object()
        self.setFocus()
        self.show()


    def ping(self):
        servidor = self.lineEdit.text()
        puerto = self.spinBox_4.value()
        url = str(servidor)+":"+str(puerto)
        self.cliente = xmlrpc.client.ServerProxy('http://localhost:1')
        try: 
            pong = self.cliente.ping()
            self.pushButton.setText("pinging...")
            if pong == "¡Pong!":
                self.pushButton.setText("¡Pong!")
        except:        
            self.pushButton.setText("No pong :c")


    def participar(self):
            part = self.cliente.yo_juego()
            print(part)
            print(part["id"])
            print(part["color"])
            self.lineEdit_2.setText(str(part["id"]))
            self.lineEdit_3.setText(str(part["color"]))
            color = "'color: "+"rgb("+str(part["color"]["r"])+", "+str(part["color"]["b"])+", "+str(part["color"]["r"])+");'"
            print(color)
            self.lineEdit_3.setStyleSheet(color)

            #self.lineEdit_3.setStyleSheet("color: rgb(255, 0, 255);")





    def focus(self):
      self.setFocus()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    serv = Cliente()
    sys.exit(app.exec_())     