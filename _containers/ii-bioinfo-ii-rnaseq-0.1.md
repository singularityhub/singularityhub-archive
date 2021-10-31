---
id: 5479
name: "ii-bioinfo/ii-rnaseq"
branch: "master"
tag: "0.1"
commit: "948d69a852a3321f60470d5cfc5d732fd968ce55"
version: "d3ff68844bca4a83c0d8cfe136f3e5f9"
build_date: "2019-09-18T08:53:23.552Z"
size_mb: 5517
size: 1736409119
sif: "https://datasets.datalad.org/shub/ii-bioinfo/ii-rnaseq/0.1/2019-09-18-948d69a8-d3ff6884/d3ff68844bca4a83c0d8cfe136f3e5f9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ii-bioinfo/ii-rnaseq/0.1/2019-09-18-948d69a8-d3ff6884/
recipe: https://datasets.datalad.org/shub/ii-bioinfo/ii-rnaseq/0.1/2019-09-18-948d69a8-d3ff6884/Singularity
collection: ii-bioinfo/ii-rnaseq
---

# ii-bioinfo/ii-rnaseq:0.1

```bash
$ singularity pull shub://ii-bioinfo/ii-rnaseq:0.1
```

## Singularity Recipe

```singularity
From:continuumio/miniconda:4.5.4
Bootstrap:docker

%labels
    MAINTAINER imp/imba bioinformatics core <bioinfo.grp@imp.ac.at>
    DESCRIPTION Container image with requirements for the ii-bioinfo/ii-rnaseq pipeline (based on nf-core/rnaseq)
    VERSION 0.1

%files
    environment.yaml /

%post
    apt-get install -y procps

    /opt/conda/bin/conda env update -n root -f /environment.yaml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [ii-bioinfo/ii-rnaseq](https://github.com/ii-bioinfo/ii-rnaseq)
 - License: None

