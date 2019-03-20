all: hwk4c hwk4fort figures

hwk4c: hw4.o hw4_funcs.o
	 icc -o hwk4c hw4.o hw4_funcs.o
hwk4fort: hwk4.o hw4module.o 
	ifort -o hw4fort hw4module.o hwk4.o
hw4_funcs.o:	hw4_funcs.c hw4_funcs.h
	icc -c  hw4_funcs.c
hw4.o:	 hw4.c hw4_funcs.h
	icc -c hw4.c 
hw4module.mod: hw4module.o hw4module.f90
	ifort -c hw4module.f90
hw4module.o: hw4module.f90 
	ifort -c hw4module.f90
hwk4.o: hw4module.mod hw4module.o hwk4.f90
	ifort -c hwk4.f90
# Define any data files
DATA	:=	$(wildcard *_*.dat)

# Define the result file basenames
BASE :=	$(patsubst %.dat, %, $(DATA))

# Define any gnuplot files
PLOT	:=	hw5.gplot

# Define any .png files
PNGS	:=	$(patsubst %.dat, %.png, $(DATA))

# Rules for creating .png plots of the data files
# --------------------------------------------------
figures:	$(PNGS)

%.png:	%.dat
	gnuplot -e "BASENAME='figures/$*'; DATAFILE='$<'; PNGFILE='$@'" $(PLOT)
.phony: clean
	 clean: rm -f *.o
	clean:rm -f *.png

