---
id: 13940
name: "prete/singularity-recipes"
branch: "master"
tag: "4.0.2"
commit: "4cc8b093666345677256671e82bd3114d5fdea06"
version: "ec063d99fcca204abeed2b2cb2e996f46665430cacc444692c8754210743cb07"
build_date: "2020-08-13T20:31:55.962Z"
size_mb: 560.88671875
size: 588132352
sif: "https://datasets.datalad.org/shub/prete/singularity-recipes/4.0.2/2020-08-13-4cc8b093-ec063d99/ec063d99fcca204abeed2b2cb2e996f46665430cacc444692c8754210743cb07.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/prete/singularity-recipes/4.0.2/2020-08-13-4cc8b093-ec063d99/
recipe: https://datasets.datalad.org/shub/prete/singularity-recipes/4.0.2/2020-08-13-4cc8b093-ec063d99/Singularity
collection: prete/singularity-recipes
---

# prete/singularity-recipes:4.0.2

```bash
$ singularity pull shub://prete/singularity-recipes:4.0.2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: rocker/r-base:4.0.2

%post
    # set RStudio Server version and architecture
    export RSERVER_VERSION=1.3.1073
    export RSERVER_ARCH=amd64

    # get packages
    DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y -qq --no-install-recommends \
        wget gdebi \
        libapparmor1 libedit2 libc6 psmisc rrdtool \

    # download rstudio server package
    wget --no-verbose -O rstudio-server.deb \
        https://download2.rstudio.org/server/bionic/amd64/rstudio-server-$RSERVER_VERSION-$RSERVER_ARCH.deb
    
    # install rstudio server
    gdebi -n rstudio-server.deb
    
#    chmod -R 777 /var/run/rstudio-server
#    chmod -R 777 /etc/rstudio/
#    chmod +t /var/run/rstudio-server

    # apt cleanup
    rm -rf  rstudio-server.deb
```

## Collection

 - Name: [prete/singularity-recipes](https://github.com/prete/singularity-recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

