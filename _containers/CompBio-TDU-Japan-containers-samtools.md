---
id: 2304
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "samtools"
commit: "58478a9f251d425fc6f576e300ac0cf22907274b"
version: "3e8ea3d658ca24ee6e9424a3b7dbd5c7"
build_date: "2021-03-10T22:36:11.933Z"
size_mb: 22
size: 6787103
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/samtools/2021-03-10-58478a9f-3e8ea3d6/3e8ea3d658ca24ee6e9424a3b7dbd5c7.simg"
url: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/samtools/2021-03-10-58478a9f-3e8ea3d6/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/samtools/2021-03-10-58478a9f-3e8ea3d6/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:samtools

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:samtools
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: alpine

%post
    apk add --update --no-cache bash ncurses bzip2-dev xz-dev
    apk --nocache add --virtual build-deps build-base build-base zlib-dev ncurses-dev musl-dev libcurl curl
    wget https://github.com/samtools/samtools/releases/download/1.7/samtools-1.7.tar.bz2
    tar xf samtools-1.7.tar.bz2
    rm -rf samtools-1.7.tar.bz2
    cd samtools-1.7
    ./configure
    make
    make install
    cd ;apk del build-deps
    rm -rf /samtools-1.7
%runscript
    samtools "$@"
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

