---
id: 14674
name: "TomHarrop/ont-containers"
branch: "master"
tag: "readfish_14ddf60"
commit: "0195125766f7ac222960cad89e75aa3d3ca5a64c"
version: "3041ac77527e014b710e75cd7a843e0eb861d86442f47b09a1cb7daa28b81c5d"
build_date: "2020-10-20T20:25:09.485Z"
size_mb: 1159.828125
size: 1216167936
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/readfish_14ddf60/2020-10-20-01951257-3041ac77/3041ac77527e014b710e75cd7a843e0eb861d86442f47b09a1cb7daa28b81c5d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/readfish_14ddf60/2020-10-20-01951257-3041ac77/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/readfish_14ddf60/2020-10-20-01951257-3041ac77/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:readfish_14ddf60

```bash
$ singularity pull shub://TomHarrop/ont-containers:readfish_14ddf60
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/ont-containers:minknow_19.12.5

%help
    readfish 14ddf60 from github
    MinKNOW 19.12.5 (MinKNOW core 3.6.5)
    Guppy 3.4.5+fb1fbfb at /guppy/bin
    Loose lab read until API 4973c67

%labels
    MAINTAINER "Tom Harrop"
    VERSION "readfish 14ddf60"

%environment
    export PATH="/guppy/bin:${PATH}"

%post
    export DEBIAN_FRONTEND=noninteractive
    export PATH="/guppy/bin:${PATH}"

    # install dependencies
    apt-get update
    apt-get install -y \
        git \
        libidn11 \
        python3-pip \
        python3.7 \
        python3.7-dev

    # install legacy guppy
    wget \
        -O /guppy.tar.gz \
        --no-check-certificate \
        https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy_3.4.5_linux64.tar.gz
    mkdir /guppy
    tar -zxf /guppy.tar.gz \
        -C /guppy \
        --strip-components 1
    rm -f /guppy.tar.gz

    # configure minion to use GPU
    # it will only work with the exact same version of guppy as guppy core (in minknow -> about)
    # /opt/ont/minknow/bin/config_editor \
    #     --conf application \
    #     --filename /opt/ont/minknow/conf/app_conf \
    #     --set guppy.server_executable="/guppy/bin/guppy_basecall_server" \
    #     --set guppy.client_executable="/guppy/bin/guppy_basecaller" \
    #     --set guppy.gpu_calling=1 \
    #     --set guppy.num_threads=3 \
    #     --set guppy.ipc_threads=2 \
    #     --set guppy.gpu_devices="cuda:0"
    # service minknow stop
    # # pkill guppy_basecall_server
    # service minknow start

    # setup python and install readfish
    /usr/bin/python3.7 -m pip install --upgrade pip setuptools wheel
    /usr/bin/python3.7 -m pip install \
        git+https://github.com/LooseLab/read_until_api_v2@4973c67

    # install readfish from github
    /usr/bin/python3.7 -m pip install \
        git+https://github.com/LooseLab/readfish@14ddf60

%runscript
    exec /usr/local/bin/readfish "@$"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

