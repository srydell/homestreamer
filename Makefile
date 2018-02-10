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

install:
	@pip3 install -r requirements.txt
	@pip3 install -U git+https://github.com/metachris/py2app.git@master
