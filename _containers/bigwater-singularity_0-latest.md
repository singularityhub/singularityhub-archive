---
id: 15511
name: "bigwater/singularity_0"
branch: "master"
tag: "latest"
commit: "ad1a20d9a4278fa11ad1db18cf49dd3e01d12a09"
version: "ceaee0be273f002f8b266cfd43e180a4"
build_date: "2021-02-10T21:31:28.946Z"
size_mb: 5919.0
size: 3674615839
sif: "https://datasets.datalad.org/shub/bigwater/singularity_0/latest/2021-02-10-ad1a20d9-ceaee0be/ceaee0be273f002f8b266cfd43e180a4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/bigwater/singularity_0/latest/2021-02-10-ad1a20d9-ceaee0be/
recipe: https://datasets.datalad.org/shub/bigwater/singularity_0/latest/2021-02-10-ad1a20d9-ceaee0be/Singularity
collection: bigwater/singularity_0
---

# bigwater/singularity_0:latest

```bash
$ singularity pull shub://bigwater/singularity_0:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    # Downloads the latest package lists (important).
    apt-get update -y
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 \
        python3-tk \
        python3-pip \
        python3-setuptools
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*
    # Install Python modules.
    pip3 install torch numpy matplotlib
```

## Collection

 - Name: [bigwater/singularity_0](https://github.com/bigwater/singularity_0)
 - License: None

