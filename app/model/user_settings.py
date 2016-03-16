import json
import os

#import main_model; reload(main_model) # DEV ONLY, REMOVE IN PRODUCTION
from main_model import BaseModel

class User_Settings(BaseModel):
	def __init__(self):
		super(User_Settings, self).__init__()
		# Initialize variables
		self._user_settings = ''
		self._mxs_repo = ''
		self._mcg_repo = ''
		self._settings_dir = os.path.abspath(os.path.abspath(os.path.dirname(__file__)) + "/../")
		
		# Load the usersettings
		self._load_usersettings()

		#self.announce_update()

	def _load_usersettings(self):
		with open(os.path.join(self._settings_dir, 'user_config.txt'), 'r') as f:
			self._user_settings = json.loads(f.read())
			self._mxs_repo = self._user_settings.get('mxs_repo', None)
			self._mcg_repo = self._user_settings.get('mcg_repo', None)

	def _save_usersetting(self, key, value):
		try:
			self._user_settings[key] = value
			with open(os.path.join(self._settings_dir, 'user_config.txt'), 'w') as f:
				f.write(json.dumps(self._user_settings, indent=4))
		except:
			pass

	# Properties for the settings
	@property
	def mxs_repo(self): return self._mxs_repo
	@mxs_repo.setter
	def mxs_repo(self, path):
		self._mxs_repo = path
		self._save_usersetting('mxs_repo', str(path))
		self.announce_update()
	
	@property
	def mcg_repo(self): return self._mcg_repo
	@mcg_repo.setter
	def mcg_repo(self, path):
		self._mcg_repo = path
		self._save_usersetting('mcg_repo', str(path))
		self.announce_update()
