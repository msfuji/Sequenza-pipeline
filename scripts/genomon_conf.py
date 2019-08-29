#! /usr/bin/env python
#
# This file was copied from GenomonPipeline and thus 
# restricted by its license, which can be found at:
# https://github.com/Genomon-Project/GenomonPipeline
#

import os, pwd, subprocess, sys
if sys.version_info.major == 2:
    import ConfigParser as cp
else:
    import configparser as cp
# from genomon_pipeline.__init__ import __version__
# import genomon_pipeline.config.run_conf as rc

global genomon_conf

genomon_conf = cp.SafeConfigParser()

# software_version ={'genomon_pipeline':'genomon_pipeline-'+__version__}

dna_reference_list = ["ref_fasta",
                      "interval_list",
                      "genome_size",
                      "gaptxt",
                      "bait_file",
                      "simple_repeat_tabix_db",
                      "HGVD_2013_tabix_db",
                      "HGVD_2016_tabix_db",
                      "HGMD_tabix_db",
                      "inhouse_tumor_tabix_db",
                      "inhouse_normal_tabix_db",
                      "ExAC_tabix_db",
                      "hotspot_db"
                      ]
           
dna_software_list = ["blat",
                     "bwa",
                     "samtools",
                     "bedtools",
                     "biobambam",
                     "bamstats",
                     "htslib",
                     "genomon_sv",
                     "sv_utils",
                     "mutfilter",
                     "ebfilter",
                     "fisher",
                     "genomon_qc",
                     "genomon_pa",
                     "paplot",
                     "mutil",
                     "mutanno",
                     "annovar",
                     "hotspot"
                     ]

dna_software_version = {"genomon_sv":"GenomonSV",
                        "sv_utils": "sv_utils",
                        "fisher":"GenomonFisher",
                        "mutfilter":"GenomonMutationFilter",
                        "ebfilter":"EBFilter",
                        "mutil": "MutationUtil",
                        "mutanno": "GenomonMutationAnnotation",
                        "genomon_qc": "genomon_qc",
                        "hotspot": "hotspotCall",
                        } 

rna_reference_list = ["star_genome"
                      ]
           
rna_software_list = ["samtools",
                     "STAR",
                     "fusionfusion"
                     ]

rna_software_version = {"STAR": "STAR",
                        "fusionfusion":"fusionfusion",
                        } 

err_msg = 'No target File : \'%s\' for the %s key in the section of %s' 


def dna_genomon_conf_check():
    """
    function for checking the validity of genomon_conf for DNA analysis
    """

    section = "REFERENCE"
    for key in dna_reference_list:

        if key == "inhouse_normal_tabix_db":
            if genomon_conf.has_option("annotation", "active_inhouse_normal_flag"):
                flag = genomon_conf.get("annotation", "active_inhouse_normal_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue
        
        if key == "inhouse_tumor_tabix_db":
            if genomon_conf.has_option("annotation", "active_inhouse_tumor_flag"):
                flag = genomon_conf.get("annotation", "active_inhouse_tumor_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue
            
        if key == "HGVD_2013_tabix_db":
            if genomon_conf.has_option("annotation", "active_HGVD_2013_flag"):
                flag = genomon_conf.get("annotation", "active_HGVD_2013_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue
            
        if key == "HGVD_2016_tabix_db":
            if genomon_conf.has_option("annotation", "active_HGVD_2016_flag"):
                flag = genomon_conf.get("annotation", "active_HGVD_2016_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue
            
        if key == "HGMD_tabix_db":
            if genomon_conf.has_option("annotation", "active_HGMD_flag"):
                flag = genomon_conf.get("annotation", "active_HGMD_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue
            
        if key == "ExAC_tabix_db":
            if genomon_conf.has_option("annotation", "active_ExAC_flag"):
                flag = genomon_conf.get("annotation", "active_ExAC_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue

        if key == "hotspot_db":
            if genomon_conf.has_option("hotspot", "active_hotspot_flag"):
                flag = genomon_conf.get("hotspot", "active_hotspot_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue
            
            
        value = genomon_conf.get(section, key)
        if not os.path.exists(value):
            raise ValueError(err_msg % (value, key, section))

    section = "SOFTWARE"
    for key in dna_software_list:
        
        if key == "annovar":
            if genomon_conf.has_option("annotation", "active_annovar_flag"):
                flag = genomon_conf.get("annotation", "active_annovar_flag")
                if flag == "True":
                    value = genomon_conf.get(section, key)
                    if not os.path.exists(value):
                        raise ValueError(err_msg % (value, key, section))
            continue
            
        value = genomon_conf.get(section, key)
        if not os.path.exists(value):
            raise ValueError(err_msg % (value, key, section))

    pass

def rna_genomon_conf_check():
    """
    function for checking the validity of genomon_conf for RNA analysis
    """

    section = "REFERENCE"
    for key in rna_reference_list:
        value = genomon_conf.get(section, key)
        if not os.path.exists(value):
            raise ValueError(err_msg % (value, key, section))

    section = "SOFTWARE"
    for key in rna_software_list:
        value = genomon_conf.get(section, key)
        if not os.path.exists(value):
            raise ValueError(err_msg % (value, key, section))

    pass


def dna_software_version_set():
    pythonhome = genomon_conf.get("ENV", "PYTHONHOME")
    pythonpath = genomon_conf.get("ENV", "PYTHONPATH")
    ld_library_path = genomon_conf.get("ENV", "LD_LIBRARY_PATH")
    export_command = "export PYTHONHOME=" +pythonhome+ ";export PATH=$PYTHONHOME/bin:$PATH;export LD_LIBRARY_PATH="+ ld_library_path +";export PYTHONPATH="+ pythonpath +";"
    for key, name in dna_software_version.items():
        command = export_command + genomon_conf.get("SOFTWARE", key) + ' --version 2>&1 | grep ' + name
        proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        version_list = str(proc.communicate()[0]).split("\n")
        software_version[key] = version_list[0]

def rna_software_version_set():
    pythonhome = genomon_conf.get("ENV", "PYTHONHOME")
    pythonpath = genomon_conf.get("ENV", "PYTHONPATH")
    ld_library_path = genomon_conf.get("ENV", "LD_LIBRARY_PATH")
    export_command = "export PYTHONHOME=" +pythonhome+ ";export PATH=$PYTHONHOME/bin:$PATH;export LD_LIBRARY_PATH="+ ld_library_path +";export PYTHONPATH="+ pythonpath +";"
    for key, name in rna_software_version.items():
        command = export_command + genomon_conf.get("SOFTWARE", key) + ' --version 2>&1 | grep ' + name
        proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        version_list = str(proc.communicate()[0]).split("\n")
        software_version[key] = version_list[0]

def get_version(key):
    return software_version[key]


def get_meta_info(softwares):

    print_meta_info = "# Version: " + ' '.join([software_version[x] for x in softwares])
    print_meta_info = print_meta_info + '\n' + "# Analysis Date: " + rc.run_conf.analysis_date
    print_meta_info = print_meta_info + '\n' + "# User: " + pwd.getpwuid(os.getuid()).pw_name
   
    return print_meta_info

