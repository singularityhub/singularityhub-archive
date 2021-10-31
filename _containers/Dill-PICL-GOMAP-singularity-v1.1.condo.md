---
id: 8525
name: "Dill-PICL/GOMAP-singularity"
branch: "v1.1"
tag: "v1.1.condo"
commit: "3e5ff1f5605b38a8bb2779d7e60e8273307826cb"
version: "9682b0337edf6145e64df77dec8dcd8b"
build_date: "2019-04-20T16:49:50.278Z"
size_mb: 2504
size: 889471007
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1.condo/2019-04-20-3e5ff1f5-9682b033/9682b0337edf6145e64df77dec8dcd8b.simg"
url: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1.condo/2019-04-20-3e5ff1f5-9682b033/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1.condo/2019-04-20-3e5ff1f5-9682b033/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:v1.1.condo

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:v1.1.condo
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: Dill-PICL/GOMAP-base:bionic

%labels
MAINTAINER Kokulapalan Wimalanathan
Version 1.1
HPC ISU-condo

%files 

%environment
    export LC_ALL=C
    export DEBIAN_FRONTEND=noninteractive
    export MYSQL_USER=pannzer
    export MYSQL_DATABASE=pannzer
    export MYSQL_ROOT_PASSWORD=mysql
    #export PYTHONUSERBASE="/tmpdir"
 
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
	git clone --branch=v1.1 https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
	chmod -R 777 /opt/GOMAP/
	mkdir -p /workdir
	mkdir -p /tmpdir
	mkdir -p /work
	mkdir -p /scratch 
	mkdir -p /var/log/mysql 
	
	echo "Completed Post"

%startscript
	nohup mysqld --user=$USER > /workdir/tmp/mysql.log 2> /workdir/tmp/mysql.err < /dev/null &

%runscript
	cd /opt/GOMAP/ 
	./gomap.py "$@"
```

## Collection

 - Name: [Dill-PICL/GOMAP-singularity](https://github.com/Dill-PICL/GOMAP-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

