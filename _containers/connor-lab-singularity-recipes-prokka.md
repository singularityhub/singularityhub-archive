---
id: 6990
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "prokka"
commit: "4256bbd659ea8fe944796488ccd8ca32a967b8d9"
version: "0d6d1d8610a9772ed3983f1af74cc6e8"
build_date: "2019-08-20T06:06:44.189Z"
size_mb: 3963
size: 1854173215
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/prokka/2019-08-20-4256bbd6-0d6d1d86/0d6d1d8610a9772ed3983f1af74cc6e8.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/prokka/2019-08-20-4256bbd6-0d6d1d86/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/prokka/2019-08-20-4256bbd6-0d6d1d86/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:prokka

```bash
$ singularity pull shub://connor-lab/singularity-recipes:prokka
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest


%post
    apt-get update && apt-get -y upgrade
    apt-get install -y procps
    /opt/conda/bin/conda install -c bioconda perl-bioperl
    /opt/conda/bin/conda install -c conda-forge -c bioconda prokka

%labels
    Maintainer m-bull
    Version prokka-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

