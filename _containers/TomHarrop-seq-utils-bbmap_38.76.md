---
id: 12288
name: "TomHarrop/seq-utils"
branch: "master"
tag: "bbmap_38.76"
commit: "aaac7a1eb699dbb70dfcb4684ae8df46e2d296de"
version: "597688a84f246245761092d696fcea1d071bb355485be8c4acba24c571543377"
build_date: "2021-03-15T23:21:08.601Z"
size_mb: 227.0
size: 161067008
sif: "https://datasets.datalad.org/shub/TomHarrop/seq-utils/bbmap_38.76/2021-03-15-aaac7a1e-597688a8/597688a84f246245761092d696fcea1d071bb355485be8c4acba24c571543377.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/seq-utils/bbmap_38.76/2021-03-15-aaac7a1e-597688a8/
recipe: https://datasets.datalad.org/shub/TomHarrop/seq-utils/bbmap_38.76/2021-03-15-aaac7a1e-597688a8/Singularity
collection: TomHarrop/seq-utils
---

# TomHarrop/seq-utils:bbmap_38.76

```bash
$ singularity pull shub://TomHarrop/seq-utils:bbmap_38.76
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/singularity-containers:samtools_1.9

%help
    Container for BBMap 38.76
    https://jgi.doe.gov/data-and-tools/bbtools/

%labels
    MAINTAINER "Tom Harrop"
    VERSION "BBMap 38.76"

%post
    apk add --update \
        gawk \
        openjdk8

    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.76.tar.gz"
    mkdir bbmap-install
    tar -zxf bbmap.tar.gz \
        -C bbmap-install \
        --strip-components 1
    cp -r bbmap-install/resources/* /
    cp -r bbmap-install/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap-install
```

## Collection

 - Name: [TomHarrop/seq-utils](https://github.com/TomHarrop/seq-utils)
 - License: None

