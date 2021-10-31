---
id: 3973
name: "remiolsen/w2rap-singularity"
branch: "master"
tag: "latest"
commit: "16c06db5fbd3a78a1e3a6781869661c10eeb9ed9"
version: "0278f891d92f21404ac74bb4489ca043"
build_date: "2018-08-14T13:13:01.635Z"
size_mb: 2922
size: 534376479
sif: "https://datasets.datalad.org/shub/remiolsen/w2rap-singularity/latest/2018-08-14-16c06db5-0278f891/0278f891d92f21404ac74bb4489ca043.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remiolsen/w2rap-singularity/latest/2018-08-14-16c06db5-0278f891/
recipe: https://datasets.datalad.org/shub/remiolsen/w2rap-singularity/latest/2018-08-14-16c06db5-0278f891/Singularity
collection: remiolsen/w2rap-singularity
---

# remiolsen/w2rap-singularity:latest

```bash
$ singularity pull shub://remiolsen/w2rap-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:9
 
%label
    Maintainer remi-andre.olsen@scilifelab.se

%post
    apt-get update
    apt-get install -y git build-essential cmake libomp-dev zlib1g-dev 

    cd /opt
    git clone https://github.com/gonzalogacc/w2rap-contigger.git
    cd w2rap-contigger
    cmake -D CMAKE_CXX_COMPILER=g++ .  
    make -j 4
    make install
```

## Collection

 - Name: [remiolsen/w2rap-singularity](https://github.com/remiolsen/w2rap-singularity)
 - License: None

