---
id: 8500
name: "Dill-PICL/GOMAP-singularity"
branch: "v1.1"
tag: "v1.1"
commit: "3e5ff1f5605b38a8bb2779d7e60e8273307826cb"
version: "c1de1c8d3ae76592f27ecea135797dd6"
build_date: "2019-04-20T16:49:50.302Z"
size_mb: 2275
size: 845692959
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1/2019-04-20-3e5ff1f5-c1de1c8d/c1de1c8d3ae76592f27ecea135797dd6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Dill-PICL/GOMAP-singularity/v1.1/2019-04-20-3e5ff1f5-c1de1c8d/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.1/2019-04-20-3e5ff1f5-c1de1c8d/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:v1.1

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:v1.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: Dill-PICL/GOMAP-base:bionic

%labels
MAINTAINER Kokulapalan Wimalanathan
Version 1.1
HPC non-mpich

%files
    my.cnf 

%environment
    export LC_ALL=C
    export DEBIAN_FRONTEND=noninteractive
    export MYSQL_USER=pannzer
    export MYSQL_DATABASE=pannzer
    export MYSQL_ROOT_PASSWORD=mysql

%post
	echo "Running post"
	
	mkdir /opt/GOMAP/
	git clone --branch=v1.1 https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
	chmod -R 777 /opt/GOMAP/
	mkdir -p /workdir
	mkdir -p /tmpdir
	mkdir -p /var/log/mysql
    #mv my.cnf /etc/mysql/
	
	echo "Completed Post"  

%startscript
	chmod 777 /tmp
	nohup mysqld > /workdir/tmp/mysql.log 2> /workdir/tmp/mysql.err < /dev/null &

%runscript
	cd /opt/GOMAP/ 
	./gomap.py "$@"
```

## Collection

 - Name: [Dill-PICL/GOMAP-singularity](https://github.com/Dill-PICL/GOMAP-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

