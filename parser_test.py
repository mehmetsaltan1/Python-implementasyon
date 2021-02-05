import unittest
from tokens import Token, TokenTip
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

	def bos_test(self):
		tokens = []
		dugum = Parser(tokens).ayir()
		self.assertEqual(dugum, None)

	def test_SAYİLAR(self):
		tokens = [Token(TokenTip.SAYİ, 51.2)]
		dugum = Parser(tokens).ayir()
		self.assertEqual(dugum, SAYİDUGUMU(51.2))

	def test_tek_operator(self):
		tokens = [
			Token(TokenTip.SAYİ, 27),
			Token(TokenTip.ARTİ),
			Token(TokenTip.SAYİ, 14),
		]

		dugum = Parser(tokens).ayir()
		self.assertEqual(dugum, EKLEDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))
		
		tokens = [
			Token(TokenTip.SAYİ, 27),
			Token(TokenTip.EKSİ),
			Token(TokenTip.SAYİ, 14),
		]

		dugum = Parser(tokens).ayir()
		self.assertEqual(dugum, CİKARDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))
			
		tokens = [
			Token(TokenTip.SAYİ, 27),
			Token(TokenTip.CARP),
			Token(TokenTip.SAYİ, 14),
		]

		dugum = Parser(tokens).ayir()
		self.assertEqual(dugum, CARPDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))
			
		tokens = [
			Token(TokenTip.SAYİ, 27),
			Token(TokenTip.BOL),
			Token(TokenTip.SAYİ, 14),
		]

		dugum = Parser(tokens).ayir()
		self.assertEqual(dugum, BOLDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))

	def tum_ifadeyi_test(self):
		tokens = [
			Token(TokenTip.SAYİ, 27),
			Token(TokenTip.ARTİ),
			Token(TokenTip.SOLPARANTEZ),
			Token(TokenTip.SAYİ, 43),
			Token(TokenTip.BOL),
			Token(TokenTip.SAYİ, 36),
			Token(TokenTip.EKSİ),
			Token(TokenTip.SAYİ, 48),
			Token(TokenTip.SAGPARANTEZ),
			Token(TokenTip.CARP),
			Token(TokenTip.SAYİ, 51),
		]

		dugum = Parser(tokens).ayir()
		self.assertEqual(dugum, EKLEDUGUMU(
			SAYİDUGUMU(27),
			CARPDUGUMU(
				CİKARDUGUMU(
					BOLDUGUMU(
						SAYİDUGUMU(43),
						SAYİDUGUMU(36)
					),
					SAYİDUGUMU(48)
				),
				SAYİDUGUMU(51)
			)
		))
