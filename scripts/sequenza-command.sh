#!/bin/bash

set -eu

sample_id=$1
tumor_bam=$2
normal_bam=$3
reference_fasta=$4
gc_wiggle=$5
num_threads=$6

chromosomes="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y"

sequenza-utils bam2seqz -n ${normal_bam} -t ${tumor_bam} \
  --fasta ${reference_fasta} -gc ${gc_wiggle} -o ${sample_id}.seqz.gz \
  -C ${chromosomes} --parallel ${num_threads}

{
  for chr in $chromosomes; do
    if [[ $chr = "1" ]]; then
      zcat ${sample_id}_1.seqz.gz
    else
      zcat ${sample_id}_${chr}.seqz.gz | tail -n +2
    fi
  done
} | sequenza-utils seqz_binning --seqz - -w 50 \
  -o ${sample_id}.small.seqz.gz

Rscript /opt/sequenza-command.R ${sample_id} ${sample_id}.small.seqz.gz
