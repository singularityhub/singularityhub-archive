---
id: 14557
name: "shiningsurya/my-singularities"
branch: "main"
tag: "vanilla"
commit: "2d544b3eee2e971cc2ec29086bd1e6cf2f2bff43"
version: "8df0eb7d1a4aaf602c26b0db8f3bc46a446d00ffa097525dd5387758abd2629d"
build_date: "2020-10-06T17:06:51.621Z"
size_mb: 2144.60546875
size: 2248781824
sif: "https://datasets.datalad.org/shub/shiningsurya/my-singularities/vanilla/2020-10-06-2d544b3e-8df0eb7d/8df0eb7d1a4aaf602c26b0db8f3bc46a446d00ffa097525dd5387758abd2629d.sif"
url: https://datasets.datalad.org/shub/shiningsurya/my-singularities/vanilla/2020-10-06-2d544b3e-8df0eb7d/
recipe: https://datasets.datalad.org/shub/shiningsurya/my-singularities/vanilla/2020-10-06-2d544b3e-8df0eb7d/Singularity
collection: shiningsurya/my-singularities
---

# shiningsurya/my-singularities:vanilla

```bash
$ singularity pull shub://shiningsurya/my-singularities:vanilla
```

## Singularity Recipe

```singularity
Bootstrap:           library
From:                ubuntu:20.04

%setup

%labels
	Author             shiningsurya
	Hosting            Github
	Version            v0.0.1


%help
	This is a vanilla flavor.


%post
	apt-get -y update 
	apt-get -y install build-essential binutils-dev
	apt-get -y install software-properties-common
	apt-get -y install ftp wget curl dkms
	apt-get -y install autoconf automake libtool autotools-dev
	apt-get -y install pkg-config
	add-apt-repository universe
	add-apt-repository multiverse
	apt-get -y update 
	apt-get -y install csh tcsh
	apt-get -y install make man mc mlocate lsof

	# GNU compiler collections
	apt-get -y install gcc g++ gfortran fort77 f2c
	apt-get -y install libboost-all-dev

	# other closely related stuff
	apt-get -y install flex bison swig libbison-dev
	apt-get -y install cmake m4
	apt-get -y install hwloc libhwloc-dev
	apt-get -y install gsl-bin libgsl-dev 

	# X11
	apt-get -y install libx11-dev libxext-dev libxext-doc
	apt-get -y install default-jre default-jdk

	# Qt5
	apt-get -y install qt5-default 

	# ssh numa nfs
	apt-get -y install openssh-server numactl
	apt-get -y install libssl-dev libsocket++-dev libsocket++1
	apt-get -y install nfs-common

	# essential libraries
	apt-get -y install libblas64-dev liblapack64-dev liblapacke64-dev libxext-dev
	apt-get -y install libeigen3-dev libxml2-dev libxml2-doc
	apt-get -y install libopenblas-base libopenblas-dev
	apt-get -y install libpng++-dev libpng-dev libpnglite-dev 
	apt-get -y install libgsl-dev libgmp-dev
	apt-get -y install libfftw3-bin libfftw3-dev
	apt-get -y install libglib2.0-dev libglib2.0-bin libbsd-dev
	apt-get -y install libhealpix-cxx-dev libhealpix-cxx2
	apt-get -y install libyaml-cpp-dev

	# unittest
	# ghost
	apt-get -y install libcppunit-dev libcppunit-subunit-dev
	apt-get -y install ghostscript dvipng gv


	# HDF5
	apt-get -y install h5utils hdf5-helpers hdf5-tools hdfview
	apt-get -y install libhdf5-dev libhdf5-serial-dev

	# Lua
	apt-get -y install liblua5.1-0 liblua5.1-0-dev liblua5.2-0 liblua5.2-dev liblua5.3-0 liblua5.3-dev

	# MPI
	apt-get -y install openmpi-bin libopenmpi-dev mpich libmpich-dev
	apt-get -y install libhdf5-openmpi-dev libhdf5-mpich-dev

	# PGPLOT-ing
	# pdf 
	# groff
	apt-get -y install pgplot5
	apt-get -y install libpoppler-dev libpoppler-glib-dev
	apt-get -y install poppler-utils
	apt-get -y install xterm imagemagick

	# GNU plotting
	# that silly interactive stuff
	# apt-get -y install gnuplot 

	# cfitsio
	apt-get -y install libcfitsio-bin libcfitsio-dev libcfitsio-doc
	# multitask
	apt-get -y install tmux screen
	# can not do anything without you
	apt-get -y install rsync parallel

	# misc
	apt-get -y install htop
	apt-get -y install cvs git subversion
	apt-get -y install sed grep gawk
	apt-get -y install vim emacs nano
	apt-get -y install groff worker

	# python
	apt-get -y install python cython python3
	apt-get -y install python3-notebook jupyter jupyter-core 
	apt-get -y install python3-numpy python3-numpydoc  python3-matplotlib python3-pip 

	# pip my image
	# installing pip via pip3 installs pip and I never got the hang
	# of it
	pip3 install -U setuptools datetime pytz bitstring
	pip3 install -U numpy scipy pandas 
	pip3 install -U matplotlib APLpy
	pip3 install -U six h5py nose
	pip3 install -U mpi4py schwimmbad joblib
	pip3 install -U scikit-learn scikit-video scikit-image
	pip3 install -U bokeh corner seaborn
	pip3 install -U paramz peakutils
	pip3 install -U splinter
	pip3 install -U emcee ChainConsumer
	pip3 install -U setuptools_scm pep517 
	
	# astropy
	pip3 install -U astropy astroplan astropy_helpers astroquery

	# ipython
	pip3 install -U ipython

	# random?
	pip3 install -U pyfits lmfit statsmodels 
	pip3 install -U pyephem psrqpy


	CTIME=`date`
	echo "export CTIME=\"${CTIME}\"" >> $SINGULARITY_ENVIRONMENT

%runscript
	echo "-------------------------------------"
	echo "------------ VANILLA -----------------
	echo "-------------------------------------"
	echo "This container was created $CTIME"
```

## Collection

 - Name: [shiningsurya/my-singularities](https://github.com/shiningsurya/my-singularities)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

