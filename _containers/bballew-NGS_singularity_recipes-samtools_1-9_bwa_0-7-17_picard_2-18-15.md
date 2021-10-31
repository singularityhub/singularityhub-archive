---
id: 5425
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "samtools_1-9_bwa_0-7-17_picard_2-18-15"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "f9139b9587c1ae2975c59102c2d41a38"
build_date: "2019-04-02T14:29:35.970Z"
size_mb: 1265
size: 422830111
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/samtools_1-9_bwa_0-7-17_picard_2-18-15/2019-04-02-261b0ba2-f9139b95/f9139b9587c1ae2975c59102c2d41a38.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/samtools_1-9_bwa_0-7-17_picard_2-18-15/2019-04-02-261b0ba2-f9139b95/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/samtools_1-9_bwa_0-7-17_picard_2-18-15/2019-04-02-261b0ba2-f9139b95/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:samtools_1-9_bwa_0-7-17_picard_2-18-15

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:samtools_1-9_bwa_0-7-17_picard_2-18-15
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
    
%post
    yum -y groupinstall "Development Tools"
    yum -y install sudo autoconf automake make gcc wget perl-Data-Dumper zlib-devel bzip2 bzip2-devel xz-devel curl-devel openssl-devel ncurses-devel


    # install bwa

    wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2
    tar xvjf bwa-0.7.17.tar.bz2
    cd bwa-0.7.17/
    make
    cp bwa /usr/local/bin
    cd -

    # install samtools

    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar xvjf samtools-1.9.tar.bz2
    cd samtools-1.9
    ./configure
    make
    make install
    cd -

    # install java

    yum -y install java-1.8.0-openjdk-devel


    # install picard

    wget https://github.com/broadinstitute/picard/releases/download/2.18.15/picard.jar
    mv picard.jar /bin
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

