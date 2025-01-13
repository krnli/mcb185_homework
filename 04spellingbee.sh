#should be run from the mcb185_homework directory
gunzip -c ../MCB185/data/dictionary.gz | grep "^[acionz]*r[acionz]*$" | grep ".{4,}"