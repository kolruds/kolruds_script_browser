import json
import os

from PySide import QtGui, QtCore

from base_model import BaseModel


class Tree_Model(BaseModel):
	def __init__(self, main_model):
		super(Tree_Model, self).__init__()
		self.main_model = main_model

		self._header_items = ['Filetype', 'Name', 'Category', 'Author', 'Version']

		self.scripts = self.read_scripts()
		self.q_model = QtGui.QStandardItemModel()
		self.q_model.setHorizontalHeaderLabels(self._header_items)


	def read_scripts(self):
		""" Return parsed json from script file.
		No args, file is specified by self.main_model.user_settings.mxs_repo
		"""
		_dir = os.path.join(self.main_model.user_settings.mxs_repo, 'scripts.txt')
		try:
			with open(_dir, 'r') as f:
				return json.loads(f.read())
		except:
			pass

	def build(self):
		""" Add all script keys found in the scripts file
		No args, data is specified by self.scripts
		"""
		self.scripts = self.read_scripts()
		
		if not self.scripts:
			self.q_model.clear()
			self.q_model.setHorizontalHeaderLabels(self._header_items)
			return

		for script in self.scripts:
			name = QtGui.QStandardItem(script)
			author = QtGui.QStandardItem(self.scripts[script]['author'])
			category = QtGui.QStandardItem(self.scripts[script]['category'])
			version = QtGui.QStandardItem(str(self.scripts[script]['version']))
			file_ext = os.path.splitext(self.scripts[script]['filename'])[1]
			filetype = QtGui.QStandardItem(self.icon_switch(file_ext), '')

			item = self.q_model.appendRow([filetype, name, category, author, version])

	def icon_switch(self, ext):
		""" Return appropriate QIcon for extensin.

		Arg ext :  File extension - 'ms'
		"""
		if ext[0] != '.':
			ext = '.' + ext

		if ext == '.ms':
			return QtGui.QIcon('icons\\file_3dsmax_ms.ico')
		elif ext == '.mse':
			return QtGui.QIcon('icons\\file_3dsmax_mse.ico')
		elif ext == '.mcr':
			return QtGui.QIcon('icons\\file_3dsmax_mcr.ico')
		elif ext == '.mcg':
			return QtGui.QIcon('icons\\file_3dsmax_maxcompound.ico')





"""
class Tree_Model(QtCore.QAbstractItemModel, BaseModel):
	def __init__(self, main_model):
		super(Tree_Model, self).__init__()
		self.main_model = main_model
		self.scripts = self.read_scripts()

		self.build()

		print(self.rowCount())

		# TODO: More dynamic header solution, preferably user controlled
		self.setHorizontalHeaderLabels(['Name', 'Category', 'Filetype', 'Version'])

	def read_scripts(self):
		"""""" Return parsed json from script file.
		No args, file is specified by self.main_model.user_settings.mxs_repo
		""""""
		_dir = os.path.join(self.main_model.user_settings.mxs_repo, 'scripts.txt')
		print _dir
		try:
			with open(_dir, 'r') as f:
				return json.loads(f.read())
		except IOError, ValueError:
			# File does not exist or is not valid json, return empty dict.
			return {}

	def build(self):
		"""""" Add all script keys found in the scripts file
		No args, data is specified by self.scripts
		""""""
		#root = self.invisibleRootItem()
		scripts = self.scripts

		for script in scripts:
			item_name = QtGui.QStandardItem(script)
			item_category = QtGui.QStandardItem(self.scripts[script]['category'])
			item_filetype = QtGui.QStandardItem(str(os.path.splitext(script)[1]))
			item_version = QtGui.QStandardItem(str(self.scripts[script]['version']))

			item = self.appendRow([item_name, item_category, item_filetype, item_version])
			#item.setData(self.data[script])

 Old, didnt work very well..
class Tree_Model(BaseModel):
	def __init__(self, main_model):
		super(Tree_Model, self).__init__()
		self.main_model = main_model
		#self._root_item = self.tree_model.invisibleRootItem()
		self.data = self.read_scripts_file()
		self.read_scripts_file()
		self.header = ['File', 'Category']
		#self.data = ''
		#self.tree_model = self.build_tree()
		#self.tree_model.setHeaderData(0, QtCore.Qt.Horizontal, self.header[0])
		#self.tree_model.setHeaderData(1, QtCore.Qt.Horizontal, self.header[1])
		#self._root_item.appendRow(QtGui.QStandardItem('test'))
		#self.tree_model.setHorizontalHeaderLabels(self.header)

		# Read and store the scripts file


	def read_scripts_file(self):
		_dir = os.path.join(self.main_model.user_settings.mxs_repo, 'scripts.txt')
		try:
			with open(_dir, 'r') as f:
				return json.loads(f.read())
		except:
			print 'could not parse'

	def get_item(self, key):
		item = QtGui.QStandardItem(key)
		category = QtGui.QStandardItem(self.data[key]['category'])
		return [item, category]

	def build_tree(self):
		tree_model = QtGui.QStandardItemModel()
		for i in self.data:
			item = self.get_item(i)
			tree_model.appendRow(item)
		tree_model.setHorizontalHeaderLabels(self.header)
		return tree_model

"""
