#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTools
id: Sequenza-command
label: Sequenza-command

requirements:
  DockerRequirement:
    dockerPull: seqz

baseCommand: ["bash", "/opt/sequenza-command.sh"]

inputs:
  tumor-bam:
    type: File
    inputBinding:
      position: 1
  normal-bam:
    type: File
    inputBinding:
      position: 2
  reference-fasta:
    type: File
    inputBinding:
      position: 3
  gc-wiggle:
    type: File
    inputBinding:
      position: 4



      inputs:
        reference-fasta:
          type: File
          inputBinding:
            position: 1
      outputs:
        gc-wiggle:
          type: File
          outputBinding:
            glob: gc50Base.wig.gz
