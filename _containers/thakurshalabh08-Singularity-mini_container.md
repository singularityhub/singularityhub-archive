---
id: 932
name: "thakurshalabh08/Singularity"
branch: "master"
tag: "mini_container"
commit: "474fd17e8ea58f09e66c1ba3a973604cdd4207bb"
version: "d329b74c3bcb49974cd8d649eff8aeb7"
build_date: "2018-05-03T18:41:39.803Z"
size_mb: 275
size: 107126815
sif: "https://datasets.datalad.org/shub/thakurshalabh08/Singularity/mini_container/2018-05-03-474fd17e-d329b74c/d329b74c3bcb49974cd8d649eff8aeb7.simg"
url: https://datasets.datalad.org/shub/thakurshalabh08/Singularity/mini_container/2018-05-03-474fd17e-d329b74c/
recipe: https://datasets.datalad.org/shub/thakurshalabh08/Singularity/mini_container/2018-05-03-474fd17e-d329b74c/Singularity
collection: thakurshalabh08/Singularity
---

# thakurshalabh08/Singularity:mini_container

```bash
$ singularity pull shub://thakurshalabh08/Singularity:mini_container
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
	This is a metagenomics container. Following is the list of programs currently installed within this container.

%runscript

	exec echo "We are running a test container today 3rd May 2018"

%environment
	LC_ALL=C
	PERL5LIB=/usr/share/perl5:/usr/share/perl/5.22.1:/usr/local/share/perl/5.22.1


%post
	apt-get update

%apphelp BLAST

	This is NCBI BLAST command line tool (version 2.2.3)

%appinstall BLAST

	apt -y install ncbi-blast+

%apphelp MUSCLE

	This is a MUSCLE help section

%appinstall MUSCLE

	apt-get -y install muscle
```

## Collection

 - Name: [thakurshalabh08/Singularity](https://github.com/thakurshalabh08/Singularity)
 - License: None

