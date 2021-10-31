---
id: 8668
name: "netcatninja/2048"
branch: "master"
tag: "latest"
commit: "acca75d8e2afd96a8469b812b0a62c6120414c26"
version: "686b5cde80b002cd55317a522628547b"
build_date: "2019-04-26T11:40:34.649Z"
size_mb: 313
size: 115855391
sif: "https://datasets.datalad.org/shub/netcatninja/2048/latest/2019-04-26-acca75d8-686b5cde/686b5cde80b002cd55317a522628547b.simg"
url: https://datasets.datalad.org/shub/netcatninja/2048/latest/2019-04-26-acca75d8-686b5cde/
recipe: https://datasets.datalad.org/shub/netcatninja/2048/latest/2019-04-26-acca75d8-686b5cde/Singularity
collection: netcatninja/2048
---

# netcatninja/2048:latest

```bash
$ singularity pull shub://netcatninja/2048:latest
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

 - Name: [netcatninja/2048](https://github.com/netcatninja/2048)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

