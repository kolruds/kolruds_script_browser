class MainController(object):
	def __init__(self, model):
		self.model = model

	def c_browse_mxs_repo(self, dialog):
		directory = dialog.run()
		if directory:
			self.model.user_settings.mxs_repo = directory

	def c_browse_mcg_repo(self, dialog):
		directory = dialog.run()
		if directory:
			self.model.user_settings.mcg_repo = directory

	def c_publish_mxs(self):
		print 'Button publish_mxs pressed'

	def c_publish_mcg(self):
		print 'Button publish_mcg pressed'

	def c_reload_scripts(self):
		print 'Button reload_scripts pressed'
