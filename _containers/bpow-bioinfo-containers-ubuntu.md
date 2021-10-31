---
id: 3353
name: "bpow/bioinfo-containers"
branch: "master"
tag: "ubuntu"
commit: "38439e639bfc50c5bfd911909f2f2cc69a4ae615"
version: "3c844ca597776cf567be5187ff5cdb48"
build_date: "2018-06-29T02:57:07.358Z"
size_mb: 562
size: 195387423
sif: "https://datasets.datalad.org/shub/bpow/bioinfo-containers/ubuntu/2018-06-29-38439e63-3c844ca5/3c844ca597776cf567be5187ff5cdb48.simg"
url: https://datasets.datalad.org/shub/bpow/bioinfo-containers/ubuntu/2018-06-29-38439e63-3c844ca5/
recipe: https://datasets.datalad.org/shub/bpow/bioinfo-containers/ubuntu/2018-06-29-38439e63-3c844ca5/Singularity
collection: bpow/bioinfo-containers
---

# bpow/bioinfo-containers:ubuntu

```bash
$ singularity pull shub://bpow/bioinfo-containers:ubuntu
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
	A collection of tools for analysis of high-throughput sequence data

%runscript
    echo "I'm just going to go ahead and drop you into a shell..."
	/bin/bash


%post
    set -eu
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get update
    apt-get -y install --no-install-recommends bwa fastqc samtools bcftools tabix picard-tools
    apt-get clean
	rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bpow/bioinfo-containers](https://github.com/bpow/bioinfo-containers)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

