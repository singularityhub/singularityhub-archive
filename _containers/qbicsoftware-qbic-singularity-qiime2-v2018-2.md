---
id: 1793
name: "qbicsoftware/qbic-singularity-qiime2"
branch: "master"
tag: "v2018-2"
commit: "859e46c9ff610bdab3b9fb6a450763a60d8be72f"
version: "16458f7990cc3bdc9d9987b518bce9f9"
build_date: "2020-09-14T12:50:21.553Z"
size_mb: 6596
size: 2846150687
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qiime2/v2018-2/2020-09-14-859e46c9-16458f79/16458f7990cc3bdc9d9987b518bce9f9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-qiime2/v2018-2/2020-09-14-859e46c9-16458f79/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qiime2/v2018-2/2020-09-14-859e46c9-16458f79/Singularity
collection: qbicsoftware/qbic-singularity-qiime2
---

# qbicsoftware/qbic-singularity-qiime2:v2018-2

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-qiime2:v2018-2
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

