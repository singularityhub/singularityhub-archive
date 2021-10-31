---
id: 1784
name: "qbicsoftware/qbic-singularity-miso"
branch: "master"
tag: "v0.5.4"
commit: "d0992c46aa15e71af06089ab4bd70de5c696bc7e"
version: "78473831df59236e4d6f912937e16ec0"
build_date: "2018-02-22T10:18:07.719Z"
size_mb: 952
size: 385269791
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-miso/v0.5.4/2018-02-22-d0992c46-78473831/78473831df59236e4d6f912937e16ec0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-miso/v0.5.4/2018-02-22-d0992c46-78473831/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-miso/v0.5.4/2018-02-22-d0992c46-78473831/Singularity
collection: qbicsoftware/qbic-singularity-miso
---

# qbicsoftware/qbic-singularity-miso:v0.5.4

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-miso:v0.5.4
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%post
/bin/sh build.sh
#We need htslib to be installed for miso 
wget https://github.com/samtools/htslib/releases/download/1.7/htslib-1.7.tar.bz2
tar jxf htslib-1.7.tar.bz2
cd htslib-1.7/
./configure --prefix=/usr/local/bin
make
make install 
pip install misopy==0.5.4


%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    miso=v0.5.4

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-miso](https://github.com/qbicsoftware/qbic-singularity-miso)
 - License: None

