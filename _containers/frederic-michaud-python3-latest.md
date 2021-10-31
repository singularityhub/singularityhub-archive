---
id: 5387
name: "frederic-michaud/python3"
branch: "master"
tag: "latest"
commit: "e6f95afea68daf4e8cb63f696cb52797df9004aa"
version: "fe67923d1f156b99367972d8779bf56a"
build_date: "2020-04-19T22:35:26.095Z"
size_mb: 966
size: 405512223
sif: "https://datasets.datalad.org/shub/frederic-michaud/python3/latest/2020-04-19-e6f95afe-fe67923d/fe67923d1f156b99367972d8779bf56a.simg"
url: https://datasets.datalad.org/shub/frederic-michaud/python3/latest/2020-04-19-e6f95afe-fe67923d/
recipe: https://datasets.datalad.org/shub/frederic-michaud/python3/latest/2020-04-19-e6f95afe-fe67923d/Singularity
collection: frederic-michaud/python3
---

# frederic-michaud/python3:latest

```bash
$ singularity pull shub://frederic-michaud/python3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu 

%help



%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post

  apt-get update
  apt-get install -y python3 python3-pip git
  apt-get clean
  pip3 install numpy matplotlib sklearn 
  pip3 install scikit-bio
  pip3 install astropy
  pip3 install numpy
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command
```

## Collection

 - Name: [frederic-michaud/python3](https://github.com/frederic-michaud/python3)
 - License: None

