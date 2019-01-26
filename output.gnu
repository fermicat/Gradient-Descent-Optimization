set term post eps color solid enh
datafile ="adam.log"
unset key
set xrange [0:5000]
set yrange [0:120000]
set output "adam.pdf"
set xlabel "step"
set ylabel "value"
plot datafile using 1:2 with lines
