# -*- MakeFile -*-
#
# Written by Simon Rydell
# February 2018
#
generate: clean
	@pyinstaller --onefile -windowed handler.py

clean:
	@rm -rf ./build ./dist ./__pycache__ handler.spec
