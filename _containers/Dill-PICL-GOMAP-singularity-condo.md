---
id: 5720
name: "Dill-PICL/GOMAP-singularity"
branch: "master"
tag: "condo"
commit: "624dc0da4ca3229e90f15531da31ad1a89131202"
version: "9fdf2610efd3355dddf5182adbf8eab9"
build_date: "2019-02-17T21:45:23.945Z"
size_mb: 1985
size: 707297311
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/condo/2019-02-17-624dc0da-9fdf2610/9fdf2610efd3355dddf5182adbf8eab9.simg"
url: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/condo/2019-02-17-624dc0da-9fdf2610/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/condo/2019-02-17-624dc0da-9fdf2610/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:condo

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:condo
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: Dill-PICL/GOMAP-base:bionic

%labels
MAINTAINER Kokulapalan Wimalanathan
Version 1.1.0
Branch ISU-condo

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
    wget http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz  && \
    tar -xf  mpich-3.2.1.tar.gz && \
    cd mpich-3.2.1 &&  \
    ./configure && make -j4 && make install && \
    cd ..
    
	pip install mpi4py==3.0.0

	mkdir /opt/GOMAP/
	git clone --branch=master https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
	chmod -R 777 /opt/GOMAP/
	mkdir -p /workdir
	mkdir -p /tmpdir
	mkdir -p /work
	mkdir -p /scratch 
	mkdir -p /var/log/mysql 
	
	echo "Completed Post "

%startscript
	nohup mysqld --user=$USER > /workdir/tmp/mysql.log 2> /workdir/tmp/mysql.err < /dev/null &

%runscript
	cd /opt/GOMAP/ 
	./gomap.py "$@"
```

## Collection

 - Name: [Dill-PICL/GOMAP-singularity](https://github.com/Dill-PICL/GOMAP-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

