---
id: 14430
name: "statiksof/singularity-recipes"
branch: "master"
tag: "jupyter"
commit: "c0ab01c089afa646f5f13ebc2f78191db2165ea1"
version: "50689f9fe403608a575c588e4b2fbc9e0b8557931271c99e8848979a04557e87"
build_date: "2020-10-07T11:22:58.218Z"
size_mb: 230.14453125
size: 241324032
sif: "https://datasets.datalad.org/shub/statiksof/singularity-recipes/jupyter/2020-10-07-c0ab01c0-50689f9f/50689f9fe403608a575c588e4b2fbc9e0b8557931271c99e8848979a04557e87.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/statiksof/singularity-recipes/jupyter/2020-10-07-c0ab01c0-50689f9f/
recipe: https://datasets.datalad.org/shub/statiksof/singularity-recipes/jupyter/2020-10-07-c0ab01c0-50689f9f/Singularity
collection: statiksof/singularity-recipes
---

# statiksof/singularity-recipes:jupyter

```bash
$ singularity pull shub://statiksof/singularity-recipes:jupyter
```

## Singularity Recipe

```singularity
bootstrap: docker
From: ubuntu:xenial

%labels
MAINTAINER statiksof

%post
    # update and install pip
    apt-get -y update
    apt-get -y install python3-pip

    # update pip and install jupyter
    pip3 install --upgrade pip
    pip3 install jupyter
    pip3 install jupyterlab

    # clean apt
    apt-get autoremove -y
    apt-get clean
```

## Collection

 - Name: [statiksof/singularity-recipes](https://github.com/statiksof/singularity-recipes)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

