---
id: 9978
name: "spono/gears-singularity"
branch: "master"
tag: "gears-cloudcompare"
commit: "5e52e260c8f22ded9575f7f415b319feaf777b07"
version: "da3a992876ed900f832283fb46fed1f2"
build_date: "2019-06-23T23:32:49.234Z"
size_mb: 2886
size: 1033605151
sif: "https://datasets.datalad.org/shub/spono/gears-singularity/gears-cloudcompare/2019-06-23-5e52e260-da3a9928/da3a992876ed900f832283fb46fed1f2.simg"
url: https://datasets.datalad.org/shub/spono/gears-singularity/gears-cloudcompare/2019-06-23-5e52e260-da3a9928/
recipe: https://datasets.datalad.org/shub/spono/gears-singularity/gears-cloudcompare/2019-06-23-5e52e260-da3a9928/Singularity
collection: spono/gears-singularity
---

# spono/gears-singularity:gears-cloudcompare

```bash
$ singularity pull shub://spono/gears-singularity:gears-cloudcompare
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tswetnam/cloudcompare:latest

%post
  apt-get clean
  apt-get -y update
  apt-get -y install xvfb  

%runscript
	Xvfb :0 -screen 0 1024x768x16 &
```

## Collection

 - Name: [spono/gears-singularity](https://github.com/spono/gears-singularity)
 - License: None

