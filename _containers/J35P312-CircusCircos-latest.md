---
id: 6579
name: "J35P312/CircusCircos"
branch: "master"
tag: "latest"
commit: "739688ea8ea8da7f0231c0817e1e6023efa0b96d"
version: "ba8bac9451be8d9143cb001aa892a76b"
build_date: "2020-09-07T13:41:20.733Z"
size_mb: 595
size: 239149087
sif: "https://datasets.datalad.org/shub/J35P312/CircusCircos/latest/2020-09-07-739688ea-ba8bac94/ba8bac9451be8d9143cb001aa892a76b.simg"
url: https://datasets.datalad.org/shub/J35P312/CircusCircos/latest/2020-09-07-739688ea-ba8bac94/
recipe: https://datasets.datalad.org/shub/J35P312/CircusCircos/latest/2020-09-07-739688ea-ba8bac94/Singularity
collection: J35P312/CircusCircos
---

# J35P312/CircusCircos:latest

```bash
$ singularity pull shub://J35P312/CircusCircos:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
SHELL=/bin/bash
PATH=/opt/anaconda/bin:${PATH}
LC_ALL=C.UTF-8

%runscript
    echo "This is what happens when you run the container..."

%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install wget git bzip2 build-essential gcc zlib1g-dev language-pack-en-base apt-transport-https make cmake unzip curl pkg-config libgd-gd2-perl libgd-svg-perl libdata-clone-perl
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    curl -L https://cpanmin.us | perl - App::cpanminus

    cpanm Clone
    cpanm Config::General
    cpanm Font::TTF::Font
    cpanm Math::VecStat
    cpanm Readonly
    cpanm Regexp::Common
    cpanm Text::Format
    cpanm Math::Bezier
    cpanm Math::Round
    cpanm Set::IntSpan
    cpanm List::MoreUtils
    cpanm Params::Validate
    cpanm Statistics::Basic

    wget http://circos.ca/distribution/circos-0.69-6.tgz
    tar -xvf circos-0.69-6.tgz
```

## Collection

 - Name: [J35P312/CircusCircos](https://github.com/J35P312/CircusCircos)
 - License: None

