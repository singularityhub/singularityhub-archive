---
id: 11568
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "quast_5.0.2"
commit: "321e91b5f4ada4a8e7cc194f35edfa84ebebd13b"
version: "c8ee58fa733f2ec0cde85754fcb368178f5f35ae3e35342a42ab8aed0e33dd03"
build_date: "2021-03-15T23:45:08.849Z"
size_mb: 1067.234375
size: 1119076352
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/quast_5.0.2/2021-03-15-321e91b5-c8ee58fa/c8ee58fa733f2ec0cde85754fcb368178f5f35ae3e35342a42ab8aed0e33dd03.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assembly-utils/quast_5.0.2/2021-03-15-321e91b5-c8ee58fa/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/quast_5.0.2/2021-03-15-321e91b5-c8ee58fa/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:quast_5.0.2

```bash
$ singularity pull shub://TomHarrop/assembly-utils:quast_5.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help
    Quast 5.0.2
    http://quast.bioinf.spbau.ru/

%labels
    MAINTAINER "Tom Harrop"
    VERSION "QUAST 5.0.2"

%post
    # faster apt downloads, will it break?
    export DEBIAN_FRONTEND=noninteractive
    (
        . /etc/os-release
        cat << _EOF_ > mirror.txt
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    # deps
    apt-get update
    apt-get install -y \
        build-essential \
        default-jre \
        language-pack-en \
        libfreetype6-dev \
        libgd-perl \
        libpng-dev \
        libtime-hr-perl \
        pkg-config \
        python \
        python-matplotlib \
        python-pip \
        python-setuptools \
        r-base-dev \
        wget \
        zlib1g-dev

    # install circos
    perl -MCPAN -e \
        'install Config::General ; \
        install Clone ; \
        install Font::TTF::Font ; \
        install List::MoreUtils ; \
        install Math::Bezier ; \
        install Math::Round ; \
        install Math::VecStat ; \
        install Params::Validate ; \
        install Readonly ; \
        install Regexp::Common ; \
        install Set::IntSpan ; \
        install Statistics::Basic ; \
        install SVG ; \
        install Text::Format'

    mkdir circos
    wget -O "circos.tar.gz" \
        http://circos.ca/distribution/circos-0.69-6.tgz
    tar -zxf circos.tar.gz \
        -C circos \
        --strip-components 1
    rm circos.tar.gz
    export PATH="${PATH}:/circos/bin"
    circos -modules

    # install quast
    mkdir quast
    wget -O "quast.tar.gz" \
        https://downloads.sourceforge.net/project/quast/quast-5.0.2.tar.gz
    tar -zxf quast.tar.gz \
        -C quast \
        --strip-components 1
    cd quast || exit 1
    ./setup.py install_full
    cd .. || exit 1
    rm quast.tar.gz

    # re-download genemark "license" (needs BASH)
    cat <<- '_EOF_' > run_me.sh
    cd /usr/local/lib/python2.7/dist-packages/quast-5.0.2-py2.7.egg/quast_libs/genemark/gm_keys || exit 1
    rm *
    wget \
        --post-data='program=gmhmme&os=linux64&name=http://singularity-hub.org/containers/6233&institution=na&country=na&email=na@na.com&submit=I+agree+to+the+terms+of+this+license+agreement' \
        http://exon.gatech.edu/GeneMark/license_download.cgi
    cat license_download.cgi
    grep -Po 'http://.*?gm_key_32.gz' license_download.cgi
    url32="$(grep -Po "http://.*?gm_key_32.gz" license_download.cgi)"
    url64="${url32/gm_key_32/gm_key_64}"
    wget "${url32}"
    wget "${url64}"
    gunzip *.gz
    rm license_download.cgi
_EOF_
    /bin/bash -eux run_me.sh
    rm run_me.sh

    # test quast
    cd quast || exit 1
    ./setup.py test
    mv quast_test_output ../
    chmod -R 777 ../quast_test_output
    cd .. || exit 1   
    rm -r quast

%environment
    export PATH="${PATH}:/circos/bin"

%runscript
    exec /usr/local/bin/quast.py "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

