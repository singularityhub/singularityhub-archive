---
id: 5438
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "mocca_0-1"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "7336688502fe54991e6fae14b110f81f"
build_date: "2019-04-02T15:48:59.936Z"
size_mb: 2089
size: 599212063
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/mocca_0-1/2019-04-02-261b0ba2-73366885/7336688502fe54991e6fae14b110f81f.simg"
url: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/mocca_0-1/2019-04-02-261b0ba2-73366885/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/mocca_0-1/2019-04-02-261b0ba2-73366885/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:mocca_0-1

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:mocca_0-1
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%labels
    AUTHOR BBallew

%setup

    mkdir -p ${SINGULARITY_ROOTFS}/input
    mkdir -p ${SINGULARITY_ROOTFS}/output
    mkdir -p ${SINGULARITY_ROOTFS}/ref
    mkdir -p ${SINGULARITY_ROOTFS}/scratch

%environment
    export PATH="/svaba/bin:/breakdancer/build/bin:/breakdancer/perl:/manta-1.4.0.centos6_x86_64/bin:$PATH"

%post
    yum -y groupinstall "Development Tools"
    yum -y install sudo autoconf automake make cmake gcc wget perl-Data-Dumper zlib zlib-devel tar bzip2 bzip2-devel xz-devel curl-devel openssl-devel ncurses-devel

    #### install bwa

    wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2
    tar xvjf bwa-0.7.17.tar.bz2
    cd bwa-0.7.17/
    make
    cp bwa /usr/local/bin
    cd -

    #### install samtools

    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar xvjf samtools-1.9.tar.bz2
    cd samtools-1.9
    ./configure
    make
    make install
    cd -

    #### install java

    yum -y install java-1.8.0-openjdk-devel

    #### install picard

    wget https://github.com/broadinstitute/picard/releases/download/2.18.15/picard.jar
    mv picard.jar /bin

    #### install svaba

    git clone --recursive https://github.com/walaj/svaba
    cd svaba
    ./configure
    make
    make install
    cd -

    #### install manta

    wget https://github.com/Illumina/manta/releases/download/v1.4.0/manta-1.4.0.centos6_x86_64.tar.bz2
    tar xvjf manta-1.4.0.centos6_x86_64.tar.bz2

    #### install delly 

    wget https://github.com/dellytools/delly/releases/download/v0.7.9/delly_v0.7.9_parallel_linux_x86_64bit
    chmod +x delly_v0.7.9_parallel_linux_x86_64bit
    mv delly_v0.7.9_parallel_linux_x86_64bit /usr/bin/delly

    #### install breakdancer

    git clone --recursive https://github.com/genome/breakdancer.git
    cd breakdancer
    mkdir build
    cd build
    cmake .. -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr/local
    make
    sudo make install
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

