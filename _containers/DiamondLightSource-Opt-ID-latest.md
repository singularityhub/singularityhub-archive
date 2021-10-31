---
id: 14172
name: "DiamondLightSource/Opt-ID"
branch: "master"
tag: "latest"
commit: "e6ac589e2a530da84797c1cf16936d6af313a746"
version: "01ea0c38841e1d66441b32f64be914df0030c97401588834cadbf4b1a8f034cd"
build_date: "2021-01-05T12:14:57.435Z"
size_mb: 536.609375
size: 562675712
sif: "https://datasets.datalad.org/shub/DiamondLightSource/Opt-ID/latest/2021-01-05-e6ac589e-01ea0c38/01ea0c38841e1d66441b32f64be914df0030c97401588834cadbf4b1a8f034cd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/DiamondLightSource/Opt-ID/latest/2021-01-05-e6ac589e-01ea0c38/
recipe: https://datasets.datalad.org/shub/DiamondLightSource/Opt-ID/latest/2021-01-05-e6ac589e-01ea0c38/Singularity
collection: DiamondLightSource/Opt-ID
---

# DiamondLightSource/Opt-ID:latest

```bash
$ singularity pull shub://DiamondLightSource/Opt-ID:latest
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

