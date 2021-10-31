---
id: 5696
name: "LokiLuciferase/exoseq"
branch: "dev"
tag: "latest"
commit: "cc11f6a4b9492f516430468f237e9600fad889f7"
version: "b59233ec18e6830c251809761fcb236f"
build_date: "2018-11-24T04:49:43.606Z"
size_mb: 3350
size: 1352269855
sif: "https://datasets.datalad.org/shub/LokiLuciferase/exoseq/latest/2018-11-24-cc11f6a4-b59233ec/b59233ec18e6830c251809761fcb236f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/LokiLuciferase/exoseq/latest/2018-11-24-cc11f6a4-b59233ec/
recipe: https://datasets.datalad.org/shub/LokiLuciferase/exoseq/latest/2018-11-24-cc11f6a4-b59233ec/Singularity
collection: LokiLuciferase/exoseq
---

# LokiLuciferase/exoseq:latest

```bash
$ singularity pull shub://LokiLuciferase/exoseq:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Lukas Lueftinger  <lukas.lueftinger@imp.ac.at>
    DESCRIPTION Container image containing all requirements for the nf-core/exoseq pipeline
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/nfcore-exoseq-1.0dev/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [LokiLuciferase/exoseq](https://github.com/LokiLuciferase/exoseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

