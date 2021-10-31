---
id: 3352
name: "bpow/bioinfo-containers"
branch: "master"
tag: "debian"
commit: "38439e639bfc50c5bfd911909f2f2cc69a4ae615"
version: "4d62e8b475947064668ae80c1b6dabc9"
build_date: "2019-10-03T19:14:20.162Z"
size_mb: 523
size: 187490335
sif: "https://datasets.datalad.org/shub/bpow/bioinfo-containers/debian/2019-10-03-38439e63-4d62e8b4/4d62e8b475947064668ae80c1b6dabc9.simg"
url: https://datasets.datalad.org/shub/bpow/bioinfo-containers/debian/2019-10-03-38439e63-4d62e8b4/
recipe: https://datasets.datalad.org/shub/bpow/bioinfo-containers/debian/2019-10-03-38439e63-4d62e8b4/Singularity
collection: bpow/bioinfo-containers
---

# bpow/bioinfo-containers:debian

```bash
$ singularity pull shub://bpow/bioinfo-containers:debian
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stretch
MirrorURL: http://httpredir.debian.org/debian

%help
	A collection of tools for analysis of high-throughput sequence data

%runscript
    echo "I'm just going to go ahead and drop you into a shell..."
	/bin/bash


%post
    set -eu
    apt-get update
    apt-get -y install --no-install-recommends bwa fastqc samtools bcftools tabix picard-tools
    apt-get clean
	rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bpow/bioinfo-containers](https://github.com/bpow/bioinfo-containers)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

