# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 605))
        MainWindow.setMaximumSize(QtCore.QSize(600, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.page = QtWidgets.QTabWidget(self.centralwidget)
        self.page.setGeometry(QtCore.QRect(250, 10, 341, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setAutoFillBackground(True)
        self.page.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.page.setIconSize(QtCore.QSize(40, 40))
        self.page.setObjectName("page")
        self.explore = QtWidgets.QWidget()
        self.explore.setObjectName("explore")
        self.groupBox_2 = QtWidgets.QGroupBox(self.explore)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 311, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.yuhun_single = QtWidgets.QRadioButton(self.layoutWidget)
        self.yuhun_single.setObjectName("yuhun_single")
        self.gridLayout.addWidget(self.yuhun_single, 0, 0, 1, 1)
        self.yuhun_driver = QtWidgets.QRadioButton(self.layoutWidget)
        self.yuhun_driver.setObjectName("yuhun_driver")
        self.gridLayout.addWidget(self.yuhun_driver, 0, 1, 1, 1)
        self.yuhun_passenger = QtWidgets.QRadioButton(self.layoutWidget)
        self.yuhun_passenger.setObjectName("yuhun_passenger")
        self.gridLayout.addWidget(self.yuhun_passenger, 0, 2, 1, 1)
        self.yuhun_two = QtWidgets.QRadioButton(self.layoutWidget)
        self.yuhun_two.setChecked(True)
        self.yuhun_two.setObjectName("yuhun_two")
        self.gridLayout.addWidget(self.yuhun_two, 1, 0, 1, 1)
        self.yuhun_three = QtWidgets.QRadioButton(self.layoutWidget)
        self.yuhun_three.setObjectName("yuhun_three")
        self.gridLayout.addWidget(self.yuhun_three, 1, 1, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.explore)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 180, 311, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 310, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.need_mark_shi_shen = QtWidgets.QCheckBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.need_mark_shi_shen.sizePolicy().hasHeightForWidth())
        self.need_mark_shi_shen.setSizePolicy(sizePolicy)
        self.need_mark_shi_shen.setObjectName("need_mark_shi_shen")
        self.horizontalLayout_2.addWidget(self.need_mark_shi_shen)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mark_shi_shen_pos_index = QtWidgets.QSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mark_shi_shen_pos_index.sizePolicy().hasHeightForWidth())
        self.mark_shi_shen_pos_index.setSizePolicy(sizePolicy)
        self.mark_shi_shen_pos_index.setMinimum(1)
        self.mark_shi_shen_pos_index.setMaximum(5)
        self.mark_shi_shen_pos_index.setObjectName("mark_shi_shen_pos_index")
        self.horizontalLayout_2.addWidget(self.mark_shi_shen_pos_index)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 70, 301, 23))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.system_resize_resolution = QtWidgets.QComboBox(self.layoutWidget2)
        self.system_resize_resolution.setMaxVisibleItems(2)
        self.system_resize_resolution.setObjectName("system_resize_resolution")
        self.system_resize_resolution.addItem("")
        self.system_resize_resolution.addItem("")
        self.horizontalLayout_3.addWidget(self.system_resize_resolution)
        self.groupBox_4 = QtWidgets.QGroupBox(self.explore)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 300, 311, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 291, 241))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border: none;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.page.addTab(self.explore, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.page.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.page.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.page.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.page.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 201, 61))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 130, 241, 481))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(5, 21, 231, 451))
        self.textBrowser.setStyleSheet("border=none;")
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(250, 580, 341, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_btn = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        self.end_btn = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_btn.sizePolicy().hasHeightForWidth())
        self.end_btn.setSizePolicy(sizePolicy)
        self.end_btn.setObjectName("end_btn")
        self.horizontalLayout.addWidget(self.end_btn)
        self.quit_btn = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit_btn.sizePolicy().hasHeightForWidth())
        self.quit_btn.setSizePolicy(sizePolicy)
        self.quit_btn.setObjectName("quit_btn")
        self.horizontalLayout.addWidget(self.quit_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "阴阳师辅助脚本"))
        self.groupBox_2.setTitle(_translate("MainWindow", "模式"))
        self.yuhun_single.setText(_translate("MainWindow", "单刷"))
        self.yuhun_driver.setText(_translate("MainWindow", "司机"))
        self.yuhun_passenger.setText(_translate("MainWindow", "乘客"))
        self.yuhun_two.setText(_translate("MainWindow", "双开"))
        self.yuhun_three.setText(_translate("MainWindow", "三开"))
        self.groupBox_3.setTitle(_translate("MainWindow", "参数"))
        self.need_mark_shi_shen.setText(_translate("MainWindow", "自动标记式神"))
        self.label_2.setText(_translate("MainWindow", "从左往右位置:"))
        self.label_3.setText(_translate("MainWindow", "WIN10系统缩放比例："))
        self.system_resize_resolution.setItemText(0, _translate("MainWindow", "125%"))
        self.system_resize_resolution.setItemText(1, _translate("MainWindow", "100%"))
        self.groupBox_4.setTitle(_translate("MainWindow", "注意事项"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">1.1111111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">2.2222222</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">3.3333333</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">4.4444444</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">5.5555555</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">6.6666666</span></p></body></html>"))
        self.page.setTabText(self.page.indexOf(self.explore), _translate("MainWindow", "御魂副本"))
        self.page.setTabText(self.page.indexOf(self.tab_2), _translate("MainWindow", "探索"))
        self.page.setTabText(self.page.indexOf(self.tab), _translate("MainWindow", "百鬼夜行"))
        self.page.setTabText(self.page.indexOf(self.tab_3), _translate("MainWindow", "说明"))
        self.page.setTabText(self.page.indexOf(self.tab_4), _translate("MainWindow", "关于"))
        self.label.setText(_translate("MainWindow", "阴阳师辅助脚本"))
        self.groupBox.setTitle(_translate("MainWindow", "日志"))
        self.start_btn.setText(_translate("MainWindow", "开始"))
        self.end_btn.setText(_translate("MainWindow", "停止"))
        self.quit_btn.setText(_translate("MainWindow", "退出"))
