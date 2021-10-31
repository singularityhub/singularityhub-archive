---
id: 10871
name: "icaoberg/singularity-octave"
branch: "master"
tag: "latest"
commit: "058afc47438cf488869fcfc9d213d88b0d2a6eb5"
version: "f82434384e24b1001eebbdf81b5bd7e2"
build_date: "2021-03-16T15:15:19.404Z"
size_mb: 1054.0
size: 373964831
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-octave/latest/2021-03-16-058afc47-f8243438/f82434384e24b1001eebbdf81b5bd7e2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/icaoberg/singularity-octave/latest/2021-03-16-058afc47-f8243438/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-octave/latest/2021-03-16-058afc47-f8243438/Singularity
collection: icaoberg/singularity-octave
---

# icaoberg/singularity-octave:latest

```bash
$ singularity pull shub://icaoberg/singularity-octave:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:latest

IncludeCmd: yes

%labels
    MAINTAINER icaoberg@alumni.cmu.edu
    WEBSITE http://linus.cbd.cs.cmu.edu
    VERSION 1.0

%runscript
    exec /bin/bash "$@"

%post
    echo "Update and upgrade"
    /usr/bin/apt-get update && apt-get install -y --no-install-recommends apt-utils
    /usr/bin/apt-get install -y octave

####################################################################################
%appenv octave
    APP=/usr/bin/octave
    export APP

%apphelp octave
    For more information about goto visit http://www.octave.info

%apprun octave
    octave "$@"
```

## Collection

 - Name: [icaoberg/singularity-octave](https://github.com/icaoberg/singularity-octave)
 - License: None

