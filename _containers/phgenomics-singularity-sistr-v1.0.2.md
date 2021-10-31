---
id: 3396
name: "phgenomics-singularity/sistr"
branch: "master"
tag: "v1.0.2"
commit: "9f3628627930dcf4ea9242cd3c4d011cb4db9baf"
version: "a76f1d1bb2f0ee47fa82bc3f6eab16ac"
build_date: "2018-07-03T09:02:32.746Z"
size_mb: 3358
size: 1384112159
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/sistr/v1.0.2/2018-07-03-9f362862-a76f1d1b/a76f1d1bb2f0ee47fa82bc3f6eab16ac.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/phgenomics-singularity/sistr/v1.0.2/2018-07-03-9f362862-a76f1d1b/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/sistr/v1.0.2/2018-07-03-9f362862-a76f1d1b/Singularity
collection: phgenomics-singularity/sistr
---

# phgenomics-singularity/sistr:v1.0.2

```bash
$ singularity pull shub://phgenomics-singularity/sistr:v1.0.2
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

