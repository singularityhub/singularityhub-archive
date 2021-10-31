---
id: 8301
name: "marchoeppner/miRNApipe"
branch: "devel"
tag: "latest"
commit: "40fd14d32322a385751a55ec2de639b13f1a9e31"
version: "f090ced1802251ab9b9d8313375a7e7d"
build_date: "2019-04-23T09:14:03.177Z"
size_mb: 2666
size: 849702943
sif: "https://datasets.datalad.org/shub/marchoeppner/miRNApipe/latest/2019-04-23-40fd14d3-f090ced1/f090ced1802251ab9b9d8313375a7e7d.simg"
url: https://datasets.datalad.org/shub/marchoeppner/miRNApipe/latest/2019-04-23-40fd14d3-f090ced1/
recipe: https://datasets.datalad.org/shub/marchoeppner/miRNApipe/latest/2019-04-23-40fd14d3-f090ced1/Singularity
collection: marchoeppner/miRNApipe
---

# marchoeppner/miRNApipe:latest

```bash
$ singularity pull shub://marchoeppner/miRNApipe:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:nfcore/base

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the miRNApipe pipeline
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/mirnapipe-1.0/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

    mkdir -p /ifs
    apt-get -y install procps
```

## Collection

 - Name: [marchoeppner/miRNApipe](https://github.com/marchoeppner/miRNApipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

