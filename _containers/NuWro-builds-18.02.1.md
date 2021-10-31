---
id: 2343
name: "NuWro/builds"
branch: "master"
tag: "18.02.1"
commit: "9621d331be9645666a8313cb7b17825ca957e0c6"
version: "ee8109437a80f0f7243077d20abf2044"
build_date: "2021-03-04T11:49:54.459Z"
size_mb: 1384
size: 421380127
sif: "https://datasets.datalad.org/shub/NuWro/builds/18.02.1/2021-03-04-9621d331-ee810943/ee8109437a80f0f7243077d20abf2044.simg"
url: https://datasets.datalad.org/shub/NuWro/builds/18.02.1/2021-03-04-9621d331-ee810943/
recipe: https://datasets.datalad.org/shub/NuWro/builds/18.02.1/2021-03-04-9621d331-ee810943/Singularity
collection: NuWro/builds
---

# NuWro/builds:18.02.1

```bash
$ singularity pull shub://NuWro/builds:18.02.1
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with ROOT 5 and NuWro 18.02.1

BootStrap: shub
From: NuWro/builds:root5

%help
See NuWro User Guide at https://nuwro.github.io/user-guide/

%labels
NuWro 18.02.1

%post
    export ROOTSYS=/opt/root/
    export PATH=$PATH:$ROOTSYS/bin/
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ROOTSYS/lib/

    ##### INSTALL NuWro #####

    cd /opt/

    # to avoid "Problem with the SSL CA cert (path? access rights?)" 
    update-ca-certificates
    git clone -b nuwro_18.02.1 --depth 1 https://github.com/NuWro/nuwro.git
    cd nuwro
    make

%runscript
    exec /opt/nuwro/bin/nuwro "$@"
```

## Collection

 - Name: [NuWro/builds](https://github.com/NuWro/builds)
 - License: None

