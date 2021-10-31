---
id: 9911
name: "Computational-Plant-Science/HairyRoots"
branch: "master"
tag: "latest"
commit: "dc13d4a2911250041f667eb2654abb0455ca060a"
version: "c5cfca09f92bc3114ee50f387d5b440b"
build_date: "2019-06-24T14:47:57.070Z"
size_mb: 3337
size: 1788383263
sif: "https://datasets.datalad.org/shub/Computational-Plant-Science/HairyRoots/latest/2019-06-24-dc13d4a2-c5cfca09/c5cfca09f92bc3114ee50f387d5b440b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Computational-Plant-Science/HairyRoots/latest/2019-06-24-dc13d4a2-c5cfca09/
recipe: https://datasets.datalad.org/shub/Computational-Plant-Science/HairyRoots/latest/2019-06-24-dc13d4a2-c5cfca09/Singularity
collection: Computational-Plant-Science/HairyRoots
---

# Computational-Plant-Science/HairyRoots:latest

```bash
$ singularity pull shub://Computational-Plant-Science/HairyRoots:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer: Peter
  Version v1.01

%setup
  #----------------------------------------------------------------------
  # commands to be executed on host outside container during bootstrap
  #----------------------------------------------------------------------
  mkdir ${SINGULARITY_ROOTFS}/opt/code/

%files
  ./* /opt/code/

%post
  #----------------------------------------------------------
  # Install common dependencies and create default entrypoint,
  # commands to be executed inside container during bootstrap
  #----------------------------------------------------------
  # Install dependencies
  apt update
  apt install -y \
    build-essential \
    python3 \
    python-setuptools \
    python-scipy \
    python-matplotlib \
    ipython \
    ipython-notebook \
    python-pandas \
    python-sympy \
    python-pip \
    python-nose \
    python-numpy \
    python-sklearn \
    python-pil \
    

  pip install --upgrade pip
  
  /usr/local/bin/pip install -U numpy 
  
  /usr/local/bin/pip install scikit-image \
                                scikit-learn \
                                networkx \
                                pillow


  mkdir /lscratch /db /work /scratch
  
  chmod -R a+rwx /opt/code/
  
%environment
  #----------------------------------------------------------
  # Setup environment variables
  #----------------------------------------------------------
  PYTHONPATH=$PYTHONPATH:/opt/code/
  export PATH
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/code/
  export LD_LIBRARY_PATH

%runscript
  #----------------------------------------------------------
  # Run scripts inside container
  #----------------------------------------------------------
   # commands to be executed when the container runs
   echo "Arguments received: $*"
   exec /usr/bin/python "$@"
  
%test
  #----------------------------------------------------------
  # commands to be executed within container at close of bootstrap process
  #----------------------------------------------------------
   python --version
```

## Collection

 - Name: [Computational-Plant-Science/HairyRoots](https://github.com/Computational-Plant-Science/HairyRoots)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

