---
id: 5188
name: "bahlolab/nf-wgs-multiqc"
branch: "master"
tag: "v0.0"
commit: "84655976c66fc68713c954baddaa7b663c39b6ac"
version: "0dfa0c357d9b3c8b7a49c36fe5053322"
build_date: "2018-10-10T10:52:37.754Z"
size_mb: 2693
size: 1044492319
sif: "https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.0/2018-10-10-84655976-0dfa0c35/0dfa0c357d9b3c8b7a49c36fe5053322.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bahlolab/nf-wgs-multiqc/v0.0/2018-10-10-84655976-0dfa0c35/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.0/2018-10-10-84655976-0dfa0c35/Singularity
collection: bahlolab/nf-wgs-multiqc
---

# bahlolab/nf-wgs-multiqc:v0.0

```bash
$ singularity pull shub://bahlolab/nf-wgs-multiqc:v0.0
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: continuumio/miniconda3:latest

%labels
  AUTHOR Jacob Munro
  AUTHOR bahlolab

%post
    alias conda="/opt/conda/bin/conda"
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels r
    conda install -y \
        gatk4=4.0.10.0 \
        samtools=1.9 \
        bcftools=1.9 \
        multiqc=1.6 \
        fastqc=0.11.8
    conda clean --all -y
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
```

## Collection

 - Name: [bahlolab/nf-wgs-multiqc](https://github.com/bahlolab/nf-wgs-multiqc)
 - License: None

