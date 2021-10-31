---
id: 5619
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "vcftools"
commit: "144df7beaa207eb20e0784ee42f833e65ffdf2f9"
version: "c4e75bb53240da2a1d423a8195494e79"
build_date: "2020-06-26T10:26:31.950Z"
size_mb: 80
size: 22085663
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/vcftools/2020-06-26-144df7be-c4e75bb5/c4e75bb53240da2a1d423a8195494e79.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CompBio-TDU-Japan/containers/vcftools/2020-06-26-144df7be-c4e75bb5/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/vcftools/2020-06-26-144df7be-c4e75bb5/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:vcftools

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:vcftools
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: alpine

%post
    apk add --update --no-cache perl bash bzip2-dev xz-dev libstdc++
    apk add --update --no-cache --virtual build-deps autoconf automake libtool git build-base zlib-dev
    git clone https://github.com/vcftools/vcftools.git
    git clone https://github.com/samtools/htslib.git
    git clone https://github.com/biosugar0/refmaker.git
    mv refmaker/refmaker /usr/local/bin/
    rm -rf refmaker
    cd /htslib
    autoheader
    autoconf
    ./configure
    make
    make install
    cd /vcftools
    ./autogen.sh
    ./configure
    make
    make install
    apk del build-deps
    cd ; rm -rf /htslib /vcftools

%apprun vcf-consensus
    vcf-consensus "$@"

%apprun tabix
    tabix "$@"

%labels
    Version v0.5
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

