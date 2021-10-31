---
id: 3550
name: "jdwheaton/singularity-ngs"
branch: "master"
tag: "basemount"
commit: "e27909088135c8a2d69e9bc5d74c8b0485b34f17"
version: "ead2a9c4fef4832ac54b1157a3c432a3"
build_date: "2018-07-16T12:36:59.545Z"
size_mb: 435
size: 112537631
sif: "https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/basemount/2018-07-16-e2790908-ead2a9c4/ead2a9c4fef4832ac54b1157a3c432a3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jdwheaton/singularity-ngs/basemount/2018-07-16-e2790908-ead2a9c4/
recipe: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/basemount/2018-07-16-e2790908-ead2a9c4/Singularity
collection: jdwheaton/singularity-ngs
---

# jdwheaton/singularity-ngs:basemount

```bash
$ singularity pull shub://jdwheaton/singularity-ngs:basemount
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

# This container holds Illumina BaseMount for accessing Basespace data

%post
	# Install required build tools
    yum -y update
    yum -y install wget gzip bzip2-devel
    bash -c "$(curl -L https://basemount.basespace.illumina.com/install)"
```

## Collection

 - Name: [jdwheaton/singularity-ngs](https://github.com/jdwheaton/singularity-ngs)
 - License: None

