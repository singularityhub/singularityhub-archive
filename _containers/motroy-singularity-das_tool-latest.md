---
id: 7161
name: "motroy/singularity-das_tool"
branch: "master"
tag: "latest"
commit: "7862c9254f5ef01bc3d6f085ad95f685c8acc56f"
version: "37d1b58581f67080f1a7256f247ddc87"
build_date: "2019-02-12T14:29:42.702Z"
size_mb: 3077
size: 1100238879
sif: "https://datasets.datalad.org/shub/motroy/singularity-das_tool/latest/2019-02-12-7862c925-37d1b585/37d1b58581f67080f1a7256f247ddc87.simg"
url: https://datasets.datalad.org/shub/motroy/singularity-das_tool/latest/2019-02-12-7862c925-37d1b585/
recipe: https://datasets.datalad.org/shub/motroy/singularity-das_tool/latest/2019-02-12-7862c925-37d1b585/Singularity
collection: motroy/singularity-das_tool
---

# motroy/singularity-das_tool:latest

```bash
$ singularity pull shub://motroy/singularity-das_tool:latest
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
    apt-get -y install make gcc zlib1g-dev libncurses5-dev build-essential openssh-server
    mkdir /DAS_Tool && cd /DAS_Tool
    wget https://github.com/cmks/DAS_Tool/archive/1.1.1.tar.gz \
        && tar xvf /DAS_Tool/1.1.1.tar.gz
    export CONDARC=/.condarc
    export PATH=/opt/conda/bin:$PATH
    conda config --file /.condarc --add channels defaults \
        && conda config --file /.condarc --add channels bioconda \
        && conda config --file /.condarc --add channels conda-forge
    conda update conda
    conda info
    conda install --yes -c bioconda das_tool
    conda clean --index-cache --tarballs --packages --yes
    mkdir /data /resources
    cd /DAS_Tool/DAS_Tool-1.1.1
    unzip db.zip -d db

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text code will run whenever the container
# is called as an executable or with `singularity run`
function usage() {
    cat <<EOF
NAME
    DAS_Tool - DAS Tool for genome resolved metagenomics
SYNOPSIS
    DAS_Tool --version
    DAS_Tool --help
DESCRIPTION
    DAS Tool is an automated method that integrates the results of a flexible number of binning algorithms to calculate an optimized, non-redundant set of bins from a single assembly.
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
export PATH="/DAS_Tool/DAS_Tool-1.1.1/:/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda
```

## Collection

 - Name: [motroy/singularity-das_tool](https://github.com/motroy/singularity-das_tool)
 - License: [MIT License](https://api.github.com/licenses/mit)

