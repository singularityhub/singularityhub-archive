---
id: 9973
name: "Kurorororo/downward-lab-experiment"
branch: "master"
tag: "latest"
commit: "d434428e9cae223c9b427a16698486e21218058f"
version: "d1247ca95172f68d298485649a840fe3"
build_date: "2019-08-19T20:26:13.965Z"
size_mb: 1659
size: 473280543
sif: "https://datasets.datalad.org/shub/Kurorororo/downward-lab-experiment/latest/2019-08-19-d434428e-d1247ca9/d1247ca95172f68d298485649a840fe3.simg"
url: https://datasets.datalad.org/shub/Kurorororo/downward-lab-experiment/latest/2019-08-19-d434428e-d1247ca9/
recipe: https://datasets.datalad.org/shub/Kurorororo/downward-lab-experiment/latest/2019-08-19-d434428e-d1247ca9/Singularity
collection: Kurorororo/downward-lab-experiment
---

# Kurorororo/downward-lab-experiment:latest

```bash
$ singularity pull shub://Kurorororo/downward-lab-experiment:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04
Stage: build

%environment
    export DOWNWARD_REPO=/fast-downward
    export DOWNWARD_BENCHMARKS=/downward-benchmarks

%post
    apt update -y
    apt install -y \
      git \
      mercurial \
      g++ \
      make \
      cmake \
      python3 \
      python3-venv \
      flex \
      bison

    python3 -m venv /lab-venv
    . /lab-venv/bin/activate
    echo '. /lab-venv/bin/activate' >> $SINGULARITY_ENVIRONMENT

    hg clone https://bitbucket.org/aibasel/downward-benchmarks /downward-benchmarks

    hg clone http://hg.fast-downward.org /fast-downward
    cd /fast-downward && ./build.py

    hg clone https://bitbucket.org/jendrikseipp/lab /lab
    pip install /lab

    git clone https://github.com/KCL-Planning/VAL.git /VAL
    cd /VAL && make clean && sed -i 's/-Werror //g' Makefile && make
    cp /VAL/validate /usr/local/bin
```

## Collection

 - Name: [Kurorororo/downward-lab-experiment](https://github.com/Kurorororo/downward-lab-experiment)
 - License: None

