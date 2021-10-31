---
id: 3663
name: "mcw-rcc/shiny-server"
branch: "master"
tag: "1.5.7.907"
commit: "33075478044eb0b135b998b565e9c272d34657c5"
version: "af7af2a7a39d1487758802058e52b2a3"
build_date: "2018-07-25T23:56:14.604Z"
size_mb: 2549
size: 922374175
sif: "https://datasets.datalad.org/shub/mcw-rcc/shiny-server/1.5.7.907/2018-07-25-33075478-af7af2a7/af7af2a7a39d1487758802058e52b2a3.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/shiny-server/1.5.7.907/2018-07-25-33075478-af7af2a7/
recipe: https://datasets.datalad.org/shub/mcw-rcc/shiny-server/1.5.7.907/2018-07-25-33075478-af7af2a7/Singularity
collection: mcw-rcc/shiny-server
---

# mcw-rcc/shiny-server:1.5.7.907

```bash
$ singularity pull shub://mcw-rcc/shiny-server:1.5.7.907
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: mcw-rcc/r-base:3.5.0

%labels
Maintainer Matthew Flister
Version 07.23.18

%help
This container runs apps in Shiny Server.

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # install gdebi
    apt-get update && apt-get install -y gdebi-core && apt-get clean

    # install R shiny package
    R -e "install.packages('shiny', repos='https://cran.rstudio.com/')"

    # install shiny server
    wget https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-1.5.7.907-amd64.deb
    gdebi --n shiny-server-1.5.7.907-amd64.deb
    rm shiny-server-1.5.7.907-amd64.deb
```

## Collection

 - Name: [mcw-rcc/shiny-server](https://github.com/mcw-rcc/shiny-server)
 - License: [MIT License](https://api.github.com/licenses/mit)

