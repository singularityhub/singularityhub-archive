---
id: 3207
name: "heathsc/gemBS"
branch: "master"
tag: "latest"
commit: "522d41a6624b97ea406962fb236523ad4ba77275"
version: "c9fa382bf2a7a5489b7bd459a0aa5124"
build_date: "2021-04-08T12:00:32.115Z"
size_mb: 679.0
size: 293077023
sif: "https://datasets.datalad.org/shub/heathsc/gemBS/latest/2021-04-08-522d41a6-c9fa382b/c9fa382bf2a7a5489b7bd459a0aa5124.sif"
url: https://datasets.datalad.org/shub/heathsc/gemBS/latest/2021-04-08-522d41a6-c9fa382b/
recipe: https://datasets.datalad.org/shub/heathsc/gemBS/latest/2021-04-08-522d41a6-c9fa382b/Singularity
collection: heathsc/gemBS
---

# heathsc/gemBS:latest

```bash
$ singularity pull shub://heathsc/gemBS:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial

%runscript
    exec /usr/local/bin/gemBS $@

%help
    gemBS singularity container
	 
%post
	 (mkdir /ext && cd /ext && mkdir disk1 disk2 disk3 disk4 disk5 disk6 disk7 disk8 disk9)
    apt-get update
	 apt-get install -y python3 build-essential git autoconf python3-pip wget lbzip2
    apt-get install -y zlib1g-dev libbz2-dev gsl-bin libgsl0-dev
    apt-get install -y libncurses5-dev liblzma-dev libssl-dev libcurl4-openssl-dev
    pip3 install 'matplotlib<3.0' multiprocess
    mkdir /usr/local/build; cd /usr/local/build
	 git clone --recursive https://github.com/heathsc/gemBS.git
    (cd gemBS; python3 setup.py install)
    rm -rf gemBS && cd && rmdir /usr/local/build
```

## Collection

 - Name: [heathsc/gemBS](https://github.com/heathsc/gemBS)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

