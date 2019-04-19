all: hwk4c hwk4fort figures

hwk4c: hw4.o
	 icc -o hwk4c hw4.o hw4_funcs.o
hwk4fort: hwk4.o
	ifort -o hw4fort hw4module.o hwk4.o
hw4funcs.o:	hw4_funcs.c hw4_funcs.h
	icc -c  hw4_funcs.o
hw4.o:	 hw4.c hw4_funcs.h
	icc -c hw4.c 

hw4module.o: hw4module.f90 
	icc -c hw4module.f90
hwk4.o: hwk4.f90
	icc -c hwk4.f90
figures: test.h
	 /bin/sh/test.sh
.phony: clean
	 clean: rm -f *.o
	clean:rm -f *.png

