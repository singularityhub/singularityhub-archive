---
id: 13528
name: "ARCLeeds/PHCpack_sing"
branch: "master"
tag: "latest"
commit: "4a152aafd7f284b74e4261f8bf38d2ff4564a834"
version: "5b3d90c3bb908f3fe4712107c6d80bf4"
build_date: "2020-07-23T14:13:44.886Z"
size_mb: 427.0
size: 171302943
sif: "https://datasets.datalad.org/shub/ARCLeeds/PHCpack_sing/latest/2020-07-23-4a152aaf-5b3d90c3/5b3d90c3bb908f3fe4712107c6d80bf4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ARCLeeds/PHCpack_sing/latest/2020-07-23-4a152aaf-5b3d90c3/
recipe: https://datasets.datalad.org/shub/ARCLeeds/PHCpack_sing/latest/2020-07-23-4a152aaf-5b3d90c3/Singularity
collection: ARCLeeds/PHCpack_sing
---

# ARCLeeds/PHCpack_sing:latest

```bash
$ singularity pull shub://ARCLeeds/PHCpack_sing:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
	######### download and install Macaulay2
	apt-get update -q
	apt-get install -y curl libblas3 libgfortran4 liblapack3 libquadmath0 libgc1c2 libgdbm5 libreadline7 libxml2
	curl -O https://faculty.math.illinois.edu/Macaulay2/Repositories/Ubuntu/dists/bionic/main/binary-amd64/Macaulay2-1.14-amd64-Linux-Ubuntu-18.04.deb
	curl -O https://faculty.math.illinois.edu/Macaulay2/Repositories/Ubuntu/dists/bionic/main/binary-amd64/Macaulay2-1.14-common.deb
	dpkg -i *.deb

	########## download PHCpack

	# get the m2 code for interfacing with PHCpack
	curl -LO http://www.math.uic.edu/~jan/PHCpack.m2

	# get compiled Linux binary from https://github.com/janverschelde/PHCpack/releases/tag/v2.4.72
	curl -LO https://github.com/janverschelde/PHCpack/files/3564263/x86_64phcv24p.tar.gz
	tar -xf x86_64phcv24p.tar.gz 
	mv phc /usr/bin
	rm x86_64phcv24p.tar.gz

%runscript

  exec /usr/bin/M2 "$@"
```

## Collection

 - Name: [ARCLeeds/PHCpack_sing](https://github.com/ARCLeeds/PHCpack_sing)
 - License: None

