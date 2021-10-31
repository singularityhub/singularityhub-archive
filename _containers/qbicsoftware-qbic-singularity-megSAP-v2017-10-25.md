---
id: 561
name: "qbicsoftware/qbic-singularity-megSAP"
branch: "master"
tag: "v2017-10-25"
commit: "0456f16145f077a9d21fe7d85b336ca86db29a44"
version: "f84e227482f1d0d695702fba77714fc3"
build_date: "2017-11-19T10:50:40.525Z"
size_mb: 1470
size: 691208223
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-megSAP/v2017-10-25/2017-11-19-0456f161-f84e2274/f84e227482f1d0d695702fba77714fc3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-megSAP/v2017-10-25/2017-11-19-0456f161-f84e2274/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-megSAP/v2017-10-25/2017-11-19-0456f161-f84e2274/Singularity
collection: qbicsoftware/qbic-singularity-megSAP
---

# qbicsoftware/qbic-singularity-megSAP:v2017-10-25

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-megSAP:v2017-10-25
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%post
/bin/sh build.sh

%post

#Installing basic dependencies
 
#Get the pipeline, rather the fork of the pipeline that we tag first and then use the newest tag as version to be able to track back what was used at a certain point 

git clone --recursive https://github.com/apeltzer/megSAP.git
cd megSAP/data/
chmod 755 download_*.sh
#/bin/bash download_tools.sh

#Symlink our data to the right folder
#This ensures that we can access the data path from inside the container, without having to download & bundle the datasets all the time (31GB is a lot)
rm -rf /megSAP/data
ln -s /lustre_cfc/qbic/megSAP-data/data /megSAP/

#We're not downloading this into the container

#/bin/bash download_GRCh37.sh
#/bin/bashsh download_dbs.sh

%files
build.sh

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
Version	20171010
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-megSAP](https://github.com/qbicsoftware/qbic-singularity-megSAP)
 - License: None

