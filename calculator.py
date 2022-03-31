import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, \
    QLineEdit, QLabel
from function_Final import *

class Interface_method:

    def __init__(self):
        self.valueFunctions = {
            'sin': self.sin,
            'arcsin': self.arcsin,
            'cos': self.cos,
            'arctan': self.arctan,
        }

    def sin(self, value):
        return mySin(value)


    def arcsin(self, value):
        return invert_angle_to_rad(asin(value))

    def cos(self, value):
        return myCos(value)

    def arctan(self, value):
        return atan(value)


    def get_func_name(self):
        return sorted(self.valueFunctions.keys())

    def get_func_result(self, name, value, isdeg):
        if isdeg == True:
            if "arc" in name:
                return math.degrees(self.valueFunctions[name](value))
            else:
                return self.valueFunctions[name](math.radians(value))
        else:
            return self.valueFunctions[name](value)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.method = Interface_method()
        self.initUI()
    #UI设计
    def initUI(self):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setFixedSize(int(self.width * 0.2), int(self.width * 0.2 * 0.3))

        self.center()
        self.setWindowTitle('Calculator')



        self.btn_Calc = QPushButton('计算', self)
        self.btn_Calc.clicked.connect(self.btn_Calc_on_click)

        self.cb_method = QComboBox(self)
        self.cb_method.addItems(self.method.get_func_name())
        self.cb_method.currentIndexChanged.connect(self.cb_method_changed)

        self.btn_format_input = QPushButton('角度制', self)
        self.btn_format_input.clicked.connect(self.btn_format_on_click)
        self.btn_format_input.setEnabled(False)

        self.btn_format_output = QPushButton('角度制', self)
        self.btn_format_output.clicked.connect(self.btn_format_on_click)

        self.qle_input = QLineEdit(self)
        self.qle_input.textEdited.connect(self.input_format_check)
        self.qle_input.returnPressed.connect(self.btn_Calc_on_click)

        self.qle_output = QLineEdit(self)
        self.qle_output.setFocusPolicy(Qt.NoFocus)

        self.qlb_result = QLabel('结果', self)

        self.hbox_input = QHBoxLayout()
        self.hbox_output = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.hbox_input.addWidget(self.cb_method, 1)
        self.hbox_input.addWidget(self.qle_input, 4)
        self.hbox_input.addWidget(self.btn_format_input, 1)

        self.hbox_output.addWidget(self.qlb_result, 1, Qt.AlignCenter)
        self.hbox_output.addWidget(self.qle_output, 4)
        self.hbox_output.addWidget(self.btn_format_output, 1)

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_output)
        self.vbox.addWidget(self.btn_Calc)
        self.setLayout(self.vbox)
        self.show()

    # 将计算UI放置屏幕中间
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #
    def input_format_check(self):
        try:
            str_input = self.qle_input.text().strip();
            self.method.get_func_result(self.cb_method.currentText(), float(eval(str_input)),
                                        self.btn_format_input.text() == "角度制" and self.btn_format_input.isEnabled() or self.btn_format_output.text() == "角度制" and self.btn_format_output.isEnabled())
        except:
            self.qle_input.setStyleSheet("color: red;")
            self.btn_Calc.setEnabled(False)
        else:
            self.qle_input.setStyleSheet("color: black;")
            self.btn_Calc.setEnabled(True)

    flag = 0
    def cb_method_changed(self):
        if "arc" in self.cb_method.currentText():
            self.btn_format_input.setEnabled(False)
            self.btn_format_output.setEnabled(True)
            # self.flag = 0
        else:
            self.btn_format_input.setEnabled(True)
            self.btn_format_output.setEnabled(False)
            # self.flag = 1
        self.input_format_check()

    def btn_format_on_click(self):
        sender = self.sender()
        text = sender.text()
        sender.setText("弧度制" if text == "角度制" else "角度制")

    def btn_Calc_on_click(self):
        str_input = self.qle_input.text().strip();
        if (str_input == ''):
            return
        try:
            self.qle_output.setText(
                str(self.method.get_func_result(self.cb_method.currentText(), float(eval(str_input)),
                                                self.btn_format_input.text() == "角度制" and self.btn_format_input.isEnabled() or self.btn_format_output.text() == "角度制" and self.btn_format_output.isEnabled())))
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
