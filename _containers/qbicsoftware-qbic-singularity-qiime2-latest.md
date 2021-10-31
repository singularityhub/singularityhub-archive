---
id: 1792
name: "qbicsoftware/qbic-singularity-qiime2"
branch: "master"
tag: "latest"
commit: "859e46c9ff610bdab3b9fb6a450763a60d8be72f"
version: "57e19debfb390b11b99b4c40068c4fac"
build_date: "2018-02-22T14:08:20.967Z"
size_mb: 6596
size: 2846150687
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qiime2/latest/2018-02-22-859e46c9-57e19deb/57e19debfb390b11b99b4c40068c4fac.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-qiime2/latest/2018-02-22-859e46c9-57e19deb/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qiime2/latest/2018-02-22-859e46c9-57e19deb/Singularity
collection: qbicsoftware/qbic-singularity-qiime2
---

# qbicsoftware/qbic-singularity-qiime2:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-qiime2:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:qiime2/core

%post
#/bin/sh build.sh

%files
#Installation of tool
#build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    QIIME2=2018-2
 #   PATH="/usr/bin/miniconda/bin:/usr/bin/miniconda/envs/qiime2-2018.2/bin<module>:$PATH"


%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-qiime2](https://github.com/qbicsoftware/qbic-singularity-qiime2)
 - License: [MIT License](https://api.github.com/licenses/mit)

