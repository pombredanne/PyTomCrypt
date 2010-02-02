
PYTHON = bin/python
PREPROCESS = ./preprocess
LIBTOMCRYPT = libtomcrypt-1.16
SUB = Makefile.sub
SUBMAKE = make -f $(SUB)

default : build

% : %.mako
	$(PREPROCESS) $< > $@

submake: Makefile.sub

preprocess: submake
	$(SUBMAKE) preprocess

build: submake
	$(SUBMAKE) build

test: build
	$(PYTHON) tests/test_cipher.py
	$(PYTHON) tests/test_hash.py
	$(PYTHON) tests/test_mac.py
	$(PYTHON) tests/test_prng.py

cleanbuild:	
	- rm -rf build

clean:
	- rm *.o
	- rm *.so
	- rm *.pyc
	- rm tomcrypt/*.c
	- rm tomcrypt/*.so
	- rm tomcrypt/*.pyc
	- rm -rf dist
	- $(SUBMAKE) clean
	- rm Makefile.sub

cleanall: clean cleanbuild

cleantest:
	make clean
	make test
