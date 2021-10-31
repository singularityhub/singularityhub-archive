---
id: 12997
name: "zhinoos/singularity"
branch: "master"
tag: "ver2"
commit: "6209c754eda80bbef4918ff0ccb9d14a50566c71"
version: "0204e732f5814dc350f88cdf3b15019624d799162acf30b9f5e184fb01a3cf04"
build_date: "2020-05-19T08:35:01.883Z"
size_mb: 3506.90234375
size: 3677253632
sif: "https://datasets.datalad.org/shub/zhinoos/singularity/ver2/2020-05-19-6209c754-0204e732/0204e732f5814dc350f88cdf3b15019624d799162acf30b9f5e184fb01a3cf04.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/zhinoos/singularity/ver2/2020-05-19-6209c754-0204e732/
recipe: https://datasets.datalad.org/shub/zhinoos/singularity/ver2/2020-05-19-6209c754-0204e732/Singularity
collection: zhinoos/singularity
---

# zhinoos/singularity:ver2

```bash
$ singularity pull shub://zhinoos/singularity:ver2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    # Downloads the latest package lists (important).
    #sudo apt-get install software-properties-common
    #apt -y install python-software-properties
    #add-apt-repository universe
    apt-get -y update
    #add-apt-repository universe
    #apt-get install python-software-properties
    
    
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

