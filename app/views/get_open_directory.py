import os

from PySide import QtGui

class Open_Directory_Dialog(QtGui.QFileDialog):
	def __init__(self):
		super(Open_Directory_Dialog, self).__init__()

		self.setFileMode(QtGui.QFileDialog.Directory)
		self.setOption(QtGui.QFileDialog.ShowDirsOnly)
		self.setOption(QtGui.QFileDialog.DontUseNativeDialog)

	def set_alternating_row_colors(self):
		tree_list = self.findChild(QtGui.QSplitter).findChild(
							   	   QtGui.QFrame).findChild(
							  	   QtGui.QStackedWidget).children()
		for i in tree_list:
			if type(i) == QtGui.QWidget:
				try:
					i.findChild(QtGui.QTreeView).setAlternatingRowColors(True)
				except:
					pass

	def run(self):
		if self.exec_():
			return self.selectedFiles()[0]
