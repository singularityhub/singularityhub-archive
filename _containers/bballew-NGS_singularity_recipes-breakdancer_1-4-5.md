---
id: 5424
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "breakdancer_1-4-5"
commit: "261b0ba21401aa85360fa54efa5ba7f093fdc71a"
version: "14ba9f68f48eeac9d9428b0981691aa0"
build_date: "2021-02-26T19:25:44.969Z"
size_mb: 1150
size: 339021855
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/breakdancer_1-4-5/2021-02-26-261b0ba2-14ba9f68/14ba9f68f48eeac9d9428b0981691aa0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bballew/NGS_singularity_recipes/breakdancer_1-4-5/2021-02-26-261b0ba2-14ba9f68/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/breakdancer_1-4-5/2021-02-26-261b0ba2-14ba9f68/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:breakdancer_1-4-5

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:breakdancer_1-4-5
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

%environment
    PATH=/breakdancer/build/bin:/breakdancer/perl:$PATH
    export PATH

%post
    yum -y groupinstall "Development Tools"
    yum -y install sudo autoconf automake make cmake gcc wget perl-Data-Dumper zlib zlib-devel tar bzip2 bzip2-devel xz-devel curl-devel openssl-devel ncurses-devel
    yum -y install epel-release perl perl-CPAN perl-App-cpanminus perl-Archive-Tar perl-Want perl-TermReadKey gd gd-devel
    #yum -y install perl-Statistics-Descriptive perl-GD-Graph-histogram
    
    cpanm Statistics::Descriptive
    cpanm GD::Graph::histogram
    
    # install samtools

    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar xvjf samtools-1.9.tar.bz2
    cd samtools-1.9
    ./configure
    make
    make install
    cd -

    # install breakdancer

    git clone --recursive https://github.com/genome/breakdancer.git
    cd breakdancer
    mkdir build
    cd build
    cmake .. -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr/local
    make
    sudo make install

    yum clean all
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

