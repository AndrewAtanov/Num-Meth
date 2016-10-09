from PyQt5 import QtGui, QtCore, QtWidgets
import sys
from design import Ui_Form
from solver import Solver
from Plotter import Plotter
import numpy as np


class MainProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)

        self.solver = Solver()
        self.plotter = Plotter(self.plot_widget, self.solver)

        # Connect "add" button with a custom function (addInputTextToListbox)

        self.plot_btn.clicked.connect(self.plot)

        # Set functions
        self.read_ro_btn.clicked.connect(self.read_ro)
        self.read_s_btn.clicked.connect(self.read_s)
        self.read_z_btn.clicked.connect(self.read_z)

    def plot(self):
        self.plotter.plot(self.plot_combobox.currentText(),
                          float(self.arg_start.text()),
                          float(self.arg_end.text()))

    def read_ro(self):
        try:
            a = float(self.ro_a.text())
            b = float(self.ro_b.text())
        except:
            a = b = 1
        self.solver.create_ro(a, b)

    def read_s(self):
        self.solver.create_s(self.s_expr.text())

    def read_z(self):
        self.solver.create_z(self.z_expr.text())




app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
prog = MainProgram(dialog)
dialog.show()
sys.exit(app.exec_())
