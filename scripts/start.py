#!/usr/bin/env python

import os
import sys
import subprocess
import contextlib
import json
import sample_conf as sc
import genomon_conf as gc


@contextlib.contextmanager
def pushd(new_dir):
    old_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(old_dir)


def make_config(tumor_id, tumor_bam, normal_bam, ref_fasta, n_threads):
    dict = {
    'sample-id': tumor_id,
    'tumor-bam': {'class': 'File', 'path': tumor_bam},
    'normal-bam': {'class': 'File', 'path': normal_bam},
    'reference-fasta': {'class': 'File', 'path': ref_fasta},
    'num-threads': n_threads / 2
    }
    config_file = 'config.json'
    with open(config_file, 'w') as f:
        json.dump(dict, f)
    return config_file


def analyze_tn_pair(qsub_script, cwl_file, config_file, n_threads):
    command = "qsub -l os7 -cwd -j y -pe def_slot {} {} {} {}".format(
        n_threads, qsub_script, cwl_file, config_file)
    print(command)
    subprocess.call(command, shell=True)


################################################################################
#
# parse args
#
if len(sys.argv) != 3:
    print("Usage: python start.py [genomon.cfg] [sample.csv]\n")
    exit(1)
genomon_conf_file = sys.argv[1]
sample_conf_file = sys.argv[2]
n_threads = 8

#
# read config files
#
gc.genomon_conf.read(genomon_conf_file)
ref_fasta = gc.genomon_conf.get("REFERENCE", "ref_fasta")
sample_conf = sc.Sample_conf()
sample_conf.parse_file(sample_conf_file)

#
# analyze pairs of tumor/normal
#
cwd = os.getcwd()
qsub_script = os.path.join(cwd, 'scripts', 'run-cwl.sh')
cwl_file = os.path.join(cwd, 'sequenza-command.cwl')
for tumor_id, normal_id, _ in sample_conf.mutation_call:
    tumor_bam = sample_conf.bam_import[tumor_id]
    normal_bam = sample_conf.bam_import[normal_id]

    # make and move into output directory
    outdir = os.path.join('output', tumor_id)
    os.makedirs(outdir)
    with pushd(outdir):
        config_file = make_config(tumor_id, tumor_bam, normal_bam,
            ref_fasta, n_threads)
        analyze_tn_pair(qsub_script, cwl_file, config_file, n_threads)
