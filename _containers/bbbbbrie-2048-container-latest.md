---
id: 2153
name: "bbbbbrie/2048-container"
branch: "master"
tag: "latest"
commit: "912d7bf1de3ad5120e4e9b86150da31abbbe89f9"
version: "22920fb441a34a29836c354a583083ee"
build_date: "2019-04-26T11:40:29.093Z"
size_mb: 317
size: 115564575
sif: "https://datasets.datalad.org/shub/bbbbbrie/2048-container/latest/2019-04-26-912d7bf1-22920fb4/22920fb441a34a29836c354a583083ee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bbbbbrie/2048-container/latest/2019-04-26-912d7bf1-22920fb4/
recipe: https://datasets.datalad.org/shub/bbbbbrie/2048-container/latest/2019-04-26-912d7bf1-22920fb4/Singularity
collection: bbbbbrie/2048-container
---

# bbbbbrie/2048-container:latest

```bash
$ singularity pull shub://bbbbbrie/2048-container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%help
    Get the elusive 2048 tile.

%runscript
    /opt/2048-cli/2048
%environment
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
    export PATH=/opt/2048-cli:/usr/bin:/usr/local/sbin:/bin:/usr/local/bin:/usr/sbin:/sbin

%post
    apt-get -y update && apt-get install -y --no-install-recommends  \
    figlet gcc git lolcat libncurses5-dev make
    git clone https://github.com/tiehuis/2048-cli.git /opt/2048-cli
    cd /opt/2048-cli
    make
    /usr/bin/figlet "hello, world" | /usr/games/lolcat
    /usr/bin/figlet "Let's play 2048..." | /usr/games/lolcat
    /usr/bin/figlet "...in a container!" | /usr/games/lolcat

%labels
    Author Brie Carranza
```

## Collection

 - Name: [bbbbbrie/2048-container](https://github.com/bbbbbrie/2048-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

