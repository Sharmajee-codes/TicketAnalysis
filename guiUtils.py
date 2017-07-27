from PyQt5 import QtWidgets 
import os, sys
from PyQt5.Qt import QPushButton, QFileDialog, QApplication, QLabel,\
    QProgressBar, QIcon
import Analysis

class TicketAnalysis(QtWidgets.QWidget):
    
    def __init__(self):
        super(TicketAnalysis, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.resize(400, 180)
        self.setWindowTitle("Ticket Analysis")
        self.setWindowIcon(QIcon('Keyword_Analysis'))
        
        
        CsvUploadBtn = QPushButton("CSV Upload",self)
        CsvUploadBtn.resize(CsvUploadBtn.sizeHint())
        CsvUploadBtn.clicked.connect(self.Browse)
        CsvUploadBtn.move(10, 10)  
        
        self.FilePathLbl = QLabel(self)
        self.FilePathLbl.move(100,15)    
        
        AnalyseBtn = QPushButton("Analyse",self)
        AnalyseBtn.move(10,40)
        AnalyseBtn.clicked.connect(self.Analyse)
        
        
        self.ProgressBar = QProgressBar(self) 
        self.ProgressBar.move(100,41)
        self.ProgressBar.hide()
        self.ProgressBar.setProperty("value", 1)
        self.ProgressBar.setMinimumWidth(300)
        
        ConfirmationLbl = QLabel("Ticket analysis done",self )
        ConfirmationLbl.move(10,110)
        
        ConfirmationLbl2 = QLabel("Please check the folder in the directory",self )
        ConfirmationLbl2.move(10,130)
        
        OpenDirectory = QPushButton("Open Directory",self)
        OpenDirectory.move(285,125)
        OpenDirectory.clicked.connect(self.OpenDir)     

        self.show()

    def Browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        
        
        
        
    def OpenDir(self):
        filedir = os.system('explorer.exe ""C:\\Users\\36474\\Downloads\\TicketAnalysis-20170612T050725Z-001\\TicketAnalysis\\Ticket\\Analysis\\output_"" ')    
        


    def Analyse(self):
        self.ProgressBar.show()