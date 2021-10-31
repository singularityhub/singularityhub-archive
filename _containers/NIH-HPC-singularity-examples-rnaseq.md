---
id: 875
name: "NIH-HPC/singularity-examples"
branch: "master"
tag: "rnaseq"
commit: "2ccdc4a334b5e669dd6eab2099623f8b0d5f5af8"
version: "ec8aa7a15c3ab3ad4d76e03b78f9f4dd"
build_date: "2019-10-21T11:22:01.848Z"
size_mb: 1284
size: 446349343
sif: "https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/rnaseq/2019-10-21-2ccdc4a3-ec8aa7a1/ec8aa7a15c3ab3ad4d76e03b78f9f4dd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NIH-HPC/singularity-examples/rnaseq/2019-10-21-2ccdc4a3-ec8aa7a1/
recipe: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/rnaseq/2019-10-21-2ccdc4a3-ec8aa7a1/Singularity
collection: NIH-HPC/singularity-examples
---

# NIH-HPC/singularity-examples:rnaseq

```bash
$ singularity pull shub://NIH-HPC/singularity-examples:rnaseq
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda:latest
IncludeCmd: yes

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    apt-get -y update
    apt-get -y install make gcc zlib1g-dev libncurses5-dev
    wget https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2 \
        && tar -xjf samtools-1.3.1.tar.bz2 \
        && cd samtools-1.3.1 \
        && make \
        && make prefix=/usr/local install
    export PATH=/opt/conda/bin:$PATH
    conda install --yes -c bioconda \
        star=2.5.2b \
        sailfish=0.10.1 \
        fastqc=0.11.5 \
        kallisto=0.43.0 \
        subread=1.5.0.post3
    conda clean --index-cache --tarballs --packages --yes
    mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /data /scratch /fdb /lscratch

%runscript
#!/bin/bash
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text will will run whenever the container is called as an executable
function usage() {
    cat <<EOF

NAME
    rnaseq - rnaseq pipeline tools 0.1

SYNOPSIS
    rnaseq tool [tool options]
    rnaseq list
    rnaseq help

DESCRIPTION
    Singularity container with tools to build rnaseq pipeline. 

EOF
}

function tools() {
    echo "conda: $(which conda)"
    echo "---------------------------------------------------------------"
    conda list
    echo "---------------------------------------------------------------"
    echo "samtools: $(samtools --version | head -n1)"
}

arg="${1:-none}"

case "$arg" in
    none) usage; exit 1;;
    help) usage; exit 0;;
    list) tools; exit 0;;
    # just try to execute it then
    *)    $@;;
esac

%environment
export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda
```

## Collection

 - Name: [NIH-HPC/singularity-examples](https://github.com/NIH-HPC/singularity-examples)
 - License: None

