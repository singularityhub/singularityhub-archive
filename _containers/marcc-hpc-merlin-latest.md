---
id: 2767
name: "marcc-hpc/merlin"
branch: "master"
tag: "latest"
commit: "aadb494295435b431acade49b6637748a8d3f963"
version: "834a1a81de8a9ff921c1140c67af910d"
build_date: "2020-04-16T23:12:11.859Z"
size_mb: 4114
size: 1794629663
sif: "https://datasets.datalad.org/shub/marcc-hpc/merlin/latest/2020-04-16-aadb4942-834a1a81/834a1a81de8a9ff921c1140c67af910d.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/merlin/latest/2020-04-16-aadb4942-834a1a81/
recipe: https://datasets.datalad.org/shub/marcc-hpc/merlin/latest/2020-04-16-aadb4942-834a1a81/Singularity
collection: marcc-hpc/merlin
---

# marcc-hpc/merlin:latest

```bash
$ singularity pull shub://marcc-hpc/merlin:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/anaconda:5.1.0

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

  # make conda accessible
  PATH=/opt/conda/bin:$PATH
  export PATH

  # use theano cuda 8.0 location but bind in driver libs separately
  LD_LIBRARY_PATH=/usr/local/8.0/nvdriver:/usr/local/8.0/lib64
  export LD_LIBRARY_PATH

  # support MKL threading layer (otherwise the demo will complain)
  export MKL_THREADING_LAYER=GNU

%post
  # locale set, apt-get updates, install editors
  export LC_ALL=C

  apt-get -y update
  apt-get -y install build-essential git python python-pip curl wget autoconf csh cmake unzip lsb-release

  /opt/conda/bin/conda install numpy scipy matplotlib lxml theano pygpu
  /opt/conda/bin/pip install bandmat

  cd opt/
  git clone https://github.com/CSTR-Edinburgh/merlin.git
  cd merlin/tools/
  bash ./compile_tools.sh

  # no overlay support on centos 6, add MARCC directories
  touch /usr/bin/nvidia-smi
  mkdir /scratch /work-zfs /home-0 /home-1 /home-2 /home-3 /home-4

  # this is an existing default assumed by theano so we'll use it too
  mkdir -p /usr/local/8.0
```

## Collection

 - Name: [marcc-hpc/merlin](https://github.com/marcc-hpc/merlin)
 - License: [MIT License](https://api.github.com/licenses/mit)

