# Sequenza-pipeline
Analyze somatic copy number alteration of tumor using [Sequenza](http://www.cbs.dtu.dk/biotools/sequenza/). WGS/WES BAM files of matched tumor and normal are analyzed.

## Requirements
- [cwltool](https://github.com/common-workflow-language/cwltool)
- [Docker](https://www.docker.com/) or [Singularity](https://sylabs.io/)

## Usage for a single pair of tumor/normal
#### 1. Pull docker image from Docker Hub.
```
docker pull mfrkn/sequenza-pipeline
```
#### 2. Download pipeline
```
git clone https://github.com/msfuji/Sequenza-pipeline.git
cd Sequenza-pipeline
```
#### 3. Prepare config file
Specify sample ID, tumor BAM, normal BAM, reference FASTA, and the number of threads for computation in a YAML-format config file. See `example/sequenza-command.yaml`.
#### 4. Run pipeline
```
cwl-runner sequenza-command.cwl config.yaml
```

## Usage for multiple pairs of tumor/normals
This option is available only for users of the SHIROKANE supercomputer.
Log in to OS7 nodes of SHIROKANE, and install cwltool.
```
qlogin -l os7
pip install cwlref-runner --user
```
Add the following command to `~/.bashrc`.
```
export PATH=$PATH:~/.local/bin
```

#### 1. Download pipeline
```
git clone https://github.com/msfuji/Sequenza-pipeline.git
cd Sequenza-pipeline
```
#### 2. Prepare config files
- List BAM files of matched tumor/normals in sample.csv. Acceptable file format is a sample config file of Genomon2. Use `[bam_import]` to specify BAM files, and `[mutation_call]` to specify pairs of tumors and normals. Panel field of `[mutation_call]` is ignored.
- Specify file path for reference human genome GRCh37 as `ref_fasta` of genomon.cfg. Other fields are ignored.
#### 3. Run pipeline
```
python scripts/start.py genomon.cfg sample.csv
```
