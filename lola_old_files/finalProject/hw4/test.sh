#!/bin/bash

#Make a directory (optional)
mkdir -p figures

#Loop through the output files that contain an underscore and end in ".dat"
for i in `ls *_*.dat`
do
  #Strip the ".dat" from the filename
  name=`basename $i .dat`

  #Call the gnuplot script with a couple of variables initialized
  gnuplot -e "filename='$i'" -e "outfile='figures/$name.png'" hw5.gplot
done
