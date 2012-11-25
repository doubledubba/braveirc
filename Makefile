binary:
	pyinstaller/pyinstaller.py -F -o bin/ --upx-dir=bin/ ui.py
	rm *.log
	mv bin/dist/ui bin/
	rm -Rf bin/build bin/dist bin/ui.spec
all:
	cd gui;make
	cd db;make
	make binary

