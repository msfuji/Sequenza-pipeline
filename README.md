# Sequenza-pipeline
Somatic CNA pipeline.

## Requirements
- [cwltool](https://github.com/common-workflow-language/cwltool)
- [Docker](https://www.docker.com/) or [Singularity](https://sylabs.io/)

## Usage
#### 1. Download pipeline
```
git clone https://github.com/msfuji/Sequenza-pipeline.git
```
#### 2. Edit config files
- List BAM files of matched tumor/normals in sample.csv. Acceptable file format is a sample config file of Genomon2. Use `[bam_import]` to specify BAM files. Use `[mutation_call]` to pair tumors and normals. Panel filed of `[mutation_call]` is ignored.
- Specify file path for reference human genome GRCh37 as `ref_fasta` of genomon.cfg. Other fields are ignored.
- Specify your sample.csv and genomon.cfg in `sequenza-workflow.yaml` .

#### 3. Pull docker image from Docher Hub.
```
docker pull mfrkn/sequenza-pipeline
```
#### 4. Run pipeline
```
cwl-runner sequenza-workflow.cwl sequenza-workflow.yaml
```
Alternatively, if you are using SHIROKANE supercomputer, try
```
bash start-shirokane.sh sequenza-workflow.yaml
```
