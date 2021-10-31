---
id: 12788
name: "TomHarrop/variant-utils"
branch: "master"
tag: "easysfs_c2b26c5"
commit: "d4b8b1b9b4e5913389382e1d34960d1f44af5961"
version: "f0b1c194c1370d4deeb893f3a71433231469dc115833bdbc35e2ee43096e0c82"
build_date: "2020-04-30T23:22:14.432Z"
size_mb: 449.26171875
size: 471085056
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/easysfs_c2b26c5/2020-04-30-d4b8b1b9-f0b1c194/f0b1c194c1370d4deeb893f3a71433231469dc115833bdbc35e2ee43096e0c82.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/easysfs_c2b26c5/2020-04-30-d4b8b1b9-f0b1c194/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/easysfs_c2b26c5/2020-04-30-d4b8b1b9-f0b1c194/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:easysfs_c2b26c5

```bash
$ singularity pull shub://TomHarrop/variant-utils:easysfs_c2b26c5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:2.7.18-buster

%help
    Container for easysfs c2b26c5

%labels
    VERSION "easysfs c2b26c5"

%environment
    export PATH="/easysfs:${PATH}"
    export LC_ALL=C

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    apt-get update
    apt-get install -y \
        build-essential

    /usr/local/bin/pip install \
        matplotlib==2.2.5 \
        numpy==1.16.6 \
        pandas==0.24.2 \
        scipy==1.2.3

    /usr/local/bin/pip install \
        dadi==2.0.5

    git clone \
        https://github.com/isaacovercast/easySFS.git \
        /easysfs
    (
    cd /easysfs || exit 1
    git checkout -f c2b26c5
    git submodule update --init --recursive
    chmod 755 easySFS.py
    )


%runscript
    exec /easysfs/easySFS.py "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

