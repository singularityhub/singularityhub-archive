---
id: 8973
name: "IngSimon/Gittest"
branch: "master"
tag: "latest"
commit: "267c71e67e26553d56e4b2da7639d0fac5a06ab5"
version: "e623fa1d3dd99ed9644147fcf52d47c4"
build_date: "2019-08-24T22:38:46.951Z"
size_mb: 1364
size: 680038431
sif: "https://datasets.datalad.org/shub/IngSimon/Gittest/latest/2019-08-24-267c71e6-e623fa1d/e623fa1d3dd99ed9644147fcf52d47c4.simg"
url: https://datasets.datalad.org/shub/IngSimon/Gittest/latest/2019-08-24-267c71e6-e623fa1d/
recipe: https://datasets.datalad.org/shub/IngSimon/Gittest/latest/2019-08-24-267c71e6-e623fa1d/Singularity
collection: IngSimon/Gittest
---

# IngSimon/Gittest:latest

```bash
$ singularity pull shub://IngSimon/Gittest:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap

OSVersion: stable

MirrorURL: http://ftp.us.debian.org/debian/

%labels


  package.name

  package.version 0.1.0

  package.homepage

  package.source.url

  package.source.mdm5

  package.license GPLv3

%post

    apt-get update

    apt-get -y install python2.7 python-pip

    apt-get -y install python-tk

    apt-get -y install git

    apt-get -y install libgsl-dev
   
    apt-get install python-dev

    pip install numpy

    pip install matplotlib

    pip install emcee

    pip install corner

    pip install pandas

    pip install seaborn

    pip install cython

    pip install pybind11

    pip install autograd

    pip install george

    pip install pyfits

    pip install pywcs
    
    pip install tqdm
    
    git clone https://github.com/dfm/celerite.git

    cd /celerite
    
    python setup.py install
  
    cd /usr/local

    git init

    git clone https://github.com/as595/pyrmsynth.git

    cd pyrmsynth/rm_tools/

    python setup.py build_ext --inplace

    apt-get clean



%runscript

    cd /mnt

    python /usr/local/pyrmsynth/rmsynthesis.py "$@"
```

## Collection

 - Name: [IngSimon/Gittest](https://github.com/IngSimon/Gittest)
 - License: None

