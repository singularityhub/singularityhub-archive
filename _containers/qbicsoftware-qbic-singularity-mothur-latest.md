---
id: 1781
name: "qbicsoftware/qbic-singularity-mothur"
branch: "master"
tag: "latest"
commit: "a1ca7720f1a73e7842dae901b20901e987d0582c"
version: "4659caf5a3c96a897fa95531edf708e5"
build_date: "2018-02-22T10:18:07.750Z"
size_mb: 492
size: 199901215
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-mothur/latest/2018-02-22-a1ca7720-4659caf5/4659caf5a3c96a897fa95531edf708e5.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-mothur/latest/2018-02-22-a1ca7720-4659caf5/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-mothur/latest/2018-02-22-a1ca7720-4659caf5/Singularity
collection: qbicsoftware/qbic-singularity-mothur
---

# qbicsoftware/qbic-singularity-mothur:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-mothur:latest
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

