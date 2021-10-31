---
id: 3994
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "trinity_2.8.0"
commit: "b9be7c14955f537fe4e83369442f353e9bb3df09"
version: "fb561f4c0dd192183da8c51ce8183ac7"
build_date: "2018-08-15T09:33:41.713Z"
size_mb: 4737
size: 1871069215
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.8.0/2018-08-15-b9be7c14-fb561f4c/fb561f4c0dd192183da8c51ce8183ac7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/trinity_2.8.0/2018-08-15-b9be7c14-fb561f4c/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/trinity_2.8.0/2018-08-15-b9be7c14-fb561f4c/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:trinity_2.8.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:trinity_2.8.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trinityrnaseq/trinityrnaseq:2.8.0

%help

    Container for Trinity 2.8.0
    https://github.com/trinityrnaseq/trinityrnaseq/releases

%labels

    VERSION "Trinity 2.8.0"

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

