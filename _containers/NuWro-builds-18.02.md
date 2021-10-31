---
id: 1867
name: "NuWro/builds"
branch: "master"
tag: "18.02"
commit: "4a855d0c66a0e68a85486036e57b4ec67fd1c78a"
version: "77b0550c3e82a9cceb248e354391d3d7"
build_date: "2021-02-03T04:46:59.217Z"
size_mb: 1384
size: 421380127
sif: "https://datasets.datalad.org/shub/NuWro/builds/18.02/2021-02-03-4a855d0c-77b0550c/77b0550c3e82a9cceb248e354391d3d7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NuWro/builds/18.02/2021-02-03-4a855d0c-77b0550c/
recipe: https://datasets.datalad.org/shub/NuWro/builds/18.02/2021-02-03-4a855d0c-77b0550c/Singularity
collection: NuWro/builds
---

# NuWro/builds:18.02

```bash
$ singularity pull shub://NuWro/builds:18.02
```

## Singularity Recipe

```singularity
# Ubuntu 14.04 based container with ROOT 5 and NuWro 18.02

BootStrap: shub
From: NuWro/builds:root5

%help
See NuWro User Guide at https://nuwro.github.io/user-guide/

%labels
NuWro 18.02

%post
    export ROOTSYS=/opt/root/
    export PATH=$PATH:$ROOTSYS/bin/
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ROOTSYS/lib/

    ##### INSTALL NuWro #####

    cd /opt/

    # to avoid "Problem with the SSL CA cert (path? access rights?)" 
    update-ca-certificates
    git clone -b nuwro_18.02 --depth 1 https://github.com/NuWro/nuwro.git
    cd nuwro
    make

%runscript
    exec /opt/nuwro/bin/nuwro "$@"
```

## Collection

 - Name: [NuWro/builds](https://github.com/NuWro/builds)
 - License: None

