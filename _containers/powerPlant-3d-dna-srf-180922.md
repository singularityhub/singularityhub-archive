---
id: 6853
name: "powerPlant/3d-dna-srf"
branch: "master"
tag: "180922"
commit: "cb2defdf92544d481d003612c801276a1612ac85"
version: "80a85d39d73a9da3c07fb4316c273fb7"
build_date: "2019-02-05T05:54:32.623Z"
size_mb: 1004
size: 410226719
sif: "https://datasets.datalad.org/shub/powerPlant/3d-dna-srf/180922/2019-02-05-cb2defdf-80a85d39/80a85d39d73a9da3c07fb4316c273fb7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/3d-dna-srf/180922/2019-02-05-cb2defdf-80a85d39/
recipe: https://datasets.datalad.org/shub/powerPlant/3d-dna-srf/180922/2019-02-05-cb2defdf-80a85d39/Singularity
collection: powerPlant/3d-dna-srf
---

# powerPlant/3d-dna-srf:180922

```bash
$ singularity pull shub://powerPlant/3d-dna-srf:180922
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:cosmic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 180922

%environment
  PATH=/opt/3d-dna:$PATH
  export PATH

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install git make openjdk-8-jre parallel python-matplotlib python-numpy python-scipy wget
  
  ## Install LastZ (version 1.03.73 released 20150708)
  wget http://www.bx.psu.edu/~rsharris/lastz/newer/lastz-1.03.73.tar.gz
  tar -xzf lastz-1.03.73.tar.gz
  cd lastz-distrib-1.03.73/src
  sed -i 's/-Werror //' Makefile
  make
  LASTZ_INSTALL=/usr/bin/ make install

  ## Install 3d-dna
  cd /opt
  git clone https://github.com/theaidenlab/3d-dna.git
  cd 3d-dna
  git checkout 3f18163
  chmod +x run-asm-pipeline.sh run-asm-pipeline-post-review.sh

  ## Cleanup
  apt-get -y remove git make wget
  apt-get -y clean all
  rm -rf /lastz*

%runscript
  exec run-asm-pipeline.sh "$@"
```

## Collection

 - Name: [powerPlant/3d-dna-srf](https://github.com/powerPlant/3d-dna-srf)
 - License: None

