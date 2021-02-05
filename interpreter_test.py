import unittest
from nodes import *
from interpreter import Interpreter
from values import SAYİ

class TestInterpreter(unittest.TestCase):

	def test_sayi(self):
		value = Interpreter().git(SAYİDUGUMU(51.2))
		self.assertEqual(value, SAYİ(51.2))

	def test_tek_operator(self):
		sonuc = Interpreter().git(EKLEDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))
		self.assertEqual(sonuc.value, 41)

		sonuc = Interpreter().git(CİKARDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))
		self.assertEqual(sonuc.value, 13)

		sonuc = Interpreter().git(CARPDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))
		self.assertEqual(sonuc.value, 378)

		sonuc = Interpreter().git(BOLDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(14)))
		self.assertAlmostEqual(sonuc.value, 1.92857, 5)

		with self.assertRaises(Exception):
			Interpreter().git(BOLDUGUMU(SAYİDUGUMU(27), SAYİDUGUMU(0)))
			
	def test_hepsi(self):
		tree = EKLEDUGUMU(
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
		)

		sonuc = Interpreter().git(tree)
		self.assertAlmostEqual(sonuc.value, -2360.08, 2)
