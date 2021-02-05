from tokens import Token, TokenTip

BOSLUK = ' \n\t'
RAKAMLAR = '0123456789'

class Lexer:
	def __init__(self, text):
		self.text = iter(text)
		self.devam_et()

	def devam_et(self):
		try:
			self.mevcut_karakter = next(self.text)
		except StopIteration:
			self.mevcut_karakter = None

	def token_olustur(self):
		while self.mevcut_karakter != None:
			if self.mevcut_karakter in BOSLUK:
				self.devam_et()
			elif self.mevcut_karakter == '.' or self.mevcut_karakter in RAKAMLAR:
				yield self.numara_olustur()
			elif self.mevcut_karakter == '+':
				self.devam_et()
				yield Token(TokenTip.ARTİ)
			elif self.mevcut_karakter == '-':
				self.devam_et()
				yield Token(TokenTip.EKSİ)
			elif self.mevcut_karakter == '*':
				self.devam_et()
				yield Token(TokenTip.CARP)
			elif self.mevcut_karakter == '/':
				self.devam_et()
				yield Token(TokenTip.BOL)
			elif self.mevcut_karakter == '(':
				self.devam_et()
				yield Token(TokenTip.SOLPARANTEZ)
			elif self.mevcut_karakter == ')':
				self.devam_et()
				yield Token(TokenTip.SAGPARANTEZ)
			else:
				raise Exception(f"Geçersiz Karakter'{self.mevcut_karakter}'")

	def numara_olustur(self):
		ondalık_say = 0
		dizi_say = self.mevcut_karakter
		self.devam_et()

		while self.mevcut_karakter != None and (self.mevcut_karakter == '.' or self.mevcut_karakter in RAKAMLAR):
			if self.mevcut_karakter == '.':
				ondalık_say += 1
				if ondalık_say > 1:
					break
			
			dizi_say += self.mevcut_karakter
			self.devam_et()

		if dizi_say.startswith('.'):
			dizi_say = '0' + dizi_say
		if dizi_say.endswith('.'):
			dizi_say += '0'

		return Token(TokenTip.SAYİ, float(dizi_say))