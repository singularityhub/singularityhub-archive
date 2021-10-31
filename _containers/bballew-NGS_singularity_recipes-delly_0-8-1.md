---
id: 8074
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "delly_0-8-1"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "ef603b0f041f63946c55a3434685a005"
build_date: "2021-03-01T17:56:24.258Z"
size_mb: 1037
size: 335581215
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/delly_0-8-1/2021-03-01-261b0ba2-ef603b0f/ef603b0f041f63946c55a3434685a005.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/delly_0-8-1/2021-03-01-261b0ba2-ef603b0f/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/delly_0-8-1/2021-03-01-261b0ba2-ef603b0f/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:delly_0-8-1

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:delly_0-8-1
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
#MirrorURL: http://vault.centos.org/6.9/os/x86_64/
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
    export PATH="/delly/src/:$PATH"

%post
   # #### rebuild rpm database ####
   # # if this image is built in a VM running centos 6.9 or 6.10, it builds successfully
   # # if it's built in a VM with centos 7 or on singularity hub, the rpm database is corrupt
   # # this should correct that issue
   # rm -f /var/lib/rpm/__db*
   # rpm -vv --rebuilddb > /tmp/rpmrebuilddb.log 2>&1


    yum -y groupinstall "Development Tools"
    yum -y install autoconf automake make gcc wget perl-Data-Dumper zlib-devel bzip2 bzip2-devel xz-devel curl-devel openssl-devel ncurses-devel boost boost-thread boost-devel


    #### install delly 

    git clone --recursive https://github.com/dellytools/delly.git
    cd delly/
    make all
    cd -

    #wget https://github.com/dellytools/delly/releases/download/v0.7.9/delly_v0.7.9_parallel_linux_x86_64bit
    #chmod +x delly_v0.7.9_parallel_linux_x86_64bit
    #mv delly_v0.7.9_parallel_linux_x86_64bit /usr/bin/delly

    yum clean all
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

