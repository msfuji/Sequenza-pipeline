# Sequenza-pipeline
Somatic CNA pipeline.

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

#### 1. Pull docker image from Docker Hub.
```
docker pull mfrkn/sequenza-pipeline
```
#### 2. Download pipeline
```
git clone https://github.com/msfuji/Sequenza-pipeline.git
cd Sequenza-pipeline
```
#### 3. Prepare config files
- List BAM files of matched tumor/normals in sample.csv. Acceptable file format is a sample config file of Genomon2. Use `[bam_import]` to specify BAM files. Use `[mutation_call]` to pair tumors and normals. Panel field of `[mutation_call]` is ignored.
- Specify file path for reference human genome GRCh37 as `ref_fasta` of genomon.cfg. Other fields are ignored.
#### 4. Run pipeline
```
python start-shirokane.py genomon.cfg sample.csv
```
