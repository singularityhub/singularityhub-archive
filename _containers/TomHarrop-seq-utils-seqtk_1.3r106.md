---
id: 11651
name: "TomHarrop/seq-utils"
branch: "master"
tag: "seqtk_1.3r106"
commit: "cd07278aabfe76ff52c524190ccbc5a5153a9061"
version: "fa5b5a3190e6c330ecc0dcb9483dbd4f46950fa0b0d126687123ffdb2d152897"
build_date: "2019-11-19T23:11:20.068Z"
size_mb: 57.53515625
size: 60329984
sif: "https://datasets.datalad.org/shub/TomHarrop/seq-utils/seqtk_1.3r106/2019-11-19-cd07278a-fa5b5a31/fa5b5a3190e6c330ecc0dcb9483dbd4f46950fa0b0d126687123ffdb2d152897.sif"
url: https://datasets.datalad.org/shub/TomHarrop/seq-utils/seqtk_1.3r106/2019-11-19-cd07278a-fa5b5a31/
recipe: https://datasets.datalad.org/shub/TomHarrop/seq-utils/seqtk_1.3r106/2019-11-19-cd07278a-fa5b5a31/Singularity
collection: TomHarrop/seq-utils
---

# TomHarrop/seq-utils:seqtk_1.3r106

```bash
$ singularity pull shub://TomHarrop/seq-utils:seqtk_1.3r106
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.10.3

%help
    Seqtk 1.3 (r106)
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Seqtk 1.3 (r106)"

%post
    # dependencies
    apk add --update \
        bash \
        build-base \
        zlib-dev

    # download seqtk
    wget \
        -O  seqtk.tar.gz \
        --no-check-certificate \
        https://github.com/lh3/seqtk/archive/v1.3.tar.gz
    mkdir seqtk
    tar -zxf seqtk.tar.gz \
        -C seqtk \
        --strip-components 1
    
    # build & install
    cd seqtk || exit 1
    make
    make install

    # tidy up
    cd .. || exit 1
    rm -rf seqtk seqtk.tar.gz

%runscript
    exec /usr/local/bin/seqtk "$@"
```

## Collection

 - Name: [TomHarrop/seq-utils](https://github.com/TomHarrop/seq-utils)
 - License: None

