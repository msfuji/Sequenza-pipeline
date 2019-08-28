# Sequenza-pipeline
Somatic CNA pipeline. List tumor/normal BAM files as a sample config file for Genomon2. Use `[bam_import]` directive.

#### 1. Download pipeline
```
git clone https://github.com/msfuji/Sequenza-pipeline.git
```

#### 1. Pull docker image from Docher Hub.
```
docker pull mfrkn/sequenza-pipeline
```
#### 2. Edit config file
Edit `sequenza-workflow.yaml`.
#### 3. Run pipeline
```
cwl-runner sequenza-workflow.cwl sequenza-workflow.yaml
```
Alternatively, if you are using SHIROKANE supercomputer, try
```
bash start-shirokane.sh sequenza-workflow.yaml
```
