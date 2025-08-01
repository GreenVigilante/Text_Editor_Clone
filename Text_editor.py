from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("qt_file.ui", self)
        self.show()

        self.action6_px.triggered.connect(lambda: self.font_size(6))
        self.action11_px.triggered.connect(lambda: self.font_size(11))
        self.action12_px.triggered.connect(lambda: self.font_size(12))
        self.action14_px.triggered.connect(lambda: self.font_size(14))
        self.action24_px.triggered.connect(lambda: self.font_size(24))
        self.action30_px.triggered.connect(lambda: self.font_size(30))
        self.action60_px.triggered.connect(lambda: self.font_size(60))
        self.action72_px.triggered.connect(lambda: self.font_size(72))
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save)
        self.actionClose.triggered.connect(exit)

        self.setWindowTitle("Text Editor")
        

        
    def font_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))
    def open_file(self):
        options_ = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)", options= options_)
        if filename!= "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())
    def save(self):
        options_ = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save Files", "", "Text Files (*.txt);;All Files (*)", options=options_)
        if filename!="":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())
    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)
        answer = dialog.exec_()
        if answer ==0:
            self.save()
            event.accept()
        elif answer == 2:
            event.ignore()
def main():
    app = QApplication([])
    win = GUI()
    app.exec_()
if __name__ =='__main__':
    main()