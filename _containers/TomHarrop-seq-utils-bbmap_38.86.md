---
id: 13952
name: "TomHarrop/seq-utils"
branch: "master"
tag: "bbmap_38.86"
commit: "81414c30d368ee8914ad4d69ea3259ad88f90277"
version: "f26c85fcae296349911cee4cd979e7650b833c89dc7636a5d178978d385f4e88"
build_date: "2021-03-03T10:36:20.432Z"
size_mb: 478.38671875
size: 501624832
sif: "https://datasets.datalad.org/shub/TomHarrop/seq-utils/bbmap_38.86/2021-03-03-81414c30-f26c85fc/f26c85fcae296349911cee4cd979e7650b833c89dc7636a5d178978d385f4e88.sif"
url: https://datasets.datalad.org/shub/TomHarrop/seq-utils/bbmap_38.86/2021-03-03-81414c30-f26c85fc/
recipe: https://datasets.datalad.org/shub/TomHarrop/seq-utils/bbmap_38.86/2021-03-03-81414c30-f26c85fc/Singularity
collection: TomHarrop/seq-utils
---

# TomHarrop/seq-utils:bbmap_38.86

```bash
$ singularity pull shub://TomHarrop/seq-utils:bbmap_38.86
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/align-utils:samtools_1.10

%help
    Container for BBMap 38.86
    https://jgi.doe.gov/data-and-tools/bbtools/

%labels
    MAINTAINER "Tom Harrop"
    VERSION "BBMap 38.86"

%post
    apt-get update
    apt-get install -y \
        default-jre-headless \
        gawk \
        pigz
     
    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.86.tar.gz/download"
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

