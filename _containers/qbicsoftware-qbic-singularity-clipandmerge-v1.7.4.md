---
id: 1800
name: "qbicsoftware/qbic-singularity-clipandmerge"
branch: "master"
tag: "v1.7.4"
commit: "255eb7d6ac49eaa3338910388f91a6e45eeacbd9"
version: "6fe792502f559e88c9e6bf5b7ad0c662"
build_date: "2018-02-22T14:08:21.003Z"
size_mb: 426
size: 176361503
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-clipandmerge/v1.7.4/2018-02-22-255eb7d6-6fe79250/6fe792502f559e88c9e6bf5b7ad0c662.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-clipandmerge/v1.7.4/2018-02-22-255eb7d6-6fe79250/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-clipandmerge/v1.7.4/2018-02-22-255eb7d6-6fe79250/Singularity
collection: qbicsoftware/qbic-singularity-clipandmerge
---

# qbicsoftware/qbic-singularity-clipandmerge:v1.7.4

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-clipandmerge:v1.7.4
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%post
/bin/sh build.sh
mv /starter.sh /usr/bin/ClipAndMerge
chmod +x /usr/bin/ClipAndMerge
wget https://github.com/apeltzer/ClipAndMerge/releases/download/v1.7.4/ClipAndMerge.jar
mv /ClipAndMerge.jar /usr/bin/ClipAndMerge.jar


%files
#Installation of tool
build.sh
starter.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    CLIPANDMERGE=v1.7.4

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-clipandmerge](https://github.com/qbicsoftware/qbic-singularity-clipandmerge)
 - License: None

