---
id: 5423
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "bedtools_2-27-1"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "2a3a2f78097d271c9e5cf5ccb4991913"
build_date: "2021-02-26T19:25:34.232Z"
size_mb: 1012
size: 339525663
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/bedtools_2-27-1/2021-02-26-261b0ba2-2a3a2f78/2a3a2f78097d271c9e5cf5ccb4991913.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/bedtools_2-27-1/2021-02-26-261b0ba2-2a3a2f78/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/bedtools_2-27-1/2021-02-26-261b0ba2-2a3a2f78/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:bedtools_2-27-1

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:bedtools_2-27-1
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

#    yum install BEDTools

    wget https://github.com/arq5x/bedtools2/releases/download/v2.27.1/bedtools-2.27.1.tar.gz
    tar -zxvf bedtools-2.27.1.tar.gz
    cd bedtools2
    make
    cp ./bin/* /usr/local/bin/
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

