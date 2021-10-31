---
id: 7796
name: "bozmik/singularity_image"
branch: "master"
tag: "latest"
commit: "0ad7d5b9380aef7f4b16fe401b9d4389b6f53f9c"
version: "7d9139794322f73dd204d0baaba472ea"
build_date: "2019-03-18T01:49:47.084Z"
size_mb: 3562
size: 1270370335
sif: "https://datasets.datalad.org/shub/bozmik/singularity_image/latest/2019-03-18-0ad7d5b9-7d913979/7d9139794322f73dd204d0baaba472ea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bozmik/singularity_image/latest/2019-03-18-0ad7d5b9-7d913979/
recipe: https://datasets.datalad.org/shub/bozmik/singularity_image/latest/2019-03-18-0ad7d5b9-7d913979/Singularity
collection: bozmik/singularity_image
---

# bozmik/singularity_image:latest

```bash
$ singularity pull shub://bozmik/singularity_image:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nfcore/base


%environment

    PATH=/opt/conda/envs/bozmik-singularity_image/bin:$PATH
    export PATH


%files
    environment.yml 

%post

    alias conda="/opt/conda/bin/conda"
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda install -y \
       spotyping=2.1
    conda clean --tarballs --index-cache --source-cache
    apt-get update && apt-get install -y procps

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [bozmik/singularity_image](https://github.com/bozmik/singularity_image)
 - License: None

