---
id: 6671
name: "DeepLearnPhysics/larcv2-singularity"
branch: "master"
tag: "ub16.04-cuda100-pytorchdev20181215"
commit: "5e63c18e5e928614efb687e6b9e9325132e6ff81"
version: "5f8a49be2039923897855cf2b137eb02"
build_date: "2019-01-29T05:23:57.051Z"
size_mb: 6589
size: 3168632863
sif: "https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-cuda100-pytorchdev20181215/2019-01-29-5e63c18e-5f8a49be/5f8a49be2039923897855cf2b137eb02.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-cuda100-pytorchdev20181215/2019-01-29-5e63c18e-5f8a49be/
recipe: https://datasets.datalad.org/shub/DeepLearnPhysics/larcv2-singularity/ub16.04-cuda100-pytorchdev20181215/2019-01-29-5e63c18e-5f8a49be/Singularity
collection: DeepLearnPhysics/larcv2-singularity
---

# DeepLearnPhysics/larcv2-singularity:ub16.04-cuda100-pytorchdev20181215

```bash
$ singularity pull shub://DeepLearnPhysics/larcv2-singularity:ub16.04-cuda100-pytorchdev20181215
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

%help
Ubuntu16.04 with cuda10.0 cudnn7
ML/DL packages  : pytorch (1.0.0=dev20181215) sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python root root_numpy
                  plotly cufflinks osfclient
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version ub16.04-cuda100-pytorchdev20181215

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
    export CUDA_DEVICE_ORDER=PCI_BUS_ID
    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH="${ROOTSYS}/lib:${LD_LIBRARY_PATH}"
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
    export CUDA_DEVICE_ORDER=PCI_BUS_ID

    export LARCV_BASEDIR=/app/larcv2
    export LARCV_BUILDDIR="${LARCV_BASEDIR}/build"
    export LARCV_COREDIR="${LARCV_BASEDIR}/larcv/core"
    export LARCV_APPDIR="${LARCV_BASEDIR}/larcv/app"
    export LARCV_LIBDIR="${LARCV_BUILDDIR}/lib"
    export LARCV_INCDIR="${LARCV_BUILDDIR}/include"
    export LARCV_BINDIR="${LARCV_BUILDDIR}/bin"
    export LARCV_ROOT6=1
    export LARCV_CXX=g++

# with numpy
    export LARCV_NUMPY=1
    export LARCV_INCLUDES="-I${LARCV_INCDIR} -I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7"
    export LARCV_LIBS="-L/usr/lib/ -L/usr/lib/python2.7/config-x86_64-linux-gnu -L/usr/lib"
    export LARCV_LIBS="${LARCV_LIBS} -lpthread -ldl -lutil -lm -lpython2.7 -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions"
    export LARCV_LIBS="${LARCV_LIBS} -L${LARCV_LIBDIR} -llarcv"

# set bin and lib path
    export PATH=${LARCV_BASEDIR}/bin:${LARCV_BINDIR}:${PATH}
    export LD_LIBRARY_PATH=${LARCV_LIBDIR}:${LD_LIBRARY_PATH}:
    export PYTHONPATH=${LARCV_BASEDIR}/python:${PYTHONPATH}

%post
apt-get -y update
apt-get -y install zsh dpkg-dev g++ gcc binutils libqt4-dev git wget emacs vim openssh-client
apt-get -y install python-dev python-tk python-pip python-qt4 python-setuptools libsparsehash-dev python3-setuptools libhdf5-dev

# asciinema
apt-get install -y locales
locale-gen en_US.UTF-8 
apt-get -y install software-properties-common python-software-properties
apt-add-repository -y ppa:zanchey/asciinema
apt-get -y update
apt-get -y install asciinema

# ROOT
wget https://root.cern.ch/download/root_v6.14.04.Linux-ubuntu16-x86_64-gcc5.4.tar.gz 
tar -xzf root_v6.14.04.Linux-ubuntu16-x86_64-gcc5.4.tar.gz 
rm root_v6.14.04.Linux-ubuntu16-x86_64-gcc5.4.tar.gz 
mv root /usr/local/root 
export ROOTSYS=/usr/local/root 
export PATH=${ROOTSYS}/bin:${PATH} 
export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

# pip basics
pip --no-cache-dir --disable-pip-version-check install --upgrade pip==9.0.3 
pip --no-cache-dir --disable-pip-version-check install --upgrade setuptools 
pip --no-cache-dir --disable-pip-version-check install 'matplotlib<3.0' 
pip --no-cache-dir --disable-pip-version-check install 'ipython<6.0'    
pip --no-cache-dir --disable-pip-version-check install 'ipykernel<5.0'  
pip --no-cache-dir --disable-pip-version-check install future numpy wheel zmq six pygments pyyaml cython gputil psutil humanize 
pip --no-cache-dir --disable-pip-version-check install h5py tqdm scipy seaborn tables root_numpy 
pip --no-cache-dir --disable-pip-version-check install pandas scikit-image scikit-learn Pillow opencv-python 
pip --no-cache-dir --disable-pip-version-check install jupyter notebook
pip --no-cache-dir --disable-pip-version-check install plotly cufflinks
pip --no-cache-dir --disable-pip-version-check install osfclient

pip --no-cache-dir --disable-pip-version-check install plotly cufflinks
pip --no-cache-dir --disable-pip-version-check install osfclient

# larcv
mkdir -p /app
cd /app
git clone https://github.com/DeepLearnPhysics/larcv2
cd larcv2
git checkout v1.0.0_rc01
export LARCV_BASEDIR=/app/larcv2
export LARCV_BUILDDIR="${LARCV_BASEDIR}/build"
export LARCV_COREDIR="${LARCV_BASEDIR}/larcv/core"
export LARCV_APPDIR="${LARCV_BASEDIR}/larcv/app"
export LARCV_LIBDIR="${LARCV_BUILDDIR}/lib"
export LARCV_INCDIR="${LARCV_BUILDDIR}/include"
export LARCV_BINDIR="${LARCV_BUILDDIR}/bin"
export LARCV_ROOT6=1
export LARCV_CXX=g++
export LARCV_NUMPY=1
export LARCV_INCLUDES="-I${LARCV_INCDIR} -I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7"
export LARCV_LIBS="-L/usr/lib/ -L/usr/lib/python2.7/config-x86_64-linux-gnu -L/usr/lib"
export LARCV_LIBS="${LARCV_LIBS} -lpthread -ldl -lutil -lm -lpython2.7 -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions"
export LARCV_LIBS="${LARCV_LIBS} -L${LARCV_LIBDIR} -llarcv"
# set bin and lib path
export PATH=${LARCV_BASEDIR}/bin:${LARCV_BINDIR}:${PATH}
export LD_LIBRARY_PATH=${LARCV_LIBDIR}:${LD_LIBRARY_PATH}:
export PYTHONPATH=${LARCV_BASEDIR}/python:${PYTHONPATH}
mkdir -p $LARCV_BUILDDIR
mkdir -p $LARCV_LIBDIR
mkdir -p $LARCV_BINDIR
make -j4

# pytorch
pip --no-cache-dir --disable-pip-version-check install torch_nightly==1.0.0.dev20181215 -f https://download.pytorch.org/whl/nightly/cu100/torch_nightly.html
ldconfig /usr/local/cuda/lib64/stubs

# scn
pip --no-cache-dir --disable-pip-version-check install --extra-index-url https://test.pypi.org/simple scn-cuda10=="0.2.2018.1218"
```

## Collection

 - Name: [DeepLearnPhysics/larcv2-singularity](https://github.com/DeepLearnPhysics/larcv2-singularity)
 - License: None

