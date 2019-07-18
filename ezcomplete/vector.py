class Vector():
	def __init__(self):
		self.dims = []

	def set(self, *dims):
		self.dims = dims

	def __str__(self):
		string=""
		for dim in self.dims:
			string=string+str(dim)+","

		return f"Vector({string})"

v1 = Vector()
v1.set(1, 9.93, 1837, 86323, 69)