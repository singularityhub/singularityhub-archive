---
id: 5999
name: "dominik-handler/AP_singu"
branch: "master"
tag: "guppy"
commit: "cb8e4a9a2b8c8189ce9bff6786d1d907f50b5483"
version: "76b7b307c964c1c344f37f9e8678a582af756e7136997813bbb9e58138c91df2"
build_date: "2021-01-30T21:41:01.817Z"
size_mb: 4870.34765625
size: 5106929664
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/guppy/2021-01-30-cb8e4a9a-76b7b307/76b7b307c964c1c344f37f9e8678a582af756e7136997813bbb9e58138c91df2.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/guppy/2021-01-30-cb8e4a9a-76b7b307/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/guppy/2021-01-30-cb8e4a9a-76b7b307/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:guppy

```bash
$ singularity pull shub://dominik-handler/AP_singu:guppy
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:11.1-devel-ubuntu20.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  guppy v 3.6.1


%runscript
  guppy_basecaller "$@"

%post
    set -e

  #fix locale
    apt-get update
    apt-get install -y locales && rm -rf /var/lib/apt/lists/* 
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
    export LC_COLLATE=C

  #installl guppy 
    apt-get update
    export DEBIAN_FRONTEND=noninteractive
    apt-get install -y wget curl lsb-release apt-transport-https git gnupg software-properties-common
    add-apt-repository universe

    cd 
    export PLATFORM=$(lsb_release -cs)
    wget -O file.key https://mirror.oxfordnanoportal.com/apt/ont-repo.pub 
    apt-key add file.key
    echo "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" |  tee /etc/apt/sources.list.d/nanoporetech.sources.list
    apt-get update
    apt-get install -y ont-guppy --no-install-recommends


    cd /
    git clone https://github.com/nanoporetech/rerio
    cd rerio
    ./download_model.py
    
    mkdir /multiporer
    curl https://gitlab.com/gringer/bioinfscripts/-/raw/master/multiporer.py?inline=false > /multiporer/multiporer.py

  #clean up
    apt-get autoremove
    apt-get clean

%environment
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LC_COLLATE=C

  export RERIOmodels=/rerio/basecall_models/

%test 
  #is not working due to libcuda no present on build-server
  # guppy_basecaller --version
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

