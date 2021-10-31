---
id: 5104
name: "ilkerkesen/ajan-metin"
branch: "master"
tag: "latest"
commit: "087ef89bdfe980abc3682b106baa3b81e76b227a"
version: "9e8f0091bd2bba8b34f1c9920ee5877e"
build_date: "2018-10-11T09:24:02.570Z"
size_mb: 2621
size: 1483046943
sif: "https://datasets.datalad.org/shub/ilkerkesen/ajan-metin/latest/2018-10-11-087ef89b-9e8f0091/9e8f0091bd2bba8b34f1c9920ee5877e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ilkerkesen/ajan-metin/latest/2018-10-11-087ef89b-9e8f0091/
recipe: https://datasets.datalad.org/shub/ilkerkesen/ajan-metin/latest/2018-10-11-087ef89b-9e8f0091/Singularity
collection: ilkerkesen/ajan-metin
---

# ilkerkesen/ajan-metin:latest

```bash
$ singularity pull shub://ilkerkesen/ajan-metin:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%runscript
    echo "Running tests"

%environment
    export DISPLAY=:99

%post
    echo "Here we are installing software and other dependencies for the container!"
    apt-get update && apt-get install -q -y \
    build-essential \
    chromium-browser \
    chromium-chromedriver \
    curl \
    gcc \
    make \
    git \
    libffi-dev \
    python3-dev \
    python3-setuptools \
    python3-pip \
    uuid-dev \
    wget

    git clone https://github.com/Microsoft/TextWorld.git
    cd TextWorld
    pip3 install -r requirements.txt
    pip3 install .[prompt,vis]

    pip3 install torch torchvision
```

## Collection

 - Name: [ilkerkesen/ajan-metin](https://github.com/ilkerkesen/ajan-metin)
 - License: [MIT License](https://api.github.com/licenses/mit)

