#!/bin/bash

reference_fasta=$1
reference_base=`basename $reference_fasta | sed -e 's/\.fa$\|\.fas$\|\.fasta$//'`
outfile="${reference_base}.gc50Base.wig.gz"
/usr/local/bin/sequenza-utils gc_wiggle -w 50 --fasta $reference_fasta -o $outfile
