---
id: 7847
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "sambamba_0.6.9"
commit: "2841ec235f50c7af78afc7623ab1368eedff2529"
version: "59c100c9c55e3b38c2bfd5d9e022d6b2"
build_date: "2019-12-03T23:40:09.130Z"
size_mb: 129
size: 54075423
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/sambamba_0.6.9/2019-12-03-2841ec23-59c100c9/59c100c9c55e3b38c2bfd5d9e022d6b2.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/sambamba_0.6.9/2019-12-03-2841ec23-59c100c9/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/sambamba_0.6.9/2019-12-03-2841ec23-59c100c9/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:sambamba_0.6.9

```bash
$ singularity pull shub://TomHarrop/singularity-containers:sambamba_0.6.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help

    Container for sambamba 0.6.9
    http://bio-bwa.sourceforge.net/

%labels

    VERSION "sambamba 0.6.9"


%post

    # install dependencies via apt
    apt update
    apt install -y \
        wget

    # download static release from git
    wget \
        -O "sambamba.gz" \
        --no-check-certificate \
        https://github.com/biod/sambamba/releases/download/v0.6.9/sambamba-0.6.9-linux-static.gz
    gunzip sambamba.gz
    chmod 755 sambamba
    mv sambamba /usr/local/bin/


%runscript

    exec /usr/local/bin/sambamba "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

