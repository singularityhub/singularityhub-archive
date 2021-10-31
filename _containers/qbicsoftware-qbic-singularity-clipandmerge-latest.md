---
id: 1799
name: "qbicsoftware/qbic-singularity-clipandmerge"
branch: "master"
tag: "latest"
commit: "e693cd1ab7712aff642b9a52fd341ce8139dd15b"
version: "baceb6d590ec6a073700422be180439a"
build_date: "2018-02-22T14:08:21.014Z"
size_mb: 426
size: 176361503
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-clipandmerge/latest/2018-02-22-e693cd1a-baceb6d5/baceb6d590ec6a073700422be180439a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-clipandmerge/latest/2018-02-22-e693cd1a-baceb6d5/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-clipandmerge/latest/2018-02-22-e693cd1a-baceb6d5/Singularity
collection: qbicsoftware/qbic-singularity-clipandmerge
---

# qbicsoftware/qbic-singularity-clipandmerge:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-clipandmerge:latest
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

