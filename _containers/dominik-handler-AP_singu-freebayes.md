---
id: 8673
name: "dominik-handler/AP_singu"
branch: "master"
tag: "freebayes"
commit: "bb73cc8fdde8aa1f2469e74159ee4b152ca9eb85"
version: "dd59e1217617919707efb139301aaa22948ca1bbb674df8c22e76ce51bf1cdad"
build_date: "2019-12-05T12:59:23.298Z"
size_mb: 280.19921875
size: 293810176
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/freebayes/2019-12-05-bb73cc8f-dd59e121/dd59e1217617919707efb139301aaa22948ca1bbb674df8c22e76ce51bf1cdad.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/freebayes/2019-12-05-bb73cc8f-dd59e121/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/freebayes/2019-12-05-bb73cc8f-dd59e121/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:freebayes

```bash
$ singularity pull shub://dominik-handler/AP_singu:freebayes
```

## Singularity Recipe

```singularity
#wtdbg2 in singularity

Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  freebayes v1.3.1 @ 54bf409 

%runscript
    "$@"

%post
    apt-get update
    apt-get --assume-yes install wget curl apt-utils

    apt-get update
    apt-get -y install build-essential git-core zlib1g-dev libbz2-dev liblzma-dev
       
    cd /
    git clone --recursive git://github.com/ekg/freebayes.git
    cd freebayes && make 
    make install


%environment

%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

