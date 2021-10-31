---
id: 3838
name: "nf-core/hlatyping"
branch: "master"
tag: "1.1.0"
commit: "a77ac44710d00c6611ec5c8369f8d37133c29b19"
version: "e6b525998e4dae8bfa05f2e7b94ac08a"
build_date: "2018-08-15T16:47:19.070Z"
size_mb: 2017
size: 591925279
sif: "https://datasets.datalad.org/shub/nf-core/hlatyping/1.1.0/2018-08-15-a77ac447-e6b52599/e6b525998e4dae8bfa05f2e7b94ac08a.simg"
url: https://datasets.datalad.org/shub/nf-core/hlatyping/1.1.0/2018-08-15-a77ac447-e6b52599/
recipe: https://datasets.datalad.org/shub/nf-core/hlatyping/1.1.0/2018-08-15-a77ac447-e6b52599/Singularity
collection: nf-core/hlatyping
---

# nf-core/hlatyping:1.1.0

```bash
$ singularity pull shub://nf-core/hlatyping:1.1.0
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Sven Fillinger <sven.fillinger@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for nf-core/hlatyping pipeline
    VERSION 1.1.0

%files
    environment.yml /

%post
    /opt/conda/bin/conda env update -n root -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/hlatyping](https://github.com/nf-core/hlatyping)
 - License: [MIT License](https://api.github.com/licenses/mit)

