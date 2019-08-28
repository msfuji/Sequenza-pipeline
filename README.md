# Sequenza-pipeline
Somatic CNA pipeline

##1. Pull docker image from Docher Hub.
```
docker pull mfrkn/sequenza-pipeline
```
##2. Edit config file `sequenza-workflow.yaml`.
##3. Run pipeline.
```
cwl-runner sequenza-workflow.cwl sequenza-workflow.yaml
```
Alternatively, if you are using SHIROKANE supercomputer, try
```
bash start-shirokane.sh sequenza-workflow.yaml
```
