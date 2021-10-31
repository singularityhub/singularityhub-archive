---
id: 1782
name: "qbicsoftware/qbic-singularity-mothur"
branch: "master"
tag: "v1.39.5"
commit: "7f13ef87081623292fb027145f6779b6b3bb1e5e"
version: "d1f2043925fa8eea0fe7ffee362de58e"
build_date: "2018-02-22T10:18:07.741Z"
size_mb: 492
size: 199901215
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-mothur/v1.39.5/2018-02-22-7f13ef87-d1f20439/d1f2043925fa8eea0fe7ffee362de58e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-mothur/v1.39.5/2018-02-22-7f13ef87-d1f20439/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-mothur/v1.39.5/2018-02-22-7f13ef87-d1f20439/Singularity
collection: qbicsoftware/qbic-singularity-mothur
---

# qbicsoftware/qbic-singularity-mothur:v1.39.5

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-mothur:v1.39.5
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%post
/bin/sh build.sh
wget https://github.com/mothur/mothur/releases/download/v1.39.5/Mothur.linux_64.noReadLine.zip
unzip Mothur.linux_64.noReadLine.zip
rm Mothur.linux_64.noReadLine.zip
mv /mothur/blast/bin/* /usr/local/bin/
mv /mothur/* /usr/local/bin/

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    MOTHUR=v1.39.5

%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-mothur](https://github.com/qbicsoftware/qbic-singularity-mothur)
 - License: [MIT License](https://api.github.com/licenses/mit)

