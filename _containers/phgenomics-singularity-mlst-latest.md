---
id: 1671
name: "phgenomics-singularity/mlst"
branch: "master"
tag: "latest"
commit: "704ac7acc374b772a2e0fb67b5c5b559ccd58f1a"
version: "f23d310635e5e92e6893bd2b8e541cb9"
build_date: "2020-02-17T23:59:57.055Z"
size_mb: 3298
size: 1258065951
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/mlst/latest/2020-02-17-704ac7ac-f23d3106/f23d310635e5e92e6893bd2b8e541cb9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/phgenomics-singularity/mlst/latest/2020-02-17-704ac7ac-f23d3106/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/mlst/latest/2020-02-17-704ac7ac-f23d3106/Singularity
collection: phgenomics-singularity/mlst
---

# phgenomics-singularity/mlst:latest

```bash
$ singularity pull shub://phgenomics-singularity/mlst:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.11

%help
A Singularity image for MLST 2.16.1

%labels
Maintainer Anders Goncalves da Silva
Build 1.0
MLST_version 2.16.1

%environment
MLST_VERSION=2.16.1
export MLST_VERSION
export PATH=/opt/conda/bin:$PATH
export PYTHONUSERBASE=False

export MLST_DB=/opt/mlst/db/blast/mlst.fa
export MLST_PUBMLST=/opt/mlst/db/pubmlst


%files
mlst_db.tar.gz mlst_db.tar.gz
mlst_db_update.log mlst_db_update.log

%post
  export PATH=/opt/conda/bin:$PATH
  
  mkdir -p /opt/mlst/db
  mv mlst_db.tar.gz mlst_db_update.log /opt/mlst/db
  cd /opt/mlst/db
  tar xzvf mlst_db.tar.gz
  rm mlst_db.tar.gz
  echo "All DBs updated on $(date "+%Y-%m-%d")" > /etc/dbupdate
  

  conda config --add channels conda-forge
  conda config --add channels defaults
  conda config --add channels r
  conda config --add channels bioconda
  conda config --add channels anaconda
  conda install -c bioconda mlst==2.16.1-0

  echo "Sorting some env variables..."
  chmod 555 /etc/dbupdate
  echo 'LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
  echo 'LANG=C.UTF-8' >>  $SINGULARITY_ENVIRONMENT 
  echo "Done"

%runscript
  echo "Welcome to MLST ${MLST_VERSION}" >&2
  cat /etc/dbupdate >&2
  
  exec mlst --blastdb $MLST_DB --datadir $MLST_PUBMLST "$@"
  

%test
  export PATH=/opt/conda/bin:$PATH
  export MLST_DB=/opt/mlst/db/blast/mlst.fa
  export MLST_PUBMLST=/opt/mlst/db/pubmlst
  
  echo "Testing MLST"
  echo "Test Genome is a Neisseria meningitidis ST74!"
  GENOME="ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/008/805/GCF_000008805.1_ASM880v1/GCF_000008805.1_ASM880v1_genomic.gbff.gz"
  wget -O /tmp/test.gbk.gz ${GENOME}
  
  mlst --blastdb $MLST_DB --datadir $MLST_PUBMLST /tmp/test.gbk.gz > /tmp/res 2> /dev/null
  
  cat /tmp/res
  res=$(grep neisseria /tmp/res)
  if [ -n "${res}" ];
    then
      echo "MLST installed successfully!";
    else
      echo "Something went wrong!";
    fi;
  rm /tmp/test.gbk.gz /tmp/res
```

## Collection

 - Name: [phgenomics-singularity/mlst](https://github.com/phgenomics-singularity/mlst)
 - License: None

