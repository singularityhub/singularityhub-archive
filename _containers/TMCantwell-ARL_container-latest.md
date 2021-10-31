---
id: 7943
name: "TMCantwell/ARL_container"
branch: "master"
tag: "latest"
commit: "2c8727df40c55d5eecc3ea6c662aa8d2cbe38684"
version: "5daa5bb6b05de85edae56604f75e4f13"
build_date: "2019-03-25T23:16:30.455Z"
size_mb: 5064
size: 1902972959
sif: "https://datasets.datalad.org/shub/TMCantwell/ARL_container/latest/2019-03-25-2c8727df-5daa5bb6/5daa5bb6b05de85edae56604f75e4f13.simg"
url: https://datasets.datalad.org/shub/TMCantwell/ARL_container/latest/2019-03-25-2c8727df-5daa5bb6/
recipe: https://datasets.datalad.org/shub/TMCantwell/ARL_container/latest/2019-03-25-2c8727df-5daa5bb6/Singularity
collection: TMCantwell/ARL_container
---

# TMCantwell/ARL_container:latest

```bash
$ singularity pull shub://TMCantwell/ARL_container:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget

%post -c /bin/bash
yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install curl
yum -y install epel-release
yum -y install git
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | bash
yum -y install git-lfs
git lfs install
yum -y install python36u-devel python36u-pip python36u-tkinter python-virtualenv python-virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/bin/virtualenvwrapper.sh
yum -y install graphviz
yum -y install mpich-devel mpich-autoload
yum -y install openmpi-devel mpi4py-openmpi
export CC=/usr/lib64/openmpi/bin/mpicc
yum -y install cfitsio-devel
yum -y install cmake cmake-gui gcc-gfortran gcc-c++ flex bison \
       blas blas-devel  lapack lapack-devel cfitsio cfitsio-devel \
       wcslib wcslib-devel ncurses ncurses-devel readline readline-devel\
       python-devel boost boost-devel fftw fftw-devel hdf5 hdf5-devel\
       numpy boost-python34
ln -s /usr/lib64/libboost_python3.so.1.53.0 /usr/lib64/libboost_python-py36.so
pip3.6 install numpy
wget ftp://ftp.astron.nl/outgoing/Measures/WSRT_Measures.ztar
mkdir WSRT_Measures
tar -C WSRT_Measures -xzvf WSRT_Measures.ztar
git clone https://github.com/casacore/casacore
cd casacore
mkdir build
cd build
cmake -DDATA_DIR=/WSRT_Measures -DUSE_FFTW3=ON -DUSE_OPENMP=ON -DBUILD_PYTHON=OFF -DBUILD_PYTHON3=ON -DUSE_THREADS=ON \
       -DPYTHON3_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON3_LIBRARY=/usr/lib64/libpython3.6m.so \
       -DPYTHON3_EXECUTABLE=/usr/bin/python3.6m  \
       -DPYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib64/python3.6/site-packages/numpy/core/include \
       -DPYTHON3_Boost_LIBRARIES=/usr/lib64/libboost_python3-mt.so ..
make 
make install
cd /
pip3 install pipenv
virtualenv -p python3.6 /arlvenv
alias start-arlvenv="source /arlvenv/bin/activate"
. /arlvenv/bin/activate
pip install pytest
pip install pylint
pip install mpi4py
pip install jupyter
pip install matplotlib
git clone https://github.com/SKA-ScienceDataProcessor/algorithm-reference-library
cd algorithm-reference-library
pip install -r requirements.txt
python setup.py install
git-lfs pull
export PYTHONPATH=/algorithm-reference-library:$PYTHONPATH
add2virtualenv /algorithm-reference-library

%environment
alias start-arlvenv="source /arlvenv/bin/activate"
export PYTHONPATH=/algorithm-reference-library:$PYTHONPATH
export XDG_RUNTIME_DIR=""
```

## Collection

 - Name: [TMCantwell/ARL_container](https://github.com/TMCantwell/ARL_container)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

