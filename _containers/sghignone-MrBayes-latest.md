---
id: 12644
name: "sghignone/MrBayes"
branch: "master"
tag: "latest"
commit: "b999235188f5dcf272d704c421c0ee74889aabdd"
version: "6492c6dd49eae023cd276ea74c4a59b0"
build_date: "2020-04-01T16:22:19.526Z"
size_mb: 268.0
size: 94003231
sif: "https://datasets.datalad.org/shub/sghignone/MrBayes/latest/2020-04-01-b9992351-6492c6dd/6492c6dd49eae023cd276ea74c4a59b0.sif"
url: https://datasets.datalad.org/shub/sghignone/MrBayes/latest/2020-04-01-b9992351-6492c6dd/
recipe: https://datasets.datalad.org/shub/sghignone/MrBayes/latest/2020-04-01-b9992351-6492c6dd/Singularity
collection: sghignone/MrBayes
---

# sghignone/MrBayes:latest

```bash
$ singularity pull shub://sghignone/MrBayes:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:latest

%post
	export MPICH_VERSION="3.2"
	export MPICH_CONFIGURE_OPTIONS="--disable-fortran"
	export MPICH_MAKE_OPTIONS

	apk update && apk upgrade \
	&& apk add --no-cache sudo build-base \
	git g++ make automake autoconf

	#install MPI
	mkdir /tmp/mpich-src
	cd /tmp/mpich-src
	wget http://www.mpich.org/static/downloads/${MPICH_VERSION}/mpich-${MPICH_VERSION}.tar.gz \
	&& tar -xzf mpich-${MPICH_VERSION}.tar.gz \
	&& cd mpich-${MPICH_VERSION} \
	&& ./configure ${MPICH_CONFIGURE_OPTIONS} \
	&& make ${MPICH_OPTIONS} && make install \
	&& rm -rf /tmp/mpich-src/

	#install MrBayes
	mkdir /tmp/mrbayes
	cd /tmp/mrbayes
	git clone --depth=1 https://github.com/NBISweden/MrBayes.git
	cd MrBayes/ \
	&& ./configure --with-mpi --without-beagle \
	&& make && make install \
	&& rm -rf /tmp/mrbayes

%labels
	author Stefano Ghignone
	maintainer sghignone
	name MrBayes
	version v3.2.7a
```

## Collection

 - Name: [sghignone/MrBayes](https://github.com/sghignone/MrBayes)
 - License: None

