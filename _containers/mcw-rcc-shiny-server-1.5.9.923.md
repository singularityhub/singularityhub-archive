---
id: 5372
name: "mcw-rcc/shiny-server"
branch: "1.5.9.923"
tag: "1.5.9.923"
commit: "3cb4b05cce2ccbd69acbcadd9c90b97e4a91231d"
version: "480125fc30b01eddefd8d33d0d05c06c"
build_date: "2021-04-03T23:27:52.705Z"
size_mb: 2542
size: 920997919
sif: "https://datasets.datalad.org/shub/mcw-rcc/shiny-server/1.5.9.923/2021-04-03-3cb4b05c-480125fc/480125fc30b01eddefd8d33d0d05c06c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/shiny-server/1.5.9.923/2021-04-03-3cb4b05c-480125fc/
recipe: https://datasets.datalad.org/shub/mcw-rcc/shiny-server/1.5.9.923/2021-04-03-3cb4b05c-480125fc/Singularity
collection: mcw-rcc/shiny-server
---

# mcw-rcc/shiny-server:1.5.9.923

```bash
$ singularity pull shub://mcw-rcc/shiny-server:1.5.9.923
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: mcw-rcc/r-base:3.5.1

%labels
Maintainer: Matthew Flister
R: 3.5.1
Shiny: 1.5.9.923

%help
This container runs apps in Shiny Server.

%runscript
    exec Rscript "$@"

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # install gdebi
    apt-get update && apt-get install -y gdebi-core && apt-get clean

    # install R shiny package
    R -e "install.packages('shiny', repos='https://cran.rstudio.com/')"

    # install shiny server
    wget https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-1.5.9.923-amd64.deb
    gdebi --n shiny-server-1.5.9.923-amd64.deb
    rm shiny-server-1.5.9.923-amd64.deb
```

## Collection

 - Name: [mcw-rcc/shiny-server](https://github.com/mcw-rcc/shiny-server)
 - License: [MIT License](https://api.github.com/licenses/mit)

