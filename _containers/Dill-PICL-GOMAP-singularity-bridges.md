---
id: 5718
name: "Dill-PICL/GOMAP-singularity"
branch: "master"
tag: "bridges"
commit: "b86e8913e5280dee5a64ae9453a3196095de9e4c"
version: "b2793c32181e7281c67416514effadb6"
build_date: "2019-01-31T21:34:11.946Z"
size_mb: 1989
size: 713969695
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/bridges/2019-01-31-b86e8913-b2793c32/b2793c32181e7281c67416514effadb6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Dill-PICL/GOMAP-singularity/bridges/2019-01-31-b86e8913-b2793c32/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/bridges/2019-01-31-b86e8913-b2793c32/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:bridges

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:bridges
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
	git clone --branch=master   https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
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

