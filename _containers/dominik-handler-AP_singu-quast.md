---
id: 7692
name: "dominik-handler/AP_singu"
branch: "master"
tag: "quast"
commit: "060ad80db789ba311fed8153b2cfad06a15b15e0"
version: "17d2426bf124cd9e11d123cb9c797c7d"
build_date: "2019-10-15T13:24:27.599Z"
size_mb: 4761
size: 1138012191
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/quast/2019-10-15-060ad80d-17d2426b/17d2426bf124cd9e11d123cb9c797c7d.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/quast/2019-10-15-060ad80d-17d2426b/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/quast/2019-10-15-060ad80d-17d2426b/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:quast

```bash
$ singularity pull shub://dominik-handler/AP_singu:quast
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest


%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  quast.version 5.0.2

%post
  ##### System #####
  apt update -y
  apt upgrade -y
  apt install -y build-essential wget zlib1g-dev pkg-config libfreetype6-dev libpng-dev perl openjdk-8-jdk python3 python3-setuptools python3-dev  ncbi-blast+ python3-matplotlib

echo "Europe/Dublin" > /etc/timezone
unlink /etc/localtime
dpkg-reconfigure -f noninteractive tzdata
apt install -y locales
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
dpkg-reconfigure -f noninteractive locales
  

  ##### Quast #####
  wget -P /tmp/ https://downloads.sourceforge.net/project/quast/quast-5.0.2.tar.gz
  cd /tmp
  tar xvzf /tmp/quast-5.0.2.tar.gz
  rm /tmp/quast-5.0.2.tar.gz
  if [ -d "/quast" ]; then
    rm -rf /quast/
  fi
  mv /tmp/quast-5.0.2 /quast
  cd /quast/
  python3 ./setup.py install_full

%runscript
  quast.py $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

