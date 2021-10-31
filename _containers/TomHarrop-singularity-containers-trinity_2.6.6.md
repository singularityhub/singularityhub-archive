---
id: 2982
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "trinity_2.6.6"
commit: "a17b60edb0e864b80b41b33d78d624a6091227fc"
version: "07006200b0c0ca0d2de9b8327a047963"
build_date: "2018-05-29T12:58:47.600Z"
size_mb: 4785
size: 1900548127
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.6.6/2018-05-29-a17b60ed-07006200/07006200b0c0ca0d2de9b8327a047963.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.6.6/2018-05-29-a17b60ed-07006200/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.6.6/2018-05-29-a17b60ed-07006200/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:trinity_2.6.6

```bash
$ singularity pull shub://TomHarrop/singularity-containers:trinity_2.6.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.6.6

%help

    Container for Trinity 2.6.6
    https://github.com/trinityrnaseq/trinityrnaseq/releases

%labels

    VERSION "Trinity 2.6.6"

%post
    
    apt-get update \
        && apt-get install -y \
        language-pack-en

    # install RSEM
    mkdir rsem-install
    wget -O "rsem.tar.gz" \
        https://github.com/deweylab/RSEM/archive/v1.3.0.tar.gz
    tar -zxf rsem.tar.gz \
        -C rsem-install \
        --strip-components 1
    cd rsem-install
    make && make install
    cd ..
    rm -rf rsem.tar.gz rsem-install

%environment

    PATH="${PATH}:/usr/local/bin/trinityrnaseq/util:/usr/local/bin/trinityrnaseq/util/support_scripts"

%runscript

    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

