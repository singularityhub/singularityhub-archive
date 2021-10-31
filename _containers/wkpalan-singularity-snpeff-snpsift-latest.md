---
id: 2555
name: "wkpalan/singularity-snpeff-snpsift"
branch: "master"
tag: "latest"
commit: "33dfac70ac1db58bc9d5d1d0cc8cfcd397383526"
version: "1a802485e8cdff1003d347309a7d2ab1"
build_date: "2021-04-09T10:53:10.491Z"
size_mb: 412
size: 183918623
sif: "https://datasets.datalad.org/shub/wkpalan/singularity-snpeff-snpsift/latest/2021-04-09-33dfac70-1a802485/1a802485e8cdff1003d347309a7d2ab1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/wkpalan/singularity-snpeff-snpsift/latest/2021-04-09-33dfac70-1a802485/
recipe: https://datasets.datalad.org/shub/wkpalan/singularity-snpeff-snpsift/latest/2021-04-09-33dfac70-1a802485/Singularity
collection: wkpalan/singularity-snpeff-snpsift
---

# wkpalan/singularity-snpeff-snpsift:latest

```bash
$ singularity pull shub://wkpalan/singularity-snpeff-snpsift:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:latest

%post
/bin/sh build.sh
/bin/sh snpsift.sh

%files
build.sh
snpsift.sh

%environment
SNPEFF_VERSION=v4.3p

%labels
Maintainer	kokulapalan@gmail.com

%test
snpEff -version

# =======================
# SnpSift
# =======================
%appenv SnpSift
    BEST_APP=SnpSift
    export BEST_APP

%apphelp SnpSift
    Please see http://snpeff.sourceforge.net/SnpSift.html for help

%apprun SnpSift
    SnpSift "$@"

# =======================
# snpEff
# =======================
%appenv snpEff
    BEST_APP=snpEff
    export BEST_APP

%apphelp snpEff
    Please see http://snpeff.sourceforge.net/index.html for help

%apprun snpEff
    snpEff "$@"
```

## Collection

 - Name: [wkpalan/singularity-snpeff-snpsift](https://github.com/wkpalan/singularity-snpeff-snpsift)
 - License: [MIT License](https://api.github.com/licenses/mit)

