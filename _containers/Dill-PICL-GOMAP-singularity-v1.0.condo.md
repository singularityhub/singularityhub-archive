---
id: 7700
name: "Dill-PICL/GOMAP-singularity"
branch: "v1.0"
tag: "v1.0.condo"
commit: "12ebff9dcf792a500b1ebf6fb810c4b1c3920c34"
version: "124895496ae3799303a6b6aece9aa35d"
build_date: "2019-03-12T08:04:32.424Z"
size_mb: 2512
size: 890966047
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0.condo/2019-03-12-12ebff9d-12489549/124895496ae3799303a6b6aece9aa35d.simg"
url: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0.condo/2019-03-12-12ebff9d-12489549/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0.condo/2019-03-12-12ebff9d-12489549/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:v1.0.condo

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:v1.0.condo
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
	git clone --branch=v1.0 https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
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

