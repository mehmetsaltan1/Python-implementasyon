from tokens import TokenTip
from nodes import *

class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.ilerle()

	def hata_firlat(self):
		raise Exception("Geçersiz sözdizimi")
	
	def ilerle(self):
		try:
			self.mevcut_belirt = next(self.tokens)
		except StopIteration:
			self.mevcut_belirt = None

	def ayir(self):
		if self.mevcut_belirt == None:
			return None

		sonuc = self.ifade()

		if self.mevcut_belirt != None:
			self.hata_firlat()

		return sonuc

	def ifade(self):
		sonuc = self.sart()

		while self.mevcut_belirt != None and self.mevcut_belirt.type in (TokenTip.ARTİ, TokenTip.EKSİ):
			if self.mevcut_belirt.type == TokenTip.ARTİ:
				self.ilerle()
				sonuc = EKLEDUGUMU(sonuc, self.sart())
			elif self.mevcut_belirt.type == TokenTip.EKSİ:
				self.ilerle()
				sonuc = CİKARDUGUMU(sonuc, self.sart())

		return sonuc

	def sart(self):
		sonuc = self.factor()

		while self.mevcut_belirt != None and self.mevcut_belirt.type in (TokenTip.CARP, TokenTip.BOL):
			if self.mevcut_belirt.type == TokenTip.CARP:
				self.ilerle()
				sonuc = CARPDUGUMU(sonuc, self.factor())
			elif self.mevcut_belirt.type == TokenTip.BOL:
				self.ilerle()
				sonuc = BOLDUGUMU(sonuc, self.factor())
				
		return sonuc

	def factor(self):
		token = self.mevcut_belirt

		if token.type == TokenTip.SOLPARANTEZ:
			self.ilerle()
			sonuc = self.ifade()

			if self.mevcut_belirt.type != TokenTip.SAGPARANTEZ:
				self.hata_firlat()
			
			self.ilerle()
			return sonuc

		elif token.type == TokenTip.SAYİ:
			self.ilerle()
			return SAYİDUGUMU(token.value)

		elif token.type == TokenTip.ARTİ:
			self.ilerle()
			return ARTIDUGUMU(self.factor())
		
		elif token.type == TokenTip.EKSİ:
			self.ilerle()
			return EKSİDUGUMU(self.factor())
		
		self.hata_firlat()
