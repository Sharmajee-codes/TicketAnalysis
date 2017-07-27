from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QFileDialog, QIcon

import os, sys
import Analysis.jsonKey
from typing import Union
from Analysis.jsonKey import TicketJson
class Ui_TicketAnalysis(object):
    def setupUi(self, TicketAnalysis):
        TicketAnalysis.setObjectName("TicketAnalysis")
        TicketAnalysis.resize(400, 180)
        
        self.formLayoutWidget = QtWidgets.QWidget(TicketAnalysis)
        
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        self.CsvUploadBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.CsvUploadBtn.setObjectName("CsvUploadBtn")
        #self.CsvUploadBtn.clicked.connect(self.Browse)
        
        
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.CsvUploadBtn)
        
        self.FilePathLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.FilePathLbl.setObjectName("FilePathLbl")
        
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.FilePathLbl)
        
        self.AnalyseBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.AnalyseBtn.setObjectName("AnalyseBtn")
        self.AnalyseBtn.clicked.connect(self.Analyse)
        
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.AnalyseBtn)
        
        self.ProgressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        
        
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ProgressBar)
        self.formLayoutWidget_2 = QtWidgets.QWidget(TicketAnalysis)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 381, 62))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.ConfirmationLbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.ConfirmationLbl.setObjectName("ConfirmationLbl")      
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ConfirmationLbl)
        self.ConfirmationLbl.hide()
        

        self.OpenDirBtn = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.OpenDirBtn.setObjectName("OpenDirBtn")
        self.OpenDirBtn.hide()
        self.OpenDirBtn.clicked.connect(self.OpenDir)     
        
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.OpenDirBtn)
        
        self.ConfirmationLbl2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.ConfirmationLbl2.setObjectName("ConfirmationLbl2")
        self.ConfirmationLbl2.hide()
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ConfirmationLbl2)

        self.retranslateUi(TicketAnalysis)
        QtCore.QMetaObject.connectSlotsByName(TicketAnalysis)

    def retranslateUi(self, TicketAnalysis):
        _translate = QtCore.QCoreApplication.translate
        TicketAnalysis.setWindowTitle(_translate("TicketAnalysis", "Ticket Analyser"))
        TicketAnalysis.setWindowIcon(QIcon('Keyword_Analysis'))
        self.CsvUploadBtn.setText(_translate("TicketAnalysis", "CSV Upload"))
        self.FilePathLbl.setText(_translate("TicketAnalysis", "Filepath"))
        self.AnalyseBtn.setText(_translate("TicketAnalysis", "Analyse"))
        self.ConfirmationLbl.setText(_translate("TicketAnalysis", "Ticket Anaysis Done. "))
        self.OpenDirBtn.setText(_translate("TicketAnalysis", "Open Directory"))
        self.ConfirmationLbl2.setText(_translate("TicketAnalysis", "Please check in the output_ folder in the directory"))
    
    def Browse(self):    
        print("Converting")
        value = self.lineeuro.text()
        if len(value)>0 and value.isdigit():
            rate = 0.86
            amountDollar = float(value)*rate
            ui.labelval.setText(str(amountDollar))
        
    def OpenDir(self):
        filedir = os.system('explorer.exe ""C:\\Users\\36474\\Downloads\\TicketAnalysis-20170612T050725Z-001\\TicketAnalysis\\Ticket\\Analysis\\output_"" ')    
     
    def Analyse(self):
        self.completed = 0
        
        
        Selector = Analysis.jsonKey.TicketJson()
        self.completed += 5
        self.ProgressBar.setValue(self.completed)
        Result = Selector.jsonCreator('input_/ServiceReport1.csv')
        self.completed += 10
        self.ProgressBar.setValue(self.completed)
        SummaryLength,SummaryIntoTokens = Selector.LenCalc("Title",Result)
        self.completed += 25
        self.ProgressBar.setValue(self.completed)
        Keysjson = Selector.jsonCreator(path='input_/KeySets.csv')   
        self.completed += 20
        self.ProgressBar.setValue(self.completed)
        KeySets = Selector.KeyGen(Keysjson,"Keys")
        self.completed += 10
        self.ProgressBar.setValue(self.completed)
        counterValue = Selector.countAppearance(KeySets,SummaryIntoTokens)
        self.completed += 10
        self.ProgressBar.setValue(self.completed)
        ResultOutput = Selector.FinalOut(counterValue=counterValue,FinalKeySet=KeySets)
        self.completed += 10
        self.ProgressBar.setValue(self.completed)
        Categorize = Selector.CreateCategorizedFiles(ResultOutput)
        self.completed += 10
        self.ProgressBar.setValue(self.completed)
        self.ConfirmationLbl.show()
        self.ConfirmationLbl2.show()
        self.OpenDirBtn.show()
    def slot_method(self):
        print('slot method called.')
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TicketAnalysis = QtWidgets.QWidget()
    ui = Ui_TicketAnalysis()
    ui.setupUi(TicketAnalysis)
    TicketAnalysis.show()
    sys.exit(app.exec_())