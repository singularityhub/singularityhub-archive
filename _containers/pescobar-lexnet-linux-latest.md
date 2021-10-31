---
id: 4989
name: "pescobar/lexnet-linux"
branch: "master"
tag: "latest"
commit: "cc3d42047bae11618803ad9fa231d9c5c8596777"
version: "0d8a1e18db915af84a317502ba041818"
build_date: "2020-02-25T22:05:20.065Z"
size_mb: 950
size: 543309855
sif: "https://datasets.datalad.org/shub/pescobar/lexnet-linux/latest/2020-02-25-cc3d4204-0d8a1e18/0d8a1e18db915af84a317502ba041818.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/lexnet-linux/latest/2020-02-25-cc3d4204-0d8a1e18/
recipe: https://datasets.datalad.org/shub/pescobar/lexnet-linux/latest/2020-02-25-cc3d4204-0d8a1e18/Singularity
collection: pescobar/lexnet-linux
---

# pescobar/lexnet-linux:latest

```bash
$ singularity pull shub://pescobar/lexnet-linux:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%post

  # instalar firefox para que se instalen todas sus dependencias
  apt-get update
  apt-get -y install firefox

  # desinstalar firefox (las dependencias se quedan)
  apt-get -y remove firefox

  # descargar firefox v51 que es el ultimo que soporta java
  apt-get -y install wget
  cd /opt 
  wget http://ftp.mozilla.org/pub/firefox/releases/51.0.1/linux-x86_64/es-ES/firefox-51.0.1.tar.bz2
  tar xf firefox-51.0.1.tar.bz2
  rm -f firefox-51.0.1.tar.bz2
  ln -s /opt/firefox/firefox /usr/local/bin/firefox

  # instalar java
  apt-key adv --recv-keys --keyserver keyserver.ubuntu.com EEA14886
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list
  apt-get update
  echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
  apt-get install -y oracle-java8-installer

  # borrar ficheros temporales de apt
  apt-get clean


%runscript

  # crear un perfil para lexnet
  firefox -no-remote -CreateProfile lexnet

  # arrancar firefox con el perfil lexnet
  firefox -no-remote -P lexnet
```

## Collection

 - Name: [pescobar/lexnet-linux](https://github.com/pescobar/lexnet-linux)
 - License: None

