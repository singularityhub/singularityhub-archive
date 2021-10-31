---
id: 2102
name: "intentions/Singularitytest"
branch: "master"
tag: "latest"
commit: "d9ffa173e2ac0832b96a3b72d9c8e11c98e87b00"
version: "5f2ec899c53aceb1106af121909eabcc"
build_date: "2020-04-02T13:32:02.511Z"
size_mb: 874
size: 316174367
sif: "https://datasets.datalad.org/shub/intentions/Singularitytest/latest/2020-04-02-d9ffa173-5f2ec899/5f2ec899c53aceb1106af121909eabcc.simg"
url: https://datasets.datalad.org/shub/intentions/Singularitytest/latest/2020-04-02-d9ffa173-5f2ec899/
recipe: https://datasets.datalad.org/shub/intentions/Singularitytest/latest/2020-04-02-d9ffa173-5f2ec899/Singularity
collection: intentions/Singularitytest
---

# intentions/Singularitytest:latest

```bash
$ singularity pull shub://intentions/Singularitytest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%help
This is a test container using the latest version of centos.  
Its purpose is just to perform basic tests of the singularity installation.

%labels
	Maintainter Kurt.J.Strosahl

%post
	echo "test image"

	echo "Installing Devlopment Tools YUM group"
	yum -y groupinstall "Development Tools"

	echo "installing kernel"
	yum -y install kernel kernel-devel
	
	echo "installing bind utils for testing."
	yum -y install bind-utils
	
	mkdir {/volatile,/cache}
%environment
BLACK='\e[0;30m'
BLUE='\e[0;34m' 
BBLUE='\e[1;34m'
GREEN='\e[0;32m'
BGREEN='\e[1;32m'
CYAN='\e[0;36m'  
BCYAN='\e[1;36m' 
RED='\e[0;31m'   
BRED='\e[1;31m'  
PURPLE='\e[0;35m'
BPURPLE='\e[1;35m'
BROWN='\e[0;33m' 
NORMAL='\e[m'

PS1="$BCYAN S $BBLUE\u$PURPLE@$BBLUE\h$BGREEN ~>$NORMAL ";export PS1

alias ll="ls -lsrt"
```

## Collection

 - Name: [intentions/Singularitytest](https://github.com/intentions/Singularitytest)
 - License: None

