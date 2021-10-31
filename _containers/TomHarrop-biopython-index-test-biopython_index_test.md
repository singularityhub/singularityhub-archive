---
id: 8960
name: "TomHarrop/biopython-index-test"
branch: "master"
tag: "biopython_index_test"
commit: "5acb1779464fc8b28ae21be246eb57671736876e"
version: "51463e59141983d6a8aa871bba15c973"
build_date: "2019-05-09T08:14:52.685Z"
size_mb: 1966
size: 615325727
sif: "https://datasets.datalad.org/shub/TomHarrop/biopython-index-test/biopython_index_test/2019-05-09-5acb1779-51463e59/51463e59141983d6a8aa871bba15c973.simg"
url: https://datasets.datalad.org/shub/TomHarrop/biopython-index-test/biopython_index_test/2019-05-09-5acb1779-51463e59/
recipe: https://datasets.datalad.org/shub/TomHarrop/biopython-index-test/biopython_index_test/2019-05-09-5acb1779-51463e59/Singularity
collection: TomHarrop/biopython-index-test
---

# TomHarrop/biopython-index-test:biopython_index_test

```bash
$ singularity pull shub://TomHarrop/biopython-index-test:biopython_index_test
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/singularity-containers:biopython_1.73

%runscript
    python3 /index_reads.py

%setup
    mydir=$(mktemp -d)
    cd "${mydir}" || exit 1
    git clone https://github.com/TomHarrop/biopython-index-test.git
    cd biopython-index-test || exit 1
    rm r1.fq.gz
    wget -O r1.fq.gz \
        --no-check-certificate \
        https://github.com/TomHarrop/biopython-index-test/raw/master/r1.fq.gz
    gunzip r1.fq.gz
    cp r1.fq ${SINGULARITY_ROOTFS}/r1.fq
    cp index_reads.py ${SINGULARITY_ROOTFS}/index_reads.py
    cd .. || exit 1
    cd .. || exit 1
    rm -rf "${mydir}"
```

## Collection

 - Name: [TomHarrop/biopython-index-test](https://github.com/TomHarrop/biopython-index-test)
 - License: None

