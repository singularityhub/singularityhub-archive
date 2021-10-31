---
id: 4177
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "trinity_2.8.3"
commit: "8c0f53404dc7a88dfd156e6d468d861156fb6e5a"
version: "b96521a7980ab68a2e75759d0c65db36"
build_date: "2018-08-24T05:04:45.715Z"
size_mb: 4735
size: 1870774303
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.8.3/2018-08-24-8c0f5340-b96521a7/b96521a7980ab68a2e75759d0c65db36.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/trinity_2.8.3/2018-08-24-8c0f5340-b96521a7/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.8.3/2018-08-24-8c0f5340-b96521a7/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:trinity_2.8.3

```bash
$ singularity pull shub://TomHarrop/singularity-containers:trinity_2.8.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.8.3

%help

    Container for Trinity 2.8.3
    https://github.com/trinityrnaseq/trinityrnaseq/releases

%labels

    VERSION "Trinity 2.8.3"

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

    PATH="${PATH}:/usr/local/bin/trinityrnaseq/util:/usr/local/bin/trinityrnaseq/util/support_scripts:/usr/local/bin/trinityrnaseq/util/misc"

%runscript

    exec /usr/local/bin/trinityrnaseq/Trinity "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

