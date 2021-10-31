---
id: 3395
name: "phgenomics-singularity/sistr"
branch: "master"
tag: "latest"
commit: "eca66fff52b6019d0c0927539a49c3fec7fc176c"
version: "ba171af1deaa6bf6d31bae264abc7d4d"
build_date: "2018-07-03T09:02:32.754Z"
size_mb: 3358
size: 1384103967
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/sistr/latest/2018-07-03-eca66fff-ba171af1/ba171af1deaa6bf6d31bae264abc7d4d.simg"
url: https://datasets.datalad.org/shub/phgenomics-singularity/sistr/latest/2018-07-03-eca66fff-ba171af1/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/sistr/latest/2018-07-03-eca66fff-ba171af1/Singularity
collection: phgenomics-singularity/sistr
---

# phgenomics-singularity/sistr:latest

```bash
$ singularity pull shub://phgenomics-singularity/sistr:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.4

%help
A Singularity image for SISTR

%labels
Maintainer Anders Goncalves da Silva
Build 1.0
SISTR VERSION 1.0.2

%environment
VERSION=1.0.2
export VERSION
PATH=/opt/conda/bin:$PATH
export PATH

%files
requirements.txt

%post
 # set versions of software to install
  VERSION=1.0.2

  export PATH=/opt/conda/bin:$PATH

  conda config --add channels conda-forge
  conda config --add channels defaults
  conda config --add channels r
  conda config --add channels bioconda

  conda install --yes --file requirements.txt
 
  echo "Sorting some env variables..."
  echo "SISTR installed on $(date "+%Y-%m-%d")" > /etc/dbupdate
  chmod 555 /etc/dbupdate
  
  echo "Done"

%runscript
  echo "Welcome to SISTR $VERSION" >&2
  cat /etc/dbupdate >&2
  exec sistr "$@"

%test
  echo "Testing SISTR"
  export PATH=/opt/conda/bin:$PATH
  cd /tmp
  GENOME=ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz
  OUT=asm.fna.gz
  wget -O $OUT $GENOME
  gzip -d $OUT
  sistr asm.fna | grep "Typhimurium"
  rm asm.fna
  echo "Success"
```

## Collection

 - Name: [phgenomics-singularity/sistr](https://github.com/phgenomics-singularity/sistr)
 - License: None

