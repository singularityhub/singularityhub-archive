---
id: 2029
name: "truatpasteurdotfr/singularity-docker-centos7-draw.io"
branch: "master"
tag: "latest"
commit: "21f148f518dd215bf920fea5e88783c927d02417"
version: "76e582fa943f754fdc0a58d2a3aa83b7"
build_date: "2018-03-13T01:25:23.385Z"
size_mb: 689
size: 293445663
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-draw.io/latest/2018-03-13-21f148f5-76e582fa/76e582fa943f754fdc0a58d2a3aa83b7.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-draw.io/latest/2018-03-13-21f148f5-76e582fa/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-draw.io/latest/2018-03-13-21f148f5-76e582fa/Singularity
collection: truatpasteurdotfr/singularity-docker-centos7-draw.io
---

# truatpasteurdotfr/singularity-docker-centos7-draw.io:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-centos7-draw.io:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:centos7

%post
yum -y update && yum -y upgrade
yum -y install epel-release && yum -y update && yum -y upgrade
# you need to create the top level directories since there is no overlay on CentOS-6
# specific to my setup
mkdir -p /local-storage /mnt/beegfs /baycells/home /baycells/scratch /c6/shared /c6/eb /local/gensoft2 /c6/shared/rpm /Bis/Scratch2 /mnt/beegfs /pasteur

yum -y install https://github.com/jgraph/drawio-desktop/releases/download/v8.0.6/draw.io-x86_64-8.0.6.rpm

yum -y install \
libXtst libXScrnSaver GConf2 alsa-lib  \
libcanberra-gtk2 libcanberra adwaita-gtk2-theme PackageKit-gtk3-module \
which xorg-x11-fonts-Type1 liberation-sans-fonts

%runscript
draw.io  "$@"
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-centos7-draw.io](https://github.com/truatpasteurdotfr/singularity-docker-centos7-draw.io)
 - License: [MIT License](https://api.github.com/licenses/mit)

