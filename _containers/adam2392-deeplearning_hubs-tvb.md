---
id: 3478
name: "adam2392/deeplearning_hubs"
branch: "tvb"
tag: "tvb"
commit: "a1f1e9664e45f967cfa85dd2c27a31296933accd"
version: "0f65d0181b518057ecd44c641d0c97ef"
build_date: "2019-08-14T22:45:41.212Z"
size_mb: 2939
size: 1166831647
sif: "https://datasets.datalad.org/shub/adam2392/deeplearning_hubs/tvb/2019-08-14-a1f1e966-0f65d018/0f65d0181b518057ecd44c641d0c97ef.simg"
url: https://datasets.datalad.org/shub/adam2392/deeplearning_hubs/tvb/2019-08-14-a1f1e966-0f65d018/
recipe: https://datasets.datalad.org/shub/adam2392/deeplearning_hubs/tvb/2019-08-14-a1f1e966-0f65d018/Singularity
collection: adam2392/deeplearning_hubs
---

# adam2392/deeplearning_hubs:tvb

```bash
$ singularity pull shub://adam2392/deeplearning_hubs:tvb
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

  # expose conda
  PATH="/opt/conda/bin:$PATH"
  export PATH
  #PATH=/opt/conda/envs/pytorch-py3.6/bin:$PATH
%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # load environment variables
  . /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths, files
  mkdir /scratch /data /work-zfs 
  
  # post-setup script
  # apk update && apk add bash
  # apt-get update
  # apt-get install -y wget
  # apt-get install -y bzip2
  # apt-get install -y vim

  conda update -y conda

  # user requests (contact marcc-help@marcc.jhu.edu)
  # conda create -n tvb python=2 && source activate tvb
  conda install nomkl numpy numexpr numba matplotlib scipy cython scikit-learn pandas
  conda install -c anaconda numpy pytest flake8 natsort
  conda install -c conda-forge tvb-gdist psutil networkx nibabel nilearn mne seaborn SALib mako

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command
  conda env list
  source activate tvb

%test
  # test that script is a success
```

## Collection

 - Name: [adam2392/deeplearning_hubs](https://github.com/adam2392/deeplearning_hubs)
 - License: [Other](None)

