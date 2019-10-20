class Prints():
	Printz = [
		"""
	Your system doesn't meet the requirements..

		1. We could try to do that for you
		2. try to install them manually
		[sudo & pip are requiered]
		""",
		"""
	Next run should start normally if all preocesses successed
	otherwise use run the script again with 'sudo'
	or use 'sudo pip3 install -r requirements.txt'
	file should be attached
		""",
		"""
	[Failed] Sorry...
	you'll need to do that manually
	you may use 'sudo pip3 install -r requirements.txt' if file exist
		""",
		"""
	DATAASE connection failed
	This may happen if you are running with 'sudo'
			,	due to internal error
			,	database wasn't created
			or	even interrupted by user
		""",
		"""
	Something went wrong..
	Exiting.
		""",
		"""
	Process ended by user..
	Hope every thing is will..
	See you :)..
		"""
	]
	np = 0

	def __str__(self):
		return self.Printz[self.np]

	def __init__(self, n):
		self.np = n if n > -1 else 0
		self.__str__()