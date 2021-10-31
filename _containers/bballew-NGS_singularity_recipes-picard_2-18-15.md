---
id: 7896
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "picard_2-18-15"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "4b6fc9dc7189352ca0578d855ca15733"
build_date: "2021-03-04T18:06:30.289Z"
size_mb: 1046
size: 350425119
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/picard_2-18-15/2021-03-04-261b0ba2-4b6fc9dc/4b6fc9dc7189352ca0578d855ca15733.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/picard_2-18-15/2021-03-04-261b0ba2-4b6fc9dc/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/picard_2-18-15/2021-03-04-261b0ba2-4b6fc9dc/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:picard_2-18-15

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:picard_2-18-15
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

    # install java

    yum -y install java-1.8.0-openjdk-devel

    # install picard

    wget https://github.com/broadinstitute/picard/releases/download/2.18.15/picard.jar
    mv picard.jar /bin
    
    yum clean all
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

