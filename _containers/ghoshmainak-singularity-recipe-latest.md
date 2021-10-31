---
id: 15168
name: "ghoshmainak/singularity-recipe"
branch: "main"
tag: "latest"
commit: "6a66598a1d0eb83ef25c9ca2db87c79a8113527b"
version: "2090c8dea7f7d80a57e31109528492cd"
build_date: "2021-02-03T17:46:50.021Z"
size_mb: 1191.0
size: 423804959
sif: "https://datasets.datalad.org/shub/ghoshmainak/singularity-recipe/latest/2021-02-03-6a66598a-2090c8de/2090c8dea7f7d80a57e31109528492cd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ghoshmainak/singularity-recipe/latest/2021-02-03-6a66598a-2090c8de/
recipe: https://datasets.datalad.org/shub/ghoshmainak/singularity-recipe/latest/2021-02-03-6a66598a-2090c8de/Singularity
collection: ghoshmainak/singularity-recipe
---

# ghoshmainak/singularity-recipe:latest

```bash
$ singularity pull shub://ghoshmainak/singularity-recipe:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels

AUTHOR Mainak
 
%post
 
apt-get -y update
apt-get -y install net-tools
apt-get -y install curl wget
 
# Install conda and check the md5 sum provided on the download site
export CONDA_DIR=/opt/conda
export PATH=$CONDA_DIR/bin:$PATH
export MINICONDA_VERSION=4.9.2
export PYTHON_VER=py37
 
cd /tmp && \
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${PYTHON_VER}_${MINICONDA_VERSION}-Linux-x86_64.sh
echo "3143b1116f2d466d9325c206b7de88f7 *Miniconda3-${PYTHON_VER}_${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c -
/bin/bash Miniconda3-${PYTHON_VER}_${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR
rm Miniconda3-${PYTHON_VER}_${MINICONDA_VERSION}-Linux-x86_64.sh
$CONDA_DIR/bin/conda config --system --prepend channels conda-forge
$CONDA_DIR/bin/conda config --system --set auto_update_conda false
$CONDA_DIR/bin/conda config --system --set show_channel_urls true
$CONDA_DIR/bin/conda install --quiet --yes conda="${MINICONDA_VERSION%.*}.*"
conda update --all --quiet --yes
conda clean -tipsy
 
conda install --quiet --yes \
    'notebook=6.0.3' \
    'numpy' \
    'pandas'


%environment
 
XDG_RUNTIME_DIR=""
PATH=/opt/conda/bin:${PATH}
```

## Collection

 - Name: [ghoshmainak/singularity-recipe](https://github.com/ghoshmainak/singularity-recipe)
 - License: None

