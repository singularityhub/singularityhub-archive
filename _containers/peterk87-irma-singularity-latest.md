---
id: 7332
name: "peterk87/irma-singularity"
branch: "master"
tag: "latest"
commit: "403635f35bbb0e75b5284a52a7a63f5b6888b7ca"
version: "a047628e4dc5b1f93e1eea778ab02295"
build_date: "2021-04-19T13:29:17.328Z"
size_mb: 1525.0
size: 491175967
sif: "https://datasets.datalad.org/shub/peterk87/irma-singularity/latest/2021-04-19-403635f3-a047628e/a047628e4dc5b1f93e1eea778ab02295.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/peterk87/irma-singularity/latest/2021-04-19-403635f3-a047628e/
recipe: https://datasets.datalad.org/shub/peterk87/irma-singularity/latest/2021-04-19-403635f3-a047628e/Singularity
collection: peterk87/irma-singularity
---

# peterk87/irma-singularity:latest

```bash
$ singularity pull shub://peterk87/irma-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:latest

%help
  A Singularity image for IRMA

%labels
  MAINTAINER Peter Kruczkiewicz
  DESCRIPTION IRMA Singularity image
  Build 1.2

%environment
  export VERSION=0.6.7
  export PATH=/opt/conda/bin:/opt/irma:$PATH
  export LANG=C.UTF-8
  export LC_ALL=C.UTF-8

%files
  flu-amd-201704.zip /

%post
  apt-get update --fix-missing
  apt-get -y install bash wget zip gzip procps wget bzip2 ca-certificates curl git libncurses5
  apt-get clean
  rm -rf /var/lib/apt/lists/*
  wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh -O /miniconda.sh 
  /bin/bash /miniconda.sh -b -p /opt/conda
  rm /miniconda.sh
  ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
  export PATH=/opt/conda/bin:/opt/irma:$PATH
  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels r
  conda config --add channels bioconda
  conda install -y conda=4.7.12
  conda install -y r-base perl=5.22.2.1 mafft samtools 
  conda clean -tipsy
  #wget https://wonder.cdc.gov/amd/flu/irma/flu-amd-201704.zip
  unzip /flu-amd-201704.zip
  rm /flu-amd-201704.zip
  rm /flu-amd/LABEL_RES/scripts/binaries_and_licenses/shogun1.1.0_cmdline_static/shogun_linux32
  rm /flu-amd/LABEL_RES/scripts/binaries_and_licenses/shogun1.1.0_cmdline_static/shogun_darwin64
  mv /flu-amd /opt/irma
  NOW=`date`
  echo "export NOW=\"${NOW}\"" >> $SINGULARITY_ENVIRONMENT
  echo "Done"

%runscript
  exec IRMA "$@"

%test
  export PATH=/opt/conda/bin:/opt/irma:$PATH
  echo "Testing LABEL"
  LABEL /opt/irma/tests/test1.fa label-test H9v2011
  echo "Testing IRMA"
  IRMA FLU /opt/irma/tests/test2.fastq irma-test

echo "Success"
```

## Collection

 - Name: [peterk87/irma-singularity](https://github.com/peterk87/irma-singularity)
 - License: None

