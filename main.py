from PyQt5 import QtGui, QtCore, QtWidgets

import sys
from design import Ui_Form
from solver import Solver
from Plotter import Plotter
import numpy as np
import Tabulate
from PyQt5.QtGui import QDoubleValidator


class MainProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)

        self.solver = Solver()

        self.plotter = Plotter(self.plot_widget, self.solver)

        self.trajectory_plot = Plotter(self.plot_trajectory, self.solver)
        self.filt_plot = Plotter(self.plot_filt, self.solver)

        # Connect "add" button with a custom function (addInputTextToListbox)

        self.plot_btn.clicked.connect(self.plot)

        self.start_btn.clicked.connect(self.start)

        # Set functions
        self.read_ro_btn.clicked.connect(self.read_ro)
        self.read_s_btn.clicked.connect(self.read_s)
        self.read_z_btn.clicked.connect(self.read_z)

        self.ro_a.setValidator(QDoubleValidator(self.beta_end))
        self.ro_b.setValidator(QDoubleValidator(self.beta_end))
        self.x0.setValidator(QDoubleValidator(self.beta_end))
        self.y0.setValidator(QDoubleValidator(self.beta_end))
        self.T.setValidator(QDoubleValidator(self.beta_end))
        self.beta_start.setValidator(QDoubleValidator(self.beta_end))
        self.beta_end.setValidator(QDoubleValidator(self.beta_end))

    def plot(self):
        self.plotter.plot(self.plot_combobox.currentText(),
                          float(self.arg_start.text()),
                          float(self.arg_end.text()))

    def read_ro(self):
        try:
            a = self.get_float_from(self.ro_a)
            b = self.get_float_from(self.ro_b)
        except ValueError:
            return
        self.solver.create_ro(a, b)

    def read_s(self):
        self.solver.create_s(self.s_expr.text())

    def read_z(self):
        self.solver.create_z(self.z_expr.text())

    def start(self):
        try:
            self.read_ro()
            self.read_s()
            self.read_z()

            self.solver.set_parameters(self.get_float_from(self.x0),
                                       self.get_float_from(self.y0),
                                       self.get_float_from(self.T))

            self.solver.save_init_func()

            if self.auto_mode.isChecked():
                beta_grid = np.linspace(self.get_float_from(self.beta_start), self.get_float_from(self.beta_end), 10)
            else:
                beta_grid = np.array([self.get_float_from(self.beta_start)])

            self.solver.tabulate_int()

            x, y, beta = self.solver.choose_best_diffeq_solve(beta_grid)

            self.solver.set_solve(x, y)
            self.solver.save_solve()

            self.trajectory_plot.plot_tabulate(x, self.solver.s(self.solver.t_grid()), 'bo-')
            self.filt_plot.plot_tabulate(self.solver.t_grid(), y, 'ro-')
        except ValueError:
            return

    def error_dialog(self, text):
        message = QtWidgets.QMessageBox.critical(None, "Error message", text,
                                                 QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def get_float_from(self, le):
        try:
            return float(le.text().replace(',','.'))
        except ValueError:
            self.error_dialog('{} should be float!'.format(le.objectName()))
            raise ValueError


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
prog = MainProgram(dialog)
dialog.show()
sys.exit(app.exec_())
