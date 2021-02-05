from dataclasses import dataclass

@dataclass
class SAYİ:
	value: any
	
	def __repr__(self):
		return f"{self.value}"
