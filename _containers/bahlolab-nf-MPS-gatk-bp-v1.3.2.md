---
id: 6917
name: "bahlolab/nf-MPS-gatk-bp"
branch: "master"
tag: "v1.3.2"
commit: "418fd02b1a9d83bc1a66870b3a11ad0e8c755ef0"
version: "f3a900a97acbf232f1f60f0608c00157"
build_date: "2019-02-21T02:19:10.060Z"
size_mb: 3309
size: 1294630943
sif: "https://datasets.datalad.org/shub/bahlolab/nf-MPS-gatk-bp/v1.3.2/2019-02-21-418fd02b-f3a900a9/f3a900a97acbf232f1f60f0608c00157.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bahlolab/nf-MPS-gatk-bp/v1.3.2/2019-02-21-418fd02b-f3a900a9/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-MPS-gatk-bp/v1.3.2/2019-02-21-418fd02b-f3a900a9/Singularity
collection: bahlolab/nf-MPS-gatk-bp
---

# bahlolab/nf-MPS-gatk-bp:v1.3.2

```bash
$ singularity pull shub://bahlolab/nf-MPS-gatk-bp:v1.3.2
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
    conda update -n base -c defaults conda -y
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels r
    conda install -y \
        gatk4=4.1.0.0 \
        bwa=0.7.17 \
        samtools=1.9 \
        bcftools=1.9 \
        r-base=3.5.1 \
        ensembl-vep=95 \
        multiqc=1.7 \
        fastp=0.19.5 \
        pysam=0.15.2 \
        openssl=1.0
    conda clean --all -y
    apt-get update && apt-get install -y procps
    sed 's:-Dsamjdk.compression_level=[0-9]:-Dsamjdk.compression_level=8:' -i /opt/conda/bin/gatk

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
    export GATK_LOCAL_JAR=/opt/conda/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar
```

## Collection

 - Name: [bahlolab/nf-MPS-gatk-bp](https://github.com/bahlolab/nf-MPS-gatk-bp)
 - License: None

