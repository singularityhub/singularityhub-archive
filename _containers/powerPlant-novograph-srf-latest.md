---
id: 7174
name: "powerPlant/novograph-srf"
branch: "master"
tag: "latest"
commit: "89148757db406954b54ef8f8b62a508d72cf6764"
version: "791542422c07b135cc264e1a860084bd"
build_date: "2019-02-13T08:56:28.422Z"
size_mb: 1159
size: 349663263
sif: "https://datasets.datalad.org/shub/powerPlant/novograph-srf/latest/2019-02-13-89148757-79154242/791542422c07b135cc264e1a860084bd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/novograph-srf/latest/2019-02-13-89148757-79154242/
recipe: https://datasets.datalad.org/shub/powerPlant/novograph-srf/latest/2019-02-13-89148757-79154242/Singularity
collection: powerPlant/novograph-srf
---

# powerPlant/novograph-srf:latest

```bash
$ singularity pull shub://powerPlant/novograph-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.0.0

%post
  ## Download prerequisites
  apt-get update
  apt-get -y install bioperl bwa g++ gcc git libbz2-dev liblzma-dev libmodule-build-perl libset-intervaltree-perl mafft make samtools sudo wget zlib1g-dev

  ## BIO::DB::HTS
  cd /opt
  wget https://github.com/Ensembl/Bio-DB-HTS/archive/2.11.tar.gz
  tar -xzf 2.11.tar.gz
  cd Bio-DB-HTS-2.11
  ./INSTALL.pl 

  ## NovoGraph
  cd /opt
  wget https://github.com/NCBI-Hackathons/NovoGraph/archive/v1.0.0.tar.gz
  tar -xzf v1.0.0.tar.gz 
  cd NovoGraph-1.0.0/src
  make all

  ## Cleanup
  SUDO_FORCE_REMOVE=yes apt-get -y remove g++ gcc git libbz2-dev liblzma-dev libmodule-build-perl make sudo wget zlib1g-dev
  apt-get -y autoremove
  apt-get -y clean all

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"$SINGULARITY_NAME <cmd>\" or \"singularity exec $SINGULARITY_NAME perl <cmd>\", where <cmd> is one of the following:\n"
  exec ls /opt/NovoGraph-1.0.0/scripts
else
  cd /opt/NovoGraph-1.0.0/scripts
  exec perl "$@"
fi
```

## Collection

 - Name: [powerPlant/novograph-srf](https://github.com/powerPlant/novograph-srf)
 - License: None

