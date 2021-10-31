---
id: 4046
name: "anushree85/singularity_imgs"
branch: "master"
tag: "larcv_ws"
commit: "6d27ab8651ddfa7368cfee95976391cff0855471"
version: "ebf7831afaec14f1d20fefe771ceb24d"
build_date: "2018-08-19T21:19:46.821Z"
size_mb: 5841
size: 2451206175
sif: "https://datasets.datalad.org/shub/anushree85/singularity_imgs/larcv_ws/2018-08-19-6d27ab86-ebf7831a/ebf7831afaec14f1d20fefe771ceb24d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/anushree85/singularity_imgs/larcv_ws/2018-08-19-6d27ab86-ebf7831a/
recipe: https://datasets.datalad.org/shub/anushree85/singularity_imgs/larcv_ws/2018-08-19-6d27ab86-ebf7831a/Singularity
collection: anushree85/singularity_imgs
---

# anushree85/singularity_imgs:larcv_ws

```bash
$ singularity pull shub://anushree85/singularity_imgs:larcv_ws
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: DeepLearnPhysics/larcv2-singularity:ubuntu16.04-gpu

%help
Ubuntu16.04 with root v06.08.06 cuda v9 cudnn7
Python packages: pip numpy tensorflow larcv matplotlib pandas ipython jupyter notebook
Development kit: g++/gcc libqt4-dev python-dev nvcc
Utility kit    : git wget emacs vim
To start your container simply try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer drinkingkazu
Version ubuntu16.04-root06.08.06-gpu-larcv2

#------------
# Global installation
#------------
%environment
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
    # make lqcd filesystem mount points
    mkdir /scratch /data /project /lqcdproj
    # ROOT    
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
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
    #install sqllalchemy
    #pip install --upgrade pip
    pip install sqlalchemy
    pip install cmake
    #pip install boost
    #git clone https://github.com/swig/swig.git
    #cd swig
   #./autogen.sh
   #./configure
   # make
   # sudo make install
```

## Collection

 - Name: [anushree85/singularity_imgs](https://github.com/anushree85/singularity_imgs)
 - License: None

