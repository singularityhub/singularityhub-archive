---
id: 1006
name: "tin6150/biolab-orange"
branch: "master"
tag: "latest"
commit: "49891c4555b733fc38d686ddc80403e6c81f62cf"
version: "0a29849594a4fb7c74f1716101aa3708"
build_date: "2017-12-11T03:00:01.747Z"
size_mb: 3770
size: 1593262111
sif: "https://datasets.datalad.org/shub/tin6150/biolab-orange/latest/2017-12-11-49891c45-0a298495/0a29849594a4fb7c74f1716101aa3708.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tin6150/biolab-orange/latest/2017-12-11-49891c45-0a298495/
recipe: https://datasets.datalad.org/shub/tin6150/biolab-orange/latest/2017-12-11-49891c45-0a298495/Singularity
collection: tin6150/biolab-orange
---

# tin6150/biolab-orange:latest

```bash
$ singularity pull shub://tin6150/biolab-orange:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
## docker container for anaconda somehow produced windows without text. missing fonts lib?
##From: continuumio/anaconda3:latest
##From: continuumio/miniconda3

##From: centos:7.3.1611


%help
Orange is a data mining tool from biolab.si
It is a both a GUI program and python modules for advance use.
[unofficial singularity container]

%runscript
	/opt/anaconda3/pkgs/orange3-3.8.0-py36_0/bin/orange-canvas "$@"
	#orange-canvas

%post
	echo singularity container build starts
	touch /THIS_IS_INSIDE_SINGULARITY
	apt-key update
	apt-get update
	apt-get -y --force-yes install vim ncurses-term gedit less wget git tar bzip2 coreutils firefox
	# browser is optional, used for displaying help, tutorial

	# install anaconda3 (python3)
	Anaconda3Ver=5.0.1
	cd /opt
	#test -f Anaconda3-${Anaconda3Ver}-Linux-x86_64.sh || wget https://repo.continuum.io/archive/Anaconda3-${Anaconda3Ver}-Linux-x86_64.sh
	#test -d /opt/anaconda3 || bash Anaconda3-${Anaconda3Ver}-Linux-x86_64.sh -p /opt/anaconda3 -b     # batch mode, accept license w/o user input
	if [ ! -d /opt/anaconda3 ]; then
		wget https://repo.continuum.io/archive/Anaconda3-${Anaconda3Ver}-Linux-x86_64.sh 
		bash Anaconda3-${Anaconda3Ver}-Linux-x86_64.sh -p /opt/anaconda3 -b     # -b = batch mode, accept license w/o user input
	fi


	/opt/anaconda3/bin/conda config --add channels conda-forge
	/opt/anaconda3/bin/conda install orange3
	/opt/anaconda3/bin/conda install -c defaults pyqt=5 qt
	#/opt/conda/bin/conda config --add channels conda-forge
	#pip install --upgrade pip
	#pip install setuptools
	#pip install orange3
	# not sure why the orange-canvas script misdetected python to be in /opt/anaconda1anaconda2anaconda3 .  tmp fix till find root cause.
	ln -s anaconda3 anaconda1anaconda2anaconda3
	# clean up
	rm Anaconda3-${Anaconda3Ver}-Linux-x86_64.sh 
	echo singularity container build ends.


%labels
MAINTAINER  Tin Ho tin(at)lbl.gov

 
# ref https://www.singularity-hub.org/collections/323
```

## Collection

 - Name: [tin6150/biolab-orange](https://github.com/tin6150/biolab-orange)
 - License: None

