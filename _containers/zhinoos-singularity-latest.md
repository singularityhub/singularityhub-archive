---
id: 12995
name: "zhinoos/singularity"
branch: "master"
tag: "latest"
commit: "a9dfc05a3570693a55e99a9102c828b23c788ff5"
version: "4fa731df60b71f1eb64c88a3c31c628121519015732c94f28c58f6281c03f653"
build_date: "2020-05-12T14:03:59.580Z"
size_mb: 1646.87109375
size: 1726869504
sif: "https://datasets.datalad.org/shub/zhinoos/singularity/latest/2020-05-12-a9dfc05a-4fa731df/4fa731df60b71f1eb64c88a3c31c628121519015732c94f28c58f6281c03f653.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/zhinoos/singularity/latest/2020-05-12-a9dfc05a-4fa731df/
recipe: https://datasets.datalad.org/shub/zhinoos/singularity/latest/2020-05-12-a9dfc05a-4fa731df/Singularity
collection: zhinoos/singularity
---

# zhinoos/singularity:latest

```bash
$ singularity pull shub://zhinoos/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: library
From: ubuntu:18.04

%post
    # Downloads the latest package lists (important).
    apt -y install software-properties-common
    add-apt-repository universe
    apt-get -y update
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 \
        python3-tk \
	    python3-distutils\
        python3-pip
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*
    # Install Python modules.
    pip3 install setuptools
    pip3 install torch numpy matplotlib
```

## Collection

 - Name: [zhinoos/singularity](https://github.com/zhinoos/singularity)
 - License: None

