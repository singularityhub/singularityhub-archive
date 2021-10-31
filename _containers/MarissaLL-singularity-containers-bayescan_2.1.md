---
id: 3580
name: "MarissaLL/singularity-containers"
branch: "master"
tag: "bayescan_2.1"
commit: "e34376dabe1cf7634e40ed8f2eed3207be3d5594"
version: "1d8731632aee596881ab88d0b1aa4e9d"
build_date: "2020-09-24T18:13:32.335Z"
size_mb: 384
size: 176492575
sif: "https://datasets.datalad.org/shub/MarissaLL/singularity-containers/bayescan_2.1/2020-09-24-e34376da-1d873163/1d8731632aee596881ab88d0b1aa4e9d.simg"
url: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/bayescan_2.1/2020-09-24-e34376da-1d873163/
recipe: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/bayescan_2.1/2020-09-24-e34376da-1d873163/Singularity
collection: MarissaLL/singularity-containers
---

# MarissaLL/singularity-containers:bayescan_2.1

```bash
$ singularity pull shub://MarissaLL/singularity-containers:bayescan_2.1
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential language-pack-en wget unzip

%labels

	MAINTAINER "Marissa Le Lec"
	VERSION "BayeScan 2.1"

%post

	wget http://cmpg.unibe.ch/software/BayeScan/files/BayeScan2.1.zip
	unzip BayeScan2.1.zip
	cd BayeScan2.1/source || exit 1
	make
	cp bayescan_2.1 /usr/local/bin/
	cd ../.. || exit 1
	rm -rf BayeScan2.1

%runscript
    exec /usr/local/bin/bayescan_2.1 "$@"
```

## Collection

 - Name: [MarissaLL/singularity-containers](https://github.com/MarissaLL/singularity-containers)
 - License: None

