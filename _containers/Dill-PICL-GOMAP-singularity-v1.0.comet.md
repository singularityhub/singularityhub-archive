---
id: 7699
name: "Dill-PICL/GOMAP-singularity"
branch: "v1.0"
tag: "v1.0.comet"
commit: "12ebff9dcf792a500b1ebf6fb810c4b1c3920c34"
version: "4b4fa61927aeb5c1c8ee27ae364fe851"
build_date: "2019-03-12T08:04:32.431Z"
size_mb: 1880
size: 693723167
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0.comet/2019-03-12-12ebff9d-4b4fa619/4b4fa61927aeb5c1c8ee27ae364fe851.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Dill-PICL/GOMAP-singularity/v1.0.comet/2019-03-12-12ebff9d-4b4fa619/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0.comet/2019-03-12-12ebff9d-4b4fa619/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:v1.0.comet

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:v1.0.comet
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
	git clone --branch=v1.0 https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
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

