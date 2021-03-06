---
id: 6937
name: "jonmiller3/singularity_imgs"
branch: "master"
tag: "larcv_fc"
commit: "374f1155d71c9dcb00bb0a6010d0fbfe3cdd2347"
version: "46ffa4ca93a7428c038fdf16d5ce37b5"
build_date: "2019-02-06T18:59:38.973Z"
size_mb: 6160
size: 2936086559
sif: "https://datasets.datalad.org/shub/jonmiller3/singularity_imgs/larcv_fc/2019-02-06-374f1155-46ffa4ca/46ffa4ca93a7428c038fdf16d5ce37b5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jonmiller3/singularity_imgs/larcv_fc/2019-02-06-374f1155-46ffa4ca/
recipe: https://datasets.datalad.org/shub/jonmiller3/singularity_imgs/larcv_fc/2019-02-06-374f1155-46ffa4ca/Singularity
collection: jonmiller3/singularity_imgs
---

# jonmiller3/singularity_imgs:larcv_fc

```bash
$ singularity pull shub://jonmiller3/singularity_imgs:larcv_fc
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

    # pip
    python -m pip install --upgrade setuptools pip
    python -m pip install --upgrade numpy
    python -m pip install scipy nose
    python -m pip install matplotlib pandas
    python -m pip install 'ipython<6.0'
    python -m pip install jupyter notebook
    python -m pip install tensorflow-gpu
    python -m pip install boost
    python -m pip install scikit-learn scikit-image


    # update TF with DANN
    git clone https://github.com/pumpikano/tf-dann.git
    

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

