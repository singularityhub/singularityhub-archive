---
id: 3595
name: "ResearchIT/singularity-keras"
branch: "master"
tag: "2"
commit: "759d746e3c79087d0f878a5c2e8e684bf6557011"
version: "2bb629c06b6b604c475ff68546aea7ed"
build_date: "2018-07-18T23:19:18.884Z"
size_mb: 7023
size: 3139608607
sif: "https://datasets.datalad.org/shub/ResearchIT/singularity-keras/2/2018-07-18-759d746e-2bb629c0/2bb629c06b6b604c475ff68546aea7ed.simg"
url: https://datasets.datalad.org/shub/ResearchIT/singularity-keras/2/2018-07-18-759d746e-2bb629c0/
recipe: https://datasets.datalad.org/shub/ResearchIT/singularity-keras/2/2018-07-18-759d746e-2bb629c0/Singularity
collection: ResearchIT/singularity-keras
---

# ResearchIT/singularity-keras:2

```bash
$ singularity pull shub://ResearchIT/singularity-keras:2
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:nvidia/cuda:9.0-cudnn7-devel-centos7

%environment
export KERAS_BACKEND=tensorflow
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64

%post
yum update -y
yum install -y @"Development Tools"
yum install -y epel-release
yum install -y libgomp cmake3 vim cuda-9.0 cuda-drivers xorg-x11-drv-nvidia-cuda
yum install -y git gcc-c++ sudo curl openblas lapack python36 wget python-devel python36-devel R-core R-devel R-Rcpp R-Rcpp-devel openssl-devel curl-devel
wget https://bootstrap.pypa.io/get-pip.py
python36 get-pip.py
python2 get-pip.py
python36 -m pip install tensorflow-gpu
python36 -m pip install keras pillow
python2 -m pip install tensorflow-gpu
python2 -m pip install keras pillow
R --no-save <<EOL
install.packages("pkgbuild", repos="https://mirror.las.iastate.edu/CRAN")
install.packages("devtools", repos="https://mirror.las.iastate.edu/CRAN")
library(devtools)
devtools::install_github("rstudio/tensorflow")
library(tensorflow)
devtools::install_github("rstudio/keras")
library(keras)
EOL

%runscript
exec $@
```

## Collection

 - Name: [ResearchIT/singularity-keras](https://github.com/ResearchIT/singularity-keras)
 - License: None

