---
id: 1103
name: "NuWro/builds"
branch: "master"
tag: "17.09"
commit: "97d9e845276a40bd8d120666898e1f30e42cf537"
version: "5e73f4254385d51e4cded541ee7b04e7"
build_date: "2021-02-05T15:55:49.441Z"
size_mb: 1424
size: 418443295
sif: "https://datasets.datalad.org/shub/NuWro/builds/17.09/2021-02-05-97d9e845-5e73f425/5e73f4254385d51e4cded541ee7b04e7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NuWro/builds/17.09/2021-02-05-97d9e845-5e73f425/
recipe: https://datasets.datalad.org/shub/NuWro/builds/17.09/2021-02-05-97d9e845-5e73f425/Singularity
collection: NuWro/builds
---

# NuWro/builds:17.09

```bash
$ singularity pull shub://NuWro/builds:17.09
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with ROOT 5 and NuWro 17.09

BootStrap: shub
From: NuWro/builds:root5

%help
See NuWro User Guide at https://nuwro.github.io/user-guide/

%labels
NuWro 17.09

%post
    export ROOTSYS=/opt/root/
    export PATH=$PATH:$ROOTSYS/bin/
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ROOTSYS/lib/

    ##### INSTALL NuWro #####

    cd /opt/

    # to avoid "Problem with the SSL CA cert (path? access rights?)" 
    update-ca-certificates
    git clone -b nuwro_17.09 --depth 1 https://github.com/NuWro/nuwro.git
    cd nuwro
    make

%runscript
    exec /opt/nuwro/bin/nuwro "$@"
```

## Collection

 - Name: [NuWro/builds](https://github.com/NuWro/builds)
 - License: None

