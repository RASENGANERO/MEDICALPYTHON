import pymysql
import time
global con 
global cursor
global login
global password
global s
global g
z=int(0)
b=bool(False)
login = str()
password = str()
s=str()
con = pymysql.connect("localhost", "root", "XfHER9aHt10R5GSgIR", "MSC")
cursor = con.cursor()
import sys
import os
from PyQt5 import Qt
from PyQt5.QtWidgets import (QWidget, QLabel,QInputDialog,QDialog,QFormLayout, QDialogButtonBox,QMessageBox,
                             QLineEdit,QGridLayout, QApplication, QTableWidget,QTableWidgetItem,QHeaderView,QComboBox,QPushButton,QAbstractItemView,QSizePolicy)
from PyQt5.QtCore import *
from PyQt5 import *
def connection(login,password):
    try:
        con = pymysql.connect("localhost", login, password, "MSC")
        s="YES" 
        
        cursor.execute("SELECT VERSION()")
        
    except Exception:
        s="NO"
class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel , self);
        layout = QFormLayout(self)
        self.setWindowTitle('Авторизация')
        layout.addRow("Введите логин", self.first)
        layout.addRow("Введите пароль", self.second)
        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)        
    def getInput1(self):
        login=self.first.text()
        return login
    def getInput2(self):
        password=self.second.text()
        return password

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.l1 = QLabel("ID_Договора")
        self.ed1 = QLineEdit()
        self.l2 = QLabel("Дата заключения")
        self.ed2 = QLineEdit()
        self.l3 = QLabel("Вид страховки")
        self.ed3 = QLineEdit()
        self.l4 = QLabel("Сумма страхования")
        self.ed4 = QLineEdit()
        self.l5 = QLabel("Филиал")
        self.ed5 = QLineEdit()
        self.l6 = QLabel("Срок")
        self.ed6 = QLineEdit()
        self.l7 = QLabel("Платёж")
        self.ed7 = QLineEdit()
        self.l8 = QLabel("ID_Клиента")
        self.ed8 = QLineEdit()
        self.name = QLabel("Медицинская страховая компания")
        self.p1 = QPushButton("Добавить")
        self.p2 = QPushButton("Удалить")
        self.p3 = QPushButton("Сбросить")
        self.p4 = QPushButton("Поиск")
        self.p5 = QPushButton("Печать")
        self.p1.clicked.connect(self.add)
        self.p2.clicked.connect(self.delete)
        self.p3.clicked.connect(self.clskey)
        self.p4.clicked.connect(self.find)
        self.p5.clicked.connect(self.printed)
        self.p3.setVisible(False)  
        self.combo = QComboBox(self)
        self.combo.addItems(["Договоры","Клиенты","Вид страхования"])
        self.table = QTableWidget()  #Создаём таблицу
        self.table.cellDoubleClicked.connect(self.edit)
        self.combo.currentIndexChanged.connect(self.my_handler)
        self.combo.currentIndexChanged.connect(self.sect)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sect(8)
        self.setGeometry(QRect(30, 30, 1271, 615))
        self.setWindowTitle('Медицинская страховая компания')
        self.show()
    def add(self):
        columnCount = self.table.columnCount()
        if columnCount==8:
            if self.ed1.text()=="" or self.ed2.text()==""  or self.ed3.text()=="" or self.ed4.text()=="" or self.ed5.text()=="" or self.ed6.text()=="" or self.ed7.text()=="" or self.ed7.text()=="":
             self.editclear()
             msg = QMessageBox()
             msg.setWindowTitle("Информация")
             msg.setText("Одно или несколько полей пустые!")
             result = msg.setStandardButtons(QMessageBox.Ok)
             retval = msg.exec_()
             if retval == QMessageBox.Ok:
                 print()
            else:
                rowPosition = self.table.rowCount()
                self.table.insertRow(rowPosition)
                self.it1 = QTableWidgetItem(self.ed1.text())
                self.it2 = QTableWidgetItem(self.ed2.text())
                self.it3 = QTableWidgetItem(self.ed3.text())
                self.it4 = QTableWidgetItem(self.ed4.text())
                self.it5 = QTableWidgetItem(self.ed5.text())
                self.it6 = QTableWidgetItem(self.ed6.text())
                self.it7 = QTableWidgetItem(self.ed7.text())
                self.it8 = QTableWidgetItem(self.ed8.text())
                self.it1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it6.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it7.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it8.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.table.setItem(self.table.rowCount()-1, 0,self.it1)
                self.table.setItem(self.table.rowCount()-1, 1,self.it2)
                self.table.setItem(self.table.rowCount()-1, 2,self.it3)
                self.table.setItem(self.table.rowCount()-1, 3,self.it4)
                self.table.setItem(self.table.rowCount()-1, 4,self.it5)
                self.table.setItem(self.table.rowCount()-1, 5,self.it6)
                self.table.setItem(self.table.rowCount()-1, 6,self.it7)
                self.table.setItem(self.table.rowCount()-1, 7,self.it8)
                v=str()
                v="INSERT INTO `dogovor` (`id_dogovor`, `date_zakl`, `vid_strah`, `sum_strah`, `filial`, `srok`, `plat`, `client_id`) VALUES ("+self.ed1.text()+","+self.ed2.text()+","+self.ed3.text()
                v=v+","+self.ed4.text()+","+self.ed5.text()+","+self.ed6.text()+","+self.ed7.text()+","+self.ed8.text()+")"
                cursor.execute(v)
                con.commit()
        if columnCount==5:
            if self.ed1.text()=="" or self.ed2.text()==""  or self.ed3.text()=="" or self.ed4.text()=="" or self.ed5.text()=="":
             self.editclear()
             msg = QMessageBox()
             msg.setWindowTitle("Информация")
             msg.setText("Одно или несколько полей пустые!")
             result = msg.setStandardButtons(QMessageBox.Ok)
             retval = msg.exec_()
             if retval == QMessageBox.Ok:
                 os.system("cls")
            else:
                rowPosition = self.table.rowCount()
                self.table.insertRow(rowPosition)
                self.it1 = QTableWidgetItem(self.ed1.text())
                self.it2 = QTableWidgetItem(self.ed2.text())
                self.it3 = QTableWidgetItem(self.ed3.text())
                self.it4 = QTableWidgetItem(self.ed4.text())
                self.it5 = QTableWidgetItem(self.ed5.text())
                self.it1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.table.setItem(self.table.rowCount()-1, 0,self.it1)
                self.table.setItem(self.table.rowCount()-1, 1,self.it2)
                self.table.setItem(self.table.rowCount()-1, 2,self.it3)
                self.table.setItem(self.table.rowCount()-1, 3,self.it4)
                self.table.setItem(self.table.rowCount()-1, 4,self.it5)
                v=str()
                v="INSERT INTO `client` (`id_client`, `fam`, `im`, `otch`, `tel`) VALUES ("+self.ed1.text()+","+self.ed2.text()+","+self.ed3.text()+","+self.ed4.text()+","+self.ed5.text()+")"
                cursor.execute(v)
                con.commit()
        if columnCount==3:
            if self.ed1.text()=="" or self.ed2.text()==""  or self.ed3.text()=="":
             self.editclear()
             msg = QMessageBox()
             msg.setWindowTitle("Информация")
             msg.setText("Одно или несколько полей пустые!")
             result = msg.setStandardButtons(QMessageBox.Ok)
             retval = msg.exec_()
             if retval == QMessageBox.Ok:
                 print()
            else:
                rowPosition = self.table.rowCount()
                self.table.insertRow(rowPosition)
                self.it1 = QTableWidgetItem(self.ed1.text())
                self.it2 = QTableWidgetItem(self.ed2.text())
                self.it3 = QTableWidgetItem(self.ed3.text())
                self.it1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.it3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.table.setItem(self.table.rowCount()-1, 0,self.it1)
                self.table.setItem(self.table.rowCount()-1, 1,self.it2)
                self.table.setItem(self.table.rowCount()-1, 2,self.it3)
                v=str()
                v="INSERT INTO vidstrah (`id_vid`, `namevid`, `strahvznos`) VALUES ("+self.ed1.text()+","+self.ed2.text()+","+self.ed3.text()
                cursor.execute(v)
                con.commit()
        self.editclear()
    def delete(self):
        rows = self.table.selectionModel().currentIndex().row();
        if rows >= 0:
             columnCount = self.table.columnCount()
             item = self.table.item(rows, 0)
             if columnCount==8:
                 g=str(item.text())
                 self.table.model().removeRow(rows)
                 v="DELETE FROM dogovor WHERE id_dogovor = "+g
                 cursor.execute(v)
                 con.commit()
             if columnCount==5:
                 g=str(item.text())
                 self.table.model().removeRow(rows)
                 v="DELETE FROM client WHERE id_client = "+g
                 cursor.execute(v)
                 con.commit()
             if columnCount==3:
                 g=str(item.text())
                 self.table.model().removeRow(rows)
                 v="DELETE FROM vidstrah WHERE id_vid = "+g
                 cursor.execute(v)
                 con.commit()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Внимание!")
            msg.setText("Строка не выбрана!")
            result = msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                os.system("cls")
    def edit(self,row,column):
        columnCount = self.table.columnCount()
        if columnCount==8:
            item = self.table.item(row, column)
            f=str(item.text())
            ok = QInputDialog.getText(self, 'Изменение',
            'Введите новое значение:')
            if ok:
                os.system("cls")
            u=str(ok)
            u=u.replace("('","")
            u=u.replace("', True)","")
            r= QTableWidgetItem(u)
            r.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.table.setItem(item.row(),item.column(),r)
            if r.column()==0:
                v="UPDATE dogovor SET id_dogovor = "+r.text()+" WHERE id_dogovor = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==1:
                v="UPDATE dogovor SET date_zakl = "+r.text()+" WHERE date_zakl = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==2:
                v="UPDATE dogovor SET vid_strah = "+r.text()+" WHERE vid_strah = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==3:
                v="UPDATE dogovor SET sum_strah = "+r.text()+" WHERE sum_strah = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==4:
                v="UPDATE dogovor SET filial = "+r.text()+" WHERE filial = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==5:
                v="UPDATE dogovor SET srok = "+r.text()+" WHERE srok = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==6:
                v="UPDATE dogovor SET plat = "+r.text()+" WHERE plat = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==7:
                v="UPDATE dogovor SET client_id = "+r.text()+" WHERE client_id = "+f
                cursor.execute(v)
                con.commit()
        if columnCount==5:
            item = self.table.item(row, column)
            f=str(item.text())
            ok = QInputDialog.getText(self, 'Изменение',
            'Введите новое значение:')
            if ok:
                os.system("cls")
            u=str(ok)
            u=u.replace("('","")
            u=u.replace("', True)","")
            r= QTableWidgetItem(u)
            r.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.table.setItem(item.row(),item.column(),r)
            if r.column()==0:
                v="UPDATE client SET id_client = "+r.text()+" WHERE id_client = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==1:
                v="UPDATE client SET fam = "+r.text()+" WHERE fam = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==2:
                v="UPDATE client SET im = "+r.text()+" WHERE im = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==3:
                v="UPDATE client SET otch = "+r.text()+" WHERE otch = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==4:
                v="UPDATE client SET tel = "+r.text()+" WHERE tel = "+f
                cursor.execute(v)
                con.commit()
        if columnCount==3:
            item = self.table.item(row, column)
            f=str(item.text())
            ok = QInputDialog.getText(self, 'Изменение',
            'Введите новое значение:')
            if ok:
                os.system("cls")
            u=str(ok)
            u=u.replace("('","")
            u=u.replace("', True)","")
            r= QTableWidgetItem(u)
            r.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.table.setItem(item.row(),item.column(),r)
            if r.column()==0:
                v="UPDATE dogovor SET id_vid = "+r.text()+" WHERE id_vid = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==1:
                v="UPDATE dogovor SET namevid = "+r.text()+" WHERE namevid = "+f
                cursor.execute(v)
                con.commit()
            if r.column()==2:
                v="UPDATE dogovor SET strahvznos = "+r.text()+" WHERE strahvznos = "+f
                cursor.execute(v)
                con.commit()
    def find(self):
        con = pymysql.connect("localhost", "root", "XfHER9aHt10R5GSgIR", "MSC")  
        cursor = con.cursor()
        count=self.table.columnCount()


        self.table.sortByColumn(1,QtCore.Qt.QtSortOrder)
        if count==8:
            for row in range(self.table.rowCount()):
                for column in range(self.table.columnCount()):
                    item = self.table.item (row, column )
                   
                    if item and item.data (QtCore.Qt.DisplayRole) == self.ed1.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed2.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed3.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed4.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed5.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed6.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed7.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed8.text():
                        self.table.item(row,0).setBackground(QtCore.Qt.green)
                        self.table.item(row,1).setBackground(QtCore.Qt.green)
                        self.table.item(row,2).setBackground(QtCore.Qt.green)
                        self.table.item(row,3).setBackground(QtCore.Qt.green)
                        self.table.item(row,4).setBackground(QtCore.Qt.green)
                        self.table.item(row,5).setBackground(QtCore.Qt.green)
                        self.table.item(row,6).setBackground(QtCore.Qt.green)
                        self.table.item(row,7).setBackground(QtCore.Qt.green)
                    else:
                        os.system("cls")
        if count==3:
            con = pymysql.connect("localhost", "root", "XfHER9aHt10R5GSgIR", "MSC")  
            cursor = con.cursor()
            for row in range(self.table.rowCount()):
                for column in range(self.table.columnCount()):
                    item = self.table.item (row, column )
                    if item and item.data (QtCore.Qt.DisplayRole) == self.ed1.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed2.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed3.text():
                        self.table.item(row,0).setBackground(QtCore.Qt.green)
                        self.table.item(row,1).setBackground(QtCore.Qt.green)
                        self.table.item(row,2).setBackground(QtCore.Qt.green)
                    else:
                        os.system("cls")        
        if count==5:
            con = pymysql.connect("localhost", "root", "XfHER9aHt10R5GSgIR", "MSC")  
            cursor = con.cursor()
            for row in range(self.table.rowCount()):
                for column in range(self.table.columnCount()):
                    item = self.table.item (row, column )
                    if item and item.data (QtCore.Qt.DisplayRole) == self.ed1.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed2.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed3.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed4.text() or item and item.data (QtCore.Qt.DisplayRole) == self.ed5.text():
                        self.table.item(row,0).setBackground(QtCore.Qt.green)
                        self.table.item(row,1).setBackground(QtCore.Qt.green)
                        self.table.item(row,2).setBackground(QtCore.Qt.green)
                        self.table.item(row,3).setBackground(QtCore.Qt.green)
                        self.table.item(row,4).setBackground(QtCore.Qt.green)
                    else:
                        os.system("cls")
        if count==0:
            msg = QMessageBox()
            msg.setWindowTitle("Внимание!")
            msg.setText("Ни одно значение для поиска не указано или таблица пуста!")
            result = msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                os.system("cls")
        self.p1.setVisible(False)
        self.p2.setVisible(False)
        self.p3.setVisible(True)
        self.p4.setVisible(False)
        self.p5.setVisible(False)
        self.combo.setVisible(False)
    def printed(self):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        printer = Qt.QPrinter()
        table = cursor.insertTable(self.table.rowCount()+1, self.table.columnCount())
        for c in range(table.columns()):
            it = self.table.horizontalHeaderItem(c)
            cursor.insertText(str(c) if it is None else it.text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
        for row in range(1, table.rows()):
            for col in range(table.columns()):
                it = self.table.item(row-1, col)
                cursor.insertText("" if it is None else it.text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        for row in range(1, table.rows()):
            for col in range(table.columns()):
                table.mergeCells(row, col, self.table.rowSpan(row-1, col), 1)
        document.print_(printer)
    def rasp(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.combo)
        self.grid.addWidget(self.l1, 1, 0)
        self.grid.addWidget(self.ed1, 1, 1)
        self.grid.addWidget(self.l2, 2, 0)
        self.grid.addWidget(self.ed2, 2, 1)
        self.grid.addWidget(self.l3, 3, 0)
        self.grid.addWidget(self.ed3, 3, 1)
        self.grid.addWidget(self.l4, 4, 0)
        self.grid.addWidget(self.ed4, 4, 1)
        self.grid.addWidget(self.l5, 5, 0)
        self.grid.addWidget(self.ed5, 5, 1)
        self.grid.addWidget(self.l6, 6, 0)
        self.grid.addWidget(self.ed6, 6, 1)
        self.grid.addWidget(self.l7, 7, 0)
        self.grid.addWidget(self.ed7, 7, 1)
        self.grid.addWidget(self.l8, 8, 0)
        self.grid.addWidget(self.ed8, 8, 1)
        self.grid.addWidget(self.p1, 9, 0)
        self.grid.addWidget(self.name, 9, 1)
        self.grid.addWidget(self.p2, 10, 0)
        self.grid.addWidget(self.p4, 11, 0)
        self.grid.addWidget(self.p5, 12, 0)
        self.grid.addWidget(self.p3, 13, 0)
    def sect(self,z):
        i = int(0)
        k=int(z)
        self.rasp() 
        if z==3:
            self.tableBD(3)
            self.visibled(3)
            self.editclear()
        if z==8:
            self.tableBD(8)
            self.visibled(8)
            self.editclear()
        if z==5:
            self.tableBD(5)
            self.visibled(5)
            self.editclear()
        i=0
        while i!=k:
            self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)     
            i+=1    
    def vis(self,b):
        self.l4.setVisible(b)
        self.l5.setVisible(b)
        self.l6.setVisible(b)
        self.l7.setVisible(b)
        self.l8.setVisible(b)
        self.ed4.setVisible(b)
        self.ed5.setVisible(b)
        self.ed6.setVisible(b)
        self.ed7.setVisible(b)
        self.ed8.setVisible(b)
    def visibled(self,t):
        if t==3:
            self.l1.setText("ID_Страховки")
            self.l2.setText("Вид страховки")
            self.l3.setText("Страховой взнос")
            self.vis(False)
            self.setLayout(self.grid)
            self.grid.addWidget(self.table, 10, 1, 5, 1)
            self.loadBD(3)
        if t==8:
            self.l1.setText("ID_Договора")
            self.l2.setText("Дата заключения")
            self.l3.setText("Вид страховки")
            self.l4.setText("Сумма страхования")
            self.l5.setText("Филиал")
            self.l6.setText("Срок")
            self.l7.setText("Платёж")
            self.l8.setText("ID_Клиента")
            self.rasp()
            self.vis(True)
            self.setLayout(self.grid)
            self.grid.addWidget(self.table, 10, 1, 5, 1)
            self.loadBD(8)
        if t==5:
            self.l1.setText("ID_Клиента")
            self.l2.setText("Фамилия")
            self.l3.setText("Имя")
            self.l4.setText("Отчество")
            self.l5.setText("Телефон")
            self.vis(True)
            self.ed6.setVisible(False)
            self.ed7.setVisible(False)
            self.ed8.setVisible(False)
            self.l6.setVisible(False)
            self.l7.setVisible(False)
            self.l8.setVisible(False)    
            self.setLayout(self.grid)
            self.grid.addWidget(self.table, 10, 1, 5, 1)
            self.loadBD(5)
    def my_handler(self, text):
        if text==0:
            self.sect(8)
        if text==1:
            self.sect(5)
        if text==2:       
            self.sect(3)
    def loadBD(self,z):
        p=int(0)
        if z==5:
            self.tableBD(5)
            con = pymysql.connect("localhost", "root", "XfHER9aHt10R5GSgIR", "MSC")  
            cursor = con.cursor()
            cursor.execute("SELECT * FROM client")
            rows = cursor.fetchall()
            self.table.setRowCount(cursor.rowcount)
            for row in rows:
                if p<cursor.rowcount:
                    self.it1 = QTableWidgetItem(str(row[0]))
                    self.it2 = QTableWidgetItem(str(row[1]))
                    self.it3 = QTableWidgetItem(str(row[2]))
                    self.it4 = QTableWidgetItem(str(row[3]))
                    self.it5 = QTableWidgetItem(str(row[4]))
                    self.it1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.table.setItem(p, 0,self.it1)
                    self.table.setItem(p, 1,self.it2)
                    self.table.setItem(p, 2,self.it3)
                    self.table.setItem(p, 3,self.it4)
                    self.table.setItem(p, 4,self.it5)
                    p+=1
        if z==3:
            self.tableBD(3)
            con = pymysql.connect("localhost", "root", "XfHER9aHt10R5GSgIR", "MSC")  
            cursor = con.cursor()
            cursor.execute("SELECT * FROM vidstrah")
            rows = cursor.fetchall()
            self.table.setRowCount(cursor.rowcount)
            for row in rows:
                if p<cursor.rowcount:
                    self.it1 = QTableWidgetItem(str(row[0]))
                    self.it2 = QTableWidgetItem(str(row[1]))
                    self.it3 = QTableWidgetItem(str(row[2]))
                    self.it1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.table.setItem(p, 0,self.it1)
                    self.table.setItem(p, 1,self.it2)
                    self.table.setItem(p, 2,self.it3)
                    p+=1
        if z==8:
            self.tableBD(8)
            con = pymysql.connect("localhost", "root", "XfHER9aHt10R5GSgIR", "MSC")  
            cursor = con.cursor()
            cursor.execute("SELECT * FROM dogovor")
            rows = cursor.fetchall()
            self.table.setRowCount(cursor.rowcount)
            for row in rows:
                if p<cursor.rowcount:
                    self.it1 = QTableWidgetItem(str(row[0]))
                    self.it2 = QTableWidgetItem(str(row[1]))
                    self.it3 = QTableWidgetItem(str(row[2]))
                    self.it4 = QTableWidgetItem(str(row[3]))
                    self.it5 = QTableWidgetItem(str(row[4]))
                    self.it6 = QTableWidgetItem(str(row[5]))
                    self.it7 = QTableWidgetItem(str(row[6]))
                    self.it8 = QTableWidgetItem(str(row[7]))
                    self.it1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it6.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it7.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.it8.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.table.setItem(p, 0,self.it1)
                    self.table.setItem(p, 1,self.it2)
                    self.table.setItem(p, 2,self.it3)
                    self.table.setItem(p, 3,self.it4)
                    self.table.setItem(p, 4,self.it5)
                    self.table.setItem(p, 5,self.it6)
                    self.table.setItem(p, 6,self.it7)
                    self.table.setItem(p, 7,self.it8)
                    p+=1
    def tableBD(self,z):
        self.table.clear()
        if z==5:
            tdataBase=5
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(["ID_Клиента","Фамилия","Имя","Отчество","Телефон"])
        if z==3:
            tdataBase=3
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["ID_Страховки","Вид страховки","Страховой взнос"])
        if z==8:
            tdataBase=8
            self.table.setColumnCount(8)
            self.table.setHorizontalHeaderLabels(["ID_Договора","Дата заключения","Вид страховки","Сумма страхования","Филиал","Срок","Платёж","ID_Клиента"])
        self.table.resizeColumnsToContents()
        self.editclear()
    def closeEvent(self,event):
        reply = QMessageBox.question(self, "Внимание",
        "Вы хотите выйти из программы?",QMessageBox.Ok | QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Ok:
            event.accept()
            con.close()
        else:
            event.ignore()
    def editclear(self):
        self.ed1.clear()
        self.ed2.clear()
        self.ed3.clear()
        self.ed4.clear()
        self.ed5.clear()
        self.ed6.clear()
        self.ed7.clear()
        self.ed8.clear()
    def clskey(self):
        self.p1.setVisible(True)
        self.p2.setVisible(True)
        self.p3.setVisible(False)
        self.p4.setVisible(True)
        self.p5.setVisible(True)
        self.combo.setVisible(True)
        self.editclear()
        count=self.table.columnCount()
        if count>0:
            for row in range(self.table.rowCount()):
                for column in range(self.table.columnCount()):
                    item = self.table.item (row, column )
                    self.table.item(row,column).setBackground(QtCore.Qt.white)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = InputDialog()
    while login!="root" and password!="XfHER9aHt10R5GSgIR":
        dialog.exec()
        login=dialog.getInput1()
        password=dialog.getInput2()
        connection(login,password)
    ex = Example()
    sys.exit(app.exec_())       