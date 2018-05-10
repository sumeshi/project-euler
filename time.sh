#!/bin/bas
echo '# project-euler  
https://projecteuler.net/' > README.md

for file in `\find . -maxdepth 2 -type f -name '*.py'`; do
    echo '\r---' >> README.md
    echo `basename $file` >> README.md
    (time `python $file > /dev/null`) >> README.md 2>&1
done