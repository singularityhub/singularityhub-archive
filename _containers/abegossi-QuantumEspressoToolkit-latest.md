---
id: 3413
name: "abegossi/QuantumEspressoToolkit"
branch: "master"
tag: "latest"
commit: "5e318e9d81ee4ebe76db520251e20efbcfbc47e1"
version: "706151d3813d6bf8a5f5bced84cda2dc"
build_date: "2018-07-05T21:26:03.930Z"
size_mb: 4710
size: 2017800223
sif: "https://datasets.datalad.org/shub/abegossi/QuantumEspressoToolkit/latest/2018-07-05-5e318e9d-706151d3/706151d3813d6bf8a5f5bced84cda2dc.simg"
url: https://datasets.datalad.org/shub/abegossi/QuantumEspressoToolkit/latest/2018-07-05-5e318e9d-706151d3/
recipe: https://datasets.datalad.org/shub/abegossi/QuantumEspressoToolkit/latest/2018-07-05-5e318e9d-706151d3/Singularity
collection: abegossi/QuantumEspressoToolkit
---

# abegossi/QuantumEspressoToolkit:latest

```bash
$ singularity pull shub://abegossi/QuantumEspressoToolkit:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:26
%environment
  export PATH="/opt/conda/bin:$PATH"              # Python anaconda
  export XDG_RUNTIME_DIR=$HOME 

%post
	echo "Hello from inside the container"
	echo "The post section is where you can install, and configure you container"
	yum update -y
	mkdir anaconda
	cd anaconda
	yum install wget -y		
	yum install bzip2 -y  	
  	wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh -P /opt
  	/bin/bash /opt/Anaconda3-5.1.0-Linux-x86_64.sh -b -p /opt/conda
  	rm /opt/Anaconda3-5.1.0-Linux-x86_64.sh   
	cd ..
	yum install git -y
	mkdir software
	cd software
	mkdir temp
	cd temp
	mkdir teste
	cd ..
	wget http://qe-forge.org/gf/download/frsrelease/247/1132/qe-6.2.1.tar.gz
	tar zxvf qe-6.2.1.tar.gz
	mkdir examples
	cd examples
	wget http://qe-forge.org/gf/download/frsrelease/247/1128/qe-6.2.1-examples.tar.gz
	tar zxvf qe-6.2.1-examples.tar.gz
	cd ..
	mkdir gfortran
	cd gfortran
	wget https://rpmfind.net/linux/fedora/linux/releases/26/Everything/x86_64/os/Packages/g/gcc-gfortran-7.1.1-3.fc26.x86_64.rpm
	dnf install gcc-gfortran-7.1.1-3.fc26.x86_64.rpm -y
	cd ..
	cd qe-6.2.1
	./configure
	yum install make -y
	make all
	yum install vim -y
	cd ..
	sed -i '19,25 d' /software/qe-6.2.1/environment_variables
	sed -i '19 aPREFIX=cd /software/qe-6.2.1' /software/qe-6.2.1/environment_variables
	sed -i '20 aBIN_DIR=/software/qe-6.2.1/bin' /software/qe-6.2.1/environment_variables
	sed -i '21 aPSEUDO_DIR=/software/qe-6.2.1/pseudo' /software/qe-6.2.1/environment_variables
	sed -i '22 aTMP_DIR=/software/temp' /software/qe-6.2.1/environment_variables
	sed -i '57 d' /software/qe-6.2.1/environment_variables
	sed -i '56 aPARA_PREFIX=" "' /software/qe-6.2.1/environment_variables
```

## Collection

 - Name: [abegossi/QuantumEspressoToolkit](https://github.com/abegossi/QuantumEspressoToolkit)
 - License: None

