---
id: 10365
name: "richelbilderbeek/singularity_example_5"
branch: "master"
tag: "latest"
commit: "bd3941f86408f8e214c41eb8a5eda2e5ae3b1575"
version: "1505c8b68cc779b21b0fee2d932733b4"
build_date: "2019-07-27T08:45:24.314Z"
size_mb: 1694.0
size: 612573215
sif: "https://datasets.datalad.org/shub/richelbilderbeek/singularity_example_5/latest/2019-07-27-bd3941f8-1505c8b6/1505c8b68cc779b21b0fee2d932733b4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/richelbilderbeek/singularity_example_5/latest/2019-07-27-bd3941f8-1505c8b6/
recipe: https://datasets.datalad.org/shub/richelbilderbeek/singularity_example_5/latest/2019-07-27-bd3941f8-1505c8b6/Singularity
collection: richelbilderbeek/singularity_example_5
---

# richelbilderbeek/singularity_example_5:latest

```bash
$ singularity pull shub://richelbilderbeek/singularity_example_5:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub

From: pavel-demin/singularity-ubuntu:1804

%runscript

    cat /etc/*-release

%post

    sed -i 's/bionic/disco/g' /etc/apt/sources.list
    apt-get update
    apt-get --yes upgrade
    apt-get --yes dist-upgrade 

%labels

    AUTHOR Richel J.C. Bilderbeek

    NAME singularity_example_5
 
    DESCRIPTION Singularity example 5: Singularity 2.5, Ubuntu 19.04 (disco)

    USAGE simply run the container

    URL https://github.com/richelbilderbeek/singularity_example_5

    VERSION 1.0
```

## Collection

 - Name: [richelbilderbeek/singularity_example_5](https://github.com/richelbilderbeek/singularity_example_5)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

