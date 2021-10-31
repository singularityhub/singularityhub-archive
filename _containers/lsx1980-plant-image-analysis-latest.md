---
id: 10061
name: "lsx1980/plant-image-analysis"
branch: "master"
tag: "latest"
commit: "6939a42243119d373fe4db7f87334db817b3056d"
version: "cb9efff5ccf4fec31c6257a115589594"
build_date: "2021-02-22T23:43:43.266Z"
size_mb: 3442
size: 1845227551
sif: "https://datasets.datalad.org/shub/lsx1980/plant-image-analysis/latest/2021-02-22-6939a422-cb9efff5/cb9efff5ccf4fec31c6257a115589594.simg"
url: https://datasets.datalad.org/shub/lsx1980/plant-image-analysis/latest/2021-02-22-6939a422-cb9efff5/
recipe: https://datasets.datalad.org/shub/lsx1980/plant-image-analysis/latest/2021-02-22-6939a422-cb9efff5/Singularity
collection: lsx1980/plant-image-analysis
---

# lsx1980/plant-image-analysis:latest

```bash
$ singularity pull shub://lsx1980/plant-image-analysis:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer: Suxing Liu
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
    python-numpy \
    python-matplotlib \
    ipython \
    ipython-notebook \
    python-pandas \
    python-sympy \
    python-nose \
    python-scipy \
    python-sklearn \
    python-numexpr \
    python-pip 

  #apt-get install --reinstall unity-gtk-module
  
  pip install --upgrade pip
  
  /usr/local/bin/pip install -U numpy 
  
  /usr/local/bin/pip install scikit-image \
                                scikit-learn \
                                opencv-python \
                                openpyxl \
                                xvfbwrapper


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
   #python requirement.py
```

## Collection

 - Name: [lsx1980/plant-image-analysis](https://github.com/lsx1980/plant-image-analysis)
 - License: None

