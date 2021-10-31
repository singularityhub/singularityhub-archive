---
id: 6151
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "pacbio_smrt_v0.3"
commit: "1067d3d7b4f2d99a17a58da32afd8d8ad81fdffa"
version: "32c9a131ff31737539c1e56f184f72d5"
build_date: "2019-01-08T15:14:12.063Z"
size_mb: 1718
size: 599396383
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.3/2019-01-08-1067d3d7-32c9a131/32c9a131ff31737539c1e56f184f72d5.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.3/2019-01-08-1067d3d7-32c9a131/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.3/2019-01-08-1067d3d7-32c9a131/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.3

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.3
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
       genomicconsensus=2.3.2 \
       pbmm2=0.11.0 \
       blasr=5.3.2 \
       lima=1.8.0 \
       pbccs=3.1.0 \
       pblaa=2.4.2 \
       pbsv=2.1.1
    conda clean --tarballs --index-cache --source-cache
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
```

## Collection

 - Name: [bahlolab/nf-pacbio-amplicon-analysis](https://github.com/bahlolab/nf-pacbio-amplicon-analysis)
 - License: None

