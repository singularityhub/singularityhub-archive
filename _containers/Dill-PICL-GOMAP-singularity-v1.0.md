---
id: 7697
name: "Dill-PICL/GOMAP-singularity"
branch: "v1.0"
tag: "v1.0"
commit: "12ebff9dcf792a500b1ebf6fb810c4b1c3920c34"
version: "9c27c44e9ad742aa683a991852f59065"
build_date: "2019-03-11T14:28:17.512Z"
size_mb: 2283
size: 847192095
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0/2019-03-11-12ebff9d-9c27c44e/9c27c44e9ad742aa683a991852f59065.simg"
url: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0/2019-03-11-12ebff9d-9c27c44e/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/v1.0/2019-03-11-12ebff9d-9c27c44e/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:v1.0

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:v1.0
```

## Singularity Recipe

```singularity
Bootstrap: shub 
From: Dill-PICL/GOMAP-base:bionic

%labels
MAINTAINER Kokulapalan Wimalanathan
Version 1.1.0
Branch non-mpich

%files

%environment
    export LC_ALL=C
    export DEBIAN_FRONTEND=noninteractive
    export MYSQL_USER=pannzer
    export MYSQL_DATABASE=pannzer
    export MYSQL_ROOT_PASSWORD=mysql 

%post
	echo "Running post"
	
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

