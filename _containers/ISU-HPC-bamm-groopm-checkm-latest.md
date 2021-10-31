---
id: 3781
name: "ISU-HPC/bamm-groopm-checkm"
branch: "master"
tag: "latest"
commit: "19e2e930842eb3b4bd320ce8757f87bc26f4568e"
version: "75c4e5b040dd85185c8cb12737020ac6"
build_date: "2018-08-30T10:21:12.728Z"
size_mb: 2990
size: 1266970655
sif: "https://datasets.datalad.org/shub/ISU-HPC/bamm-groopm-checkm/latest/2018-08-30-19e2e930-75c4e5b0/75c4e5b040dd85185c8cb12737020ac6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/bamm-groopm-checkm/latest/2018-08-30-19e2e930-75c4e5b0/
recipe: https://datasets.datalad.org/shub/ISU-HPC/bamm-groopm-checkm/latest/2018-08-30-19e2e930-75c4e5b0/Singularity
collection: ISU-HPC/bamm-groopm-checkm
---

# ISU-HPC/bamm-groopm-checkm:latest

```bash
$ singularity pull shub://ISU-HPC/bamm-groopm-checkm:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
from:continuumio/miniconda

%labels
MAINTAINER Yasasvy Nanyam ynanyam@iastate.edu

%post
apt-get update
apt-get install -y gcc libgl1-mesa-glx
export PATH=/opt/conda/bin:$PATH
conda config --add channels conda-forge
conda config --add channels bioconda
conda install bamm 
pip install --no-cache-dir cython GroopM pillow refinem 
ln -s /opt/conda/lib/libhts.so /opt/conda/lib/libhts.so.1
conda install checkm-genome
conda install functools_lru_cache
echo 'export PATH=/usr/local/bin:/opt/conda/bin:$PATH' >>$SINGULARITY_ENVIRONMENT
# INSTALL PRODIGAL
apt-get update
apt-get install -y build-essential
cd /opt
git clone https://github.com/hyattpd/Prodigal.git
cd Prodigal
make install
cd ..
rm -rf Prodigal
#INSTALL BLAST+
apt install -y ncbi-blast+
# INSTALL DIAMOND
cd /opt
wget http://github.com/bbuchfink/diamond/releases/download/v0.9.22/diamond-linux64.tar.gz
tar xzf diamond-linux64.tar.gz
mv diamond /usr/local/bin
cd ..
rm -rf /var/lib/apt/lists/*
# Install Krona
cd /opt
wget https://github.com/marbl/Krona/releases/download/v2.7/KronaTools-2.7.tar
tar xf KronaTools-2.7.tar
cd KronaTools-2.7
./install.pl
```

## Collection

 - Name: [ISU-HPC/bamm-groopm-checkm](https://github.com/ISU-HPC/bamm-groopm-checkm)
 - License: None

