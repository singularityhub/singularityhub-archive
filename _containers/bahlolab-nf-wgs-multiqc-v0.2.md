---
id: 5192
name: "bahlolab/nf-wgs-multiqc"
branch: "master"
tag: "v0.2"
commit: "3b470b01befd53ae275737734f17ea1edb79c94f"
version: "81a327205f726c1581f58575437f0237"
build_date: "2018-10-11T09:24:02.674Z"
size_mb: 2686
size: 1035816991
sif: "https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.2/2018-10-11-3b470b01-81a32720/81a327205f726c1581f58575437f0237.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.2/2018-10-11-3b470b01-81a32720/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.2/2018-10-11-3b470b01-81a32720/Singularity
collection: bahlolab/nf-wgs-multiqc
---

# bahlolab/nf-wgs-multiqc:v0.2

```bash
$ singularity pull shub://bahlolab/nf-wgs-multiqc:v0.2
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
        multiqc=1.6 \
        fastp=0.19.4 \
        bwa=0.7.17
    conda clean --all -y
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
```

## Collection

 - Name: [bahlolab/nf-wgs-multiqc](https://github.com/bahlolab/nf-wgs-multiqc)
 - License: None

