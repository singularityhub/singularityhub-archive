---
id: 6921
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "gatk4_v0.1"
commit: "967b673a42875b5a78d32a8f24f24485a55c667b"
version: "3d3bfc536760b37b17802b913b414dee"
build_date: "2019-02-06T08:23:48.111Z"
size_mb: 936
size: 534425631
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/gatk4_v0.1/2019-02-06-967b673a-3d3bfc53/3d3bfc536760b37b17802b913b414dee.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/gatk4_v0.1/2019-02-06-967b673a-3d3bfc53/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/gatk4_v0.1/2019-02-06-967b673a-3d3bfc53/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:gatk4_v0.1

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:gatk4_v0.1
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
    conda install -y gatk4=4.1.0.0
    conda clean --all -y
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
    export GATK_LOCAL_JAR=/opt/conda/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar
```

## Collection

 - Name: [bahlolab/nf-pacbio-amplicon-analysis](https://github.com/bahlolab/nf-pacbio-amplicon-analysis)
 - License: None

