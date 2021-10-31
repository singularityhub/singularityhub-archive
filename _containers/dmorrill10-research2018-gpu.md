---
id: 5401
name: "dmorrill10/research2018"
branch: "master"
tag: "gpu"
commit: "26d55be36b9ee1ca64fd5674a380214c15e971d3"
version: "fb5f82c0a49ccc7594b5ab81cfc254fe"
build_date: "2018-11-01T21:55:11.790Z"
size_mb: 3266
size: 1616293919
sif: "https://datasets.datalad.org/shub/dmorrill10/research2018/gpu/2018-11-01-26d55be3-fb5f82c0/fb5f82c0a49ccc7594b5ab81cfc254fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dmorrill10/research2018/gpu/2018-11-01-26d55be3-fb5f82c0/
recipe: https://datasets.datalad.org/shub/dmorrill10/research2018/gpu/2018-11-01-26d55be3-fb5f82c0/Singularity
collection: dmorrill10/research2018
---

# dmorrill10/research2018:gpu

```bash
$ singularity pull shub://dmorrill10/research2018:gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.12.0-rc2-gpu-py3

%help

To install python libraries after this image is built, create a virtual environment that uses the system packages with `virtualenv --system-site-packages venv && source venv/bin/activate`, then use `pip` as usual.


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
  chmod +x /environment

  # default mount paths
  mkdir -p /scratch /data /usr/bin

  apt-get update
  apt-get install ca-certificates curl
  apt-get clean

  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  pip install numpy virtualenv

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [dmorrill10/research2018](https://github.com/dmorrill10/research2018)
 - License: [MIT License](https://api.github.com/licenses/mit)

