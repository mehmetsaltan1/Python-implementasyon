from dataclasses import dataclass

@dataclass
class SAYİDUGUMU:
	value: any

	def __repr__(self):
		return f"{self.value}"

@dataclass
class EKLEDUGUMU:
	dugum_a: any
	dugum_b: any

	def __repr__(self):
		return f"({self.dugum_a}+{self.dugum_b})"

@dataclass
class CİKARDUGUMU:
	dugum_a: any
	dugum_b: any

	def __repr__(self):
		return f"({self.dugum_a}-{self.dugum_b})"

@dataclass
class CARPDUGUMU:
	dugum_a: any
	dugum_b: any

	def __repr__(self):
		return f"({self.dugum_a}*{self.dugum_b})"

@dataclass
class BOLDUGUMU:
	dugum_a: any
	dugum_b: any

	def __repr__(self):
		return f"({self.dugum_a}/{self.dugum_b})"

@dataclass
class ARTIDUGUMU:
	dugum: any

	def __repr__(self):
		return f"(+{self.dugum})"
	
@dataclass
class EKSİDUGUMU:
	dugum: any

	def __repr__(self):
		return f"(-{self.dugum})"
