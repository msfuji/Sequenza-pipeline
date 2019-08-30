#!/bin/bash
#$ -S /bin/bash

cwl-runner --singularity $cwl_file $config_file
