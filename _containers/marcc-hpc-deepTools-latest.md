---
id: 989
name: "marcc-hpc/deepTools"
branch: "master"
tag: "latest"
commit: "692c25866e6244e457aacf834f47efefc1465fa3"
version: "096b12b388caa821ad793209406781ba"
build_date: "2020-05-27T14:35:23.227Z"
size_mb: 4173
size: 1204170783
sif: "https://datasets.datalad.org/shub/marcc-hpc/deepTools/latest/2020-05-27-692c2586-096b12b3/096b12b388caa821ad793209406781ba.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/deepTools/latest/2020-05-27-692c2586-096b12b3/
recipe: https://datasets.datalad.org/shub/marcc-hpc/deepTools/latest/2020-05-27-692c2586-096b12b3/Singularity
collection: marcc-hpc/deepTools
---

# marcc-hpc/deepTools:latest

```bash
$ singularity pull shub://marcc-hpc/deepTools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/bgruening/galaxy-deeptools

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir -p /scratch /data 

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/deepTools](https://github.com/marcc-hpc/deepTools)
 - License: None

