---
id: 8543
name: "SysBioChalmers/rnaseq"
branch: "hebbe"
tag: "hebbe"
commit: "aa871ae163e77e6720a25d2af268b35346c5beeb"
version: "8830c7a29a61f255c5afadcccd99680d"
build_date: "2019-12-13T16:41:22.231Z"
size_mb: 3342
size: 1072554015
sif: "https://datasets.datalad.org/shub/SysBioChalmers/rnaseq/hebbe/2019-12-13-aa871ae1-8830c7a2/8830c7a29a61f255c5afadcccd99680d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/SysBioChalmers/rnaseq/hebbe/2019-12-13-aa871ae1-8830c7a2/
recipe: https://datasets.datalad.org/shub/SysBioChalmers/rnaseq/hebbe/2019-12-13-aa871ae1-8830c7a2/Singularity
collection: SysBioChalmers/rnaseq
---

# SysBioChalmers/rnaseq:hebbe

```bash
$ singularity pull shub://SysBioChalmers/rnaseq:hebbe
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Phil Ewels <phil.ewels@scilifelab.se>
    DESCRIPTION Singularity image containing all requirements for the nf-core/rnaseq pipeline
    VERSION 1.1

%environment
    PATH=/opt/conda/envs/nf-core-rnaseq-1.1/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
    mkdir -p /c3se
    mkdir -p /local
    mkdir -p /apps
    mkdir -p /priv
    mkdir -p /usr/share/lmod/lmod
    mkdir -p /var/hasplm
    mkdir -p /var/opt/thinlinc
    mkdir -p /usr/lib64
    touch /usr/lib64/libdlfaker.so
    touch /usr/lib64/libvglfaker.so
    touch /usr/bin/nvidia-smi
```

## Collection

 - Name: [SysBioChalmers/rnaseq](https://github.com/SysBioChalmers/rnaseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

