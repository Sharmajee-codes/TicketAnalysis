from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QFileDialog, QIcon
import os
import Analysis.jsonKey

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 184)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CsvUploadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CsvUploadBtn.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.CsvUploadBtn.setObjectName("pushButton")
        self.CsvUploadBtn.clicked.connect(self.Browse)
        
        self.pathlabel = QtWidgets.QLabel(self.centralwidget)
        self.pathlabel.setGeometry(QtCore.QRect(130, 15, 220, 21))
        self.pathlabel.setObjectName("label")
        
        self.analyseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.analyseBtn.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.analyseBtn.setObjectName("pushButton_2")
        self.analyseBtn.clicked.connect(self.Analyse)
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(130, 50, 231, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        
        self.confirmationlbl = QtWidgets.QLabel(self.centralwidget)
        self.confirmationlbl.setGeometry(QtCore.QRect(20, 100, 141, 16))
        self.confirmationlbl.setObjectName("label_2")
        self.confirmationlbl2 = QtWidgets.QLabel(self.centralwidget)
        self.confirmationlbl2.setGeometry(QtCore.QRect(20, 120, 251, 20))
        self.confirmationlbl2.setObjectName("label_3")
        self.openDirBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openDirBtn.setGeometry(QtCore.QRect(260, 110, 91, 31))
        self.openDirBtn.setObjectName("pushButton_3")
        self.openDirBtn.clicked.connect(self.OpenDir)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowIcon(QIcon('Keyword_Analysis'))
        self.CsvUploadBtn.setText(_translate("MainWindow", "Upload File"))
        self.pathlabel.setText(_translate("MainWindow", "TextLabel"))
        self.analyseBtn.setText(_translate("MainWindow", "Analyse"))
        self.confirmationlbl.setText(_translate("MainWindow", "Ticket analysis completed"))
        self.confirmationlbl2.setText(_translate("MainWindow", "Check the output_ folder in the directory for files"))
        self.openDirBtn.setText(_translate("MainWindow", "Open folder"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        #self.actionExit.clicked.connect(self.OpenDir)
        self.actionNew.setText(_translate("MainWindow", "New"))
        #self.actionNew.clicked.connect(self.OpenDir)
    def Browse(self):
        fileName, _ = QFileDialog.getOpenFileName() 
        if fileName:
            
            self.abspath = os.path.abspath(fileName) #input_/CSVBigData
            ui.pathlabel.setText(str(self.abspath))

            
    def OpenDir(self):
        filedir = os.system('explorer.exe ""C:\\Users\\36474\\Downloads\\TicketAnalysis-20170612T050725Z-001\\TicketAnalysis\\Ticket\\Analysis\\output_"" ')    
     

    def Analyse(self):
        self.completed = 0
        Selector = Analysis.jsonKey.TicketJson()
        self.completed += 5
        self.progressBar.setValue(self.completed)
        Result = Selector.jsonCreator(self.abspath)
        self.completed += 10
        self.progressBar.setValue(self.completed)
        SummaryLength,SummaryIntoTokens = Selector.LenCalc("Title",Result)
        self.completed += 25
        self.progressBar.setValue(self.completed)
        Keysjson = Selector.jsonCreator(path='input_/KeySets.csv')   
        self.completed += 20
        self.progressBar.setValue(self.completed)
        KeySets = Selector.KeyGen(Keysjson,"Keys")
        self.completed += 10
        self.progressBar.setValue(self.completed)
        counterValue = Selector.countAppearance(KeySets,SummaryIntoTokens)
        self.completed += 10
        self.progressBar.setValue(self.completed)
        ResultOutput = Selector.FinalOut(counterValue=counterValue,FinalKeySet=KeySets)
        self.completed += 10
        self.progressBar.setValue(self.completed)
        Categorize = Selector.CreateCategorizedFiles(ResultOutput)
        self.completed += 10
        self.progressBar.setValue(self.completed)
        self.ConfirmationLbl.show()
        self.ConfirmationLbl2.show()
        self.OpenDirBtn.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

