#!/bin/bash
yaml=$1

qsub="qsub -l os7 -cwd -pe def_slot 8 -l s_vmem=5.3G,mem_req=5.3G"

$qsub -S ~/.local/bin/cwl-runner --strict-memory-limit cwl/sequenza-command.cwl $yaml
