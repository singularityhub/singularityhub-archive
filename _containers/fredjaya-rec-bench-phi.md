---
id: 9821
name: "fredjaya/rec-bench"
branch: "dev"
tag: "phi"
commit: "88933dd48fe3743c159488ee65f8a6d0f6cf0315"
version: "504008dda59023e7ea5862130357a12d"
build_date: "2019-06-26T22:56:26.350Z"
size_mb: 540
size: 184090655
sif: "https://datasets.datalad.org/shub/fredjaya/rec-bench/phi/2019-06-26-88933dd4-504008dd/504008dda59023e7ea5862130357a12d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/fredjaya/rec-bench/phi/2019-06-26-88933dd4-504008dd/
recipe: https://datasets.datalad.org/shub/fredjaya/rec-bench/phi/2019-06-26-88933dd4-504008dd/Singularity
collection: fredjaya/rec-bench
---

# fredjaya/rec-bench:phi

```bash
$ singularity pull shub://fredjaya/rec-bench:phi
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://fredjaya/rec-bench:base@digest

%post
    # Add phipack
    cd /usr/src
    wget https://www.maths.otago.ac.nz/~dbryant/software/PhiPack.tar.gz
    tar xzf PhiPack.tar.gz
    rm -rf PhiPack.tar.gz
    cd PhiPack/src
    make

%environment
    export PATH=/usr/src/PhiPack/:$PATH
```

## Collection

 - Name: [fredjaya/rec-bench](https://github.com/fredjaya/rec-bench)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

