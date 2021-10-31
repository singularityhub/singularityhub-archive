---
id: 11702
name: "dominik-handler/AP_singu"
branch: "master"
tag: "hicassembler"
commit: "6e0745794f1a25b9333f0b28f2a3e6b5be1a1b7a"
version: "904af7f57ef0c9f8361e44484fedc7a2fac992ec59e950c565581cf88fee29c0"
build_date: "2020-03-04T16:47:43.490Z"
size_mb: 551.04296875
size: 577810432
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/hicassembler/2020-03-04-6e074579-904af7f5/904af7f57ef0c9f8361e44484fedc7a2fac992ec59e950c565581cf88fee29c0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/hicassembler/2020-03-04-6e074579-904af7f5/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/hicassembler/2020-03-04-6e074579-904af7f5/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:hicassembler

```bash
$ singularity pull shub://dominik-handler/AP_singu:hicassembler
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  all tools required for the AnnotationPipeline

%post    
  apt-get update
  apt-get -y install locales
  locale-gen en_US.UTF-8

  export LANG=en_US.UTF-8  
  export LANGUAGE=en_US:en  
  export LC_ALL=en_US.UTF-8  

  mkdir /install
  cd /install

  #install all required tools

    apt-get update
    apt-get -y install bzip2 wget python2.7 python2.7-dev python-pip python2.7-setuptools git-core
    apt-get -y install  zlib1g-dev build-essential
    
    wget https://bootstrap.pypa.io/get-pip.py
    #python get-pip.py -c <(echo 'pip==18.0')
    python get-pip.py 

    pip install 'networkx==2.2'
    pip install pytest==4.6
    pip install git+https://github.com/deeptools/HiCExplorer.git@2.1.4
    
    #pip install git+https://github.com/maxplanck-ie/HiCAssembler.git
    pip install git+https://github.com/dominik-handler/HiCAssembler.git

  #clean up and make container smaller
    rm -rf /install
   
%environment
  #!/bin/bash
  export LANG=en_US.UTF-8  
  export LANGUAGE=en_US:en  
  export LC_ALL=en_US.UTF-8  

%runscript
  $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

