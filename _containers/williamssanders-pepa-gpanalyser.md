---
id: 7207
name: "williamssanders/pepa"
branch: "master"
tag: "gpanalyser"
commit: "fe1f07628ebfcab3dafb8833109f6063bbe11722"
version: "f26fd584f0d5f0444dbbaee36469863d"
build_date: "2020-01-10T17:50:41.833Z"
size_mb: 563
size: 203087903
sif: "https://datasets.datalad.org/shub/williamssanders/pepa/gpanalyser/2020-01-10-fe1f0762-f26fd584/f26fd584f0d5f0444dbbaee36469863d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/williamssanders/pepa/gpanalyser/2020-01-10-fe1f0762-f26fd584/
recipe: https://datasets.datalad.org/shub/williamssanders/pepa/gpanalyser/2020-01-10-fe1f0762-f26fd584/Singularity
collection: williamssanders/pepa
---

# williamssanders/pepa:gpanalyser

```bash
$ singularity pull shub://williamssanders/pepa:gpanalyser
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:6

%files
	#/home/ssanders/Desktop/GPEPA/jdk-6u45-linux-x64.bin /opt
%post
	echo "Updating system"
	yum update -y
	echo "Installing xauth and xterm"
	yum install -y xauth xterm wget unzip libXtst.x86_64 mesa-libGL.x86_64
	echo "Installing JRE 1.6"
	cd /opt
	#/bin/bash /opt/jdk-6u45-linux-x64.bin
	#alternatives --install /usr/bin/java java /opt/jdk1.6.0_45/bin/java 1
	#alternatives --set java /opt/jdk1.6.0_45/bin/java
	yum install -y java-1.7.0-openjdk-devel
	echo "Downloading gpa and examples"
	wget "https://storage.googleapis.com/google-code-archive-source/v2/code.google.com/gpanalyser/models.source-archive.zip"
	wget "https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/gpanalyser/gpa-0.9.2.zip"
	unzip models.source-archive.zip
	unzip gpa-0.9.2.zip
	#rm *.zip jdk-6u45-linux-x64.bin

%runscript
	cd /opt/gpa-0.9.2 
	exec bash gpa-0.9.2-linux-amd64.sh "$@"
```

## Collection

 - Name: [williamssanders/pepa](https://github.com/williamssanders/pepa)
 - License: None

