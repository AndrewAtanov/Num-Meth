from PyQt5 import QtGui, QtCore, QtWidgets

import sys
from design import Ui_Form
from solver import Solver
from Plotter import Plotter
import numpy as np
import Tabulate

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

    def start(self):

        self.read_ro()
        self.read_s()
        self.read_z()

        self.solver.set_parameters(self.get_float_from(self.x0),
                                   self.get_float_from(self.y0),
                                   self.get_float_from(self.T))

        self.solver.save_init_func()

        if self.auto_mode.isChecked():
            beta_grid = np.linspace(-4, 4, 10)
        else:
            try:
                beta = float(self.beta.text())
            except ValueError:
                self.error_dialog('Beta should be float!')
                return
            beta_grid = np.array([beta])


        x, y, beta = self.solver.choose_best_diffeq_solve(beta_grid)

        self.solver.set_solve(x, y)
        self.solver.save_solve()

        self.trajectory_plot.plot_tabulate(x, self.solver.s(self.solver.t_grid()), 'bo-')
        self.filt_plot.plot_tabulate(self.solver.t_grid(), y, 'ro-')

    def error_dialog(self, text):
        message = QtWidgets.QMessageBox.critical(None, "Error message", text,
                                                 QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def get_float_from(self, le):
        try:
            return float(le.text())
        except ValueError:
            self.error_dialog('{} should be float!'.format(le.objectName()))


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
prog = MainProgram(dialog)
dialog.show()
sys.exit(app.exec_())
