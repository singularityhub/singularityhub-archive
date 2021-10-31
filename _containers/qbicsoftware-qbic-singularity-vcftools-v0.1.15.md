---
id: 1882
name: "qbicsoftware/qbic-singularity-vcftools"
branch: "master"
tag: "v0.1.15"
commit: "8c472e4c61e03e6978e0afb9df44d857ba7a8022"
version: "b5eb98f57c14246311d5b9bc6b04dc82"
build_date: "2018-02-27T17:10:25.454Z"
size_mb: 49
size: 16420895
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-vcftools/v0.1.15/2018-02-27-8c472e4c-b5eb98f5/b5eb98f57c14246311d5b9bc6b04dc82.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-vcftools/v0.1.15/2018-02-27-8c472e4c-b5eb98f5/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-vcftools/v0.1.15/2018-02-27-8c472e4c-b5eb98f5/Singularity
collection: qbicsoftware/qbic-singularity-vcftools
---

# qbicsoftware/qbic-singularity-vcftools:v0.1.15

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-vcftools:v0.1.15
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/vcftools:0.1.15--1
Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    VCFTools=0.1.15
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-vcftools](https://github.com/qbicsoftware/qbic-singularity-vcftools)
 - License: None

