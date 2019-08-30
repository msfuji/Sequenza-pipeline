#!/bin/bash
#$ -S /bin/bash

cwl_file=$1
config_file=$2
cwl-runner --singularity $cwl_file $config_file
