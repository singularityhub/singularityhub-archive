---
id: 9115
name: "wezen/singularity"
branch: "master"
tag: "v1"
commit: "64f33a35742f8918cbc8cac5e82b9dd5f77dfa0c"
version: "9db589eb07971de0c39a1c3f7a9df6ee"
build_date: "2019-05-16T20:22:33.749Z"
size_mb: 818
size: 293085215
sif: "https://datasets.datalad.org/shub/wezen/singularity/v1/2019-05-16-64f33a35-9db589eb/9db589eb07971de0c39a1c3f7a9df6ee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/wezen/singularity/v1/2019-05-16-64f33a35-9db589eb/
recipe: https://datasets.datalad.org/shub/wezen/singularity/v1/2019-05-16-64f33a35-9db589eb/Singularity
collection: wezen/singularity
---

# wezen/singularity:v1

```bash
$ singularity pull shub://wezen/singularity:v1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:stable
IncludeCmd: yes

%setup

%files
lipmutils/bin/* /usr/local/bin/
lipmutils/corelib /usr/local/lib/

%post
	apt update
	apt install -y build-essential software-properties-common zlib1g-dev libgomp1
	apt-add-repository contrib
	apt-add-repository non-free
	apt update
	apt upgrade -y
	apt install -y subversion gawk ghostscript wget fastqc bedtools
	
	# install
	cd /tmp/
	# glint
	wget http://lipm-bioinfo.toulouse.inra.fr/download/glint/glint-1.0.rc12.826_833.tgz
	tar xzf glint-1.0.rc12.826_833.tgz
	cd glint-1.0.rc12
	make all
	make install
	mv bin/glint /usr/local/bin/
	cd .. && rm -rf glint-1.0.rc12.826_833 glint-1.0.rc12.826_833.tgz
	
	apt install -y liberror-perl liburi-encode-perl libswitch-perl
	
	# clean
	apt purge -y zlib1g-dev subversion wget build-essential
	apt clean && apt autoremove -y

%environment
    export LC_ALL=C
    export PERL5LIB=/usr/local/lib/corelib

%runscript
	"$@"
```

## Collection

 - Name: [wezen/singularity](https://github.com/wezen/singularity)
 - License: None

