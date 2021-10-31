---
id: 11529
name: "Dill-PICL/GOMAP-base"
branch: "master"
tag: "latest"
commit: "6092de4e799c67c49787c0780f158a827acb1084"
version: "28a6d1a857a66ff73aba068975ee84fd488b162231feab735b70eb563e8c7354"
build_date: "2020-12-26T17:32:07.543Z"
size_mb: 833.1640625
size: 873635840
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-base/latest/2020-12-26-6092de4e-28a6d1a8/28a6d1a857a66ff73aba068975ee84fd488b162231feab735b70eb563e8c7354.sif"
url: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-base/latest/2020-12-26-6092de4e-28a6d1a8/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-base/latest/2020-12-26-6092de4e-28a6d1a8/Singularity
collection: Dill-PICL/GOMAP-base
---

# Dill-PICL/GOMAP-base:latest

```bash
$ singularity pull shub://Dill-PICL/GOMAP-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
BASE_OWNER Wimalanathan Kokulapalan
BASE_MAINTAINER Wimalanathan Kokulapalan
BASE_VERSION 1.1.1

%environment
	export IRODS_HOST="data.cyverse.org"
	export  IRODS_PORT="1247"
    export  IRODS_USER_NAME="anonymous"
    export  IRODS_ZONE_NAME="iplant"

%post
	export LC_ALL=C
	export DEBIAN_FRONTEND=noninteractive
	export TZ=America/Chicago
	echo "Running post.sh"
	apt-get -q -y update
	apt-get -yq install bsdutils lsb-base passwd perl psmisc debconf libc6 libevent-core-2.1-6 libgcc1 liblz4-1 libstdc++6 zlib1g gfortran rsync build-essential less vim wget python-pip libfuse2 r-base openjdk-8-jdk libidn11-dev libssl1.0-dev libssl1.0.0 git ncbi-blast+ octave octave-dataframe sqlite3 libsqlite3-dev python3-pip
	update-java-alternatives -s java-1.8.0-openjdk-amd64 

	R -e 'install.packages(c("data.table","futile.logger","ontologyIndex","yaml"), repos="https://mirror.las.iastate.edu/CRAN/", INSTALL_opts="--no-html")'

	pip install numpy==1.14.5
	pip install pyrsistent==0.14.0
	pip install scipy==1.1.0
	pip install jsonmerge==1.5.1
	pip install jsonschema==2.6.0
	pip install lxml==4.2.1
	pip install PyYAML==3.12
	pip install yamldirs==1.1.3
	pip install pyrocopy==0.8.0  
	pip install requests==2.19.1
	pip install requests-toolbelt==0.8.0
	pip install numpydoc==0.8.0
	pip install biopython==1.70
	pip install joblib==0.12.2
	pip install natsort==5.3.3

	wget "https://files.renci.org/pub/irods/releases/4.1.12/ubuntu14/irods-icommands-4.1.12-ubuntu14-x86_64.deb"
	dpkg -i irods-icommands-4.1.12-ubuntu14-x86_64.deb

	ls 
	
	
	wget -O azcopy_v10.tar.gz https://aka.ms/downloadazcopy-v10-linux && \
	tar -xf azcopy_v10.tar.gz --strip-components=1 && \
	cp azcopy /usr/bin/ && \
	chmod 755 /usr/bin/azcopy

	echo "=============================================="
	echo "Completed Post" 
	echo "=============================================="

%startscript
	chmod 777 /tmp

%runscript
	cd /opt/GOMAP/ 
	./gomap.py "$@"
```

## Collection

 - Name: [Dill-PICL/GOMAP-base](https://github.com/Dill-PICL/GOMAP-base)
 - License: None

