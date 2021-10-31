---
id: 1881
name: "qbicsoftware/qbic-singularity-vcftools"
branch: "master"
tag: "latest"
commit: "8c472e4c61e03e6978e0afb9df44d857ba7a8022"
version: "0ca7659f8678d125322c16b2c408f5b9"
build_date: "2018-02-27T17:10:25.446Z"
size_mb: 49
size: 16420895
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-vcftools/latest/2018-02-27-8c472e4c-0ca7659f/0ca7659f8678d125322c16b2c408f5b9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-vcftools/latest/2018-02-27-8c472e4c-0ca7659f/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-vcftools/latest/2018-02-27-8c472e4c-0ca7659f/Singularity
collection: qbicsoftware/qbic-singularity-vcftools
---

# qbicsoftware/qbic-singularity-vcftools:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-vcftools:latest
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

