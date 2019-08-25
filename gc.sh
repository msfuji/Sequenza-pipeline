#!/bin/bash
reference_fasta=$1
/usr/local/bin/sequenza-utils gc_wiggle -w 50 --fasta $1 -o gc50Base.wig.gz
