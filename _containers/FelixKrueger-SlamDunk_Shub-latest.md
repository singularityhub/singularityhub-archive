---
id: 4919
name: "FelixKrueger/SlamDunk_Shub"
branch: "master"
tag: "latest"
commit: "bcd48f4462b4a8d6a0b9ea8742aa931dc5766362"
version: "c83fd4f42e3af9c6f6faf854d21917fa"
build_date: "2019-10-05T01:19:52.145Z"
size_mb: 5060
size: 2175971359
sif: "https://datasets.datalad.org/shub/FelixKrueger/SlamDunk_Shub/latest/2019-10-05-bcd48f44-c83fd4f4/c83fd4f42e3af9c6f6faf854d21917fa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/FelixKrueger/SlamDunk_Shub/latest/2019-10-05-bcd48f44-c83fd4f4/
recipe: https://datasets.datalad.org/shub/FelixKrueger/SlamDunk_Shub/latest/2019-10-05-bcd48f44-c83fd4f4/Singularity
collection: FelixKrueger/SlamDunk_Shub
---

# FelixKrueger/SlamDunk_Shub:latest

```bash
$ singularity pull shub://FelixKrueger/SlamDunk_Shub:latest
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

%environment
    PATH=/opt/miniconda/bin:$PATH
    export PATH
    
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
  
  # Installing Java
  yum -y install java-1.8.0-openjdk
  
%runscript
```

## Collection

 - Name: [FelixKrueger/SlamDunk_Shub](https://github.com/FelixKrueger/SlamDunk_Shub)
 - License: None

