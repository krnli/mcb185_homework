#should be run from the mcb185_homework directory
gunzip -c ../MCB185/data/dictionary.gz | grep "^[acionrz]*r[acionrz]*$" | grep -E ".{4,}"