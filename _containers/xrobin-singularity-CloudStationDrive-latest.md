---
id: 7301
name: "xrobin/singularity-CloudStationDrive"
branch: "master"
tag: "latest"
commit: "d3438bb98f0c40ce2e2f15c29732aad71cf7eed5"
version: "919748ece838453479fc333cf5080405"
build_date: "2019-02-18T23:30:20.365Z"
size_mb: 474
size: 216657951
sif: "https://datasets.datalad.org/shub/xrobin/singularity-CloudStationDrive/latest/2019-02-18-d3438bb9-919748ec/919748ece838453479fc333cf5080405.simg"
url: https://datasets.datalad.org/shub/xrobin/singularity-CloudStationDrive/latest/2019-02-18-d3438bb9-919748ec/
recipe: https://datasets.datalad.org/shub/xrobin/singularity-CloudStationDrive/latest/2019-02-18-d3438bb9-919748ec/Singularity
collection: xrobin/singularity-CloudStationDrive
---

# xrobin/singularity-CloudStationDrive:latest

```bash
$ singularity pull shub://xrobin/singularity-CloudStationDrive:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%post
    # install some system deps
    apt-get -y update
    # build-dep
    apt-get -y install wget
    # undeclared dependency:
    apt-get -y install libqt5gui5

    wget https://global.download.synology.com/download/Tools/CloudStationDrive/4.2.8-4421/Ubuntu/Installer/x86_64/synology-cloud-station-drive-4421.x86_64.deb
    dpkg -i synology-cloud-station-drive-4421.x86_64.deb || apt-get -yf install
    rm synology-cloud-station-drive-4421.x86_64.deb
    
    apt-get -y remove wget
    apt-get -y autoremove
    apt-get clean

%runscript
	exec /usr/bin/synology-cloud-station-drive "$@"
```

## Collection

 - Name: [xrobin/singularity-CloudStationDrive](https://github.com/xrobin/singularity-CloudStationDrive)
 - License: None

