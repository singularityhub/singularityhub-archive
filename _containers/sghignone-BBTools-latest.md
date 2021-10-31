---
id: 12653
name: "sghignone/BBTools"
branch: "master"
tag: "latest"
commit: "6047ccf7437683806a21d48ad260cf5dde8f64a6"
version: "242079d57b057aa4115bf34f7394a9e7"
build_date: "2021-03-25T19:59:14.966Z"
size_mb: 323.0
size: 112119839
sif: "https://datasets.datalad.org/shub/sghignone/BBTools/latest/2021-03-25-6047ccf7-242079d5/242079d57b057aa4115bf34f7394a9e7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sghignone/BBTools/latest/2021-03-25-6047ccf7-242079d5/
recipe: https://datasets.datalad.org/shub/sghignone/BBTools/latest/2021-03-25-6047ccf7-242079d5/Singularity
collection: sghignone/BBTools
---

# sghignone/BBTools:latest

```bash
$ singularity pull shub://sghignone/BBTools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: anapsix/alpine-java:latest


%labels
	author Stefano Ghignone
	maintainer sghignone
	name BBTools
	version v38.90 (released 2021-02-03) 
	bbmap 38.90
%post
	apk update && apk upgrade \
	&& apk add --no-cache sudo build-base wget

	#download and unpack bbtools from Sourgeforge
	wget -c https://downloads.sourceforge.net/project/bbmap/BBMap_38.90.tar.gz -P /opt/
	tar -xvzf /opt/BBMap_38.90.tar.gz -C /opt/
	rm /opt/BBMap_38.90.tar.gz

%environment
	export PATH=/opt/bbmap:$PATH
```

## Collection

 - Name: [sghignone/BBTools](https://github.com/sghignone/BBTools)
 - License: None

