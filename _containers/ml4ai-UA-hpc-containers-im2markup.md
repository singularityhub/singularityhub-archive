---
id: 6651
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "im2markup"
commit: "975fbb1d8508925b3ad8d0e6edc02173d33ced50"
version: "03312a1eb6b591d8328d00925b33f2dd"
build_date: "2021-02-17T13:35:09.789Z"
size_mb: 6904
size: 2402938911
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/im2markup/2021-02-17-975fbb1d-03312a1e/03312a1eb6b591d8328d00925b33f2dd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ml4ai/UA-hpc-containers/im2markup/2021-02-17-975fbb1d-03312a1e/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/im2markup/2021-02-17-975fbb1d-03312a1e/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:im2markup

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:im2markup
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ml4ai/UA-hpc-containers:torch

%help
  This container is built on top of the ML4AI Torch container. It includes additional pre-reqs needed to preprocess/train/evaluate using Harvards im2markup tool

%setup
  # Place any commands here that need to be executed on the host OS (i.e. the HPC shell) after the base of the container is made, but before the post section.

%files
  # Use this section to copy any files from the host OS to the container during the build (don't use this if building on singularity-hub)

%labels
  Maintainer ML4AI Lab
  Version v0.1

%environment
  # Use this section to add any environment variables that will be needed in the container. (Be sure to add an export {<var-name>}* command for any environment variables defined here so they are seen by the container)

%post
  apt-get -y update

  # Installing some Python packages that are needed for pre-processing
  apt-get -y install python3 python3-pip python3-matplotlib python3-numpy
  pip3 install pillow numpy python-Levenshtein
  wget http://lstm.seas.harvard.edu/latex/third_party/Distance-0.1.3.tar.gz
  tar zxf Distance-0.1.3.tar.gz
  cd /distance
  python3 setup.py install
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

