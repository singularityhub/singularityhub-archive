---
id: 6996
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "shovill"
commit: "9ca0d11edea4db0296734c8cb45d187903b60fc9"
version: "efeab3a08d50ca20d691241594924fdd"
build_date: "2019-06-18T17:08:02.399Z"
size_mb: 1398
size: 593707039
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/shovill/2019-06-18-9ca0d11e-efeab3a0/efeab3a08d50ca20d691241594924fdd.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/shovill/2019-06-18-9ca0d11e-efeab3a0/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/shovill/2019-06-18-9ca0d11e-efeab3a0/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:shovill

```bash
$ singularity pull shub://connor-lab/singularity-recipes:shovill
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest


%post
    apt-get update && apt-get -y upgrade
    apt-get install -y procps
    /opt/conda/bin/conda install -c bioconda shovill

%labels
    Maintainer m-bull
    Version shovill-conda-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

