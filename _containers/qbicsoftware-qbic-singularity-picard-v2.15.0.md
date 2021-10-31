---
id: 1135
name: "qbicsoftware/qbic-singularity-picard"
branch: "master"
tag: "v2.15.0"
commit: "5e402d75d0e3f5a395195d72ddedd392a7b809d9"
version: "80e924aa8209415f0c0086f2b6cdc7b4"
build_date: "2020-05-07T04:13:59.797Z"
size_mb: 561
size: 213520415
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-picard/v2.15.0/2020-05-07-5e402d75-80e924aa/80e924aa8209415f0c0086f2b6cdc7b4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-picard/v2.15.0/2020-05-07-5e402d75-80e924aa/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-picard/v2.15.0/2020-05-07-5e402d75-80e924aa/Singularity
collection: qbicsoftware/qbic-singularity-picard
---

# qbicsoftware/qbic-singularity-picard:v2.15.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-picard:v2.15.0
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

