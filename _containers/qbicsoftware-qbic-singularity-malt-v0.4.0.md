---
id: 1868
name: "qbicsoftware/qbic-singularity-malt"
branch: "master"
tag: "v0.4.0"
commit: "9088bfc4c9d7c419e78d0da68851c52caaa81235"
version: "8614b0378862c6cac2feddc274023a7b"
build_date: "2018-02-26T19:44:16.672Z"
size_mb: 556
size: 244863007
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-malt/v0.4.0/2018-02-26-9088bfc4-8614b037/8614b0378862c6cac2feddc274023a7b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/qbicsoftware/qbic-singularity-malt/v0.4.0/2018-02-26-9088bfc4-8614b037/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-malt/v0.4.0/2018-02-26-9088bfc4-8614b037/Singularity
collection: qbicsoftware/qbic-singularity-malt
---

# qbicsoftware/qbic-singularity-malt:v0.4.0

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-malt:v0.4.0
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:16.04

%post
/bin/sh build.sh

%files
#Installation of tool
build.sh

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    MALT_VERSION=v0_4_0

%runscript
exec malt-run "$@"

%test
java -version

%labels
Maintainer  sven.fillinger@qbic.uni-tuebingen.de+
Organization    Quantitative Biology Center (QBiC)
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-malt](https://github.com/qbicsoftware/qbic-singularity-malt)
 - License: [MIT License](https://api.github.com/licenses/mit)

