---
id: 7895
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "bwa_0-7-17"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "8fee55b9da09bee2976d3a78a04e1735"
build_date: "2020-08-26T20:39:41.692Z"
size_mb: 802
size: 254275615
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/bwa_0-7-17/2020-08-26-261b0ba2-8fee55b9/8fee55b9da09bee2976d3a78a04e1735.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/bwa_0-7-17/2020-08-26-261b0ba2-8fee55b9/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/bwa_0-7-17/2020-08-26-261b0ba2-8fee55b9/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:bwa_0-7-17

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:bwa_0-7-17
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
    yum -y install sudo autoconf automake make gcc wget perl-Data-Dumper zlib-devel bzip2 bzip2-devel xz-devel curl-devel openssl-devel ncurses-devel


    # install bwa

    wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2
    tar xvjf bwa-0.7.17.tar.bz2
    cd bwa-0.7.17/
    make
    cp bwa /usr/local/bin

    yum clean all
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

