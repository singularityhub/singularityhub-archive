---
id: 8996
name: "netcatninja/cookbook"
branch: "master"
tag: "2048"
commit: "6480510861738230d2fec299367e6c2d7218ba90"
version: "e05bb89300ffcc1c4f17f2c2fa95e88f"
build_date: "2019-05-10T10:48:53.374Z"
size_mb: 313
size: 116015135
sif: "https://datasets.datalad.org/shub/netcatninja/cookbook/2048/2019-05-10-64805108-e05bb893/e05bb89300ffcc1c4f17f2c2fa95e88f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/netcatninja/cookbook/2048/2019-05-10-64805108-e05bb893/
recipe: https://datasets.datalad.org/shub/netcatninja/cookbook/2048/2019-05-10-64805108-e05bb893/Singularity
collection: netcatninja/cookbook
---

# netcatninja/cookbook:2048

```bash
$ singularity pull shub://netcatninja/cookbook:2048
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

 - Name: [netcatninja/cookbook](https://github.com/netcatninja/cookbook)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

