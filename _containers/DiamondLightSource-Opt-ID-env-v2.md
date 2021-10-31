---
id: 14173
name: "DiamondLightSource/Opt-ID"
branch: "master"
tag: "env-v2"
commit: "e6ac589e2a530da84797c1cf16936d6af313a746"
version: "bf46aae0b7cd5259530c221a31c801e2cd74a625741f30cd22006ebf01643660"
build_date: "2021-01-15T10:59:50.108Z"
size_mb: 536.59765625
size: 562663424
sif: "https://datasets.datalad.org/shub/DiamondLightSource/Opt-ID/env-v2/2021-01-15-e6ac589e-bf46aae0/bf46aae0b7cd5259530c221a31c801e2cd74a625741f30cd22006ebf01643660.sif"
url: https://datasets.datalad.org/shub/DiamondLightSource/Opt-ID/env-v2/2021-01-15-e6ac589e-bf46aae0/
recipe: https://datasets.datalad.org/shub/DiamondLightSource/Opt-ID/env-v2/2021-01-15-e6ac589e-bf46aae0/Singularity
collection: DiamondLightSource/Opt-ID
---

# DiamondLightSource/Opt-ID:env-v2

```bash
$ singularity pull shub://DiamondLightSource/Opt-ID:env-v2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04
Stage: build

%post
    # Log when this container was built into a .sif file
    CONTAINER_BUILD_DATE=`date`
    echo "export CONTAINER_BUILD_DATE=\"${CONTAINER_BUILD_DATE}\"" >> $SINGULARITY_ENVIRONMENT

    # Update apt-get so we can install python3-pip
    apt update -q
    apt install -y -q software-properties-common
    add-apt-repository universe > /dev/null 2>&1

    # Install build dependencies
    apt update -q
    apt install -y -q build-essential python3-pip libopenmpi-dev openmpi-bin texlive texlive-xetex texlive-fonts-recommended texlive-latex-recommended pandoc

    # Install majority of needed python packages
    pip3 install --no-cache-dir mock pytest numpy h5py mpi4py scipy ruamel.yaml Jinja2 matplotlib pandoc jupyter jupyter_client nbformat nbconvert
    find /usr/lib/python3.*/ -name 'tests' -exec rm -r '{}' +

    # Clean unused packages to make the image smaller
    apt autoremove -y --purge
    apt clean -y
    rm -rf /var/lib/apt/lists/*

%test
    echo "Container was build on ${CONTAINER_BUILD_DATE}"

    # Test that python 3+ and pip3 are installed correctly
    python3 --version && echo "PYTHON3 FOUND" || echo "PYTHON3 NOT FOUND"
    pip3 --version    && echo "PIP3    FOUND" || echo "PIP3    NOT FOUND"

%labels
    Owner   Rosalind Franklin Institute
    Author  joss.whittle@rfi.ac.uk
    Version v2.0

%help
    Provides a base environment for provisioning an ubuntu 20.04 image with pip3.
```

## Collection

 - Name: [DiamondLightSource/Opt-ID](https://github.com/DiamondLightSource/Opt-ID)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

