---
id: 15613
name: "heathsc/gemBS-rs"
branch: "master"
tag: "latest"
commit: "29b0dc4939cbb8e85bd16a23efc9cf6bc201a62d"
version: "262a07c31712af627664a100897519fccc1f1eadcd744f902e710f31f1fb2d30"
build_date: "2021-04-08T14:32:25.156Z"
size_mb: 85.00390625
size: 89133056
sif: "https://datasets.datalad.org/shub/heathsc/gemBS-rs/latest/2021-04-08-29b0dc49-262a07c3/262a07c31712af627664a100897519fccc1f1eadcd744f902e710f31f1fb2d30.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/heathsc/gemBS-rs/latest/2021-04-08-29b0dc49-262a07c3/
recipe: https://datasets.datalad.org/shub/heathsc/gemBS-rs/latest/2021-04-08-29b0dc49-262a07c3/Singularity
collection: heathsc/gemBS-rs
---

# heathsc/gemBS-rs:latest

```bash
$ singularity pull shub://heathsc/gemBS-rs:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial
Stage: build

%post
    apt-get update
    apt-get install -y build-essential git autoconf wget lbzip2 pkg-config cmake
    apt-get install -y zlib1g-dev libbz2-dev libexpat1-dev
    apt-get install -y libncurses5-dev liblzma-dev libssl-dev libcurl4-openssl-dev curl
    apt-get install -y libfreetype6-dev libfontconfig1-dev
    curl https://sh.rustup.rs -sSf > rust.sh && sh rust.sh -y
    mkdir -p /usr/local/build; cd /usr/local/build
    git clone --recursive https://github.com/heathsc/gemBS-rs.git
    (cd gemBS-rs; PATH=$PATH:/root/.cargo/bin GEMBS_CONTAINER=1 make install)
    echo /usr/local/lib/gemBS/lib > /etc/ld.so.conf.d/gemBS.conf && ldconfig

BootStrap: docker
From: ubuntu:xenial

%files from build
    /usr/local/lib/gemBS

%runscript
    exec gemBS $@

%environment
    export PATH=/usr/local/lib/gemBS/bin:/usr/local/lib/gemBS/texlive/bin/x86_64-linux:$PATH

%help
    gemBS singularity container
 
%post
    apt-get update
    (mkdir /ext && cd /ext && mkdir disk1 disk2 disk3 disk4 disk5 disk6 disk7 disk8 disk9)
    apt-get install -y lbzip2 zlib1g libexpat1
    apt-get install -y libncurses5 liblzma5 libssl1.0.0 libcurl3
    apt-get install -y libfreetype6 libfontconfig1 perl-modules-5.22
    echo /usr/local/lib/gemBS/lib > /etc/ld.so.conf.d/gemBS.conf && ldconfig
```

## Collection

 - Name: [heathsc/gemBS-rs](https://github.com/heathsc/gemBS-rs)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

