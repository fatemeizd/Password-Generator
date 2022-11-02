#Libraries my app
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import random
import string
import secrets
import uuid

#Base Structure
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 588)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(239, 201, 175);\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.s_label = QtWidgets.QLabel(self.centralwidget)
        self.s_label.setGeometry(QtCore.QRect(10, 0, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s_label.setFont(font)
        self.s_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.s_label.setStyleSheet("QLabel{\n"
"    border:2px solid;\n"
"    border-color: rgb(251, 209, 210);\n"
"    background-color: rgb(206, 226, 235);\n"
"}")
        self.s_label.setFrameShape(QtWidgets.QFrame.Box)
        self.s_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.s_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.s_label.setObjectName("s_label")
        self.e_label = QtWidgets.QLabel(self.centralwidget)
        self.e_label.setGeometry(QtCore.QRect(360, 0, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.e_label.setFont(font)
        self.e_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.e_label.setMouseTracking(False)
        self.e_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.e_label.setStyleSheet("QLabel{\n"
"    border:2px solid;\n"
"    border-color: rgb(251, 209, 210);\n"
"    background-color: rgb(206, 226, 235);\n"
"}")
        self.e_label.setFrameShape(QtWidgets.QFrame.Box)
        self.e_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.e_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.e_label.setObjectName("e_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, -5, 20, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(350, 50, 351, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.out_label = QtWidgets.QLabel(self.centralwidget)
        self.out_label.setGeometry(QtCore.QRect(10, 59, 691, 131))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.out_label.setFont(font)
        self.out_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.out_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(181, 182, 200);\n"
"}")
        self.out_label.setFrameShape(QtWidgets.QFrame.Box)
        self.out_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_label.setText("")
        self.out_label.setTextFormat(QtCore.Qt.AutoText)
        self.out_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_label.setObjectName("out_label")
        self.c_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.copy())
        self.c_pushButton.setGeometry(QtCore.QRect(660, 120, 41, 31))
        self.c_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_pushButton.setToolTip("")
        self.c_pushButton.setStatusTip("")
        self.c_pushButton.setWhatsThis("")
        self.c_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.c_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(181, 182, 200);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color:rgb(85, 170, 255);\n"
"}")
        self.c_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.c_pushButton.setIcon(icon)
        self.c_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.c_pushButton.setShortcut("")
        self.c_pushButton.setFlat(True)
        self.c_pushButton.setObjectName("c_pushButton")
        self.g_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.gen_pass())
        self.g_pushButton.setGeometry(QtCore.QRect(90, 200, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g_pushButton.setFont(font)
        self.g_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.g_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(65, 109, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(41, 50, 65);\n"
"}")
        self.g_pushButton.setDefault(False)
        self.g_pushButton.setFlat(False)
        self.g_pushButton.setObjectName("g_pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 691, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    background-color: rgb(203, 213, 255);\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.input_horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.input_horizontalSlider.setGeometry(QtCore.QRect(10, 60, 671, 22))
        self.input_horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.input_horizontalSlider.setStyleSheet("QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: #1d4e89\n"
"}\n"
"QSlider::pressed {\n"
"     background-color: #fbd1a2;\n"
"}")
        self.input_horizontalSlider.setMinimum(5)
        self.input_horizontalSlider.setMaximum(1000)
        self.input_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.input_horizontalSlider.setObjectName("input_horizontalSlider")
        self.input1_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.input1_spinBox.setGeometry(QtCore.QRect(140, 30, 81, 22))
        self.input1_spinBox.setStyleSheet("QSpinBox{\n"
"    background-color: rgb(211, 208, 255);\n"
"}")
        self.input1_spinBox.setFrame(False)
        self.input1_spinBox.setMinimum(5)
        self.input1_spinBox.setMaximum(1000)
        self.input1_spinBox.setObjectName("input1_spinBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 150, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStyleSheet("QCheckBox{\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"QCheckBox::pressed{\n"
"    background-color: rgb(251, 248, 190);\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 190, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_2.setStyleSheet("QCheckBox{\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"QCheckBox::pressed{\n"
"    background-color: rgb(251, 248, 190);\n"
"}")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(250, 150, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_3.setStyleSheet("QCheckBox{\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"QCheckBox::pressed{\n"
"    background-color: rgb(251, 248, 190);\n"
"}")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 190, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_4.setStyleSheet("QCheckBox{\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"QCheckBox::pressed{\n"
"    background-color: rgb(251, 248, 190);\n"
"}")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(460, 150, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_5.setStyleSheet("QCheckBox{\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"QCheckBox::pressed{\n"
"    background-color: rgb(251, 248, 190);\n"
"}")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(460, 190, 211, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_6.setStyleSheet("QCheckBox{\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"QCheckBox::pressed{\n"
"    background-color: rgb(251, 248, 190);\n"
"}")
        self.checkBox_6.setObjectName("checkBox_6")
        self.e_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.exit())
        self.e_pushButton.setGeometry(QtCore.QRect(10, 510, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.e_pushButton.setFont(font)
        self.e_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.e_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(65, 109, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(238, 108, 77);\n"
"}")
        self.e_pushButton.setFlat(False)
        self.e_pushButton.setObjectName("e_pushButton")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 490, 691, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionThis_App_Generate_Random_Passwords = QtWidgets.QAction(MainWindow)
        self.actionThis_App_Generate_Random_Passwords.setObjectName("actionThis_App_Generate_Random_Passwords")
        self.actionThis_App_Generate_Random_Passwords_2 = QtWidgets.QAction(MainWindow)
        self.actionThis_App_Generate_Random_Passwords_2.setObjectName("actionThis_App_Generate_Random_Passwords_2")
        self.actionpass = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/icons/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpass.setIcon(icon1)
        self.actionpass.setObjectName("actionpass")
        self.menuAbout.addAction(self.actionThis_App_Generate_Random_Passwords_2)
        self.menubar.addAction(self.menuAbout.menuAction())

        #Move The Slider 
        self.input1_spinBox.valueChanged.connect(self.slid_it)
        #Change SpinBox
        self.input_horizontalSlider.valueChanged.connect(self.spin_it)
        #Change the Statusbar font
        self.statusbar.setFont(QFont('Times', 14))
        self.statusbar.showMessage("Ready!")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #For Slider
    def slid_it(self, value):
        self.input_horizontalSlider.setValue(value)

    #For SpinBox
    def spin_it(self, value):
        self.input1_spinBox.setValue(value)

    #Entre Password Length and generate password
    def gen_pass(self):
        #Grab a length that get from spinbox or slider
        length = self.input1_spinBox.value()
        #An empty string for save character of password 
        my_pass = ''

        #Getting character for password
        while True:
            if (self.checkBox.isChecked() == True):
                my_pass += string.ascii_uppercase
            if (self.checkBox_2.isChecked() == True):
                my_pass += string.ascii_lowercase
            if (self.checkBox_3.isChecked() == True):
                my_pass += string.digits
            if (self.checkBox_4.isChecked() == True):
                my_pass += string.punctuation
            if (self.checkBox_5.isChecked() == True):
                my_pass = secrets.token_hex()
            if (self.checkBox_6.isChecked() == True):
                my_pass = str(uuid.uuid4())

            break

        password = []
        for l in range(length):
            random_pass = random.choice(my_pass)
            password.append(random_pass)    
            
        result = "".join(password)
        self.out_label.setText(f'{result}')

        
        #Show Password's Score
        if length == 5:
            self.s_label.setStyleSheet("color:red")
            self.s_label.setText('Bad Password')
            self.e_label.setStyleSheet("color:red")
            self.e_label.setText('Ten Second!')
        elif length > 5 and length <= 10:
            self.s_label.setStyleSheet("color:orange")
            self.s_label.setText('Week Password')
            self.e_label.setStyleSheet("color:orange")
            self.e_label.setText('One Hour!')
        elif length > 10 and length <= 30:
            self.s_label.setStyleSheet("color:blue")
            self.s_label.setText('Normal Password')
            self.e_label.setStyleSheet("color:blue")
            self.e_label.setText('One Day!')
        elif length > 30 and length <= 50:
            self.s_label.setStyleSheet("color:lime")
            self.s_label.setText('Good Password')
            self.e_label.setStyleSheet("color:lime")
            self.e_label.setText('Seven Day!')
        elif length > 50 and length <= 1000:
            self.s_label.setStyleSheet("color:darkgreen")
            self.s_label.setText('Very Strong Password')
            self.e_label.setStyleSheet("color:darkgreen")
            self.e_label.setText('One Year :)')

        #Show messagee in statusbar
        self.statusbar.setStyleSheet('color:darkblue')
        self.statusbar.showMessage("Done!")
        #Clear the spin box
        self.input1_spinBox.clear()
        #Reset the slider
        self.input_horizontalSlider.setValue(5)

    #Copy To Clipboard           
    def copy(self):
        #Get password and Copy
        c_pass = QtWidgets.QApplication.clipboard()
        c_pass.clear(mode=c_pass.Clipboard)
        c_pass.setText(self.out_label.text(), mode=c_pass.Clipboard)
        #Clear The output label
        self.out_label.clear()

    #Exit From App
    def exit(self):
        #closing the window
        MainWindow.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.s_label.setText(_translate("MainWindow", "Your Password\'s Score:"))
        self.e_label.setText(_translate("MainWindow", "Estimated Time To Hack:"))
        self.g_pushButton.setText(_translate("MainWindow", "Generate Password"))
        self.groupBox.setTitle(_translate("MainWindow", "Costomize Your Password"))
        self.label.setText(_translate("MainWindow", "Password Length:"))
        self.label_2.setText(_translate("MainWindow", "Additional Options"))
        self.checkBox.setText(_translate("MainWindow", "Include Upper Letter"))
        self.checkBox_2.setText(_translate("MainWindow", "Include Lower Letter"))
        self.checkBox_3.setText(_translate("MainWindow", "Include Digit"))
        self.checkBox_4.setText(_translate("MainWindow", "Include Symbols"))
        self.checkBox_5.setText(_translate("MainWindow", "String Token"))
        self.checkBox_6.setText(_translate("MainWindow", "Secure UUID"))
        self.e_pushButton.setText(_translate("MainWindow", "Exit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionThis_App_Generate_Random_Passwords.setText(_translate("MainWindow", "This App Generate Random Passwords"))
        self.actionThis_App_Generate_Random_Passwords_2.setText(_translate("MainWindow", "This App Generate Random Passwords"))
        self.actionpass.setText(_translate("MainWindow", "pass"))

#Initialize the APP
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
