---
id: 1082
name: "qbicsoftware/qbic-singularity-trimgalore"
branch: "master"
tag: "v0.4.5"
commit: "0c6540ceda902337476f9bffc5879e52f1f82b14"
version: "682749f1d4112616412514eaa20d96b6"
build_date: "2017-12-08T13:31:57.423Z"
size_mb: 310
size: 112795679
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-trimgalore/v0.4.5/2017-12-08-0c6540ce-682749f1/682749f1d4112616412514eaa20d96b6.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-trimgalore/v0.4.5/2017-12-08-0c6540ce-682749f1/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-trimgalore/v0.4.5/2017-12-08-0c6540ce-682749f1/Singularity
collection: qbicsoftware/qbic-singularity-trimgalore
---

# qbicsoftware/qbic-singularity-trimgalore:v0.4.5

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-trimgalore:v0.4.5
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:3.6

%post
/bin/sh build.sh
pip install cutadapt==1.14
DEST_DIR=/opt/
mkdir -p ${DEST_DIR}
cd /opt/
wget https://github.com/FelixKrueger/TrimGalore/archive/0.4.5.zip
unzip 0.4.5.zip
rm 0.4.5.zip
ln -s /opt/TrimGalore-0.4.5/trim_galore /usr/bin/trim_galore

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
trimgalore_VERSION=v0.4.5



%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-trimgalore](https://github.com/qbicsoftware/qbic-singularity-trimgalore)
 - License: None

