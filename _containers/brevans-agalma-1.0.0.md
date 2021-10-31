---
id: 1065
name: "brevans/agalma"
branch: "master"
tag: "1.0.0"
commit: "819218857c1e9cbbd39255b2481bfe539e9c9b10"
version: "41ca3dcb7007fefbdc0097ec846ab41d"
build_date: "2017-12-08T10:41:24.298Z"
size_mb: 4546
size: 1422200863
sif: "https://datasets.datalad.org/shub/brevans/agalma/1.0.0/2017-12-08-81921885-41ca3dcb/41ca3dcb7007fefbdc0097ec846ab41d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/brevans/agalma/1.0.0/2017-12-08-81921885-41ca3dcb/
recipe: https://datasets.datalad.org/shub/brevans/agalma/1.0.0/2017-12-08-81921885-41ca3dcb/Singularity
collection: brevans/agalma
---

# brevans/agalma:1.0.0

```bash
$ singularity pull shub://brevans/agalma:1.0.0
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
    Version 1.0.0
    Architecture x86_64
    URL https://bitbucket.org/caseywdunn/agalma

%post
    MINICONDA=Miniconda2-latest-Linux-x86_64.sh
    PREFIX=/opt/agalma
    AGALMABIN=$PREFIX/bin
    AGALMAVERSION=1.0.0

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

