---
id: 3778
name: "ISU-HPC/py2-and-py3"
branch: "master"
tag: "latest"
commit: "70dad2362c6c597a4d7b01cc02270109ad3311b2"
version: "c63915a0d52f1d1ac4718c4cd77fe727"
build_date: "2018-07-30T21:57:56.217Z"
size_mb: 158
size: 43851807
sif: "https://datasets.datalad.org/shub/ISU-HPC/py2-and-py3/latest/2018-07-30-70dad236-c63915a0/c63915a0d52f1d1ac4718c4cd77fe727.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/py2-and-py3/latest/2018-07-30-70dad236-c63915a0/
recipe: https://datasets.datalad.org/shub/ISU-HPC/py2-and-py3/latest/2018-07-30-70dad236-c63915a0/Singularity
collection: ISU-HPC/py2-and-py3
---

# ISU-HPC/py2-and-py3:latest

```bash
$ singularity pull shub://ISU-HPC/py2-and-py3:latest
```

## Singularity Recipe

```singularity
# Starts with python:3.6.0-alpine and then installs most of python:2.7.13-alpine on top
# to allows us to choose Python versions at runtime via: python2, python3, pip2, pip3, etc.
Bootstrap:docker
From:python:3.6.0-alpine

%post

export GPG_KEY=C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF
export PYTHON_VERSION=2.7.13

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
export PYTHON_PIP_VERSION=9.0.1

#set -ex \
	apk add --no-cache --virtual .fetch-deps \
		gnupg \
		openssl \
		tar \
		xz \
#	\
	wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" 
	wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" 
	export GNUPGHOME="$(mktemp -d)" 
	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" 
	gpg --batch --verify python.tar.xz.asc python.tar.xz 
	rm -r python.tar.xz.asc 
	mkdir -p /usr/src/python 
	tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz 
	rm python.tar.xz 
	apk add --no-cache --virtual .build-deps  \
		bzip2-dev \
		gcc \
		gdbm-dev \
		libc-dev \
		linux-headers \
		make \
		ncurses-dev \
		openssl \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		zlib-dev 
# add build deps before removing fetch deps in case there's overlap
	apk del .fetch-deps 
	
	cd /usr/src/python 
	./configure \
		--enable-shared \
		--enable-unicode=ucs4 
	make -j$(getconf _NPROCESSORS_ONLN) 
	make install 
	
		wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' 
		python2 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" 
		rm /tmp/get-pip.py 
# we use "--force-reinstall" for the case where the version of pip we're trying to install is the same as the version bundled with Python
# ("Requirement already up-to-date: pip==8.1.2 in /usr/local/lib/python3.6/site-packages")
# https://github.com/docker-library/python/pull/143#issuecomment-241032683
	pip install --no-cache-dir --upgrade --force-reinstall "pip==$PYTHON_PIP_VERSION" 
# then we use "pip list" to ensure we don't have more than one pip version installed
# https://github.com/docker-library/python/pull/100
#	&& [ "$(pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" { print $2; exit }')" = "$PYTHON_PIP_VERSION" ] \
	
	find /usr/local -depth \
		\( \
			\( -type d -a -name test -o -name tests \) \
			-o \
			\( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
		\) -exec rm -rf '{}' + 
	runDeps="$( \
		scanelf --needed --nobanner --recursive /usr/local \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| sort -u \
			| xargs -r apk info --installed \
			| sort -u \
	)" 
	apk add --virtual .python-rundeps $runDeps 
	apk del .build-deps 
	rm -rf /usr/src/python ~/.cache 
    cp /usr/local/bin/pip3.6 /usr/local/bin/pip3  # reenable pip3

cd /

ls -Fla /usr/local/bin/p* 
    which python  && python -V 
    which python2 && python2 -V 
    which python3 && python3 -V 
    which pip     && pip -V 
    which pip2    && pip2 -V 
    which pip3    && pip3 -V
```

## Collection

 - Name: [ISU-HPC/py2-and-py3](https://github.com/ISU-HPC/py2-and-py3)
 - License: None

