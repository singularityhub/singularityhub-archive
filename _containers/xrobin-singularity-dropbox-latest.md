---
id: 5603
name: "xrobin/singularity-dropbox"
branch: "master"
tag: "latest"
commit: "756cb32583636f25e50a865a2b0bba5cf1c0d6a8"
version: "e2ace61ce4ed05b839bd8976026c0d56"
build_date: "2020-04-23T13:19:39.910Z"
size_mb: 420
size: 147406879
sif: "https://datasets.datalad.org/shub/xrobin/singularity-dropbox/latest/2020-04-23-756cb325-e2ace61c/e2ace61ce4ed05b839bd8976026c0d56.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/xrobin/singularity-dropbox/latest/2020-04-23-756cb325-e2ace61c/
recipe: https://datasets.datalad.org/shub/xrobin/singularity-dropbox/latest/2020-04-23-756cb325-e2ace61c/Singularity
collection: xrobin/singularity-dropbox
---

# xrobin/singularity-dropbox:latest

```bash
$ singularity pull shub://xrobin/singularity-dropbox:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%post
    # install some system deps
    echo `pwd`
    apt-get -y update
    apt-get -y install wget libxslt1.1 libxxf86vm1  libqt5gui5

    wget -O dropbox.deb https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2015.10.28_amd64.deb
    dpkg -i dropbox.deb || apt-get -yf install
    rm dropbox.deb
    
    apt-get -y remove wget
    apt-get -y autoremove
    apt-get clean

%runscript
	exec /usr/bin/dropbox "$@"
```

## Collection

 - Name: [xrobin/singularity-dropbox](https://github.com/xrobin/singularity-dropbox)
 - License: None

