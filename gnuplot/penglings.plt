set style fill transparent solid 0.8 noborder
set datafile separator ","

set palette maxcolors 3 model RGB defined (0 "#ffaa33", 1 "#aa33ff", 3 "#33bbaa")
set cbrange [0:3]
set cbtics offset 0,1 ('Adelie' 0, 'Chinstrap' 1, 'Gentoo' 2)

ilerp(min, max, x) = (x - min) / (max - min)
lerp(min, max, x) = x * (max - min) + min
cmap(species) = (species eq "Adelie" ? 0 : (species eq "Chinstrap" ? 1 : 2))
sval(fmin, fmax, tmin, tmax, x) = (x - fmin) / (fmax - fmin) * (tmax - tmin) + tmin

set xlabel "Flipper Length (mm)"
set ylabel "Body Mass (g)"
set yrange [*:*]
set key title "Bill Length (mm)"
stats "../penglings.csv" using (real($4))
plot "../penglings.csv" using 6:7:(sval(STATS_min, STATS_max, 0.5, 1.5, $4)):(cmap(stringcolumn(2))) with circles notitle lc palette,\
  1/0 with points lc "#000000" pt 0 lw 6 ps 0 title sprintf("%.2f", STATS_min),\
  1/0 with points lc "#000000" pt 0 lw 15 ps 3 title sprintf("%.2f", STATS_max)

# vi:ft=gnuplot
