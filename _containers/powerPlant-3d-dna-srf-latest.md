---
id: 6852
name: "powerPlant/3d-dna-srf"
branch: "master"
tag: "latest"
commit: "725a62030e94fc0bd4b5f35d52177c0bd89c828e"
version: "1753c6c6361b0de88579a56fa37912b4"
build_date: "2019-02-04T09:08:23.937Z"
size_mb: 1004
size: 410185759
sif: "https://datasets.datalad.org/shub/powerPlant/3d-dna-srf/latest/2019-02-04-725a6203-1753c6c6/1753c6c6361b0de88579a56fa37912b4.simg"
url: https://datasets.datalad.org/shub/powerPlant/3d-dna-srf/latest/2019-02-04-725a6203-1753c6c6/
recipe: https://datasets.datalad.org/shub/powerPlant/3d-dna-srf/latest/2019-02-04-725a6203-1753c6c6/Singularity
collection: powerPlant/3d-dna-srf
---

# powerPlant/3d-dna-srf:latest

```bash
$ singularity pull shub://powerPlant/3d-dna-srf:latest
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
  run-asm-pipeline.sh "$@"
```

## Collection

 - Name: [powerPlant/3d-dna-srf](https://github.com/powerPlant/3d-dna-srf)
 - License: None

