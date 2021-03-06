---
id: 7698
name: "Dill-PICL/GOMAP-singularity"
branch: "v1.0"
tag: "v1.0.bridges"
commit: "12ebff9dcf792a500b1ebf6fb810c4b1c3920c34"
version: "7e17b5bc75c6be10b5f60f7f26f79304"
build_date: "2019-03-11T14:44:01.606Z"
size_mb: 2511
size: 890863647
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0.bridges/2019-03-11-12ebff9d-7e17b5bc/7e17b5bc75c6be10b5f60f7f26f79304.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Dill-PICL/GOMAP-singularity/v1.0.bridges/2019-03-11-12ebff9d-7e17b5bc/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0.bridges/2019-03-11-12ebff9d-7e17b5bc/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:v1.0.bridges

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:v1.0.bridges
```

## Singularity Recipe

```singularity
Bootstrap: shub 
From: Dill-PICL/GOMAP-base:bionic

%labels
MAINTAINER Kokulapalan Wimalanathan
Version 1.1.0
Branch PSC-Bridges

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
	git clone --branch=v1.0 https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
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

