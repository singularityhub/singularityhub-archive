---
id: 4069
name: "dominik-handler/AP_singu"
branch: "master"
tag: "mashmap"
commit: "d1ba2e26976dcd2b36ab6ebbf27d4d45e875668f"
version: "789d834aab6d5c6cae03f0939e4564b3"
build_date: "2019-01-15T15:20:37.235Z"
size_mb: 1070
size: 479539231
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/mashmap/2019-01-15-d1ba2e26-789d834a/789d834aab6d5c6cae03f0939e4564b3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/mashmap/2019-01-15-d1ba2e26-789d834a/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/mashmap/2019-01-15-d1ba2e26-789d834a/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:mashmap

```bash
$ singularity pull shub://dominik-handler/AP_singu:mashmap
```

## Singularity Recipe

```singularity
#graphmap in singularity

BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    mashmap "$@"

%post
    apt-get --assume-yes install wget
    apt-get --assume-yes install 

     apt-get update
      
     apt-get -y install software-properties-common build-essential zlib1g-dev git autoconf
     add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"
     apt-get update
    
     apt-get -y install gnuplot gnuplot-x11 gnuplot-doc 
     apt-get update
     apt-get -y install xfig transfig xfig-libs libgsl-dev
           
     cd /
     git clone https://github.com/marbl/MashMap.git

     mkdir -p /mashmap
     
     
     cd MashMap
     ./bootstrap.sh
     ./configure --prefix=/mashmap/
     make
     
     cd 
     rm -rf /MashMap
     
     mkdir /groups
     mkdir /scratch
     mkdir /scratch-ii2
     mkdir /clustertmp

%environment
    PATH="PATH=/mashmap/bin/:${PATH}"
    export $PATH


%test
  PATH="PATH=/mashmap/bin/:${PATH}"
  export $PATH
  #mashmap -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

