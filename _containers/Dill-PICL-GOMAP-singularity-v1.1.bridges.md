---
id: 8523
name: "Dill-PICL/GOMAP-singularity"
branch: "v1.1"
tag: "v1.1.bridges"
commit: "3e5ff1f5605b38a8bb2779d7e60e8273307826cb"
version: "176a7ddf522dd428f2c2809ff2b7faa0"
build_date: "2019-04-20T16:49:50.292Z"
size_mb: 2503
size: 889364511
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1.bridges/2019-04-20-3e5ff1f5-176a7ddf/176a7ddf522dd428f2c2809ff2b7faa0.simg"
url: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1.bridges/2019-04-20-3e5ff1f5-176a7ddf/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1.bridges/2019-04-20-3e5ff1f5-176a7ddf/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:v1.1.bridges

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:v1.1.bridges
```

## Singularity Recipe

```singularity
Bootstrap: shub 
From: Dill-PICL/GOMAP-base:bionic

%labels
MAINTAINER Kokulapalan Wimalanathan
Version 1.1
HPC PSC-Bridges

%files 

%environment
    export LC_ALL=C 
    export DEBIAN_FRONTEND=noninteractive
    export MYSQL_USER=pannzer
    export MYSQL_DATABASE=pannzer
    export MYSQL_ROOT_PASSWORD=mysql 

%post
    echo "Running post"

    #Installing mpich 
    wget http://www.mpich.org/static/downloads/3.2/mpich-3.2.tar.gz &&  \
    tar -xf  mpich-3.2.tar.gz && \
    cd mpich-3.2 &&  \
    ./configure && make -j4 && make install && \
    cd .. 
    
	pip install mpi4py==3.0.0  

	mkdir /opt/GOMAP/
	git clone --branch=v1.1 https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
	chmod -R 777 /opt/GOMAP/
	mkdir -p /workdir
	mkdir -p /tmpdir
	mkdir -p /var/log/mysql
	

	echo "Completed Post"

%startscript
	chmod 777 /tmp
	nohup mysqld --user=$USER > /dev/null 2>&1 < /dev/null &

%runscript
	cd /opt/GOMAP/ 
	./gomap.py "$@"
```

## Collection

 - Name: [Dill-PICL/GOMAP-singularity](https://github.com/Dill-PICL/GOMAP-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

