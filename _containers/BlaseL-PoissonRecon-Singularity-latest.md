---
id: 7009
name: "BlaseL/PoissonRecon-Singularity"
branch: "master"
tag: "latest"
commit: "71c48f6c53000f6dcdd21a07ee8493cd293c8acc"
version: "ab4dc87eff18f05563c34d3c256fe09f"
build_date: "2019-04-09T21:41:40.417Z"
size_mb: 649
size: 252018719
sif: "https://datasets.datalad.org/shub/BlaseL/PoissonRecon-Singularity/latest/2019-04-09-71c48f6c-ab4dc87e/ab4dc87eff18f05563c34d3c256fe09f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/BlaseL/PoissonRecon-Singularity/latest/2019-04-09-71c48f6c-ab4dc87e/
recipe: https://datasets.datalad.org/shub/BlaseL/PoissonRecon-Singularity/latest/2019-04-09-71c48f6c-ab4dc87e/Singularity
collection: BlaseL/PoissonRecon-Singularity
---

# BlaseL/PoissonRecon-Singularity:latest

```bash
$ singularity pull shub://BlaseL/PoissonRecon-Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
   echo "This container is for Poisson Reconstruction"
   echo "See https://github.com/BlaseL/PoissonRecon for further detail"
   echo "Type: $ PoissonRecon --help for usage instructions"
   /bin/bash

%environment
   PATH=/PoissonRecon/Bin/Linux:$PATH
   export PATH

%post
   echo "Let\'s do some Poisson Reconstruction!"
   apt-get -y update && apt-get -y upgrade
   touch /`date -u -Iseconds`

   apt-get install -y git gcc g++ make bash-completion libpng-dev libjpeg-dev

   git clone https://github.com/BlaseL/PoissonRecon
   cd PoissonRecon
   make poissonrecon
   make chunkply
   export PATH=/PoissonRecon/Bin/Linux/:$PATH

   # in-container bind points for UA HPC shared filesystem
   mkdir -p /extra /xdisk /uaopt /cm /rsgrps

%labels
   MAINTAINER Blase LaSala blasel@email.arizona.edu
   DATE 2019-1-19
   VERSION 0.2
```

## Collection

 - Name: [BlaseL/PoissonRecon-Singularity](https://github.com/BlaseL/PoissonRecon-Singularity)
 - License: None

