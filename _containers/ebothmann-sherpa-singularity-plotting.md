---
id: 7314
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "plotting"
commit: "e9c3a47f8a6f796b64ad659417c2b349d498c662"
version: "8c94a3574049904bf231cfcee666b7db"
build_date: "2019-04-03T14:45:49.554Z"
size_mb: 1348
size: 453996575
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/plotting/2019-04-03-e9c3a47f-8c94a357/8c94a3574049904bf231cfcee666b7db.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebothmann/sherpa-singularity/plotting/2019-04-03-e9c3a47f-8c94a357/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/plotting/2019-04-03-e9c3a47f-8c94a357/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:plotting

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:plotting
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity:rivet


%help
A Singularity file to define an image that includes support for the
rivet-mkhtml tool by including a texlive installation.  In addition,
the Compare plotting tool and its dependency ROOT v5.34.36 are
installed in order to plot results from the internal analysis module
of Sherpa.


%labels
    Maintainer Enrico Bothmann
    Version v0.1


%runscript
    rivet-mkhtml "$@"


%environment
    . /opt/root/bin/thisroot.sh


%files
    Compare-1.9_patch
    Compare-logo.gif
    install_Compare


%post
    echo Installing yum dependencies ...
    # install rivet-mkhtml run-time dependencies
    yum -y install \
        ghostscript \
        ImageMagick \
        texlive \
        texlive-latex

    echo Installing ROOT
    mkdir /scratch
    cd /scratch
    wget https://root.cern.ch/download/root_v5.34.36.Linux-centos7-x86_64-gcc4.8.tar.gz -O- | tar xz
    mv root /opt

    echo Installing Compare
    cd /scratch
    chmod +x /install_Compare
    /install_Compare

    echo Clean up
    cd /
    rm -rf /scratch
    ldconfig
    yum clean all
```

## Collection

 - Name: [ebothmann/sherpa-singularity](https://github.com/ebothmann/sherpa-singularity)
 - License: None

