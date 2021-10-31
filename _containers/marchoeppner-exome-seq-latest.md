---
id: 8022
name: "marchoeppner/exome-seq"
branch: "master"
tag: "latest"
commit: "598b67c8ec994704ea32ae336cb77d69e9e16736"
version: "72726214d4161589b9933dedf0fe5175"
build_date: "2019-04-03T10:00:06.836Z"
size_mb: 5225
size: 1817653279
sif: "https://datasets.datalad.org/shub/marchoeppner/exome-seq/latest/2019-04-03-598b67c8-72726214/72726214d4161589b9933dedf0fe5175.simg"
url: https://datasets.datalad.org/shub/marchoeppner/exome-seq/latest/2019-04-03-598b67c8-72726214/
recipe: https://datasets.datalad.org/shub/marchoeppner/exome-seq/latest/2019-04-03-598b67c8-72726214/Singularity
collection: marchoeppner/exome-seq
---

# marchoeppner/exome-seq:latest

```bash
$ singularity pull shub://marchoeppner/exome-seq:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/anaconda

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the exome-seq pipeline
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/exome-seq-1.0/bin:$PATH
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

 - Name: [marchoeppner/exome-seq](https://github.com/marchoeppner/exome-seq)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

