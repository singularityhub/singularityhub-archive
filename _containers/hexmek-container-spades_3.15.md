---
id: 15323
name: "hexmek/container"
branch: "master"
tag: "spades_3.15"
commit: "bbe9ff3bde8c5095f49ac51f4208bec71994fc74"
version: "e01da4a2ccd9e4fe5b5b20cb902117acd2ae068a013b85448daff59a1fbcee14"
build_date: "2021-02-22T12:15:41.552Z"
size_mb: 359.9765625
size: 377462784
sif: "https://datasets.datalad.org/shub/hexmek/container/spades_3.15/2021-02-22-bbe9ff3b-e01da4a2/e01da4a2ccd9e4fe5b5b20cb902117acd2ae068a013b85448daff59a1fbcee14.sif"
url: https://datasets.datalad.org/shub/hexmek/container/spades_3.15/2021-02-22-bbe9ff3b-e01da4a2/
recipe: https://datasets.datalad.org/shub/hexmek/container/spades_3.15/2021-02-22-bbe9ff3b-e01da4a2/Singularity
collection: hexmek/container
---

# hexmek/container:spades_3.15

```bash
$ singularity pull shub://hexmek/container:spades_3.15
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: stable
MirrorURL: http://httpredir.debian.org/debian


%post
    apt update
    apt upgrade -y
    apt install -y make cmake g++ wget curl \
    procps \
    python3 \
    procps  python3-pip \
    python3-dev build-essential wget bzip2 libz-dev
    update-alternatives --install /usr/bin/python python $(which python3) 1

    cd /opt
    wget -O spades.tar.gz http://cab.spbu.ru/files/release3.15.1/SPAdes-3.15.1-Linux.tar.gz
    tar xzvf spades.tar.gz
    

%environment
    export LC_ALL=C     
    export PATH="/opt/SPAdes-3.15.1-Linux/bin:$PATH"
```

## Collection

 - Name: [hexmek/container](https://github.com/hexmek/container)
 - License: None

