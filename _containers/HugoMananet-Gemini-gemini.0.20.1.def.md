---
id: 5750
name: "HugoMananet/Gemini"
branch: "master"
tag: "gemini.0.20.1.def"
commit: "bf8846e08b167c84dfdd3ba19c5e979efc5a0a3e"
version: "ce0d133aa74f056ed5bee2f170d637d5"
build_date: "2018-12-21T17:01:17.137Z"
size_mb: 15603
size: 14474231839
sif: "https://datasets.datalad.org/shub/HugoMananet/Gemini/gemini.0.20.1.def/2018-12-21-bf8846e0-ce0d133a/ce0d133aa74f056ed5bee2f170d637d5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/HugoMananet/Gemini/gemini.0.20.1.def/2018-12-21-bf8846e0-ce0d133a/
recipe: https://datasets.datalad.org/shub/HugoMananet/Gemini/gemini.0.20.1.def/2018-12-21-bf8846e0-ce0d133a/Singularity
collection: HugoMananet/Gemini
---

# HugoMananet/Gemini:gemini.0.20.1.def

```bash
$ singularity pull shub://HugoMananet/Gemini:gemini.0.20.1.def
```

## Singularity Recipe

```singularity
#!/bin/bash
Bootstrap: docker
From: phusion/baseimage:0.10.2


%label

	MAINTAINER Hugo Mananet

%post


    mkdir /soft
	mkdir /work
	mkdir /user1
	mkdir /user2
	mkdir /tmp3
    
    add-apt-repository ppa:deadsnakes/ppa
    apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y build-essential \
    libpython2.7 \
    python2.7 \
    git \
    gcc \
    zlib1g-dev \
    wget \
    tabix

    wget https://raw.github.com/arq5x/gemini/master/gemini/scripts/gemini_install.py

    python2.7 gemini_install.py /usr/local /usr/local/share/gemini
    export PATH=$PATH:/usr/local/gemini/bin

    wget -P /opt/ https://github.com/arq5x/grabix/archive/0.1.6.tar.gz
    cd /opt && tar -xzvf 0.1.6.tar.gz
    cd /opt/grabix-0.1.6 && make

%runscript

    exec gemini "$@"
```

## Collection

 - Name: [HugoMananet/Gemini](https://github.com/HugoMananet/Gemini)
 - License: None

