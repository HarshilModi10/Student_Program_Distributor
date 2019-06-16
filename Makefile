PY = python
PYFLAGS = pytest -v
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = docConfig

SRC = src/test_Calc.py

.PHONY: all test doc clean

test: 
	$(PYFLAGS) $(SRC) 

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: test doc

clean:
	rm -rf html
	rm -rf latex
