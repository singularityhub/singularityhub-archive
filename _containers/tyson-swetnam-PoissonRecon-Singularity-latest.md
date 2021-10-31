---
id: 4051
name: "tyson-swetnam/PoissonRecon-Singularity"
branch: "master"
tag: "latest"
commit: "3c37d2b34ec4c1c83b643d0722f5a587b661d013"
version: "742bf4d51541d76292097736cb0a065c"
build_date: "2020-02-06T16:44:24.283Z"
size_mb: 918
size: 305721375
sif: "https://datasets.datalad.org/shub/tyson-swetnam/PoissonRecon-Singularity/latest/2020-02-06-3c37d2b3-742bf4d5/742bf4d51541d76292097736cb0a065c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tyson-swetnam/PoissonRecon-Singularity/latest/2020-02-06-3c37d2b3-742bf4d5/
recipe: https://datasets.datalad.org/shub/tyson-swetnam/PoissonRecon-Singularity/latest/2020-02-06-3c37d2b3-742bf4d5/Singularity
collection: tyson-swetnam/PoissonRecon-Singularity
---

# tyson-swetnam/PoissonRecon-Singularity:latest

```bash
$ singularity pull shub://tyson-swetnam/PoissonRecon-Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
   echo "This container is for Poisson Reconstruction"
   echo "See https://github.com/mkazhdan/PoissonRecon for further detail"
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

   git clone https://github.com/mkazhdan/PoissonRecon
   cd PoissonRecon
   make all
   export PATH=/PoissonRecon/Bin/Linux/:$PATH

   # in-container bind points for UA HPC shared filesystem
   mkdir -p /extra /xdisk /uaopt /cm/shared /rsgrps

%labels
   MAINTAINER Tyson Lee Swetnam tswetnam@cyverse.org
   DATE 2018-10-10
   VERSION 0.2
```

## Collection

 - Name: [tyson-swetnam/PoissonRecon-Singularity](https://github.com/tyson-swetnam/PoissonRecon-Singularity)
 - License: None

