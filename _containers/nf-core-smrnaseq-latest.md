---
id: 3515
name: "nf-core/smrnaseq"
branch: "master"
tag: "latest"
commit: "553e17f87ecfa7880053122776fac00bdcc263b4"
version: "d0c7fb2af68a0c824fbde9c6db949b28"
build_date: "2018-07-13T21:19:59.912Z"
size_mb: 2490
size: 851406879
sif: "https://datasets.datalad.org/shub/nf-core/smrnaseq/latest/2018-07-13-553e17f8-d0c7fb2a/d0c7fb2af68a0c824fbde9c6db949b28.simg"
url: https://datasets.datalad.org/shub/nf-core/smrnaseq/latest/2018-07-13-553e17f8-d0c7fb2a/
recipe: https://datasets.datalad.org/shub/nf-core/smrnaseq/latest/2018-07-13-553e17f8-d0c7fb2a/Singularity
collection: nf-core/smrnaseq
---

# nf-core/smrnaseq:latest

```bash
$ singularity pull shub://nf-core/smrnaseq:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Alexander Peltzer <alex.peltzer@gmail.com>
    DESCRIPTION Container image containing all requirements for the nf-core/smrnaseq pipeline
    VERSION 0.2dev

%files
    environment.yml /

%post
    /opt/conda/bin/conda env update -n root -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/smrnaseq](https://github.com/nf-core/smrnaseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

