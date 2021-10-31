---
id: 9708
name: "llucifer97/Pose-analysis-of-art"
branch: "master"
tag: "latest"
commit: "72744f62054dcc0ca880e7d1c9c8bf866eb8bbdf"
version: "d3a4ce3c2589aaa309ee1aff77e0a7f0"
build_date: "2019-06-14T10:36:12.584Z"
size_mb: 4738
size: 1935712287
sif: "https://datasets.datalad.org/shub/llucifer97/Pose-analysis-of-art/latest/2019-06-14-72744f62-d3a4ce3c/d3a4ce3c2589aaa309ee1aff77e0a7f0.simg"
url: https://datasets.datalad.org/shub/llucifer97/Pose-analysis-of-art/latest/2019-06-14-72744f62-d3a4ce3c/
recipe: https://datasets.datalad.org/shub/llucifer97/Pose-analysis-of-art/latest/2019-06-14-72744f62-d3a4ce3c/Singularity
collection: llucifer97/Pose-analysis-of-art
---

# llucifer97/Pose-analysis-of-art:latest

```bash
$ singularity pull shub://llucifer97/Pose-analysis-of-art:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
        MAINTAINER ayushraj

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
	apt-get update && apt-get install -y --no-install-recommends software-properties-common wget
add-apt-repository universe
apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates curl git nano less \
  build-essential cmake pkg-config libopencv-dev caffe-cpu libgoogle-glog-dev libcaffe-cpu-dev \
  libboost-dev libprotobuf-dev gpg-agent locales language-pack-en
locale-gen en_US.UTF-8 && dpkg-reconfigure locales
wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
wget https://apt.repos.intel.com/setup/intelproducts.list -O /etc/apt/sources.list.d/intelproducts.list
apt-get update && apt-get install -y --no-install-recommends intel-mkl-64bit-2018.2

# option caffe-cuda
# http://caffe.berkeleyvision.org/install_apt.html
# In case we need to turn off ssl verify
# RUN  git config --global http.sslVerify false

mkdir /localdata
cd /localdata
mkdir src
cd src
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
cd openpose
mkdir build
cd build
export MKLVARS_ARCHITECTURE=intel64
. /opt/intel/mkl/bin/mklvars.sh
# Apparently not all shells allow parameters with source.
#. /opt/intel/mkl/bin/mklvars.sh intel64

cmake -DGPU_MODE=CPU_ONLY -DBUILD_CAFFE=OFF -DCaffe_INCLUDE_DIRS=/usr/include/caffe/ -DCaffe_LIBS=/usr/lib/x86_64-linux-gnu/libcaffe.so ..
make
make install

	 apt update	
         apt install -y python3-pip
         apt install -y git-all            

# Installing some Python packages that are needed for pre-processing
  apt install -y python3 python3-matplotlib python3-numpy
  pip3 install pillow numpy opencv-python image sklearn statistics beautifulsoup4 ipaddress ipykernel ipython ipython-genutils ipywidgets jsonschema jupyter jupyter-client jupyter-console jupyter-core natsort notebook bqplot pandas scikit-image scikit-learn seaborn plotly requests appmode 
   
                                     

        git clone https://github.com/llucifer97/Pose-analysis-of-art

        cd Pose-analysis-of-art/annotator_tool

%runscript
  unset XDG_RUNTIME_DIR && \ 
  python -m notebook
  
  
  
 # jupyter notebook --allow-root "$@"
```

## Collection

 - Name: [llucifer97/Pose-analysis-of-art](https://github.com/llucifer97/Pose-analysis-of-art)
 - License: [MIT License](https://api.github.com/licenses/mit)

