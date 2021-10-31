---
id: 11800
name: "thakk/lolcow"
branch: "master"
tag: "latest"
commit: "3cf95c24e6286ce9179bd31bd8bf05b1695d4d65"
version: "88846654122efbbf01afa817b4fb8a3e"
build_date: "2020-12-17T14:09:26.002Z"
size_mb: 76.0
size: 24125471
sif: "https://datasets.datalad.org/shub/thakk/lolcow/latest/2020-12-17-3cf95c24-88846654/88846654122efbbf01afa817b4fb8a3e.sif"
url: https://datasets.datalad.org/shub/thakk/lolcow/latest/2020-12-17-3cf95c24-88846654/
recipe: https://datasets.datalad.org/shub/thakk/lolcow/latest/2020-12-17-3cf95c24-88846654/Singularity
collection: thakk/lolcow
---

# thakk/lolcow:latest

```bash
$ singularity pull shub://thakk/lolcow:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine:3.10.3

%post
	apk update
	apk add fortune
	apk add -X http://dl-cdn.alpinelinux.org/alpine/edge/testing lolcat
	apk add perl
	apk add git
	apk add bash
	git clone https://github.com/tnalpgge/rank-amateur-cowsay
	cd rank-amateur-cowsay/
	./install.sh /

%environment
	export LC_ALL=C
	export PATH=/usr/games:$PATH

%runscript
	fortune | cowsay | lolcat

%labels
	Author "SoMany"
	Version 0.1
```

## Collection

 - Name: [thakk/lolcow](https://github.com/thakk/lolcow)
 - License: None

