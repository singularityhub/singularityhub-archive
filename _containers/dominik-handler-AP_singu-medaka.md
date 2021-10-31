---
id: 7801
name: "dominik-handler/AP_singu"
branch: "master"
tag: "medaka"
commit: "521aeb80fc1354863e6781127192ca66bf05ef62"
version: "6b6199841d4fc4c2c7dd421957c307a181666dd3a0fb80983e72c496f3fe5788"
build_date: "2020-05-04T11:51:32.599Z"
size_mb: 920.44140625
size: 965152768
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/medaka/2020-05-04-521aeb80-6b619984/6b6199841d4fc4c2c7dd421957c307a181666dd3a0fb80983e72c496f3fe5788.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/medaka/2020-05-04-521aeb80-6b619984/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/medaka/2020-05-04-521aeb80-6b619984/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:medaka

```bash
$ singularity pull shub://dominik-handler/AP_singu:medaka
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: conda/miniconda3

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  medaka v0.11.0 

%post
    set -e

    apt-get update
    apt-get -y install bzip2 g++ zlib1g-dev libbz2-dev liblzma-dev libffi-dev libncurses5-dev libcurl4-gnutls-dev libssl-dev curl make cmake wget python3-all-dev python-virtualenv git-core sed
    
    wget --no-check-certificate --content-disposition https://github.com/git-lfs/git-lfs/releases/download/v2.9.2/git-lfs-linux-amd64-v2.9.2.tar.gz
    tar -zxvf git-lfs-linux-amd64-v2.9.2.tar.gz
    cat install.sh | sed 's/git lfs install/git lfs install --skip-repo/' > install_mod.sh
    chmod 777 install_mod.sh
    ./install_mod.sh

    cd /
    git clone https://github.com/nanoporetech/medaka.git
    cd medaka
    sed -i 's/tar -xvf minimap2-${MINIMAPVER}_x64-linux.tar.bz2/tar -xvf minimap2-${MINIMAPVER}_x64-linux.tar.bz2 --no-same-owner /' Makefile
    make install


%environment
    export PATH=/medaka/venv/bin/:${PATH}
    

%runscript
  "$@"
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

