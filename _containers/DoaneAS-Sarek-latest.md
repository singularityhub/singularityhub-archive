---
id: 10487
name: "DoaneAS/Sarek"
branch: "master"
tag: "latest"
commit: "7f7f2c263377a0885fad7f59b9d832f3e8820488"
version: "295b0ad38e10f57922506ccdd7922ba0"
build_date: "2019-08-06T00:48:34.040Z"
size_mb: 3072.0
size: 1160949791
sif: "https://datasets.datalad.org/shub/DoaneAS/Sarek/latest/2019-08-06-7f7f2c26-295b0ad3/295b0ad38e10f57922506ccdd7922ba0.sif"
url: https://datasets.datalad.org/shub/DoaneAS/Sarek/latest/2019-08-06-7f7f2c26-295b0ad3/
recipe: https://datasets.datalad.org/shub/DoaneAS/Sarek/latest/2019-08-06-7f7f2c26-295b0ad3/Singularity
collection: DoaneAS/Sarek
---

# DoaneAS/Sarek:latest

```bash
$ singularity pull shub://DoaneAS/Sarek:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Maxime Garcia <maxime.garcia@scilifelab.se>
    DESCRIPTION Singularity image containing all requirements for the Sarek pipeline
    VERSION 2.3

%environment
    PATH=/opt/conda/envs/sarek-2.3/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [DoaneAS/Sarek](https://github.com/DoaneAS/Sarek)
 - License: [MIT License](https://api.github.com/licenses/mit)

