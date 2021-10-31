---
id: 2370
name: "verdurin/singularity-defs"
branch: "master"
tag: "latest"
commit: "83856dc0664b48b3ec82767b5c76fe0a8ca00806"
version: "62af60e75077022953a1939682e24b43"
build_date: "2018-04-02T02:50:45.159Z"
size_mb: 3651
size: 2415251487
sif: "https://datasets.datalad.org/shub/verdurin/singularity-defs/latest/2018-04-02-83856dc0-62af60e7/62af60e75077022953a1939682e24b43.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/verdurin/singularity-defs/latest/2018-04-02-83856dc0-62af60e7/
recipe: https://datasets.datalad.org/shub/verdurin/singularity-defs/latest/2018-04-02-83856dc0-62af60e7/Singularity
collection: verdurin/singularity-defs
---

# verdurin/singularity-defs:latest

```bash
$ singularity pull shub://verdurin/singularity-defs:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://uk.archive.ubuntu.com/ubuntu/

%post
    apt-get update && apt-get install -y curl bzip2

    curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
    bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
    rm Miniconda-latest-Linux-x86_64.sh
    PATH=/miniconda/bin:${PATH}
    conda update -y conda


    conda install -y pytorch
```

## Collection

 - Name: [verdurin/singularity-defs](https://github.com/verdurin/singularity-defs)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

