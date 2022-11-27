from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql
import random
import ast

#below this is the ui
class Ui_editItem(object): #editItem UI
    def searchClicked(self):
        print('search')
        q = "SELECT * FROM inventory"
        try:
            cur.execute(q)
            result = cur.fetchall()
            for row in result:
                if row[0] == self.idText.text():
                    self.search.setEnabled(False)
                    self.idText.setReadOnly(True)
                    self.okButton.setEnabled(True)
                    self.itemText.setText(row[1])
                    self.brandText.setText(row[2])
                    self.priceText.setText(row[3])
                    self.stockText.setText(row[4])
            print('wtf')
        except:
            print('no such record')
    def okClicked(self):
        print('ok')
        item = self.itemText.text()
        brand = self.brandText.text()
        price = self.priceText.text()
        stock = self.stockText.text()
        q = "UPDATE inventory SET item_name=%s,item_brand=%s,item_price=%s,stock_amount=%s WHERE item_id = %s"
        try:
            print("execute")
            value = (item, brand, price, stock, self.idText.text())
            cur.execute(q, value)
            print("commit")
            db.commit()
            print('added to db')
        except Exception:
            db.rollback()
        self.centralwidget.close()

    def setupUi(self, editItem):
        editItem.setObjectName("editItem")
        editItem.resize(405, 400)
        editItem.setMinimumSize(QtCore.QSize(405, 400))
        editItem.setMaximumSize(QtCore.QSize(405, 400))
        self.centralwidget = QtWidgets.QWidget(editItem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.label_5.setObjectName("label_5")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(30, 310, 93, 28))
        self.okButton.setObjectName("okButton")
        self.okButton.setEnabled(False)
        self.okButton.clicked.connect(self.okClicked)

        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(260, 60, 93, 28))
        self.search.setObjectName("search")

        self.search.clicked.connect(self.searchClicked)

        self.idText = QtWidgets.QLineEdit(self.centralwidget)
        self.idText.setGeometry(QtCore.QRect(30, 60, 211, 22))
        self.idText.setObjectName("idText")
        self.itemText = QtWidgets.QLineEdit(self.centralwidget)
        self.itemText.setGeometry(QtCore.QRect(30, 110, 211, 22))
        self.itemText.setObjectName("itemText")
        self.brandText = QtWidgets.QLineEdit(self.centralwidget)
        self.brandText.setGeometry(QtCore.QRect(30, 160, 211, 22))
        self.brandText.setObjectName("brandText")
        self.priceText = QtWidgets.QLineEdit(self.centralwidget)
        self.priceText.setGeometry(QtCore.QRect(30, 210, 211, 22))
        self.priceText.setObjectName("priceText")
        self.stockText = QtWidgets.QLineEdit(self.centralwidget)
        self.stockText.setGeometry(QtCore.QRect(30, 260, 211, 22))
        self.stockText.setObjectName("stockText")
        editItem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(editItem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 26))
        self.menubar.setObjectName("menubar")
        editItem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(editItem)
        self.statusbar.setObjectName("statusbar")
        editItem.setStatusBar(self.statusbar)

        self.retranslateUi(editItem)
        QtCore.QMetaObject.connectSlotsByName(editItem)

    def retranslateUi(self, editItem):
        _translate = QtCore.QCoreApplication.translate
        editItem.setWindowTitle(_translate("editItem", "Edit Item"))
        self.label.setText(_translate("editItem", "Item ID"))
        self.label_4.setText(_translate("editItem", "Item Price"))
        self.label_2.setText(_translate("editItem", "Item Name"))
        self.label_3.setText(_translate("editItem", "Item Brand"))
        self.label_5.setText(_translate("editItem", "Item Stock"))
        self.okButton.setText(_translate("editItem", "OK"))
        self.search.setText(_translate("editItem", "Search"))


class Ui_deleteItem(object): #deleteitItem UI ##----- delete querry work on it
    def searchClicked(self):
        print('search')
        q = "SELECT * FROM inventory"
        try:
            cur.execute(q)
            result = cur.fetchall()
            for row in result:
                if row[0] == self.idText.text():
                    self.search.setEnabled(False)
                    self.idText.setReadOnly(True)
                    self.okButton.setEnabled(True)
                    self.itemText.setText(row[1])
                    self.brandText.setText(row[2])
                    self.priceText.setText(row[3])
                    self.stockText.setText(row[4])
        except:
            print('no such record')
    def okClicked(self):
        print('remove')
        id = self.idText.text()
        q = "DELETE FROM inventory WHERE item_id = %s"
        try:
            print("execute")
            cur.execute(q, id)
            print("commit")
            db.commit()
            print('deleted from inventory')
        except Exception as e:
            db.rollback()
            print(e)
        self.centralwidget.close()

    def setupUi(self, deleteItem):
        deleteItem.setObjectName("deleteItem")
        deleteItem.resize(405, 400)
        deleteItem.setMinimumSize(QtCore.QSize(405, 400))
        deleteItem.setMaximumSize(QtCore.QSize(405, 400))
        self.centralwidget = QtWidgets.QWidget(deleteItem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.label_5.setObjectName("label_5")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(30, 310, 93, 28))
        self.okButton.setObjectName("okButton")
        self.okButton.setEnabled(False)
        self.okButton.clicked.connect(self.okClicked)   

        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(260, 60, 93, 28))
        self.search.setObjectName("search")

        self.search.clicked.connect(self.searchClicked)

        self.idText = QtWidgets.QLineEdit(self.centralwidget)
        self.idText.setGeometry(QtCore.QRect(30, 60, 211, 22))
        self.idText.setObjectName("idText")
        self.itemText = QtWidgets.QLineEdit(self.centralwidget)
        self.itemText.setGeometry(QtCore.QRect(30, 110, 211, 22))
        self.itemText.setObjectName("itemText")
        self.brandText = QtWidgets.QLineEdit(self.centralwidget)
        self.brandText.setGeometry(QtCore.QRect(30, 160, 211, 22))
        self.brandText.setObjectName("brandText")
        self.priceText = QtWidgets.QLineEdit(self.centralwidget)
        self.priceText.setGeometry(QtCore.QRect(30, 210, 211, 22))
        self.priceText.setObjectName("priceText")
        self.stockText = QtWidgets.QLineEdit(self.centralwidget)
        self.stockText.setGeometry(QtCore.QRect(30, 260, 211, 22))
        self.stockText.setObjectName("stockText")
        deleteItem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(deleteItem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 26))
        self.menubar.setObjectName("menubar")
        deleteItem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(deleteItem)
        self.statusbar.setObjectName("statusbar")
        deleteItem.setStatusBar(self.statusbar)

        self.retranslateUi(deleteItem)
        QtCore.QMetaObject.connectSlotsByName(deleteItem)

    def retranslateUi(self, deleteItem):
        _translate = QtCore.QCoreApplication.translate
        deleteItem.setWindowTitle(_translate("deleteItem", "Delete Item"))
        self.label.setText(_translate("deleteItem", "Item ID"))
        self.label_4.setText(_translate("deleteItem", "Item Price"))
        self.label_2.setText(_translate("deleteItem", "Item Name"))
        self.label_3.setText(_translate("deleteItem", "Item Brand"))
        self.label_5.setText(_translate("deleteItem", "Item Stock"))
        self.okButton.setText(_translate("deleteItem", "Remove"))
        self.search.setText(_translate("deleteItem", "Search"))


class Ui_addItem(object): #addItem UI
    def okClicked(self):
        print("ok")
        id = self.idText.text()
        item = self.nameText.text()
        brand = self.brandText.text()
        price = self.priceText.text()
        stock = self.stockText.text()
        expiration = self.dateEdit.text()
        q = "INSERT INTO inventory (`item_id`, `item_name`, `item_brand`, `item_price`, `stock_amount`, `item_expiration`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}') ".format(id, item, brand, price, stock, expiration )
        try:
            print("execute")
            cur.execute(q)
            print("commit")
            db.commit()
            print('added to db')
        except Exception:
            db.rollback()
            print()
    def setupUi(self, addItem):
        addItem.setObjectName("addItem")
        addItem.resize(405, 400)
        addItem.setMinimumSize(QtCore.QSize(405, 400))
        addItem.setMaximumSize(QtCore.QSize(405, 400))
        self.centralwidget = QtWidgets.QWidget(addItem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.label.setObjectName("label")
        self.idText = QtWidgets.QLineEdit(self.centralwidget)
        self.idText.setGeometry(QtCore.QRect(30, 60, 221, 21))
        self.idText.setReadOnly(True)
        self.idText.setObjectName("idText")
        self.idText.setText(str(random.randint(1000,5000)))
        self.nameText = QtWidgets.QLineEdit(self.centralwidget)
        self.nameText.setGeometry(QtCore.QRect(30, 110, 221, 22))
        self.nameText.setObjectName("nameText")
        self.brandText = QtWidgets.QLineEdit(self.centralwidget)
        self.brandText.setGeometry(QtCore.QRect(30, 160, 221, 22))
        self.brandText.setObjectName("brandText")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 81, 16))
        self.label_4.setObjectName("label_4")
        self.priceText = QtWidgets.QLineEdit(self.centralwidget)
        self.priceText.setGeometry(QtCore.QRect(30, 210, 221, 22))
        self.priceText.setObjectName("priceText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.stockText = QtWidgets.QLineEdit(self.centralwidget)
        self.stockText.setGeometry(QtCore.QRect(30, 260, 221, 22))
        self.stockText.setObjectName("stockText")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 290, 91, 16))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(30, 310, 221, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(280, 300, 93, 28))
        self.okButton.setObjectName("okButton")
        
        self.okButton.clicked.connect(self.okClicked)
        

        addItem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addItem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 26))
        self.menubar.setObjectName("menubar")
        addItem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addItem)
        self.statusbar.setObjectName("statusbar")
        addItem.setStatusBar(self.statusbar)

        self.retranslateUi(addItem)
        QtCore.QMetaObject.connectSlotsByName(addItem)

    def retranslateUi(self, addItem):
        _translate = QtCore.QCoreApplication.translate
        addItem.setWindowTitle(_translate("addItem", "Add Item"))
        self.label.setText(_translate("addItem", "Item ID"))
        self.label_2.setText(_translate("addItem", "Item Name"))
        self.label_3.setText(_translate("addItem", "Item Brand"))
        self.label_4.setText(_translate("addItem", "Item Price"))
        self.label_5.setText(_translate("addItem", "Item Stock"))
        self.label_6.setText(_translate("addItem", "Item Expiration"))
        self.okButton.setText(_translate("addItem", "Add"))

    
class Ui_MainWindow(object): #main window

    def MyConverter(self, mydata):
        def cvt(data):
            try :
                return ast.literal_eval(data)
            except:
                return str(data)
        return tuple(map(cvt, mydata))
    def refreshData(self):
        self.itemTable.setRowCount(0)
        q = "select * from inventory"
        cur.execute(q)
        data = cur.fetchall()
        for row in data:
            self.addTable(self.MyConverter(row))

    def addTable(self, columns):
        rowPosition = self.itemTable.rowCount()
        self.itemTable.insertRow(rowPosition)
        for i, columns in enumerate(columns):
            self.itemTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(columns)))

    def addItemClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_addItem()
        self.ui.setupUi(self.window)
        self.window.show()

    def editItemClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_editItem()
        self.ui.setupUi(self.window)
        self.window.show()

    def removeItemClicked(self):
        print("deleteitem")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_deleteItem()
        self.ui.setupUi(self.window)
        self.window.show()

    def refreshClicked(self):
        print("refresh")
        self.refreshData()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 496)
        MainWindow.setMinimumSize(QtCore.QSize(916, 496))
        MainWindow.setMaximumSize(QtCore.QSize(916, 496))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewItems = QtWidgets.QGroupBox(self.centralwidget)
        self.viewItems.setGeometry(QtCore.QRect(20, 20, 881, 441))
        self.viewItems.setObjectName("viewItems")
        self.itemTable = QtWidgets.QTableWidget(self.viewItems)
        self.itemTable.setGeometry(QtCore.QRect(130, 50, 731, 351))
        self.itemTable.setColumnCount(6)
        self.itemTable.setObjectName("itemTable")
        self.itemTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(5, item)
        self.addItem = QtWidgets.QPushButton(self.viewItems)
        self.addItem.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.addItem.setObjectName("addItem")
        self.addItem.clicked.connect(self.addItemClicked)

        self.editItem = QtWidgets.QPushButton(self.viewItems)
        self.editItem.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.editItem.setObjectName("editItem")
        
        self.editItem.clicked.connect(self.editItemClicked)

        self.removeItem = QtWidgets.QPushButton(self.viewItems)
        self.removeItem.setGeometry(QtCore.QRect(20, 340, 93, 28))
        self.removeItem.setObjectName("removeItem")
        
        self.removeItem.clicked.connect(self.removeItemClicked)

        self.refresh = QtWidgets.QPushButton(self.viewItems)
        self.refresh.setGeometry(QtCore.QRect(20, 300, 93, 28))
        self.refresh.setObjectName("refresh")
        
        self.refresh.clicked.connect(self.refreshClicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Drug Inventory"))
        self.viewItems.setTitle(_translate("MainWindow", "Items"))
        item = self.itemTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Id"))
        item = self.itemTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.itemTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item Brand"))
        item = self.itemTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item Price"))
        item = self.itemTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stock Amount"))
        item = self.itemTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Item Expiration"))
        self.addItem.setText(_translate("MainWindow", "Add Item"))
        self.editItem.setText(_translate("MainWindow", "Edit Item"))
        self.removeItem.setText(_translate("MainWindow", "Remove Item"))
        self.refresh.setText(_translate("MainWindow", "Refresh List"))
        self.refreshData()


def openMainWindow():#opens the main window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        print("Connecting to DB")
        db = pymysql.connect("localhost", "root", "", "drug_inventory")
        cur = db.cursor()
        print("Succesfully connected to DB")
        print("Starting program...")
        openMainWindow()
        cur.close()
        db.close()
        print("Exiting program")
    except pymysql.DatabaseError:
        print('sorry cannot connect to the database')
        sys.exit()
    except:
        print ('Exiting program')