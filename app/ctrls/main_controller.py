class MainController(object):
	def __init__(self, model):
		self.model = model

	def c_browse_mxs_repo(self, directory):
		self.model.tree_model.q_model.clear()
		if directory:
			self.model.user_settings.mxs_repo = directory

	def c_browse_mcg_repo(self, directory):
		self.model.tree_model.q_model.clear()
		if directory:
			self.model.user_settings.mcg_repo = directory

	def c_publish_mxs(self, mxs_file):
		print mxs_file
		return

	def c_publish_mcg(self, mcg_file):
		return

	def c_reload_scripts(self):
		""" Controlled from view """
		return NotImplemented
