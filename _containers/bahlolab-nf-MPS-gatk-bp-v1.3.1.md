---
id: 6258
name: "bahlolab/nf-MPS-gatk-bp"
branch: "master"
tag: "v1.3.1"
commit: "305bc71c78ef2ff7df55ebdf612fad02e934d8b7"
version: "d61d756c0496b5b184cff6ba7172b865"
build_date: "2019-01-21T15:26:38.557Z"
size_mb: 3291
size: 1286311967
sif: "https://datasets.datalad.org/shub/bahlolab/nf-MPS-gatk-bp/v1.3.1/2019-01-21-305bc71c-d61d756c/d61d756c0496b5b184cff6ba7172b865.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bahlolab/nf-MPS-gatk-bp/v1.3.1/2019-01-21-305bc71c-d61d756c/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-MPS-gatk-bp/v1.3.1/2019-01-21-305bc71c-d61d756c/Singularity
collection: bahlolab/nf-MPS-gatk-bp
---

# bahlolab/nf-MPS-gatk-bp:v1.3.1

```bash
$ singularity pull shub://bahlolab/nf-MPS-gatk-bp:v1.3.1
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
        gatk4=4.0.12.0 \
        bwa=0.7.17 \
        samtools=1.9 \
        bcftools=1.9 \
        r-base=3.5.1 \
        ensembl-vep=95 \
        multiqc=1.7 \
        fastp=0.19.5
    conda clean --all -y
    apt-get update && apt-get install -y procps
    sed 's:-Dsamjdk.compression_level=[0-9]:-Dsamjdk.compression_level=8:' -i /opt/conda/bin/gatk

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
    export GATK_LOCAL_JAR=/opt/conda/share/gatk4-4.0.12.0-0/gatk-package-4.0.12.0-local.jar
```

## Collection

 - Name: [bahlolab/nf-MPS-gatk-bp](https://github.com/bahlolab/nf-MPS-gatk-bp)
 - License: None

