---
id: 9818
name: "fredjaya/rec-bench"
branch: "dev"
tag: "prepro"
commit: "88933dd48fe3743c159488ee65f8a6d0f6cf0315"
version: "950dcdaa40ed5c5dae91f30a2e31913e"
build_date: "2019-06-26T22:56:26.343Z"
size_mb: 1061
size: 319455263
sif: "https://datasets.datalad.org/shub/fredjaya/rec-bench/prepro/2019-06-26-88933dd4-950dcdaa/950dcdaa40ed5c5dae91f30a2e31913e.simg"
url: https://datasets.datalad.org/shub/fredjaya/rec-bench/prepro/2019-06-26-88933dd4-950dcdaa/
recipe: https://datasets.datalad.org/shub/fredjaya/rec-bench/prepro/2019-06-26-88933dd4-950dcdaa/Singularity
collection: fredjaya/rec-bench
---

# fredjaya/rec-bench:prepro

```bash
$ singularity pull shub://fredjaya/rec-bench:prepro
```

## Singularity Recipe

```singularity
# https://tecadmin.net/install-python-3-7-on-centos/

BootStrap: shub
From: shub://fredjaya/rec-bench:base@digest

%post
    # Add python 3.7.3
    cd /usr/src
    wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
    tar xzf Python-3.7.3.tgz
    rm -rf Python-3.7.3.tgz
    cd Python-3.7.3
    ./configure --enable-optimizations
    make altinstall

    # Add python dependencies
    python3.7 -m pip install matplotlib

%test
    python3.7 -V
```

## Collection

 - Name: [fredjaya/rec-bench](https://github.com/fredjaya/rec-bench)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

