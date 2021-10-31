---
id: 3583
name: "nf-core/hlatyping"
branch: "master"
tag: "1.0.0"
commit: "eda4fedd5ddc3c1cffcf404a4ec4dd3fd75fa8d8"
version: "f2b76fe3c0d5022b9cf25e677f990d6a"
build_date: "2018-07-18T15:17:48.484Z"
size_mb: 1885
size: 549478431
sif: "https://datasets.datalad.org/shub/nf-core/hlatyping/1.0.0/2018-07-18-eda4fedd-f2b76fe3/f2b76fe3c0d5022b9cf25e677f990d6a.simg"
url: https://datasets.datalad.org/shub/nf-core/hlatyping/1.0.0/2018-07-18-eda4fedd-f2b76fe3/
recipe: https://datasets.datalad.org/shub/nf-core/hlatyping/1.0.0/2018-07-18-eda4fedd-f2b76fe3/Singularity
collection: nf-core/hlatyping
---

# nf-core/hlatyping:1.0.0

```bash
$ singularity pull shub://nf-core/hlatyping:1.0.0
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Sven Fillinger <sven.fillinger@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for nf-core/hlatyping pipeline
    VERSION 1.0.0

%files
    environment.yml /

%post
    /opt/conda/bin/conda env update -n root -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/hlatyping](https://github.com/nf-core/hlatyping)
 - License: [MIT License](https://api.github.com/licenses/mit)

