---
id: 5469
name: "tonyswoo/naturalbugpatch"
branch: "master"
tag: "latest"
commit: "b907ad56243276ab8666e4379b0778a46e9acaf4"
version: "b3426dc28ac59d26359e806dd0062e12"
build_date: "2018-11-07T13:35:07.928Z"
size_mb: 2490
size: 1620709407
sif: "https://datasets.datalad.org/shub/tonyswoo/naturalbugpatch/latest/2018-11-07-b907ad56-b3426dc2/b3426dc28ac59d26359e806dd0062e12.simg"
url: https://datasets.datalad.org/shub/tonyswoo/naturalbugpatch/latest/2018-11-07-b907ad56-b3426dc2/
recipe: https://datasets.datalad.org/shub/tonyswoo/naturalbugpatch/latest/2018-11-07-b907ad56-b3426dc2/Singularity
collection: tonyswoo/naturalbugpatch
---

# tonyswoo/naturalbugpatch:latest

```bash
$ singularity pull shub://tonyswoo/naturalbugpatch:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
      HOME=/home
      D4J_HOME=/home/naturalbugpatch/defects4j
      SCRIPTS=/home/naturalbugpatch/GenProgScripts
      export HOME D4J_HOME SCRIPTS

%post
      apt-get update && apt-get install -y software-properties-common
      add-apt-repository -y ppa:openjdk-r/ppa
      apt-get update
      apt-get install -y openjdk-7-jdk openjdk-8-jdk openjdk-9-jdk git subversion make gcc wget vim maven zip
      git clone https://github.com/tonyswoo/naturalbugpatch.git /home/naturalbugpatch
      /home/naturalbugpatch/initialize.sh
      mkdir /home/naturalbugpatch/defects4j/D4JwithGP
      chown nobody:nogroup -R /home
```

## Collection

 - Name: [tonyswoo/naturalbugpatch](https://github.com/tonyswoo/naturalbugpatch)
 - License: None

