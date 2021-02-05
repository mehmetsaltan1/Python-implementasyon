from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
	try:
		girdi = input("4 İşlem Yapılacak Sayıları Giriniz > ")
		lexer = Lexer(girdi)
		tokens = lexer.token_olustur()
		parser = Parser(tokens)
		tree = parser.ayir()
		if not tree: continue
		interpreter = Interpreter()
		value = interpreter.git(tree)
		print(value)
	except Exception as e:
		print(e)
