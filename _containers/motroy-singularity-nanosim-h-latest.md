---
id: 6879
name: "motroy/singularity-nanosim-h"
branch: "master"
tag: "latest"
commit: "9d7e32b2a5ef316bb373c2ce9b84bfb91dcf6beb"
version: "862940daef45d1f03ec1abdb30c60f89"
build_date: "2020-12-05T20:59:56.874Z"
size_mb: 1847.0
size: 876453919
sif: "https://datasets.datalad.org/shub/motroy/singularity-nanosim-h/latest/2020-12-05-9d7e32b2-862940da/862940daef45d1f03ec1abdb30c60f89.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-nanosim-h/latest/2020-12-05-9d7e32b2-862940da/
recipe: https://datasets.datalad.org/shub/motroy/singularity-nanosim-h/latest/2020-12-05-9d7e32b2-862940da/Singularity
collection: motroy/singularity-nanosim-h
---

# motroy/singularity-nanosim-h:latest

```bash
$ singularity pull shub://motroy/singularity-nanosim-h:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/miniconda/miniconda3/bin:$PATH"
export CONDARC="/.condarc"



%post
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate build-essential openssh-server
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh 
./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda/miniconda3
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels defaults
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels bioconda
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels conda-forge
export PATH="/miniconda/miniconda3/bin:$PATH"
export CONDARC="/.condarc"
/miniconda/miniconda3/bin/conda install -y nanosim-h=1.1.0.4
```

## Collection

 - Name: [motroy/singularity-nanosim-h](https://github.com/motroy/singularity-nanosim-h)
 - License: [MIT License](https://api.github.com/licenses/mit)

