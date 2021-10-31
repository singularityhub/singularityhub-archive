---
id: 14877
name: "mmirko/singularitytest"
branch: "main"
tag: "latest"
commit: "03795caece822c1cb065bd80baf67be9aa7480ae"
version: "bee52426f17e5a77ce870ddc78582d6f"
build_date: "2020-11-13T09:05:14.487Z"
size_mb: 894.0
size: 311746591
sif: "https://datasets.datalad.org/shub/mmirko/singularitytest/latest/2020-11-13-03795cae-bee52426/bee52426f17e5a77ce870ddc78582d6f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/mmirko/singularitytest/latest/2020-11-13-03795cae-bee52426/
recipe: https://datasets.datalad.org/shub/mmirko/singularitytest/latest/2020-11-13-03795cae-bee52426/Singularity
collection: mmirko/singularitytest
---

# mmirko/singularitytest:latest

```bash
$ singularity pull shub://mmirko/singularitytest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: amd64/centos:7

%post
    yum update -y && \
    	yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    
    yum group install -y "Development Tools"

    yum update -y && \
    	yum -y install \
	    wget \
	    openssh-clients \
	    openssl \
	    glibc-devel \
	    glibc-static \
	    git \
	    bash \
	    centos-release-scl\

    yum update -y && \
    	yum -y install \
	    devtoolset-7 \


%files

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript
    /bin/bash
```

## Collection

 - Name: [mmirko/singularitytest](https://github.com/mmirko/singularitytest)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

