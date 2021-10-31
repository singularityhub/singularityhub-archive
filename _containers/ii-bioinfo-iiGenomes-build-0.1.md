---
id: 4843
name: "ii-bioinfo/iiGenomes-build"
branch: "master"
tag: "0.1"
commit: "f3e3f4ca3b9fef740c0fbdd92cd5d10399087b1b"
version: "cd1527d8a17ea09a012da4f42060dd50"
build_date: "2018-10-30T12:35:59.845Z"
size_mb: 3248
size: 998629407
sif: "https://datasets.datalad.org/shub/ii-bioinfo/iiGenomes-build/0.1/2018-10-30-f3e3f4ca-cd1527d8/cd1527d8a17ea09a012da4f42060dd50.simg"
url: https://datasets.datalad.org/shub/ii-bioinfo/iiGenomes-build/0.1/2018-10-30-f3e3f4ca-cd1527d8/
recipe: https://datasets.datalad.org/shub/ii-bioinfo/iiGenomes-build/0.1/2018-10-30-f3e3f4ca-cd1527d8/Singularity
collection: ii-bioinfo/iiGenomes-build
---

# ii-bioinfo/iiGenomes-build:0.1

```bash
$ singularity pull shub://ii-bioinfo/iiGenomes-build:0.1
```

## Singularity Recipe

```singularity
From:continuumio/miniconda:4.5.4
Bootstrap:docker

%labels
    MAINTAINER imp/imba bioinformatics core <ii-bioinfo@imp.ac.at>
    DESCRIPTION Container image with requirements for the building the iiGenome reference genomes
    VERSION 0.1

%files
    environment.yaml /

%post
    apt-get install -y procps

    /opt/conda/bin/conda env update -n root -f /environment.yaml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [ii-bioinfo/iiGenomes-build](https://github.com/ii-bioinfo/iiGenomes-build)
 - License: None

