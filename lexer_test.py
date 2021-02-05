import unittest
from tokens import Token, TokenTip
from lexer import Lexer

class TestLexer(unittest.TestCase):
	
	def bos_test(self):
		tokens = list(Lexer("").token_olustur())
		self.assertEqual(tokens, [])
	
	def bosluk_test(self):
		tokens = list(Lexer(" \t\n  \t\t\n\n").token_olustur())
		self.assertEqual(tokens, [])

	def test_sayi(self):
		tokens = list(Lexer("123 123.456 123. .456 .").token_olustur())
		self.assertEqual(tokens, [
			Token(TokenTip.SAYİ, 123.000),
			Token(TokenTip.SAYİ, 123.456),
			Token(TokenTip.SAYİ, 123.000),
			Token(TokenTip.SAYİ, 000.456),
			Token(TokenTip.SAYİ, 000.000),
		])
	
	def test_operatorler(self):
		tokens = list(Lexer("+-*/").token_olustur())
		self.assertEqual(tokens, [
			Token(TokenTip.ARTİ),
			Token(TokenTip.EKSİ),
			Token(TokenTip.CARP),
			Token(TokenTip.BOL),
		])

	def test_parentez(self):
		tokens = list(Lexer("()").token_olustur())
		self.assertEqual(tokens, [
			Token(TokenTip.SOLPARANTEZ),
			Token(TokenTip.SAGPARANTEZ),
		])
	
	def test_hepsi(self):
		tokens = list(Lexer("27 + (43 / 36 - 48) * 51").token_olustur())
		self.assertEqual(tokens, [
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
		])
