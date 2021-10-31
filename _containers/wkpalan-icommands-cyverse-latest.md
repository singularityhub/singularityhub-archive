---
id: 11502
name: "wkpalan/icommands-cyverse"
branch: "master"
tag: "latest"
commit: "8ceb6400b74e7a38b961bfb2715f2297972eb65d"
version: "a29cba509af365fff79cee502fddabbca0f423eff45603054f07383f70645a1e"
build_date: "2021-04-19T21:25:59.115Z"
size_mb: 109.61328125
size: 114937856
sif: "https://datasets.datalad.org/shub/wkpalan/icommands-cyverse/latest/2021-04-19-8ceb6400-a29cba50/a29cba509af365fff79cee502fddabbca0f423eff45603054f07383f70645a1e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/wkpalan/icommands-cyverse/latest/2021-04-19-8ceb6400-a29cba50/
recipe: https://datasets.datalad.org/shub/wkpalan/icommands-cyverse/latest/2021-04-19-8ceb6400-a29cba50/Singularity
collection: wkpalan/icommands-cyverse
---

# wkpalan/icommands-cyverse:latest

```bash
$ singularity pull shub://wkpalan/icommands-cyverse:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
OWNER Kokulapalan Wimalanathan
MAINTAINER Kokulapalan Wimalanathan
ICOMMANDS_Version 4.1.12

%environment
    export LC_ALL=C 
    export DEBIAN_FRONTEND=noninteractive

%post
    
    export IRODS_HOST="data.cyverse.org"
    export IRODS_PORT="1247"
    export IRODS_USER_NAME="anonymous"
    export IRODS_ZONE_NAME="iplant"
    
	echo "Running Post"

	apt-get -yq update
    apt-get -yq install wget gnupg2
    
    wget -qO - https://packages.irods.org/irods-signing-key.asc | apt-key add -
    echo "deb [arch=amd64] https://packages.irods.org/apt/ bionic main" | tee /etc/apt/sources.list.d/renci-irods.list
    apt-get -yq update
    apt-get -yq install irods-icommands

	#wget https://files.renci.org/pub/irods/releases/4.1.12/ubuntu14/irods-icommands-4.1.12-ubuntu14-x86_64.deb
	#dpkg -i irods-icommands-4.1.12-ubuntu14-x86_64.deb
   
    ils /iplant/home/shared/dillpicl

	echo "=============================================="
	echo "Completed Post" 
	echo "=============================================="
```

## Collection

 - Name: [wkpalan/icommands-cyverse](https://github.com/wkpalan/icommands-cyverse)
 - License: None

