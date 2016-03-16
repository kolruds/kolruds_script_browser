from PySide import QtCore, QtGui

import base_model; reload(base_model)
from base_model import BaseModel

import user_settings; reload(user_settings) # DEV ONLY, REMOVE IN PRODUCTION
from user_settings import User_Settings

import tree_scripts_model; reload(tree_scripts_model) # DEV ONLY, REMOVE IN PRODUCTION
from tree_scripts_model import Tree_Model


class MainModel(object):
	def __init__(self):
		self.user_settings = User_Settings()
		self.tree_model = Tree_Model(self)
