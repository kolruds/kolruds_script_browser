import os

from PySide import QtCore, QtGui

from gen.ui_kolruds_script_browser import Ui_kolruds_script_browser
import scripts_tree_view; reload(scripts_tree_view)
from scripts_tree_view import Scripts_Tree

class MainView(QtGui.QWidget):
	def __init__(self, model, ctrl):
		self.model = model
		self.ctrl = ctrl
		super(MainView, self).__init__()

		self.build_ui()
		self.custom_attributes_treeview()
		self.connect_signals()

		# Initialize the values for user settings
		self.model.user_settings.announce_update()
		#self.set_models()

	#def set_models(self):
		#self.ui.view_tree_scripts.setModel(self.model.tree_model.tree_model)

	def set_style(self):
		with open(str(os.path.join(os.path.dirname(__file__), 'styles', 'style.txt')), 'r') as f:
			self._style = f.read()
			self.setStyleSheet(self._style)

	def build_ui(self):
		# Load and build UI
		self.ui = Ui_kolruds_script_browser()
		self.ui.setupUi(self)

		# Apply stylesheet
		self.set_style()

		# MVC stuff, add subscribe to model
		self.model.user_settings.subscribe_update(self.mxs_repo_changed)
		self.model.user_settings.subscribe_update(self.mcg_repo_changed)
		#self.model.user_settings.subscribe_update(self.browse_mxs_repo)

	def custom_attributes_treeview(self):
		# Get the position of tree in layout, then delete with takeAt(index)
		idx = self.ui.verticalLayout.indexOf(self.ui.view_tree_scripts)
		t = self.ui.verticalLayout.takeAt(idx)
		# Add our subclassed tree
		self.ui.view_tree_scripts = Scripts_Tree(self.ui.tab_scripts)
		self.ui.view_tree_scripts.setObjectName('view_tree_scripts')
		self.ui.verticalLayout.addWidget(self.ui.view_tree_scripts)

	def resize_cols(self):
		self.ui.view_tree_scripts.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
		self.ui.view_tree_scripts.header().setResizeMode(1, QtGui.QHeaderView.Stretch)
		self.ui.view_tree_scripts.header().setResizeMode(2, QtGui.QHeaderView.Stretch)
		self.ui.view_tree_scripts.header().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
		self.ui.view_tree_scripts.header().setStretchLastSection(False)
		self.ui.view_tree_scripts.header().resizeSection(4, 45)

	def connect_signals(self):
		# Connect signals:
		self.ui.btn_browse_mxs_repo.clicked.connect(self.browse_mxs_repo)
		self.ui.btn_browse_mcg_repo.clicked.connect(self.browse_mcg_repo)
		self.ui.btn_open_mxs_publish.clicked.connect(self.publish_mxs)
		self.ui.btn_open_mcg_publish.clicked.connect(self.publish_mcg)
		self.ui.btn_refresh_tree.clicked.connect(self.reload_scripts)
		self.ui.view_tree_scripts.clicked.connect(self.tree_clicked)
		self.ui.view_tree_scripts.doubleClicked.connect(self.tree_doubleClicked)
		#self.ui.view_tree_scripts.rightClick.connect(self.tree_rightClick)

	def browse_mxs_repo(self):
		from get_open_directory import Open_Directory_Dialog
		dialog = Open_Directory_Dialog()
		dialog.setStyleSheet(self._style)
		self.ctrl.c_browse_mxs_repo(dialog)

	def mxs_repo_changed(self):
		self.ui.lne_mxs_repo_path.setText(self.model.user_settings.mxs_repo)
		self.reload_scripts()

	def browse_mcg_repo(self):
		from get_open_directory import Open_Directory_Dialog
		dialog = Open_Directory_Dialog()
		dialog.setStyleSheet(self._style)
		self.ctrl.c_browse_mcg_repo(dialog)

	def mcg_repo_changed(self):
		self.ui.lne_mcg_repo_path.setText(self.model.user_settings.mcg_repo)
		#self.model.tree_model.build_tree()
		#self.set_models()

	def publish_mxs(self):
		from get_open_file import Open_File_Dialog
		dialog = Open_File_Dialog('MaxScript (*.ms *.mcr)')
		dialog.setStyleSheet(self._style)
		self.ctrl.c_publish_mxs(dialog)

	def publish_mcg(self):
		self.ctrl.c_publish_mcg(dialog)

	def reload_scripts(self):
		self.model.tree_model.build()
		self.ui.view_tree_scripts.setModel(self.model.tree_model.q_model)
		self.ui.view_tree_scripts.create_menus()
		self.resize_cols()

	def tree_clicked(self, index):
		print 'tree clicked at index: ' + str(index)

	def tree_doubleClicked(self, index):
		print 'tree doubleClicked at index: ' + str(index)
