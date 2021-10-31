---
id: 11789
name: "dominik-handler/AP_singu"
branch: "master"
tag: "purge_dups"
commit: "ca73dc38a5939a062463fded6dcef37dea6776bd"
version: "9a92313f27985451a882658db737d1af42d627af1fa5d475f0487e409bf0d7cf"
build_date: "2021-03-25T16:24:06.613Z"
size_mb: 199.48046875
size: 209170432
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/purge_dups/2021-03-25-ca73dc38-9a92313f/9a92313f27985451a882658db737d1af42d627af1fa5d475f0487e409bf0d7cf.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/purge_dups/2021-03-25-ca73dc38-9a92313f/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/purge_dups/2021-03-25-ca73dc38-9a92313f/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:purge_dups

```bash
$ singularity pull shub://dominik-handler/AP_singu:purge_dups
```

## Singularity Recipe

```singularity
#minimap2 in singularity

Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  purge_dups 1964aaa

%runscript
    "$@"

%post
    apt-get update
    apt-get --assume-yes install wget curl bzip2 git-core build-essential zlib1g-dev python3-dev python3-setuptools

    cd /
    git clone https://github.com/lh3/minimap2
    cd minimap2 && make
    cp minimap2 /usr/bin 

    cd /
    git clone https://github.com/dfguan/purge_dups.git
    cd purge_dups/src && make
    cp /purge_dups/bin/* /usr/bin

    cd /
    git clone https://github.com/dfguan/runner.git
    cd runner && python3 setup.py install 
    #cp bin/* /usr/bin

    cd /
    git clone https://github.com/dfguan/KMC.git 
    cd KMC && make 
    #cp bin/* /usr/bin

%environment


%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

