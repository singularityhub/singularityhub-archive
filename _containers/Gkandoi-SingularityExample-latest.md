---
id: 3600
name: "Gkandoi/SingularityExample"
branch: "master"
tag: "latest"
commit: "8e6587003ea191773ef24c26879103514d0ba0ca"
version: "343f7acdaf24be61bd09264c7f465675"
build_date: "2018-07-20T04:10:47.464Z"
size_mb: 14
size: 7901215
sif: "https://datasets.datalad.org/shub/Gkandoi/SingularityExample/latest/2018-07-20-8e658700-343f7acd/343f7acdaf24be61bd09264c7f465675.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Gkandoi/SingularityExample/latest/2018-07-20-8e658700-343f7acd/
recipe: https://datasets.datalad.org/shub/Gkandoi/SingularityExample/latest/2018-07-20-8e658700-343f7acd/Singularity
collection: Gkandoi/SingularityExample
---

# Gkandoi/SingularityExample:latest

```bash
$ singularity pull shub://Gkandoi/SingularityExample:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine

%post
	apk update
	apk add wget
	wget http://github.com/bbuchfink/diamond/releases/download/v0.9.22/diamond-linux64.tar.gz
	tar xzf diamond-linux64.tar.gz
	wget https://raw.githubusercontent.com/upendrak/diamond_blast_docker/master/mouse.1.protein.faa
	wget https://raw.githubusercontent.com/upendrak/diamond_blast_docker/master/zebrafish.1.protein.faa

%environment
	export PATH=/:$PATH

%runscript
	diamond


## Sample Singularity file created during NSF Cyber Carpentry 2018. Parts taken from the original Diamond dockerfile and lecture notes.
```

## Collection

 - Name: [Gkandoi/SingularityExample](https://github.com/Gkandoi/SingularityExample)
 - License: None

