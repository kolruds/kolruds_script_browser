from PySide import QtGui, QtCore

class Scripts_Tree(QtGui.QTreeView):
	"""
	Subclass of QtGui.QTreeView.
	Implements deselection and various context menus.
	"""
	def __init__(self, parent=None):
		super(Scripts_Tree, self).__init__(parent)

		self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
		self.header().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.header().customContextMenuRequested.connect(self.header_menu)
		self.addMenuActions()
		#self.menus = self.create_menus()

	def addMenuActions(self):
		self.run = QtGui.QAction(self)
		self.run.setText('Run')
		self.info = QtGui.QAction(self)
		self.info.setText('Info')
		self.addAction(self.run)
		self.addAction(self.info)

	def create_menus(self):
		menus = []
		for i in range(self.model().columnCount()):
			m = self.create_menu(i)
			menus.append(m)
		self.menus = menus

	def create_menu(self, index):
		items = []
		for i in range(self.model().rowCount()):
			items.append(self.model().item(i, index).text())
		self.menu = QtGui.QMenu(self.header())
		for i in set(items):
			item = QtGui.QAction(i, self)
			item.setCheckable(True)
			item.setChecked(True)
			#item.toggled.connect(self.header_menu_item_clicked)
			self.menu.addAction(item)
		return self.menu

	def header_menu_item_clicked(self, toggle):
		#print toggle
		pass

	def header_menu(self, pos):
		logical_index = self.header().logicalIndexAt(pos)
		section_x = self.header().sectionPosition(logical_index)
		section_y = self.header().pos().y()
		logical_pos = QtCore.QPoint(section_x, section_y)
		global_pos = self.mapToGlobal(logical_pos)

		if not logical_index == 1:
			""""""
			menu = self.menus[logical_index]
			#menu = self.create_menu(logical_index)
			menu.setMinimumWidth(self.header().sectionSize(logical_index))
			menu_click = menu.exec_(self.mapToGlobal(logical_pos))
			#print menu_click.text()
			if menu_click:
				self.hide_row_by_value(logical_index, menu_click.text(), menu_click.isChecked())

	def hide_row_by_value(self, column, value, hidden):
		for i in range(self.model().rowCount()):
			val = self.model().item(i, column).text()
			if val == value:
				self.setRowHidden(i, self.model().invisibleRootItem().index(), (not hidden))


	def mousePressEvent(self, event):
		item = self.indexAt(event.pos())
		QtGui.QTreeView.mousePressEvent(self, event)
		if not self.selectionModel().isSelected(item):
			self.clearSelection()