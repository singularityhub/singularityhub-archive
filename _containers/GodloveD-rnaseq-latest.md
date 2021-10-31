---
id: 48
name: "GodloveD/rnaseq"
branch: "master"
tag: "latest"
commit: "ce0ab3b6a95492b235c7e485b900b1a2f364d406"
version: "80e3bb9959cf161069f4fb72d30fa7d0"
build_date: "2019-09-22T19:47:11.831Z"
size_mb: 1324
size: 480903199
sif: "https://datasets.datalad.org/shub/GodloveD/rnaseq/latest/2019-09-22-ce0ab3b6-80e3bb99/80e3bb9959cf161069f4fb72d30fa7d0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GodloveD/rnaseq/latest/2019-09-22-ce0ab3b6-80e3bb99/
recipe: https://datasets.datalad.org/shub/GodloveD/rnaseq/latest/2019-09-22-ce0ab3b6-80e3bb99/Singularity
collection: GodloveD/rnaseq
---

# GodloveD/rnaseq:latest

```bash
$ singularity pull shub://GodloveD/rnaseq:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3:latest
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

cat > /singularity <<'EORUNSCRIPT'
#!/bin/bash
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text will get copied to /singularity and will run whenever the container
# is called as an executable
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

export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda

arg="${1:-none}"

case "$arg" in
    none) usage; exit 1;;
    help) usage; exit 0;;
    list) tools; exit 0;;
    # just try to execute it then
    *)    $@;;
esac
EORUNSCRIPT
chmod 755 /singularity
```

## Collection

 - Name: [GodloveD/rnaseq](https://github.com/GodloveD/rnaseq)
 - License: None

