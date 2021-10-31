---
id: 6665
name: "icaoberg/singularity-rstudio"
branch: "master"
tag: "latest"
commit: "78d23562ee8a4388ed6e3950ca3be1516525e42e"
version: "fb19ed286a29a8a8aa07e747b2b36908"
build_date: "2020-03-05T14:06:06.682Z"
size_mb: 705
size: 278618143
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-rstudio/latest/2020-03-05-78d23562-fb19ed28/fb19ed286a29a8a8aa07e747b2b36908.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/icaoberg/singularity-rstudio/latest/2020-03-05-78d23562-fb19ed28/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-rstudio/latest/2020-03-05-78d23562-fb19ed28/Singularity
collection: icaoberg/singularity-rstudio
---

# icaoberg/singularity-rstudio:latest

```bash
$ singularity pull shub://icaoberg/singularity-rstudio:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

IncludeCmd: yes

%help
    Container R-base

%runscript
    exec "$@"

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%post
    /usr/bin/apt-get update && /usr/bin/apt-get -y upgrade
    /usr/bin/apt-get update --fix-missing
    /usr/bin/apt-get install -y --no-install-recommends apt-utils
    /usr/bin/apt-get install -y software-properties-common

    # Make folders for CBD HPC cluster
    if [ ! -d /images ]; then mkdir /images; fi
    if [ ! -d /projects ]; then mkdir /containers; fi
    if [ ! -d /containers ]; then mkdir /containers; fi
    if [ ! -d /share ]; then mkdir /share; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi

%appinstall R
    /usr/bin/apt-get install r-base

%appenv R
    BEST_APP=R
    export BEST_APP

%apphelp R
    For more information visit https://www.rdocumentation.org/

%apprun R
    R "$@"

%appinstall Rscript
    /usr/bin/apt-get install r-base

%appenv Rscript
    BEST_APP=Rscript
    export BEST_APP

%apphelp Rscript
    For more information visit https://www.rdocumentation.org/

%apprun Rscript
    Rscript "$@"
```

## Collection

 - Name: [icaoberg/singularity-rstudio](https://github.com/icaoberg/singularity-rstudio)
 - License: None

