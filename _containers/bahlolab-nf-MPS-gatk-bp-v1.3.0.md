---
id: 5520
name: "bahlolab/nf-MPS-gatk-bp"
branch: "master"
tag: "v1.3.0"
commit: "e4ecfee5c5482e116b0562b6eed0cc6f2ef0900f"
version: "eb62b13db33d62525938e6101f92342b"
build_date: "2019-01-16T03:42:16.183Z"
size_mb: 3246
size: 1172762655
sif: "https://datasets.datalad.org/shub/bahlolab/nf-MPS-gatk-bp/v1.3.0/2019-01-16-e4ecfee5-eb62b13d/eb62b13db33d62525938e6101f92342b.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-MPS-gatk-bp/v1.3.0/2019-01-16-e4ecfee5-eb62b13d/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-MPS-gatk-bp/v1.3.0/2019-01-16-e4ecfee5-eb62b13d/Singularity
collection: bahlolab/nf-MPS-gatk-bp
---

# bahlolab/nf-MPS-gatk-bp:v1.3.0

```bash
$ singularity pull shub://bahlolab/nf-MPS-gatk-bp:v1.3.0
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
        gatk4=4.0.11.0 \
        bwa=0.7.17 \
        samtools=1.9 \
        bcftools=1.9 \
        ensembl-vep=94.4 \
        multiqc=1.6  \
        fastp=0.19.4
    conda clean --all -y
    apt-get update && apt-get install -y procps
    sed 's:-Dsamjdk.compression_level=[0-9]:-Dsamjdk.compression_level=8:' -i /opt/conda/bin/gatk

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
    export GATK_LOCAL_JAR=/opt/conda/share/gatk4-4.0.11.0-0/gatk-package-4.0.11.0-local.jar
```

## Collection

 - Name: [bahlolab/nf-MPS-gatk-bp](https://github.com/bahlolab/nf-MPS-gatk-bp)
 - License: None

