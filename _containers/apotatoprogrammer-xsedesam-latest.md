---
id: 13474
name: "apotatoprogrammer/xsedesam"
branch: "master"
tag: "latest"
commit: "12486ad3ea82d606d12918d5a8636924dda8dfa2"
version: "9edbe73975f8c5cdb17f971f2d799dae"
build_date: "2020-07-05T20:13:43.323Z"
size_mb: 2556.0
size: 1048686623
sif: "https://datasets.datalad.org/shub/apotatoprogrammer/xsedesam/latest/2020-07-05-12486ad3-9edbe739/9edbe73975f8c5cdb17f971f2d799dae.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/apotatoprogrammer/xsedesam/latest/2020-07-05-12486ad3-9edbe739/
recipe: https://datasets.datalad.org/shub/apotatoprogrammer/xsedesam/latest/2020-07-05-12486ad3-9edbe739/Singularity
collection: apotatoprogrammer/xsedesam
---

# apotatoprogrammer/xsedesam:latest

```bash
$ singularity pull shub://apotatoprogrammer/xsedesam:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest
%labels
	APPLICATION_NAME ajd_environment
	AUTHOR_NAME Samuel Aragones
	AUTHOR_EMAIL saragones@g.ucla.edu

%setup

%environment

%post -c /bin/bash
	#here we install all of our core packages
	apt-get update
	apt-get -y install apt-utils
	apt-get -y install python3-dev
	apt-get -y install python3-pip
	apt-get -y install python3-setuptools
	apt-get -y install python3-virtualenv
	apt-get -y install python3-numpy
	apt-get -y install python3-scipy
	apt-get -y install python3-sklearn
	apt-get -y install python3-skimage
	apt-get -y install python3-statsmodels
	apt-get -y install python3-matplotlib
	apt-get -y install python3-seaborn
	apt-get -y install g++
	apt-get -y install unzip
	apt-get -y install zip
	apt-get -y install git
	apt-get -y install openjdk-11-jdk
	#Jupyter
	apt-get -y install jupyter
	pip3 install jupyterlab
	pip3 install louvain
	pip3 install kneed
	pip3 install python-igraph
	pip3 install scanpy
	#PROSSTT
	pip3 install newick
	pip3 install git+git://github.com/soedinglab/prosstt.git
	#R
	apt-get -y install apt-transport-https software-properties-common
	#apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
	#add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/'
	#R --vanilla -e 'install.packages("forecast", repos="http://cran.us.r-project.org")'
	apt-get -y install build-essential
	apt-get -y install r-base
	apt-get -y install r-base-dev
	R --vanilla -e 'install.packages("BiocManager",repos="https://cran.us.r-project.org")'
	R --vanilla -e 'BiocManager::install("splatter")'
	


%files

%runscript

%test
```

## Collection

 - Name: [apotatoprogrammer/xsedesam](https://github.com/apotatoprogrammer/xsedesam)
 - License: None

