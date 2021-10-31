---
id: 5565
name: "mherkazandjian/singularity_avogadro"
branch: "master"
tag: "latest"
commit: "8790786da07ac3d07b79685c882f5017cbbf74c2"
version: "29920d911f4e1062445137866e121be0"
build_date: "2018-11-11T00:03:06.767Z"
size_mb: 541
size: 188325919
sif: "https://datasets.datalad.org/shub/mherkazandjian/singularity_avogadro/latest/2018-11-11-8790786d-29920d91/29920d911f4e1062445137866e121be0.simg"
url: https://datasets.datalad.org/shub/mherkazandjian/singularity_avogadro/latest/2018-11-11-8790786d-29920d91/
recipe: https://datasets.datalad.org/shub/mherkazandjian/singularity_avogadro/latest/2018-11-11-8790786d-29920d91/Singularity
collection: mherkazandjian/singularity_avogadro
---

# mherkazandjian/singularity_avogadro:latest

```bash
$ singularity pull shub://mherkazandjian/singularity_avogadro:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%runscript
    avogadro


%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get update
    apt-get -y install vim
    apt-get -y install avogadro
    apt-get clean
```

## Collection

 - Name: [mherkazandjian/singularity_avogadro](https://github.com/mherkazandjian/singularity_avogadro)
 - License: None

