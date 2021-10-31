---
id: 1066
name: "brevans/agalma"
branch: "master"
tag: "1.0.1"
commit: "819218857c1e9cbbd39255b2481bfe539e9c9b10"
version: "ac31905477318d18e3f27f80ef7d551b"
build_date: "2017-12-08T10:41:24.290Z"
size_mb: 4546
size: 1422196767
sif: "https://datasets.datalad.org/shub/brevans/agalma/1.0.1/2017-12-08-81921885-ac319054/ac31905477318d18e3f27f80ef7d551b.simg"
url: https://datasets.datalad.org/shub/brevans/agalma/1.0.1/2017-12-08-81921885-ac319054/
recipe: https://datasets.datalad.org/shub/brevans/agalma/1.0.1/2017-12-08-81921885-ac319054/Singularity
collection: brevans/agalma
---

# brevans/agalma:1.0.1

```bash
$ singularity pull shub://brevans/agalma:1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%labels
    Name agalma
    Maintainer "Benjamin Evans" <b.evans@yale.edu>
    Version 1.0.1
    Architecture x86_64
    URL https://bitbucket.org/caseywdunn/agalma

%post
    MINICONDA=Miniconda2-latest-Linux-x86_64.sh
    PREFIX=/opt/agalma
    AGALMABIN=$PREFIX/bin
    AGALMAVERSION=1.0.1

    cd /tmp

    # yum updates and prereqs
    yum update -y
    yum install -y gzip bzip2 wget which tar

    # install miniconda
    wget https://repo.continuum.io/miniconda/$MINICONDA
    bash $MINICONDA -b -p $PREFIX
    PATH=$AGALMABIN:$PATH

    # install agalma
    conda install -yc dunnlab agalma=$AGALMAVERSION

    # cleanup
    yum autoremove -y
    yum clean all
    conda clean -ay
    rm $MINICONDA
    
    # simple test
    agalma -h

%environment
    # add agalma environment variables to singularity runtime environment
    export AGALMABIN=/opt/agalma/bin
    export PATH=$AGALMABIN:$PATH

%runscript
    exec agalma "$@"
```

## Collection

 - Name: [brevans/agalma](https://github.com/brevans/agalma)
 - License: [MIT License](https://api.github.com/licenses/mit)

