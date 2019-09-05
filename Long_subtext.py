class LongSubtext:
	def __init__(self, texta, textb):
		self.a = texta
		self.b = textb
		self.result = ""

	def attach(self):
		self.result = self.a + self.b

	def printResult(self):
		print("'s answer is "+ self.result)

at = LongSubtext("photography", "autograph")
bt = LongSubtext("thereisnocowlevel", "thereisnocowlevel")
ct = LongSubtext("blackofh", "kingdomofheaven")

at.attach()
at.printResult()
bt.attach()
bt.printResult()
ct.attach()
ct.printResult()
