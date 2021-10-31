---
id: 5315
name: "schluenz/calipsoplus"
branch: "master"
tag: "pymca"
commit: "42cb84a62f827139e5267cb7da443d2fd5f728e2"
version: "d347dff8fde8c1cf6bde5b43fce7f194"
build_date: "2018-10-23T17:47:48.202Z"
size_mb: 7214
size: 2996240415
sif: "https://datasets.datalad.org/shub/schluenz/calipsoplus/pymca/2018-10-23-42cb84a6-d347dff8/d347dff8fde8c1cf6bde5b43fce7f194.simg"
url: https://datasets.datalad.org/shub/schluenz/calipsoplus/pymca/2018-10-23-42cb84a6-d347dff8/
recipe: https://datasets.datalad.org/shub/schluenz/calipsoplus/pymca/2018-10-23-42cb84a6-d347dff8/Singularity
collection: schluenz/calipsoplus
---

# schluenz/calipsoplus:pymca

```bash
$ singularity pull shub://schluenz/calipsoplus:pymca
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/centos

%help
Singularity Container for the PyMca package

%apprun pymca
   exec /opt/anaconda/3/bin/pymca

%labels
  org.label-schema.version  5.4.0
  org.label-schema.url      http://pymca.sourceforge.net/
  org.label-schema.name     pymca
  org.label-schema.vendor   calipso+
  Version  5.4.0
  Packager Calipso+
  Author   Calipso+

%environment
export PATH=/opt/anaconda/3/bin:$PATH

%post
#
#  install base packages
#
yum install -y dbus dejavu-lgc-sans-fonts gedit unzip gzip tar pam libXt GConf2 gtk2 libXtst python xterm wget which curl mesa-libGLU-devel mesa-libGL
yum install -y bzip2 hdf5 hdf5-devel gtk2-devel libpng-devel ncurses-devel fftw-devel gmp-devel mpfr-devel libmpc-devel autoconf automake m4
yum groupinstall -y "Development tools"

mkdir -p /TMP
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O /TMP/Anaconda3-5.3.0-Linux-x86_64.sh
/bin/bash /TMP/Anaconda3-5.3.0-Linux-x86_64.sh -b -p /opt/anaconda/3

export PATH=/opt/anaconda/3/bin:$PATH

conda install -y numpy h5py matplotlib
conda install -y -c conda-forge fisx silx pyside libglu 

pip install pymca==5.4.0

#
#  Clean up
#
yum remove -y \*-devel
rm -rf /TMP
```

## Collection

 - Name: [schluenz/calipsoplus](https://github.com/schluenz/calipsoplus)
 - License: None

