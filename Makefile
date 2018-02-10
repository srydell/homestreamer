# -*- MakeFile -*-
#
# Written by Simon Rydell
# February 2018
#
# @pyinstaller --onedir--onefile -windowed handler.py

run:
	@python3 handler.py

generate: clean
	@python3 setup.py py2app

clean:
	@rm -rf ./build ./dist ./__pycache__ handler.spec
