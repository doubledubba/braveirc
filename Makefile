binary:
	pyinstaller.py -F -o bin/ --upx-dir=bin/ ui.py
	rm *.log
clean:
	rm -Rf bin/build bin/dist bin/ui.spec
all:
	cd gui;make
	cd db;make
	make bin

