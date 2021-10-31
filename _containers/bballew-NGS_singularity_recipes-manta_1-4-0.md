---
id: 7899
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "manta_1-4-0"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "dc91903d1f63c512adc912d1cd77cbf5"
build_date: "2021-02-26T19:25:29.048Z"
size_mb: 1134
size: 289968159
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/manta_1-4-0/2021-02-26-261b0ba2-dc91903d/dc91903d1f63c512adc912d1cd77cbf5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/manta_1-4-0/2021-02-26-261b0ba2-dc91903d/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/manta_1-4-0/2021-02-26-261b0ba2-dc91903d/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:manta_1-4-0

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:manta_1-4-0
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
    export PATH="/manta-1.4.0.centos6_x86_64/bin:$PATH"

%post
    yum -y groupinstall "Development Tools"
    yum -y install wget tar bzip2 bzip2-devel

    #### install manta

    wget https://github.com/Illumina/manta/releases/download/v1.4.0/manta-1.4.0.centos6_x86_64.tar.bz2
    tar xvjf manta-1.4.0.centos6_x86_64.tar.bz2

    yum clean all
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

