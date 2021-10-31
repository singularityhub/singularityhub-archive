---
id: 7334
name: "motroy/singularity-bob-gridtk"
branch: "master"
tag: "latest"
commit: "6c2a53a663a6354ed218c18d2c0e23b71b75dcef"
version: "f745f69bb9a3a554440b02c4cb5d1478"
build_date: "2019-03-10T12:12:53.542Z"
size_mb: 852
size: 328699935
sif: "https://datasets.datalad.org/shub/motroy/singularity-bob-gridtk/latest/2019-03-10-6c2a53a6-f745f69b/f745f69bb9a3a554440b02c4cb5d1478.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-bob-gridtk/latest/2019-03-10-6c2a53a6-f745f69b/
recipe: https://datasets.datalad.org/shub/motroy/singularity-bob-gridtk/latest/2019-03-10-6c2a53a6-f745f69b/Singularity
collection: motroy/singularity-bob-gridtk
---

# motroy/singularity-bob-gridtk:latest

```bash
$ singularity pull shub://motroy/singularity-bob-gridtk:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/miniconda/miniconda3/bin:$PATH"
export CONDARC=/.condarc

%post
export CONDARC=/.condarc
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate build-essential openssh-server apt-transport-https software-properties-common libssl-dev libcurl4-openssl-dev
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
apt update && apt install -y r-base
#wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
#chmod +x Miniconda3-latest-Linux-x86_64.sh
#./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda/miniconda3
#/miniconda/miniconda3/bin/conda update -n base conda && /miniconda/miniconda3/bin/conda config --set show_channel_urls True
#/miniconda/miniconda3/bin/conda config --file /.condarc --add channels defaults && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels https://www.idiap.ch/software/bob/conda
R Rscript -e 'install.packages("ggplot2")'
R Rscript -e 'install.packages("devtools")'
R Rscript -e 'library("devtools"); install_github("larmarange/JLutils")'
```

## Collection

 - Name: [motroy/singularity-bob-gridtk](https://github.com/motroy/singularity-bob-gridtk)
 - License: [MIT License](https://api.github.com/licenses/mit)

