---
id: 5422
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "svaba"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "f3ae1487882eda114fe9726af6ffb44e"
build_date: "2021-02-26T19:25:10.900Z"
size_mb: 1088
size: 348872735
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/svaba/2021-02-26-261b0ba2-f3ae1487/f3ae1487882eda114fe9726af6ffb44e.simg"
url: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/svaba/2021-02-26-261b0ba2-f3ae1487/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/svaba/2021-02-26-261b0ba2-f3ae1487/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:svaba

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:svaba
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
    PATH=/svaba/bin:$PATH
    export PATH

%post
    yum -y groupinstall "Development Tools"
    yum -y install sudo autoconf automake make cmake gcc wget perl-Data-Dumper zlib zlib-devel tar bzip2 bzip2-devel xz-devel curl-devel openssl-devel ncurses-devel

    git clone --recursive https://github.com/walaj/svaba
    cd svaba
    ./configure
    make
    make install

    yum clean all
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

