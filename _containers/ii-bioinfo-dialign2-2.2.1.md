---
id: 5265
name: "ii-bioinfo/dialign2"
branch: "master"
tag: "2.2.1"
commit: "b409431e3471ddc9aaea068dc1e988d08092eff8"
version: "bb6625a94a46e62f432321d202f883df"
build_date: "2018-10-18T17:22:06.231Z"
size_mb: 523
size: 179589151
sif: "https://datasets.datalad.org/shub/ii-bioinfo/dialign2/2.2.1/2018-10-18-b409431e-bb6625a9/bb6625a94a46e62f432321d202f883df.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ii-bioinfo/dialign2/2.2.1/2018-10-18-b409431e-bb6625a9/
recipe: https://datasets.datalad.org/shub/ii-bioinfo/dialign2/2.2.1/2018-10-18-b409431e-bb6625a9/Singularity
collection: ii-bioinfo/dialign2
---

# ii-bioinfo/dialign2:2.2.1

```bash
$ singularity pull shub://ii-bioinfo/dialign2:2.2.1
```

## Singularity Recipe

```singularity
From:continuumio/miniconda:4.5.4
Bootstrap:docker

%labels
    MAINTAINER imp/imba bioinformatics core <ii-bioinfo@imp.ac.at>
    DESCRIPTION dialign2 v2.2.1 conda based singularity container
    VERSION 2.2.1

%files
    environment.yaml /

%post
    apt-get install -y procps

    /opt/conda/bin/conda env update -n root -f /environment.yaml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [ii-bioinfo/dialign2](https://github.com/ii-bioinfo/dialign2)
 - License: None

