class BaseModel(object):
	def __init__(self):
		self._update_funcs = []

	# Subscribe a view method for updating
	def subscribe_update(self, function):
		if function not in self._update_funcs:
			self._update_funcs.append(function)

	# Unsubscribe a view method for updating
	def unsubscribe_update(self, function):
		if function in self._update_funcs:
			self._update_funcs.remove(function)

	# Announce update to view methods
	def announce_update(self):
		for f in self._update_funcs:
			f()