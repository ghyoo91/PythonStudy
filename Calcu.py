class FourCal:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		return self.first+self.second

	def sub(self):
		return self.first-self.second

	def mul(self):
		return self.first*self.second

	def div(self):
		return self.first/self.second

	def mod(self):
		return self.first%self.second

a = FourCal(2, 4)
b = FourCal(6, 4)

print(a.div())

print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())
print(a.mod())

print(b.sum())
print(b.sub())
print(b.mul())
print(b.div())
print(b.mod())
