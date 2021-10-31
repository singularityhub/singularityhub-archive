---
id: 2288
name: "alexiswl/singularity"
branch: "master"
tag: "nanopolish"
commit: "4ba356918e6ead2c825d6e64b7229ee3496e4e6f"
version: "94cda17ddae8825c49e3c44c095cde02"
build_date: "2018-03-26T10:14:22.756Z"
size_mb: 1256
size: 388702239
sif: "https://datasets.datalad.org/shub/alexiswl/singularity/nanopolish/2018-03-26-4ba35691-94cda17d/94cda17ddae8825c49e3c44c095cde02.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/alexiswl/singularity/nanopolish/2018-03-26-4ba35691-94cda17d/
recipe: https://datasets.datalad.org/shub/alexiswl/singularity/nanopolish/2018-03-26-4ba35691-94cda17d/Singularity
collection: alexiswl/singularity
---

# alexiswl/singularity:nanopolish

```bash
$ singularity pull shub://alexiswl/singularity:nanopolish
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
Singularity container for nanopolish

%labels
	Maintainer Alexis Lucattini
	Version v1.0

%post
	cd /
	yum group install "Development Tools" -y
	yum install git wget tar zlib-devel -y
	git clone --recursive https://github.com/jts/nanopolish.git
	cd /nanopolish
	make all

%runscript
	exec ./nanopolish "$@"
```

## Collection

 - Name: [alexiswl/singularity](https://github.com/alexiswl/singularity)
 - License: None

