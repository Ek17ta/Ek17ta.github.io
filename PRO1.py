# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PROJECT_INTERNSHIP.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#pycharm
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

e1 = "okay you have selected how you are feeling is "

class Ui_MainWindow(object):

    def values1(self):
        size = self.verticalSlider.value()
        e = "The Emotional Range is :"
        size = e + str(size)
        self.label_12.setText(str(size))

    def values(self, b):
        btn1 = b.text()
        btn = e1 + btn1
        self.label_10.setText(str(btn))

        if btn1=="GRATEFUL":
                self.label_14.setText("Awesome!!!,Tracking your mood and understanding the factors"+"\n"+" influencing is are key to moving towards best life.")
        elif btn1=="SAD":
                self.label_14.setText("Okay,Allowing yourself feel sad,angry,anxious,etc--all the people think we shouldent fell-->is essential for life.In fact it's oppurtinity to learn and improve.")
        elif btn1=="TIRED":
                self.label_14.setText("OKAY,Never be tired of a dream, if not fulfilled. Fear of failure should not deter you from your path of self belief. Your belief and determination will get you to your destination and make the dream come true.")
        elif btn1=="HAPPY":
                self.label_14.setText("Give the world the best you have and you'll get kicked in the teeth.Give the world the best you have anyway.")
        elif btn1=="JOYFUL":
                self.label_14.setText("Understanding more about your feeling can help you take control of your emotional health.")
        elif btn1=="PROUD":
                self.label_14.setText("Don't chase people. The right ones will stay in your life and the wrong ones will leave. Be proud of who you are and what you stand for.")
        elif btn1=="FRUSTRATED":
                self.label_14.setText("To conquer frustration, one must remain intensely focused on the outcome, not the obstacles.")
        elif btn1=="NUMB":
                self.label_14.setText("Okay,Be careful with too much joy,it can make you numb in life.")
        elif btn1=="ok":
                self.label_14.setText("GREAT!!! you are feeling okay,its Good to know your emotions.")
        elif btn1=="ANNOYED":
                self.label_14.setText("OK, Factors are always changing over time. Life is always a flux.Thats why you need to keep tracking them.")
        elif btn1=="ANGRY":
                self.label_14.setText("Okay,Allowing yourself feel sad,angry,anxious,etc--all the people think we shouldent fell-->is essential for life.In fact it's oppurtinity to learn and improve.")
        elif btn1=="OVERWHELMED":
                self.label_14.setText("Thats Fantastic To hear always stay positive.")
        elif btn1=="ANXIOUS":
                self.label_14.setText("Okay,Allowing yourself feel sad,angry,anxious,etc--all the people think we shouldent fell-->is essential for life.In fact it's oppurtinity to learn and improve.")
        elif btn1=="AFRAID":
                self.label_14.setText("Always Try to overcome it -->the basic key factor to be motivated .")
        elif btn1=="INSECURE":
                self.label_14.setText("Regardless of how you feel inside, always try to look like a winner. Despite of Insecurites the one who move forward always shine the brightest")
        elif btn1 == "ASHAMED":
                self.label_14.setText("Understanding more about your feeling can help you take control of your emotional health,Great said Where there is no shame there is no Honour")
        elif btn1 == "BORED":
                self.label_14.setText("okay,as you are feeling bored i would say Boredom always predicates a period of great creativity.")
        elif btn1 == "GUILTY":
                self.label_14.setText(" If You ever  feel guilty about -->you should continiously work to overcome it.")
        elif btn1 == "LOVING":
                self.label_14.setText("Thats Fantastic To hear always stay positive,Understanding more about your feeling can help you take control of your emotional health")
        elif btn1 == "EXCITED":
                self.label_14.setText("Understanding more about your feeling can help you take control of your emotional health.")
        elif btn1 == "CONFIDENT":
                self.label_14.setText("Thats Fantastic To hear always stay positive.")
        elif btn1 == "OPTIMISTIC":
                self.label_14.setText("Thats Fantastic To hear that you stay positive,When you are positive ,good things happen.")
        elif btn1=="CALM":
                self.label_14.setText("Understanding more about your feeling can help you take control of your emotional health.")
        elif btn1=="DEPRESSED":
                self.label_14.setText("Understanding more about your feeling can help you take control of your emotional health.During the Great Depression, when people laughed their worries disappeared. Audiences loved these funny men. I decided to become one will you??")

    def values3(self, b):
        btn1 = b.text()
        e2 = "The Factor That is Influencing You is "
        btn1 = e2 + btn1
        self.label_13.setText(str(btn1))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 1181, 801))
        self.stackedWidget.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
            "image: url(:/newPrefix/emt1.jpg);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(200, 70, 761, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pp1 = QtWidgets.QPushButton(self.page)
        self.pp1.setGeometry(QtCore.QRect(410, 630, 391, 28))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pp1.setFont(font)
        self.pp1.setStyleSheet("font: 22pt \"MV Boli\";")
        self.pp1.setObjectName("pp1")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(750, 760, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(240, 170, 671, 371))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/EMOTION.jpg);\n"
                                   "")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(240, 560, 141, 231))
        self.label_17.setStyleSheet("image: url(:/newPrefix/q5.jpg);")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/newPrefix/q5.jpg"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.p11 = QtWidgets.QPushButton(self.page_2)
        self.p11.setGeometry(QtCore.QRect(70, 290, 130, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p11.setFont(font)
        self.p11.setMouseTracking(True)
        self.p11.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p11.setObjectName("p11")
        self.p20 = QtWidgets.QPushButton(self.page_2)
        self.p20.setGeometry(QtCore.QRect(420, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p20.setFont(font)
        self.p20.setMouseTracking(True)
        self.p20.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p20.setObjectName("p20")
        self.p3 = QtWidgets.QPushButton(self.page_2)
        self.p3.setGeometry(QtCore.QRect(460, 430, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p3.setFont(font)
        self.p3.setMouseTracking(True)
        self.p3.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p3.setObjectName("p3")
        self.p5 = QtWidgets.QPushButton(self.page_2)
        self.p5.setGeometry(QtCore.QRect(360, 180, 151, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p5.setFont(font)
        self.p5.setMouseTracking(True)
        self.p5.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p5.setObjectName("p5")
        self.p21 = QtWidgets.QPushButton(self.page_2)
        self.p21.setGeometry(QtCore.QRect(530, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p21.setFont(font)
        self.p21.setMouseTracking(True)
        self.p21.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p21.setObjectName("p21")
        self.p2 = QtWidgets.QPushButton(self.page_2)
        self.p2.setGeometry(QtCore.QRect(340, 430, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p2.setFont(font)
        self.p2.setMouseTracking(True)
        self.p2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p2.setObjectName("p2")
        self.p1 = QtWidgets.QPushButton(self.page_2)
        self.p1.setGeometry(QtCore.QRect(220, 430, 100, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p1.setFont(font)
        self.p1.setMouseTracking(True)
        self.p1.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p1.setObjectName("p1")
        self.p6 = QtWidgets.QPushButton(self.page_2)
        self.p6.setGeometry(QtCore.QRect(690, 180, 130, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p6.setFont(font)
        self.p6.setMouseTracking(True)
        self.p6.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p6.setObjectName("p6")
        self.p24 = QtWidgets.QPushButton(self.page_2)
        self.p24.setGeometry(QtCore.QRect(870, 370, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p24.setFont(font)
        self.p24.setMouseTracking(True)
        self.p24.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p24.setObjectName("p24")
        self.p12 = QtWidgets.QPushButton(self.page_2)
        self.p12.setGeometry(QtCore.QRect(230, 290, 120, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p12.setFont(font)
        self.p12.setMouseTracking(True)
        self.p12.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p12.setObjectName("p12")
        self.p9 = QtWidgets.QPushButton(self.page_2)
        self.p9.setGeometry(QtCore.QRect(60, 180, 120, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p9.setFont(font)
        self.p9.setMouseTracking(True)
        self.p9.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p9.setObjectName("p9")
        self.p10 = QtWidgets.QPushButton(self.page_2)
        self.p10.setGeometry(QtCore.QRect(200, 180, 130, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p10.setFont(font)
        self.p10.setMouseTracking(True)
        self.p10.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p10.setObjectName("p10")
        self.p22 = QtWidgets.QPushButton(self.page_2)
        self.p22.setGeometry(QtCore.QRect(640, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p22.setFont(font)
        self.p22.setMouseTracking(True)
        self.p22.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p22.setObjectName("p22")
        self.p14 = QtWidgets.QPushButton(self.page_2)
        self.p14.setGeometry(QtCore.QRect(520, 290, 143, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p14.setFont(font)
        self.p14.setMouseTracking(True)
        self.p14.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p14.setObjectName("p14")
        self.p8 = QtWidgets.QPushButton(self.page_2)
        self.p8.setGeometry(QtCore.QRect(700, 430, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p8.setFont(font)
        self.p8.setMouseTracking(True)
        self.p8.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p8.setObjectName("p8")
        self.p18 = QtWidgets.QPushButton(self.page_2)
        self.p18.setGeometry(QtCore.QRect(200, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p18.setFont(font)
        self.p18.setMouseTracking(True)
        self.p18.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p18.setObjectName("p18")
        self.p7 = QtWidgets.QPushButton(self.page_2)
        self.p7.setGeometry(QtCore.QRect(570, 430, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p7.setFont(font)
        self.p7.setMouseTracking(True)
        self.p7.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p7.setObjectName("p7")
        self.p23 = QtWidgets.QPushButton(self.page_2)
        self.p23.setGeometry(QtCore.QRect(750, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p23.setFont(font)
        self.p23.setMouseTracking(True)
        self.p23.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p23.setObjectName("p23")
        self.p15 = QtWidgets.QPushButton(self.page_2)
        self.p15.setGeometry(QtCore.QRect(710, 290, 143, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p15.setFont(font)
        self.p15.setMouseTracking(True)
        self.p15.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p15.setObjectName("p15")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_19.setGeometry(QtCore.QRect(860, 180, 110, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setMouseTracking(True)
        self.pushButton_19.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.pushButton_19.setObjectName("p16")
        self.p25 = QtWidgets.QPushButton(self.page_2)
        self.p25.setGeometry(QtCore.QRect(880, 290, 91, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p25.setFont(font)
        self.p25.setMouseTracking(True)
        self.p25.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p25.setObjectName("p25")
        self.p13 = QtWidgets.QPushButton(self.page_2)
        self.p13.setGeometry(QtCore.QRect(370, 290, 130, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p13.setFont(font)
        self.p13.setMouseTracking(True)
        self.p13.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p13.setObjectName("p13")
        self.p19 = QtWidgets.QPushButton(self.page_2)
        self.p19.setGeometry(QtCore.QRect(310, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p19.setFont(font)
        self.p19.setMouseTracking(True)
        self.p19.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p19.setObjectName("p19")
        self.p17 = QtWidgets.QPushButton(self.page_2)
        self.p17.setGeometry(QtCore.QRect(80, 370, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p17.setFont(font)
        self.p17.setMouseTracking(True)
        self.p17.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p17.setObjectName("p17")
        self.p4 = QtWidgets.QPushButton(self.page_2)
        self.p4.setGeometry(QtCore.QRect(530, 180, 130, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold,")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.p4.setFont(font)
        self.p4.setMouseTracking(True)
        self.p4.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "font: 63 8pt \"Segoe UI Semibold,\";\n"
            "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color:blue\n"
            "\n"
            "\n"
            "")
        self.p4.setObjectName("p4")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(170, 60, 761, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 12pt \"Ravie\";")
        self.label_11.setObjectName("label_11")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_20.setGeometry(QtCore.QRect(470, 520, 241, 28))
        self.pushButton_20.setStyleSheet("font: 12pt \"Pristina\";")
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(290, 560, 601, 211))
        self.label_16.setStyleSheet("image: url(:/newPrefix/q3.jpg);")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/newPrefix/q3.jpg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.progressBar = QtWidgets.QProgressBar(self.page_3)
        self.progressBar.setGeometry(QtCore.QRect(430, 550, 501, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setGeometry(QtCore.QRect(570, 620, 181, 28))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 12pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalSlider = QtWidgets.QSlider(self.page_3)
        self.verticalSlider.setGeometry(QtCore.QRect(620, 60, 31, 441))
        self.verticalSlider.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "background-color: rgb(255, 255, 0);")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label_ = QtWidgets.QLabel(self.page_3)
        self.label_.setGeometry(QtCore.QRect(390, 70, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_.setFont(font)
        self.label_.setObjectName("label_")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(390, 160, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(390, 250, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(390, 350, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(400, 470, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_21.setGeometry(QtCore.QRect(610, 680, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("font: 10pt \"MV Boli\";")
        self.pushButton_21.setObjectName("pushButton_21")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(40, 30, 1041, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 75 20pt \"Script MT Bold\";\n"
                                   "font: 18pt \"8514oem\";\n"
                                   "text-decoration: underline;")
        self.label_8.setObjectName("label_8")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(150, 120, 831, 401))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 4, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 2, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 3, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 4, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 0, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 0, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_22.setGeometry(QtCore.QRect(510, 560, 93, 28))
        self.pushButton_22.setStyleSheet("font: 10pt \"Roman\";")
        self.pushButton_22.setObjectName("pushButton_22")
        self.label_18 = QtWidgets.QLabel(self.page_4)
        self.label_18.setGeometry(QtCore.QRect(230, 630, 691, 111))
        self.label_18.setStyleSheet("image: url(:/newPrefix/q.jpg);")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/newPrefix/q.jpg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setGeometry(QtCore.QRect(230, 40, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
                                   "font: 20pt \"Old English Text MT\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_5)
        self.label_10.setGeometry(QtCore.QRect(230, 150, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(True)
        self.label_10.setStyleSheet("alternate-background-color: rgb(255, 255, 255);\n"
                                    "color:blue")
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_17.setGeometry(QtCore.QRect(370, 640, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_18.setGeometry(QtCore.QRect(690, 640, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_12 = QtWidgets.QLabel(self.page_5)
        self.label_12.setGeometry(QtCore.QRect(230, 220, 741, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:blue")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(230, 290, 741, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:blue")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_5)
        self.label_14.setGeometry(QtCore.QRect(230, 380, 741, 181))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:blue")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setGeometry(QtCore.QRect(470, 570, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: 17pt \"Showcard Gothic\";")
        self.label_15.setObjectName("label_15")
        self.line = QtWidgets.QFrame(self.page_5)
        self.line.setGeometry(QtCore.QRect(140, 110, 931, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_20 = QtWidgets.QLabel(self.page_5)
        self.label_20.setGeometry(QtCore.QRect(280, 700, 561, 16))
        self.label_20.setStyleSheet("font: 10pt \"Snap ITC\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_5)
        self.label_21.setGeometry(QtCore.QRect(860, 740, 271, 20))
        self.label_21.setStyleSheet("font: 10pt \"Snap ITC\";")
        self.label_21.setObjectName("label_21")
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pp1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        # 2ND PAGE BUTTON EVENT

        self.p1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p8.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p9.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p10.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p11.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p12.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p13.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p14.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p15.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_19.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p17.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p18.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p19.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p20.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p21.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p22.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p23.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p24.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.p25.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        # self.p1.clicked.connect(self.stackedWidget.text_change1)
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_14.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_18.clicked.connect(lambda: MainWindow.close())
        # m1=self.pushButton_14.text()
        # self.textEdit.setText(m1)
        # changes done
        self.verticalSlider.valueChanged.connect(self.values1)
        self.p1.clicked.connect(lambda: self.values(self.p1))
        self.p2.clicked.connect(lambda: self.values(self.p2))
        self.p3.clicked.connect(lambda: self.values(self.p3))
        self.p4.clicked.connect(lambda: self.values(self.p4))
        self.p5.clicked.connect(lambda: self.values(self.p5))
        self.p6.clicked.connect(lambda: self.values(self.p6))
        self.p7.clicked.connect(lambda: self.values(self.p7))
        self.p8.clicked.connect(lambda: self.values(self.p8))
        self.p9.clicked.connect(lambda: self.values(self.p9))
        self.p10.clicked.connect(lambda: self.values(self.p10))
        self.p11.clicked.connect(lambda: self.values(self.p11))
        self.p12.clicked.connect(lambda: self.values(self.p12))
        self.p13.clicked.connect(lambda: self.values(self.p13))
        self.p14.clicked.connect(lambda: self.values(self.p14))
        self.p15.clicked.connect(lambda: self.values(self.p15))
        self.pushButton_19.clicked.connect(lambda: self.values(self.pushButton_19))
        self.p17.clicked.connect(lambda: self.values(self.p17))
        self.p18.clicked.connect(lambda: self.values(self.p18))
        self.p19.clicked.connect(lambda: self.values(self.p19))
        self.p20.clicked.connect(lambda: self.values(self.p20))
        self.p21.clicked.connect(lambda: self.values(self.p21))
        self.p22.clicked.connect(lambda: self.values(self.p22))
        self.p23.clicked.connect(lambda: self.values(self.p23))
        self.p24.clicked.connect(lambda: self.values(self.p24))
        self.p25.clicked.connect(lambda: self.values(self.p25))

        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_10.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_11.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_12.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_13.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_14.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_15.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_16.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        # elf.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.pushButton_2.clicked.connect(lambda: self.values3(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.values3(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.values3(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.values3(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.values3(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.values3(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.values3(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.values3(self.pushButton_9))
        self.pushButton_10.clicked.connect(lambda: self.values3(self.pushButton_10))
        self.pushButton_11.clicked.connect(lambda: self.values3(self.pushButton_11))
        self.pushButton_12.clicked.connect(lambda: self.values3(self.pushButton_12))
        self.pushButton_13.clicked.connect(lambda: self.values3(self.pushButton_13))
        self.pushButton_14.clicked.connect(lambda: self.values3(self.pushButton_14))
        self.pushButton_15.clicked.connect(lambda: self.values3(self.pushButton_15))
        self.pushButton_16.clicked.connect(lambda: self.values3(self.pushButton_16))
        # bck button
        self.pushButton_20.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_21.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_22.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        # self.progressBar.valueChanged['int'].connect(self.verticalSlider.setValue)
        self.verticalSlider.valueChanged['int'].connect(self.progressBar.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME TO EMOTIONAL HEALTH ASSISTANCE"))
        self.pp1.setText(_translate("MainWindow", "LETS EXPLORE IT"))
        self.label_3.setText(_translate("MainWindow", "CREATED BY- EKTA KUMARI"))
        self.p11.setText(_translate("MainWindow", "NUMB"))
        self.p20.setText(_translate("MainWindow", "ASHAMED"))
        self.p3.setText(_translate("MainWindow", "CONFIDENT"))
        self.p5.setText(_translate("MainWindow", "HAPPY"))
        self.p21.setText(_translate("MainWindow", "SAD"))
        self.p2.setText(_translate("MainWindow", "EXCITED"))
        self.p1.setText(_translate("MainWindow", "LOVING"))
        self.p6.setText(_translate("MainWindow", "PROUD"))
        self.p24.setText(_translate("MainWindow", "DEPRESSED"))
        self.p12.setText(_translate("MainWindow", "OK"))
        self.p9.setText(_translate("MainWindow", "GRATEFUL"))
        self.p10.setText(_translate("MainWindow", "TIRED"))
        self.p22.setText(_translate("MainWindow", "BORED"))
        self.p14.setText(_translate("MainWindow", "ANGRY"))
        self.p8.setText(_translate("MainWindow", "CALM"))
        self.p18.setText(_translate("MainWindow", "AFRAID"))
        self.p7.setText(_translate("MainWindow", "OPTIMISTIC"))
        self.p23.setText(_translate("MainWindow", "GUILTY"))
        self.p15.setText(_translate("MainWindow", "OVERWHELMED"))
        self.pushButton_19.setText(_translate("MainWindow", "FRUSTRATED"))
        self.p25.setText(_translate("MainWindow", "NUMB"))
        self.p13.setText(_translate("MainWindow", "ANNOYED"))
        self.p19.setText(_translate("MainWindow", "INSECURE"))
        self.p17.setText(_translate("MainWindow", "ANXIOUS"))
        self.p4.setText(_translate("MainWindow", "JOYFUL"))
        self.label_11.setText(_translate("MainWindow", "OKAY NOW TELL US WHAT WOULD YOU LIKE TO ACHIEVE"))
        self.pushButton_20.setText(_translate("MainWindow", "BACK"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_.setText(_translate("MainWindow", "EXTREMELY"))
        self.label_4.setText(_translate("MainWindow", "VERY"))
        self.label_5.setText(_translate("MainWindow", "FAIRLY"))
        self.label_6.setText(_translate("MainWindow", "A LITTLE"))
        self.label_7.setText(_translate("MainWindow", "SLIGHTLY"))
        self.pushButton_21.setText(_translate("MainWindow", "BACK"))
        self.label_8.setText(_translate("MainWindow",
                                        "OK NOW TELL US WHATS THE FACTOR INFLUENCING YOUR STRESS.THIS WILL HELP US TO GUIDE YOU BETTER"))
        self.pushButton_10.setText(_translate("MainWindow", "PARTENER"))
        self.pushButton_5.setText(_translate("MainWindow", "SOCIAL MEDIA"))
        self.pushButton_2.setText(_translate("MainWindow", "PARTENER"))
        self.pushButton_9.setText(_translate("MainWindow", "FRIENDS"))
        self.pushButton_12.setText(_translate("MainWindow", "WEATHER"))
        self.pushButton_6.setText(_translate("MainWindow", "HOME"))
        self.pushButton_4.setText(_translate("MainWindow", "BEING MYSELLF"))
        self.pushButton_13.setText(_translate("MainWindow", "MONEY"))
        self.pushButton_7.setText(_translate("MainWindow", "BODY"))
        self.pushButton_16.setText(_translate("MainWindow", "FOOD"))
        self.pushButton_11.setText(_translate("MainWindow", "FAMILY"))
        self.pushButton_8.setText(_translate("MainWindow", "BAD SLEEP"))
        self.pushButton_3.setText(_translate("MainWindow", "SCHOOL"))
        self.pushButton_15.setText(_translate("MainWindow", "HEALTH"))
        self.pushButton_14.setText(_translate("MainWindow", "WORK"))
        self.pushButton_22.setText(_translate("MainWindow", "BACK"))
        self.label_9.setText(_translate("MainWindow", "Okay Here is Our Solution According to the Problem"))
        self.label_10.setText(_translate("MainWindow", "hell"))
        self.pushButton_17.setText(_translate("MainWindow", "BACK"))
        self.pushButton_18.setText(_translate("MainWindow", "EXIT"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "THANK YOU"))
        self.label_20.setText(_translate("MainWindow", "GIVE YOUR STRESS WINGS AND LET IT FLY AWAY"))
        self.label_21.setText(_translate("MainWindow", "- TERRI GUILLEMETS"))


import icons
import test

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
