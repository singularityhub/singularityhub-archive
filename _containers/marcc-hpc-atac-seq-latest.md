---
id: 1513
name: "marcc-hpc/atac-seq"
branch: "master"
tag: "latest"
commit: "98a61eef2cf19dc76ae1800e5066f78e53e2e125"
version: "a6f2c34a44b0444a227e9ba5300a1be9"
build_date: "2018-01-31T15:33:59.020Z"
size_mb: 2912
size: 1189576735
sif: "https://datasets.datalad.org/shub/marcc-hpc/atac-seq/latest/2018-01-31-98a61eef-a6f2c34a/a6f2c34a44b0444a227e9ba5300a1be9.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/atac-seq/latest/2018-01-31-98a61eef-a6f2c34a/
recipe: https://datasets.datalad.org/shub/marcc-hpc/atac-seq/latest/2018-01-31-98a61eef-a6f2c34a/Singularity
collection: marcc-hpc/atac-seq
---

# marcc-hpc/atac-seq:latest

```bash
$ singularity pull shub://marcc-hpc/atac-seq:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: zhanglab/atac-seq:base

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
  mkdir /scratch /data 

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/atac-seq](https://github.com/marcc-hpc/atac-seq)
 - License: [MIT License](https://api.github.com/licenses/mit)

