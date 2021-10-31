---
id: 5719
name: "Dill-PICL/GOMAP-singularity"
branch: "master"
tag: "comet"
commit: "26636dc00365d1aef1801d9207aab989fcb598ee"
version: "b88022508511e06198b13967530eaadf"
build_date: "2019-01-31T22:31:28.034Z"
size_mb: 1887
size: 701308959
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/comet/2019-01-31-26636dc0-b8802250/b88022508511e06198b13967530eaadf.simg"
url: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/comet/2019-01-31-26636dc0-b8802250/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/comet/2019-01-31-26636dc0-b8802250/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:comet

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:comet
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: Dill-PICL/GOMAP-base:xenial

%labels
MAINTAINER Kokulapalan Wimalanathan
Version 1.1.0
Branch Comet

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
	mkdir -p /oasis /projects /scratch
	
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

