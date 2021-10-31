---
id: 7277
name: "ebothmann/sherpa-singularity"
branch: "master"
tag: "rivet-mkhtml"
commit: "d7b607ab12cbb9874dce513ee5b1b80254c766f1"
version: "49037cb9f085bc1eb2bfd330fd8551a1"
build_date: "2019-02-17T21:45:27.125Z"
size_mb: 1418
size: 480739359
sif: "https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/rivet-mkhtml/2019-02-17-d7b607ab-49037cb9/49037cb9f085bc1eb2bfd330fd8551a1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ebothmann/sherpa-singularity/rivet-mkhtml/2019-02-17-d7b607ab-49037cb9/
recipe: https://datasets.datalad.org/shub/ebothmann/sherpa-singularity/rivet-mkhtml/2019-02-17-d7b607ab-49037cb9/Singularity
collection: ebothmann/sherpa-singularity
---

# ebothmann/sherpa-singularity:rivet-mkhtml

```bash
$ singularity pull shub://ebothmann/sherpa-singularity:rivet-mkhtml
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ebothmann/sherpa-singularity


%help
A Singularity file to define an image for running Sherpa 2.2.6 including
support for FastJet, HepMC2, LHAPDF and Rivet. For the latter, also the
rivet-mkhtml tool is supported by including a texlive installation.


%labels
    Maintainer Enrico Bothmann
    Version v0.1


%post
    echo Installing yum dependencies ...

    yum -y install \
        ghostscript \
        ImageMagick \
        texlive \
	texlive-latex \
        which

    ldconfig
    yum clean all
```

## Collection

 - Name: [ebothmann/sherpa-singularity](https://github.com/ebothmann/sherpa-singularity)
 - License: None

