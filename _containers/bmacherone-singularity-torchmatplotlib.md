---
id: 9587
name: "bmacherone/singularity"
branch: "master"
tag: "torchmatplotlib"
commit: "190d3a9ce4693ad0d5bfa425f45faf123a15bbf0"
version: "7e279845b48fa2308f351a5ad3c78a9f"
build_date: "2019-06-05T18:27:51.234Z"
size_mb: 2187
size: 1474228255
sif: "https://datasets.datalad.org/shub/bmacherone/singularity/torchmatplotlib/2019-06-05-190d3a9c-7e279845/7e279845b48fa2308f351a5ad3c78a9f.simg"
url: https://datasets.datalad.org/shub/bmacherone/singularity/torchmatplotlib/2019-06-05-190d3a9c-7e279845/
recipe: https://datasets.datalad.org/shub/bmacherone/singularity/torchmatplotlib/2019-06-05-190d3a9c-7e279845/Singularity
collection: bmacherone/singularity
---

# bmacherone/singularity:torchmatplotlib

```bash
$ singularity pull shub://bmacherone/singularity:torchmatplotlib
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04
# torch matplotlib test environment

%post
    # download the latest package lists
    apt-get update -y
    
    # python3-tk, python3-cairo are required by matplotlib
    DEBIAN_FRONTEND=noninteractive

    apt-get install -y --no-install-recommends \
        python3 \
        python3-tk \
        python3-pip \
	python3-cairo

    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*
    
    # Install Python modules.
    pip3 install torch numpy matplotlib
```

## Collection

 - Name: [bmacherone/singularity](https://github.com/bmacherone/singularity)
 - License: None

