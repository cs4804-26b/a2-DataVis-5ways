set datafile separator ","
set datafile missing "NA"

set title "Flipper Length vs Body Mass vs Beak Length"
set xlabel "Flipper Length (mm)"
set ylabel "Body Mass (g)"
set zlabel "Beak Length (mm)"
set grid

filter(col, species) = (strcol(2) eq species) ? col : 1/0

splot 'penglings.csv' using (filter($6, "Adelie")):7:4     with points pt 7 ps 1.5 lc rgb "#0000FF" title "Adelie", \
      'penglings.csv' using (filter($6, "Chinstrap")):7:4  with points pt 7 ps 1.5 lc rgb "#FF0000" title "Chinstrap", \
      'penglings.csv' using (filter($6, "Gentoo")):7:4     with points pt 7 ps 1.5 lc rgb "#00FF00" title "Gentoo"