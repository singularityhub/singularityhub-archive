---
id: 5740
name: "mcw-rcc/anvio"
branch: "5.2"
tag: "5.2"
commit: "40c195c9484a2eb80f0ed1a6f186ed38058dea32"
version: "c8831dbd6045c18dcd1cc071b7aa8f8e"
build_date: "2019-12-13T08:22:37.887Z"
size_mb: 1359
size: 443060255
sif: "https://datasets.datalad.org/shub/mcw-rcc/anvio/5.2/2019-12-13-40c195c9-c8831dbd/c8831dbd6045c18dcd1cc071b7aa8f8e.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/anvio/5.2/2019-12-13-40c195c9-c8831dbd/
recipe: https://datasets.datalad.org/shub/mcw-rcc/anvio/5.2/2019-12-13-40c195c9-c8831dbd/Singularity
collection: mcw-rcc/anvio
---

# mcw-rcc/anvio:5.2

```bash
$ singularity pull shub://mcw-rcc/anvio:5.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: meren/anvio:5.2

%labels
Maintainer Matthew Flister
Version 11.29.18

%help
This container runs anvi'o 5.2.

%environment
    SHELL=/bin/bash

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    anvi-setup-ncbi-cogs
```

## Collection

 - Name: [mcw-rcc/anvio](https://github.com/mcw-rcc/anvio)
 - License: [MIT License](https://api.github.com/licenses/mit)

