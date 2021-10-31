---
id: 2665
name: "Darkmon93/singularityConfig"
branch: "master"
tag: "latest"
commit: "c634ec4df30b3ab6e6e43a8ca87252966d19a5d5"
version: "39674b75af16f316f8153ff43af05a66"
build_date: "2018-04-27T08:59:00.298Z"
size_mb: 477
size: 205541407
sif: "https://datasets.datalad.org/shub/Darkmon93/singularityConfig/latest/2018-04-27-c634ec4d-39674b75/39674b75af16f316f8153ff43af05a66.simg"
url: https://datasets.datalad.org/shub/Darkmon93/singularityConfig/latest/2018-04-27-c634ec4d-39674b75/
recipe: https://datasets.datalad.org/shub/Darkmon93/singularityConfig/latest/2018-04-27-c634ec4d-39674b75/Singularity
collection: Darkmon93/singularityConfig
---

# Darkmon93/singularityConfig:latest

```bash
$ singularity pull shub://Darkmon93/singularityConfig:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%runscript
    echo "This is what happens when you run the container..."

%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get -y --force-yes install vim libunwind8 icu-devtools curl wget software-properties-common apt-transport-https ca-certificates sudo
    apt-get -y --force-yes update
    apt-get -y --force-yes install openvpn easy-rsa openssh-server
```

## Collection

 - Name: [Darkmon93/singularityConfig](https://github.com/Darkmon93/singularityConfig)
 - License: None

