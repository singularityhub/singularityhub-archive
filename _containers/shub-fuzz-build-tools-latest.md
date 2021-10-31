---
id: 12944
name: "shub-fuzz/build-tools"
branch: "master"
tag: "latest"
commit: "b7b7d525eb285f8fe52a26d771008177685315c4"
version: "3369ab2b7f664f69a80201893b6cad4003764145accb7df7b56d96dc05a95871"
build_date: "2021-01-18T16:26:43.983Z"
size_mb: 364.04296875
size: 381726720
sif: "https://datasets.datalad.org/shub/shub-fuzz/build-tools/latest/2021-01-18-b7b7d525-3369ab2b/3369ab2b7f664f69a80201893b6cad4003764145accb7df7b56d96dc05a95871.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/shub-fuzz/build-tools/latest/2021-01-18-b7b7d525-3369ab2b/
recipe: https://datasets.datalad.org/shub/shub-fuzz/build-tools/latest/2021-01-18-b7b7d525-3369ab2b/Singularity
collection: shub-fuzz/build-tools
---

# shub-fuzz/build-tools:latest

```bash
$ singularity pull shub://shub-fuzz/build-tools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker 
From: ubuntu:rolling


%environment
    export LC_ALL=C
    export LANG=en_US.UTF-8

%post
    apt-get -qq update
    DEBIAN_FRONTEND=noninteractive apt-get -qq install -y \
      build-essential \
      clang \
      cmake \
      gdb \
      libtool-bin \
      llvm-dev \
      locales \
      procps \
      python3-dev \
      python3-pip \
      sqlite3 \
      strace \
      tmux \
      vim-nox
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
    NOW=`date`
    echo "export NOW=\"${NOW}\"" >> $SINGULARITY_ENVIRONMENT

%runscript
    echo "Container was created $NOW"
    echo "Arguments received: $*"
    exec echo "$@"

%startscript
    python3 -m http.server 

%test
    grep -q NAME=\"Ubuntu\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is Ubuntu as expected."
    else
        echo "Container base is not Ubuntu."
    fi

%labels
    Author jmb@iseclab.org
    MAINTAINER Josh Bundt
    Version v0.0.3

%help
    Ubuntu rolling with build tools.
```

## Collection

 - Name: [shub-fuzz/build-tools](https://github.com/shub-fuzz/build-tools)
 - License: None

