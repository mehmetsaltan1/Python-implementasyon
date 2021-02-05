from nodes import *
from values import SAYİ

class Interpreter:
	def __init__(self):
		pass

	def git(self, dugum):
		gitme_methodu = f'git_{type(dugum).__name__}'
		method = getattr(self, gitme_methodu)
		return method(dugum)
		
	def git_SAYİDUGUMU(self, dugum):
		return SAYİ(dugum.value)

	def git_EKLEDUGUMU(self, dugum):
		return SAYİ(self.git(dugum.dugum_a).value + self.git(dugum.dugum_b).value)

	def git_DUGUMCİKARU(self, dugum):
		return SAYİ(self.git(dugum.dugum_a).value - self.git(dugum.dugum_b).value)

	def git_CARPDUGUMU(self, dugum):
		return SAYİ(self.git(dugum.dugum_a).value * self.git(dugum.dugum_b).value)

	def git_BOLDUGUMU(self, dugum):
		try:
			return SAYİ(self.git(dugum.dugum_a).value / self.git(dugum.dugum_b).value)
		except:
			raise Exception("Çalışma zamanı matematik hatası")
