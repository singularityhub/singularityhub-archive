---
id: 5752
name: "HugoMananet/VarScan"
branch: "master"
tag: "varscan.2.4.2"
commit: "808506bce5fddfd6ea579de05d60b0fab3d22f9b"
version: "ea43683d17db00bf4f87952c79985321"
build_date: "2018-12-03T17:26:31.297Z"
size_mb: 705
size: 274321439
sif: "https://datasets.datalad.org/shub/HugoMananet/VarScan/varscan.2.4.2/2018-12-03-808506bc-ea43683d/ea43683d17db00bf4f87952c79985321.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/HugoMananet/VarScan/varscan.2.4.2/2018-12-03-808506bc-ea43683d/
recipe: https://datasets.datalad.org/shub/HugoMananet/VarScan/varscan.2.4.2/2018-12-03-808506bc-ea43683d/Singularity
collection: HugoMananet/VarScan
---

# HugoMananet/VarScan:varscan.2.4.2

```bash
$ singularity pull shub://HugoMananet/VarScan:varscan.2.4.2
```

## Singularity Recipe

```singularity
#!/bin/bash


Bootstrap: docker
From: phusion/baseimage:0.10.2

%label

	MAINTAINER Hugo Mananet
	VERSION 2.4.2

%post

	mkdir /soft
	mkdir /work
	mkdir /user1
	mkdir /user2
	mkdir /tmp3

	apt-get -y update
	apt-get -y install build-essential \
	wget \
	openjdk-8-jre 

	mkdir -p /opt/varscan_2.4.2/
	wget https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar && mv VarScan.v2.4.2.jar /opt/varscan_2.4.2/varscan.jar

%runscript

	java -jar /opt/varscan_2.4.2/varscan.jar "$@"
```

## Collection

 - Name: [HugoMananet/VarScan](https://github.com/HugoMananet/VarScan)
 - License: [Other](None)

