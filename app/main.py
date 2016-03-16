import os
import sys

from PySide import QtCore, QtGui, shiboken

import views.main_app_view; reload(views.main_app_view) # DEV ONLY, REMOVE IN PRODUCTION
from views.main_app_view import MainView
import ctrls.main_controller; reload(ctrls.main_controller) # DEV ONLY, REMOVE IN PRODUCTION
from ctrls.main_controller import MainController
import model.main_model; reload(model.main_model) # DEV ONLY, REMOVE IN PRODUCTION
from model.main_model import MainModel


class Main_App(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Main_App, self).__init__(parent)
		self.model = MainModel()
		self.controller = MainController(self.model)
		self.main_view = MainView(self.model, self.controller)
		#self.main_view.show()


if __name__ == '__main__':
	# Do a try except to run app either as 3dsmax child, or standalone
	try:
		from MaxPlus import AttachQWidgetToMax
		# Protect script from being garbage collected by max
		class _GCProtector(object):
		    widgets = []

		# QApplication already running in max, fetch the instance
		app = QtGui.QApplication.instance()
		if not app:
		    app = QtGui.QApplication([])

		main_app = Main_App()
		MaxPlus.AttachQWidgetToMax(main_app.main_view)
		main_app.main_view.show()
		_GCProtector.widgets.append(main_app)
		_GCProtector.widgets.append(main_app.main_view)
	except ImportError:
		app = QtGui.QApplication([])
		main_app = Main_App()
		main_app.main_view.show()
		app.exec_()
