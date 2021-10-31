---
id: 6315
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "amplicon_phasing_utils_v0.2"
commit: "93c6890c48147f71f962ff68743c200de45bbef6"
version: "b9cf6edf6114dfb415fce768022afb66"
build_date: "2019-01-18T10:30:21.636Z"
size_mb: 1372
size: 420515871
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/amplicon_phasing_utils_v0.2/2019-01-18-93c6890c-b9cf6edf/b9cf6edf6114dfb415fce768022afb66.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/amplicon_phasing_utils_v0.2/2019-01-18-93c6890c-b9cf6edf/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/amplicon_phasing_utils_v0.2/2019-01-18-93c6890c-b9cf6edf/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:amplicon_phasing_utils_v0.2

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:amplicon_phasing_utils_v0.2
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
    conda install -y \
       pysam=0.15.2 \
       samtools=1.9 \
       bcftools=1.9 \
       ensembl-vep=95.0 \
       whatshap=0.17
    conda clean --all -y
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
```

## Collection

 - Name: [bahlolab/nf-pacbio-amplicon-analysis](https://github.com/bahlolab/nf-pacbio-amplicon-analysis)
 - License: None

