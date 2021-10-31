---
id: 12927
name: "willgpaik/afni_aci"
branch: "master"
tag: "latest"
commit: "8ef4519305a1aff8f932037b18bf20f3950d696b"
version: "43f14b87dd00cba270e77f608e6259e232f4460f4eac00a445fbd9edeaeed0fd"
build_date: "2021-04-09T19:11:55.187Z"
size_mb: 3202.0
size: 6109896704
sif: "https://datasets.datalad.org/shub/willgpaik/afni_aci/latest/2021-04-09-8ef45193-43f14b87/43f14b87dd00cba270e77f608e6259e232f4460f4eac00a445fbd9edeaeed0fd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/afni_aci/latest/2021-04-09-8ef45193-43f14b87/
recipe: https://datasets.datalad.org/shub/willgpaik/afni_aci/latest/2021-04-09-8ef45193-43f14b87/Singularity
collection: willgpaik/afni_aci
---

# willgpaik/afni_aci:latest

```bash
$ singularity pull shub://willgpaik/afni_aci:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: willgpaik/centos7_aci

%environment
  PATH="/usr/local/bin/:$PATH:/usr/lib64/openmpi/bin/"
	LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
	MPI_ROOT=/usr/lib64/openmpi/
	export PATH
	export LD_LIBRARY_PATH
	export MPI_ROOT
	export BOOST_ROOT=/usr/local/
	source /opt/rh/devtoolset-8/enable
  
  export R_LIBS=/usr/R:$R_LIBS
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export PATH=/usr/local/bin:$PATH
  export PATH=/usr/abin:$PATH
  export LD_LIBRARY_PATH=/usr/lib64:$LD_LIBRARY_PATH
  export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH

%post
	PATH="/usr/local/bin/:$PATH:/usr/lib64/openmpi/bin/"
	LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
	MPI_ROOT=/usr/lib64/openmpi/
	export PATH
	export LD_LIBRARY_PATH
	export MPI_ROOT
	export BOOST_ROOT=/usr/local/
	source /opt/rh/devtoolset-8/enable

	yum -y update
	yum -y install tcsh libXp openmotif gsl xorg-x11-fonts-misc \
		PyQt4 R-devel netpbm-progs gnome-tweak-tool ed \
		libpng12 xorg-x11-server-Xvfb firefox \
    		mesa-libGLw-devel

	mkdir -p /usr/abin

	export HOME=/usr
	export PATH=/usr/abin:$PATH
	
	cd $HOME

	curl -O https://afni.nimh.nih.gov/pub/dist/bin/misc/@update.afni.binaries
	tcsh @update.afni.binaries -package linux_centos_7_64 -do_extras

	cp $HOME/abin/AFNI.afnirc $HOME/.afnirc
	suma -update_env

	export R_LIBS=$HOME/R
	mkdir $R_LIBS
	echo 'export R_LIBS=$HOME/R' >> ~/.bashrc
	echo  'setenv R_LIBS ~/R'     >> ~/.cshrc
	source ~/.bashrc

	rPkgsInstall -pkgs ALL

	cp $HOME/abin/AFNI.afnirc $HOME/.afnirc
	suma -update_env

	curl -O https://afni.nimh.nih.gov/pub/dist/edu/data/CD.tgz
	tar xvzf CD.tgz
	cd CD
	tcsh s2.cp.files . ~
	cd ..
	# https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/install_instructs/steps_linux_Fed_RH.html#prepare-for-bootcamp
	rm CD.tgz
	rm -rf CD

	afni_system_check.py -check_all

	@afni_R_package_install -shiny -circos

	@update.afni.binaries -d
```

## Collection

 - Name: [willgpaik/afni_aci](https://github.com/willgpaik/afni_aci)
 - License: None

