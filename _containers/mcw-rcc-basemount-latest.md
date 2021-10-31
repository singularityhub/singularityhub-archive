---
id: 5964
name: "mcw-rcc/basemount"
branch: "master"
tag: "latest"
commit: "9f514d2b6ceeacb5ddc0bafc0ca5381c864289cd"
version: "223a7db7b0dec28dab254ca87b3caba0"
build_date: "2018-12-14T05:20:15.395Z"
size_mb: 449
size: 167596063
sif: "https://datasets.datalad.org/shub/mcw-rcc/basemount/latest/2018-12-14-9f514d2b-223a7db7/223a7db7b0dec28dab254ca87b3caba0.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/basemount/latest/2018-12-14-9f514d2b-223a7db7/
recipe: https://datasets.datalad.org/shub/mcw-rcc/basemount/latest/2018-12-14-9f514d2b-223a7db7/Singularity
collection: mcw-rcc/basemount
---

# mcw-rcc/basemount:latest

```bash
$ singularity pull shub://mcw-rcc/basemount:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version v1.0

%help
This container runs Basemount.

%post
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # Install necessary packages.
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        ca-certificates \
        zlib1g-dev \
        libssl-dev \
        curl \
        wget
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    bash -c "$(curl -L https://basemount.basespace.illumina.com/install)"
    wget "https://api.bintray.com/content/basespace/BaseSpaceCLI-EarlyAccess-BIN/latest/\$latest/amd64-linux/bs?bt_package=latest" -O /usr/local/bin/bs && chmod +x /usr/local/bin/bs
    wget "https://api.bintray.com/content/basespace/BaseSpace-Copy-BIN/\$latest/linux/bscp?bt_package=develop" -O /usr/local/bin/bs-cp && chmod +x /usr/local/bin/bs-cp
```

## Collection

 - Name: [mcw-rcc/basemount](https://github.com/mcw-rcc/basemount)
 - License: [MIT License](https://api.github.com/licenses/mit)

