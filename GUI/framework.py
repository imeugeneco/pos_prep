# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'framework.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -1, 1201, 771))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 1161, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 401, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 50, 261, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 50, 61, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(470, 20, 86, 20))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 401, 33))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.gridLayout_2.addWidget(self.dateEdit_4, 0, 2, 1, 1)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.gridLayout_2.addWidget(self.dateEdit_3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 401, 33))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.dateEdit_5 = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.gridLayout_3.addWidget(self.dateEdit_5, 0, 2, 1, 1)
        self.dateEdit_6 = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.gridLayout_3.addWidget(self.dateEdit_6, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 401, 33))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 0, 3, 1, 1)
        self.dateEdit_9 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        self.dateEdit_9.setObjectName("dateEdit_9")
        self.gridLayout_5.addWidget(self.dateEdit_9, 0, 2, 1, 1)
        self.dateEdit_10 = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        self.dateEdit_10.setObjectName("dateEdit_10")
        self.gridLayout_5.addWidget(self.dateEdit_10, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.label_2.setText(_translate("MainWindow", "배달의민족"))
        self.label.setText(_translate("MainWindow", "검색기간"))
        self.label_3.setText(_translate("MainWindow", "나우웨이팅"))
        self.label_4.setText(_translate("MainWindow", "배달의민족"))
        self.pushButton_2.setText(_translate("MainWindow", "파일 첨부"))
        self.pushButton_3.setText(_translate("MainWindow", "완료"))
        self.label_5.setText(_translate("MainWindow", "크롤링"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "크롤링"))
        self.label_7.setText(_translate("MainWindow", "검색기간"))
        self.pushButton_4.setText(_translate("MainWindow", "검색"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "매출분석"))
        self.label_8.setText(_translate("MainWindow", "검색기간"))
        self.pushButton_5.setText(_translate("MainWindow", "검색"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "배달분석"))
        self.label_10.setText(_translate("MainWindow", "검색기간"))
        self.pushButton_7.setText(_translate("MainWindow", "검색"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "인건비"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "매입"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "재고"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "순수익"))