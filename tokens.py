from enum import Enum
from dataclasses import dataclass

class TokenTip(Enum):
	SAYİ    = 0
	ARTİ      = 1
	EKSİ     = 2
	CARP  = 3
	BOL    = 4
	SOLPARANTEZ    = 5
	SAGPARANTEZ    = 6

@dataclass
class Token:
	type: TokenTip
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")
