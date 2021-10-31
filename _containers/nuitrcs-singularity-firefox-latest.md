---
id: 7582
name: "nuitrcs/singularity-firefox"
branch: "master"
tag: "latest"
commit: "51097bc3b9718be73fb4bb817f1aa3ca407b140c"
version: "143479e0ac6e60e0d93d72fdf57bd2cc"
build_date: "2021-04-17T07:21:41.310Z"
size_mb: 544
size: 193634335
sif: "https://datasets.datalad.org/shub/nuitrcs/singularity-firefox/latest/2021-04-17-51097bc3-143479e0/143479e0ac6e60e0d93d72fdf57bd2cc.simg"
url: https://datasets.datalad.org/shub/nuitrcs/singularity-firefox/latest/2021-04-17-51097bc3-143479e0/
recipe: https://datasets.datalad.org/shub/nuitrcs/singularity-firefox/latest/2021-04-17-51097bc3-143479e0/Singularity
collection: nuitrcs/singularity-firefox
---

# nuitrcs/singularity-firefox:latest

```bash
$ singularity pull shub://nuitrcs/singularity-firefox:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post 
	yum update -y
	yum install -y firefox

%runscript
	firefox
```

## Collection

 - Name: [nuitrcs/singularity-firefox](https://github.com/nuitrcs/singularity-firefox)
 - License: None

