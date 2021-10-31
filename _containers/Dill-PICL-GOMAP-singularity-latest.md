---
id: 5717
name: "Dill-PICL/GOMAP-singularity"
branch: "master"
tag: "latest"
commit: "26636dc00365d1aef1801d9207aab989fcb598ee"
version: "47abddb2428d8cb694224d86bc6cfc91"
build_date: "2021-04-07T03:06:10.886Z"
size_mb: 1761
size: 670318623
sif: "https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/latest/2021-04-07-26636dc0-47abddb2/47abddb2428d8cb694224d86bc6cfc91.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Dill-PICL/GOMAP-singularity/latest/2021-04-07-26636dc0-47abddb2/
recipe: https://datasets.datalad.org/shub/Dill-PICL/GOMAP-singularity/latest/2021-04-07-26636dc0-47abddb2/Singularity
collection: Dill-PICL/GOMAP-singularity
---

# Dill-PICL/GOMAP-singularity:latest

```bash
$ singularity pull shub://Dill-PICL/GOMAP-singularity:latest
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
	git clone --branch=master https://github.com/Dill-PICL/GOMAP.git /opt/GOMAP/
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

