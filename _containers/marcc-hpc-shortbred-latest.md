---
id: 1704
name: "marcc-hpc/shortbred"
branch: "master"
tag: "latest"
commit: "47ed95063dc07a27a5ca4d4299e0d5129b7a7a0e"
version: "4262adbb8371829bb4cbb513291eb606"
build_date: "2020-07-14T11:29:27.481Z"
size_mb: 2342
size: 1094397983
sif: "https://datasets.datalad.org/shub/marcc-hpc/shortbred/latest/2020-07-14-47ed9506-4262adbb/4262adbb8371829bb4cbb513291eb606.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/shortbred/latest/2020-07-14-47ed9506-4262adbb/
recipe: https://datasets.datalad.org/shub/marcc-hpc/shortbred/latest/2020-07-14-47ed9506-4262adbb/Singularity
collection: marcc-hpc/shortbred
---

# marcc-hpc/shortbred:latest

```bash
$ singularity pull shub://marcc-hpc/shortbred:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: biobakery/shortbred:latest

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

  # use bash as default shell and prepend /scratch/bin to PATH
  echo 'SHELL=/bin/bash' >> /environment
  echo 'PATH=/scratch/bin:$PATH' >> /environment
  echo 'export PATH' >> /environment
  echo '. /home/linuxbrew/.profile' >> /environment
  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /scratch /data 

%apprun identify
  exec shortbred_identify.py "$@"
  
%apprun quantify
  exec shortbred_quantify.py "$@" 
  
%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/shortbred](https://github.com/marcc-hpc/shortbred)
 - License: None

