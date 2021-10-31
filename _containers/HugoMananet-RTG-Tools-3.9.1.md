---
id: 5261
name: "HugoMananet/RTG-Tools"
branch: "master"
tag: "3.9.1"
commit: "bf130f377e5ad232043fcfb7d74d4675f77060fb"
version: "e1047a0378ddb7d7faae94eb1d120da8"
build_date: "2018-10-18T10:53:34.330Z"
size_mb: 998
size: 363274271
sif: "https://datasets.datalad.org/shub/HugoMananet/RTG-Tools/3.9.1/2018-10-18-bf130f37-e1047a03/e1047a0378ddb7d7faae94eb1d120da8.simg"
url: https://datasets.datalad.org/shub/HugoMananet/RTG-Tools/3.9.1/2018-10-18-bf130f37-e1047a03/
recipe: https://datasets.datalad.org/shub/HugoMananet/RTG-Tools/3.9.1/2018-10-18-bf130f37-e1047a03/Singularity
collection: HugoMananet/RTG-Tools
---

# HugoMananet/RTG-Tools:3.9.1

```bash
$ singularity pull shub://HugoMananet/RTG-Tools:3.9.1
```

## Singularity Recipe

```singularity
#!/bin/bash
#

Bootstrap: docker
From: phusion/baseimage:0.11

%label
	MAINTAINER Hugo Mananet
	VERSION 3.9.1


%environment

	JAVA_LIBRARY_PATH=/usr/lib/jni
	JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
	ANT_HOME=/opt/apache-ant-1.10.5/
	export JAVA_LIBRARY_PATH JAVA_HOME ANT_HOME

	PATH=/opt/apache-ant-1.10.5/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
	export PATH

%post
	apt-get -y update
	apt-get -y install build-essential \
	wget \
	openjdk-8-jdk \
	tar \
	unzip

	wget -P /opt/ https://www.apache.org/dist/ant/binaries/apache-ant-1.10.5-bin.tar.gz
	cd /opt && tar -xvf apache-ant-1.10.5-bin.tar.gz
	rm /opt/apache-ant-1.10.5-bin.tar.gz
	cd /opt/apache-ant-1.10.5/ && /opt/apache-ant-1.10.5/bin/ant -autoproxy -f fetch.xml -Ddest=system
	ln -s /opt/apache-ant-1.10.5/bin/ant /usr/local/bin/

	mkdir -p /opt/rtg-tools/
	wget -P /opt/ https://github.com/RealTimeGenomics/rtg-tools/releases/download/3.9.1/rtg-tools-3.9.1-linux-x64.zip
	unzip -d /opt/ /opt/rtg-tools-3.9.1-linux-x64.zip
	rm /opt/rtg-tools-3.9.1-linux-x64.zip
	chmod 777 /opt/rtg-tools-3.9.1/*
	chmod 777 /opt/rtg-tools-3.9.1/scripts/*
	chmod 777 /opt/rtg-tools-3.9.1/third-party/*
	ln -s /opt/rtg-tools-3.9.1/RTG.jar /usr/local/bin/RTG.jar


%runscript

	java -jar /opt/rtg-tools-3.9.1/RTG.jar "$@"
```

## Collection

 - Name: [HugoMananet/RTG-Tools](https://github.com/HugoMananet/RTG-Tools)
 - License: [Other](None)

