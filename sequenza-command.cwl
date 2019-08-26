#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTools
id: Sequenza-command
label: Sequenza-command

requirements:
  DockerRequirement:
    dockerPull: mfrkn/sequenza-pipeline:latest

baseCommand: ["bash", "/opt/sequenza-command.sh"]

inputs:
  sample_id:
    type: string
    inputBinding:
      position: 1
  tumor-bam:
    type: File
    inputBinding:
      position: 2
  normal-bam:
    type: File
    inputBinding:
      position: 3
  reference-fasta:
    type: File
    inputBinding:
      position: 4
  gc-wiggle:
    type: File
    inputBinding:
      position: 5
  num-threads:
    type: int
    inputBinding:
      position: 6

outputs:
  cn_bars:
    type: File
    outputBinding:
      glob: '*_CN_bars.pdf'
  cp_contours:
    type: File
    outputBinding:
      glob: '*_CP_contours.pdf'
  alternative_fit:
    type: File
    outputBinding:
      glob: '*_alternative_fit.pdf'
  alternative_solutions:
    type: File
    outputBinding:
      glob: '*_alternative_solutions.txt'
  chromosome_depths:
    type: File
    outputBinding:
      glob: '*_chromosome_depths.pdf'
  chromosome_view:
    type: File
    outputBinding:
      glob: '*_chromosome_view.pdf'
  confints_cp:
    type: File
    outputBinding:
      glob: '*_confints_CP.txt'
  gc_plots:
    type: File
    outputBinding:
      glob: '*_gc_plots.pdf'
  genome_view:
    type: File
    outputBinding:
      glob: '*_genome_view.pdf'
  model_fit:
    type: File
    outputBinding:
      glob: '*_model_fit.pdf'
  mutations:
    type: File
    outputBinding:
      glob: '*_mutations.txt'
  segments:
    type: File
    outputBinding:
      glob: '*_segments.txt'
  sequenza_cp_table:
    type: File
    outputBinding:
      glob: '*_sequenza_cp_table.RData'
  sequenza_extract:
    type: File
    outputBinding:
      glob: '*_sequenza_extract.RData'
  sequenza_log:
    type: File
    outputBinding:
      glob: '*_sequenza_log.txt'
