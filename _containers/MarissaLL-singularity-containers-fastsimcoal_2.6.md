---
id: 3638
name: "MarissaLL/singularity-containers"
branch: "master"
tag: "fastsimcoal_2.6"
commit: "e34376dabe1cf7634e40ed8f2eed3207be3d5594"
version: "6081abe4ab765de9d920af30f176c2c9"
build_date: "2020-05-22T06:23:43.953Z"
size_mb: 383
size: 175448095
sif: "https://datasets.datalad.org/shub/MarissaLL/singularity-containers/fastsimcoal_2.6/2020-05-22-e34376da-6081abe4/6081abe4ab765de9d920af30f176c2c9.simg"
url: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/fastsimcoal_2.6/2020-05-22-e34376da-6081abe4/
recipe: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/fastsimcoal_2.6/2020-05-22-e34376da-6081abe4/Singularity
collection: MarissaLL/singularity-containers
---

# MarissaLL/singularity-containers:fastsimcoal_2.6

```bash
$ singularity pull shub://MarissaLL/singularity-containers:fastsimcoal_2.6
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: build-essential language-pack-en wget unzip

%labels

	MAINTAINER "Marissa Le Lec"
	VERSION "fastsimcoal 2.6"

%post

	wget http://cmpg.unibe.ch/software/fastsimcoal2/downloads/fsc26_linux64.zip
	unzip fsc26_linux64.zip
	cd fsc26_linux64 || exit 1
	chmod +x fsc26
	cp fsc26 /usr/local/bin/fsc26
	cd .. || exit 1
	rm -rf fsc26_linux64

%runscript
	exec /usr/local/bin/fsc26 "$@"
```

## Collection

 - Name: [MarissaLL/singularity-containers](https://github.com/MarissaLL/singularity-containers)
 - License: None

