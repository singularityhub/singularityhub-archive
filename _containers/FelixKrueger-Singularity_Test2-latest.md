---
id: 4938
name: "FelixKrueger/Singularity_Test2"
branch: "master"
tag: "latest"
commit: "c847f32cc0207358dad6f1c5f45ff2822233e09c"
version: "e357bad109a7687f8d37661c6dfa53c5"
build_date: "2018-09-24T17:40:58.491Z"
size_mb: 5143
size: 2211987487
sif: "https://datasets.datalad.org/shub/FelixKrueger/Singularity_Test2/latest/2018-09-24-c847f32c-e357bad1/e357bad109a7687f8d37661c6dfa53c5.simg"
url: https://datasets.datalad.org/shub/FelixKrueger/Singularity_Test2/latest/2018-09-24-c847f32c-e357bad1/
recipe: https://datasets.datalad.org/shub/FelixKrueger/Singularity_Test2/latest/2018-09-24-c847f32c-e357bad1/Singularity
collection: FelixKrueger/Singularity_Test2
---

# FelixKrueger/Singularity_Test2:latest

```bash
$ singularity pull shub://FelixKrueger/Singularity_Test2:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
  This is a test message.

%setup

%labels
    DESCRIPTION Singularity image containing all requirements for a SlamDunk installation
    VERSION 1.0

%post
  yum -y install wget
  yum -y install epel-release
  yum -y update
  yum -y install bzip2
  yum -y install python-pip
  yum -y install tar
  yum -y install which
  
  echo "Installing Development Tools YUM group"
  yum -y groupinstall "Development tools"
  
  wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O $HOME/miniconda.sh
  bash $HOME/miniconda.sh -b -p $SINGULARITY_ROOT/opt/miniconda
  export PATH="$SINGULARITY_ROOT/opt/miniconda/bin:$PATH"
 
  # Bioconda (http://ddocent.com//bioconda/)
  conda config --add channels r
  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels bioconda
  conda create -y --name SlamDunk -c bioconda slamdunk
 
  # Installing Bowtie2
  conda install bowtie2=2.3.0
  
  %environment
  #Set your toolname here and the appropriate version to have this in the metadata of your container
    #BOWTIE2=v2.3.0
  
%runscript
```

## Collection

 - Name: [FelixKrueger/Singularity_Test2](https://github.com/FelixKrueger/Singularity_Test2)
 - License: None

