from PyQt5.Qt import QApplication
import sys
from Analysis.guiUtils import TicketAnalysis
import Analysis.jsonKey

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = TicketAnalysis()
    Progress = ui.initUI()
    sys.exit(app.exec_())


