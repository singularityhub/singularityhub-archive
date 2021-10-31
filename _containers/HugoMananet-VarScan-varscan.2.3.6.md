---
id: 5751
name: "HugoMananet/VarScan"
branch: "master"
tag: "varscan.2.3.6"
commit: "81c4b04a33c07968aa8b3498530289fdc6d29259"
version: "dc0cebb70178c6ef9a6cad063e163a37"
build_date: "2018-11-30T19:45:31.341Z"
size_mb: 752
size: 271675423
sif: "https://datasets.datalad.org/shub/HugoMananet/VarScan/varscan.2.3.6/2018-11-30-81c4b04a-dc0cebb7/dc0cebb70178c6ef9a6cad063e163a37.simg"
url: https://datasets.datalad.org/shub/HugoMananet/VarScan/varscan.2.3.6/2018-11-30-81c4b04a-dc0cebb7/
recipe: https://datasets.datalad.org/shub/HugoMananet/VarScan/varscan.2.3.6/2018-11-30-81c4b04a-dc0cebb7/Singularity
collection: HugoMananet/VarScan
---

# HugoMananet/VarScan:varscan.2.3.6

```bash
$ singularity pull shub://HugoMananet/VarScan:varscan.2.3.6
```

## Singularity Recipe

```singularity
#!/bin/bash
#

Bootstrap: docker
From: phusion/baseimage:0.11

%label
	MAINTAINER Hugo Mananet
	VERSION 2.3.6


%post
	apt-get -y update
	apt-get -y install build-essential \
	wget \
	openjdk-8-jre \

	mkdir -p /opt/varscan_2.3.6
	wget http://netcologne.dl.sourceforge.net/project/varscan/VarScan.v2.3.6.jar && mv VarScan.v2.3.6.jar /opt/varscan_2.3.6/VarScan.jar

#%environment
#	export LANGUAGE=fr_FR.UTF-8
#	export LANG=fr_FR.UTF-8
#	export LC_ALL=fr_FR.UTF-8
```

## Collection

 - Name: [HugoMananet/VarScan](https://github.com/HugoMananet/VarScan)
 - License: [Other](None)

