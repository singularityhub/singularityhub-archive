---
id: 4711
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "htslib_1-9"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "b682c5dda24d4a676e9a115f791e5411"
build_date: "2019-04-02T14:29:35.863Z"
size_mb: 1010
size: 321712159
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/htslib_1-9/2019-04-02-261b0ba2-b682c5dd/b682c5dda24d4a676e9a115f791e5411.simg"
url: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/htslib_1-9/2019-04-02-261b0ba2-b682c5dd/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/htslib_1-9/2019-04-02-261b0ba2-b682c5dd/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:htslib_1-9

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:htslib_1-9
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%labels
    AUTHOR BBallew

%post
    yum -y groupinstall "Development Tools"
    yum -y install autoconf automake make gcc wget perl-Data-Dumper zlib-devel bzip2 bzip2-devel xz-devel curl-devel openssl-devel

    wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
    tar xvjf htslib-1.9.tar.bz2
    cd htslib-1.9
    ./configure
    make
    make install
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

