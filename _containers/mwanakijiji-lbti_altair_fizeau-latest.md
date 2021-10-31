---
id: 14205
name: "mwanakijiji/lbti_altair_fizeau"
branch: "hpc_lambda_over_B"
tag: "latest"
commit: "93414cc95e7e153a64113c7db294e9fac59a9c4a"
version: "9812c46a02e7fb8e16a68f820c4fa3fd"
build_date: "2020-09-23T01:18:56.058Z"
size_mb: 1446.0
size: 568397855
sif: "https://datasets.datalad.org/shub/mwanakijiji/lbti_altair_fizeau/latest/2020-09-23-93414cc9-9812c46a/9812c46a02e7fb8e16a68f820c4fa3fd.sif"
url: https://datasets.datalad.org/shub/mwanakijiji/lbti_altair_fizeau/latest/2020-09-23-93414cc9-9812c46a/
recipe: https://datasets.datalad.org/shub/mwanakijiji/lbti_altair_fizeau/latest/2020-09-23-93414cc9-9812c46a/Singularity
collection: mwanakijiji/lbti_altair_fizeau
---

# mwanakijiji/lbti_altair_fizeau:latest

```bash
$ singularity pull shub://mwanakijiji/lbti_altair_fizeau:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.6.6

# copy files required for the app to run
%setup
  mkdir -p ${SINGULARITY_ROOTFS}/modules
  mkdir -p ${SINGULARITY_ROOTFS}/vol_c/180507_fizeau_altair

%files
  requirements.txt /
  altair_pipeline.py /
  # copy Python modules
  modules/*py /modules/
  # copy config file
  modules/*ini /modules/
  # kludge: this file is used as an initial template in the pipeline
  ## ## needs to change later!
  lm_180507_009030.fits /

%environment
  # set environment variable to retrieve new image each time
  export SINGULARITY_DISABLE_CACHE=True

%post
  # install pip
  apt-get update
  apt-get install -y python3-pip
  pip install -U pip
  # get dependencies
  pip install -r requirements.txt

# run the application (step not necessary if the verbose version
# of the command is in the PBS file)

%runscript
  echo "Runscript; Python version is"
  python --version
  #exec /bin/bash python3 /usr/src/app/altair_pipeline.py "$@"
%startscript
  echo "Startscript"
  #exec /bin/bash python3 /usr/src/app/altair_pipeline.py "$@"
```

## Collection

 - Name: [mwanakijiji/lbti_altair_fizeau](https://github.com/mwanakijiji/lbti_altair_fizeau)
 - License: [MIT License](https://api.github.com/licenses/mit)

