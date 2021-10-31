---
id: 5421
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "samtools_1-9"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "5df4bfb0c08aeeca05e1c2d6ca7cbfae"
build_date: "2021-03-01T17:54:45.693Z"
size_mb: 864
size: 273350687
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/samtools_1-9/2021-03-01-261b0ba2-5df4bfb0/5df4bfb0c08aeeca05e1c2d6ca7cbfae.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/samtools_1-9/2021-03-01-261b0ba2-5df4bfb0/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/samtools_1-9/2021-03-01-261b0ba2-5df4bfb0/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:samtools_1-9

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:samtools_1-9
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
    mkdir -p ${SINGULARITY_ROOTFS}/exec
    
%post
    yum -y groupinstall "Development Tools"
    yum -y install autoconf automake make gcc wget perl-Data-Dumper zlib-devel bzip2 bzip2-devel xz-devel curl-devel openssl-devel ncurses-devel

    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar xvjf samtools-1.9.tar.bz2
    cd samtools-1.9
    ./configure
    make
    make install

    yum clean all
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

