---
id: 4710
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "bcftools_1-9"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "43001681fa923ad3f4c79a10c460c55b"
build_date: "2021-02-26T19:25:23.222Z"
size_mb: 986
size: 312713247
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/bcftools_1-9/2021-02-26-261b0ba2-43001681/43001681fa923ad3f4c79a10c460c55b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/bcftools_1-9/2021-02-26-261b0ba2-43001681/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/bcftools_1-9/2021-02-26-261b0ba2-43001681/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:bcftools_1-9

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:bcftools_1-9
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
    yum -y install autoconf automake make gcc wget perl-Data-Dumper zlib-devel bzip2 bzip2-devel xz-devel curl-devel openssl-devel

    wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
    tar xvjf bcftools-1.9.tar.bz2
    cd bcftools-1.9
    ./configure
    make
    make install
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

