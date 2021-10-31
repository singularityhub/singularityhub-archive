---
id: 11710
name: "MBlaschek/singularity-jupyter"
branch: "master"
tag: "jupyter3rttov"
commit: "6c67323abf270207695638fddad895daf81671c6"
version: "c6d548fd33281990c251bb917d52d7c70a4d5dcc5d7848b401a27cc6137f319c"
build_date: "2020-12-25T17:15:34.610Z"
size_mb: 1429.91015625
size: 1499369472
sif: "https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter3rttov/2020-12-25-6c67323a-c6d548fd/c6d548fd33281990c251bb917d52d7c70a4d5dcc5d7848b401a27cc6137f319c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MBlaschek/singularity-jupyter/jupyter3rttov/2020-12-25-6c67323a-c6d548fd/
recipe: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter3rttov/2020-12-25-6c67323a-c6d548fd/Singularity
collection: MBlaschek/singularity-jupyter
---

# MBlaschek/singularity-jupyter:jupyter3rttov

```bash
$ singularity pull shub://MBlaschek/singularity-jupyter:jupyter3rttov
```

## Singularity Recipe

```singularity
# BootStrap: localimage
# From: jupyter23
Bootstrap: shub
From: MBlaschek/singularity-jupyter:jupyter23


%help
	Container Centos 6.10 (docker)
	Glibc: 2.12-1.212.el6.x86_64
	Installed: wget, git, curl, bzip2 ca-certificates

	Run a jupyter notebook Server in a container
	Usually: http://localhost:8888
	Anaconda Python 3 (plus 2.7)
	When using Virtualbox supply: --ip=0.0.0.0 to notebook

	Run RTTOV 12.3 inside a container
	Download Rttov from
	https://www.nwpsaf.eu/site/software/rttov/download/#Software
	into rttov directory

%setup
	mkdir -p ${SINGULARITY_ROOTFS}/rttov
	mkdir -p ${SINGULARITY_ROOTFS}/rtcoef
	mkdir -p ${SINGULARITY_ROOTFS}/rtdoc

%files
	# DOC
	rttov/rttov-wrapper-python.pdf /rtdoc/RTTOV_Python_wrapper.pdf
	rttov/users_guide_rttov12_v1.3.pdf /rtdoc/RTTOV_User_guide_v12_v1.3.pdf
	rttov/rttov_gui_v12.pdf /rtdoc/RTTOV_gui_v12.pdf
	# SRC
	# RTTOV Source is not available like this
	# rttov/rttov123.tar.gz /rttov/rttov123.tar.gz
	rttov/Makefile.local /rttov/Makefile.local
	rttov/gfortran-anaconda /rttov/gfortran-anaconda

	run.sh /usr/bin

%apprun rthelp
	echo "RTTOV User guide and Python wrapper"
	echo "Supply execute as Argument to copy to ./rtdoc"
	echo "$@" | grep execute > /dev/null
	if [ $? -eq 0 ]; then
		mkdir -vp ./rtdoc
		cp -ruv /rtdoc/* ./rtdoc/
	fi

%apprun rtcoef
	echo "Download RTTOV coefficient files to your host"
	[ -z "$SINGULARITY_BIND" ] && echo "Bind /rtcoef to the container (RW) \n BASH ENV e.g.:    export SINGULARITY_BIND=\"${PWD}/rtcoef:/rtcoef\""
	echo "Supply execute as argument to run rttov_coef_download.sh"
	echo "$@" | grep execute > /dev/null
	if [ $? -eq 0 ]; then
		mkdir -vp ./rtcoef
		cp -nruv /rttov/rtcoef_backup/* ./rtcoef
		cd ./rtcoef
		# comment out directory check
		sed -i '159,174 {s/^/#/}' rttov_coef_download.sh
		exec ./rttov_coef_download.sh
	fi

%apprun rttest
	echo "Running the test suite"
	cat <<EOF
	Options:
			: Default (no options) runs test_rttov12.sh
		fwd  	: forward model
		hires	: hires IR sounders
		solar	: visible/near-IR solar
		multi	: multiple instruments together
		pc	: principal components
		htfrtc	: HTFRTC
EOF
	[ -z "$SINGULARITY_BIND" ] && echo "Bind /rtcoef to the container \n e.g.:    export SINGULARITY_BIND=\"${PWD}/rtcoef:/rtcoef\""
	[ -z "$SINGULARITY_BIND" ] || echo "Found Bind: $SINGULARITY_BIND"
	mkdir -p /tmp/rttest
	cd /tmp/rttest
	cp -urf /rttov/rttov_test . && echo "Tests copied to /tmp/rttest"
	ln -fvs /rtcoef rtcoef_rttov${RTTOV_VERSION} && echo "Coefficients linked"
	cd rttov_test
	echo
	echo "#####################################################"
	echo "Testting: "
	echo "$@" | grep fwd > /dev/null
	if [ $? -eq 0 ]; then
		./test_fwd.sh ARCH=gfortran-anaconda BIN=../../usr/local/bin
	fi
	echo "$@" | grep hires > /dev/null
	if [ $? -eq 0 ]; then
		./test_rttov12_hires.sh ARCH=gfortran-anaconda BIN=../../usr/local/bin
	fi

	echo "$@" | grep solar > /dev/null
	if [ $? -eq 0 ]; then
		./test_solar.sh ARCH=gfortran-anaconda BIN=../../usr/local/bin
	fi
	echo "$@" | grep multi > /dev/null
	if [ $? -eq 0 ]; then
		./test_multi_instrument.sh ARCH=gfortran-anaconda BIN=../../usr/local/bin
	fi
	echo "$@" | grep pc > /dev/null
	if [ $? -eq 0 ]; then
		./test_pc.sh ARCH=gfortran-anaconda BIN=../../usr/local/bin
	fi
	if [ $# -eq 0 ]; then
		./test_rttov12.sh ARCH=gfortran-anaconda BIN=../../usr/local/bin
	fi

	echo "rttest used /tmp/rttest"
	echo "Finished"

%apprun rtgui
	echo "Running the Rttov Gui"
	cd /rttov/gui
	# Required by GUI
	export cmdpython=/opt/conda/envs/py2/bin/python
	exec ./rttovgui

%runscript
	exec /usr/bin/run.sh "$@"

%post
	# Additonal
	yum check-update && yum -y update
	# gfortran
	yum groupinstall -y "Development Tools"
	yum install -y cmake doxygen graphviz
	# install gfortran from anaconda
	/opt/conda/bin/conda install gfortran_linux-64 sphinx -y
	# conda install libgfortran -y
	# need netcdf.mod
	/opt/conda/bin/conda install -c conda-forge netcdf-fortran -y
	# Clean
	yum clean all

	# required for CMAKE
	export PATH=/opt/conda/bin:$PATH
	export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
	export RTTOV_VERSION=12
	#
	# Compile
	#
	cd /rttov
	if [ ! -e rttov123.tar.gz ]; then
	    wget ftp://srvx1.img.univie.ac.at/pub/upload/mblaschek/rttov123.tar.gz
	fi
	tar -xzf rttov*.tar.gz
	#
	# Potentiall add bug fixes tar's here end overwrite
	#

	#
	# Copy Makefile.local (HDF, Netcdf libs from Conda)
	#
	mv Makefile.local ./build
	mv gfortran-anaconda ./build/arch
	#
	# Compile using conda gfortran + hdf, netcdf, f2py
	#
	cd src/
	../build/Makefile.PL RTTOV_HDF=1 RTTOV_F2PY=1 RTTOV_USER_LAPACK=0
	make ARCH=gfortran-anaconda INSTALLDIR=../usr/local
	#
	# Backup std coef-files and make links
	# Host can bind coef-files to container (/rtcoef)
	#
	cd ..
	mv rtcoef_rttov${RTTOV_VERSION} rtcoef_backup
	rm -rf rtcoef_rttov*
	ln -s /rtcoef/ rtcoef_rttov${RTTOV_VERSION}
	cp -rfv rtcoef_backup/* /rtcoef
	#
	# Fix links of F2py libs
	#
	cd wrapper
	ln -sf /usr/local/lib/rttov_wrapper_f2py.so .
	cd ../gui
	ln -sf /usr/local/lib/rttov_gui_f2py.so .
	cd ..
	#
	# Python Wrapper
	#
	cd wrapper
	#
	# make library accessable from python
	#
	echo "/rttov/wrapper" > /opt/conda/lib/python3.7/site-packages/rttov.pth
	#
	# Documentation of Python Interface
	#
	doxygen doxygen_config_wrapper
	mv doxygen_doc_wrapper/html /rtdoc/wrapper
	cd pyrttov_doc
	make html
	mv _build/html /rtdoc/pyrttov
	cd ..
	mkdir -p /rtdoc/pyexamples
	cp *.py /rtdoc/pyexamples/
	cd ..
	mv *.pdf /rtdoc
	#
	# Gui (requires py2 and wxpython)
	# recompile with Python2
	#
	/opt/conda/bin/conda install -n py2 -c anaconda wxpython=3.0 h5py matplotlib scipy numpy -y
	# x11 windows for wxpython
	# need to change Library path because yum needs system libs
	oldLD=$LD_LIBRARY_PATH
	export LD_LIBRARY_PATH=/usr/lib64:/usr/lib:$LD_LIBRARY_PATH
	# apt install -y libgtk2.0
	yum install -y gtk2-devel
	export LD_LIBRARY_PATH=$oldLD
	# recompile
	cd src
	rm -v /usr/local/lib/rttov_gui_f2py.so
	# change PATH, LD for python 2
	export PATH=/opt/conda/envs/py2/bin:$PATH
	export LD_LIBRARY_PATH=/opt/conda/envs/py2/lib:$LD_LIBRARY_PATH
	make ARCH=gfortran-anaconda INSTALLDIR=../usr/local
	#
	# fix link
	#
	cp -v ../tmp-gfortran-anaconda/gui/rttov_gui_f2py.so /usr/local/lib
	cd ..
	# Clean
	/opt/conda/bin/conda clean -a -y

%environment
	# important part otherwise the server will try to access /run/user and fail
	export JUPYTER_RUNTIME_DIR=$PWD/.runtime
	# Make sure we use container kernels
	export JUPYTER_DATA_DIR=$PWD/.kernels
	# Development

	export PATH=/opt/conda/bin:$PATH
	export LD_LIBRARY_PATH=/opt/conda/lib:/usr/local/lib:$LD_LIBRARY_PATH
	# RTTOV Options
	export RTTOV_VERSION=12
	export OMP_STACKSIZE=1000M
	export RTTOV_DIR=/rttov
	export RTTOV_COEF=/rtcoef
	# GUI options
	export RTTOV_GUI_PREFIX=/rttov/gui
	export RTTOV_GUI_EMISS_DIR=${RTTOV_GUI_PREFIX}/../
	export RTTOV_GUI_COEFF_DIR=${RTTOV_GUI_PREFIX}/../rtcoef_rttov${RTTOV_VERSION}
	export RTTOV_GUI_PROFILE_DIR=${RTTOV_GUI_PREFIX}/../rttov_test/profile-datasets-hdf
```

## Collection

 - Name: [MBlaschek/singularity-jupyter](https://github.com/MBlaschek/singularity-jupyter)
 - License: None

