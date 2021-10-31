---
id: 1134
name: "qbicsoftware/qbic-singularity-picard"
branch: "master"
tag: "latest"
commit: "5e402d75d0e3f5a395195d72ddedd392a7b809d9"
version: "be16d3c0e959be2e24a2b6fa118b75d2"
build_date: "2018-01-15T15:00:26.079Z"
size_mb: 561
size: 213524511
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-picard/latest/2018-01-15-5e402d75-be16d3c0/be16d3c0e959be2e24a2b6fa118b75d2.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-picard/latest/2018-01-15-5e402d75-be16d3c0/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-picard/latest/2018-01-15-5e402d75-be16d3c0/Singularity
collection: qbicsoftware/qbic-singularity-picard
---

# qbicsoftware/qbic-singularity-picard:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-picard:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh
#get things up and running
PICARD_VERSION=2.15.0
PICARD_HOME=/opt/picard
mkdir -p $PICARD_HOME
cd $PICARD_HOME
wget --quiet https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar 
#Install call script
mv /picard.sh /usr/bin/picard
chmod +x /usr/bin/picard

%files
#Installation of tool
build.sh
#Call script
picard.sh 

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    PICARD_VERSION=2.15.0
    PICARD_HOME=/opt/picard

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-picard](https://github.com/qbicsoftware/qbic-singularity-picard)
 - License: [MIT License](https://api.github.com/licenses/mit)

