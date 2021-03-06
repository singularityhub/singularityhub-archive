---
id: 7039
name: "jonmiller3/singularity_imgs"
branch: "master"
tag: "larcv_cpu.txt"
commit: "5a1c3167c9b4e5e4460db0ea8ab2cac6658d079a"
version: "a83957434c137e7fa018297ff02254af"
build_date: "2019-02-08T18:50:09.714Z"
size_mb: 5371
size: 2556682271
sif: "https://datasets.datalad.org/shub/jonmiller3/singularity_imgs/larcv_cpu.txt/2019-02-08-5a1c3167-a8395743/a83957434c137e7fa018297ff02254af.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jonmiller3/singularity_imgs/larcv_cpu.txt/2019-02-08-5a1c3167-a8395743/
recipe: https://datasets.datalad.org/shub/jonmiller3/singularity_imgs/larcv_cpu.txt/2019-02-08-5a1c3167-a8395743/Singularity
collection: jonmiller3/singularity_imgs
---

# jonmiller3/singularity_imgs:larcv_cpu.txt

```bash
$ singularity pull shub://jonmiller3/singularity_imgs:larcv_cpu.txt
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
    # for larcv
    export LARCV_BASEDIR=/app/larcv2
    export LARCV_BUILDDIR=${LARCV_BASEDIR}/build
    export LARCV_COREDIR=${LARCV_BASEDIR}/larcv/core
    export LARCV_APPDIR=${LARCV_BASEDIR}/larcv/app
    export LARCV_LIBDIR=${LARCV_BUILDDIR}/lib
    export LARCV_INCDIR=${LARCV_BUILDDIR}/include
    export LARCV_BINDIR=${LARCV_BUILDDIR}/bin
    # without numpy
    #export LARCV_NUMPY=0
    #export LARCV_INCLUDES="-I${LARCV_INCDIR} "
    #export LARCV_LIBS="-L${LARCV_LIBDIR} -llarcv"

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
    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python-dev python-pip git wget emacs vim cmake nano sqlite3 curl
  
     

    # ROOT    
    wget https://root.cern.ch/download/root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    tar -xzf root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    rm root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    mv root /usr/local/root
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}

    ##git clone https://github.com/maxhgerlach/tensorflow-1.8.0-ubuntu16.04-py27-no_avx-xeon_x5650.git
    ##git clone https://github.com/mdsimmo/tensorflow-community-wheels/releases/download/1.13.0_cpu_amd64/tensorflow-1.13.0rc0-cp27-cp27mu-linux_x86_64.whl

    # pip
    python -m pip install --upgrade setuptools pip
    python -m pip install --upgrade numpy
    python -m pip install scipy nose
    python -m pip install matplotlib pandas
    python -m pip install 'ipython<6.0'
    python -m pip install jupyter notebook
    ##python -m pip install tensorflow-1.8.0-ubuntu16.04-py27-no_avx-xeon_x5650/tensorflow-1.8.0-cp27-cp27mu-linux_x86_64.whl



    # update TF with DANN
    git clone https://github.com/pumpikano/tf-dann.git
    

    curl -L -O https://github.com/mdsimmo/tensorflow-community-wheels/releases/download/1.13.0_cpu_amd64/tensorflow-1.13.0rc0-cp27-cp27mu-linux_x86_64.whl

    python -m pip install tensorflow-1.13.0rc0-cp27-cp27mu-linux_x86_64.whl
    python -m pip install boost
    python -m pip install scikit-learn scikit-image

    mkdir /scratch 
    mkdir /data 
    mkdir /project 
    mkdir /lfstev


    # larcv
    export LARCV_BASEDIR=/app/larcv2
    export LARCV_BUILDDIR=${LARCV_BASEDIR}/build
    export LARCV_COREDIR=${LARCV_BASEDIR}/larcv/core
    export LARCV_APPDIR=${LARCV_BASEDIR}/larcv/app
    export LARCV_LIBDIR=${LARCV_BUILDDIR}/lib
    export LARCV_INCDIR=${LARCV_BUILDDIR}/include
    export LARCV_BINDIR=${LARCV_BUILDDIR}/bin
    export LARCV_ROOT6=1
    export LARCV_CXX=g++
    # without numpy
    #ENV LARCV_NUMPY=0
    #export LARCV_INCLUDES="-I${LARCV_INCDIR} "
    #export LARCV_LIBS="-L${LARCV_LIBDIR} -llarcv"
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
    mkdir /app && cd /app
    git clone https://github.com/DeepLearnPhysics/larcv2
    mkdir -p $LARCV_BUILDDIR
    mkdir -p $LARCV_LIBDIR
    mkdir -p $LARCV_BINDIR
    cd $LARCV_BASEDIR && make -j4
```

## Collection

 - Name: [jonmiller3/singularity_imgs](https://github.com/jonmiller3/singularity_imgs)
 - License: None

