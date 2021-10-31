---
id: 2844
name: "mih/ohbm2018-training"
branch: "master"
tag: "fsl"
commit: "470f4df574cdd8c9711e2a9d446d0fca7d85b2ce"
version: "b8a3453e757c6c4a00f753cdc137aeb5"
build_date: "2021-01-29T08:26:01.839Z"
size_mb: 647
size: 273047583
sif: "https://datasets.datalad.org/shub/mih/ohbm2018-training/fsl/2021-01-29-470f4df5-b8a3453e/b8a3453e757c6c4a00f753cdc137aeb5.simg"
url: https://datasets.datalad.org/shub/mih/ohbm2018-training/fsl/2021-01-29-470f4df5-b8a3453e/
recipe: https://datasets.datalad.org/shub/mih/ohbm2018-training/fsl/2021-01-29-470f4df5-b8a3453e/Singularity
collection: mih/ohbm2018-training
---

# mih/ohbm2018-training:fsl

```bash
$ singularity pull shub://mih/ohbm2018-training:fsl
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:neurodebian:non-free

%post
    echo "Configuring the environment"
    apt-get -y update

    # setup the container sources themselves
    apt-get -y install eatmydata
    # proper locale setup for UTF8
    eatmydata apt-get -y install locales
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen

    # the least possible bit of FSL
    eatmydata apt-get -y install --no-install-recommends fsl-5.0-core fsl-mni152-templates

    # and some dependencies that it doesnt declare...shame!
    eatmydata apt-get -y install --no-install-recommends file

    # clean up
    apt-get clean

    # inject FSL setup
    ln -fs /etc/fsl/5.0/fsl.sh /.singularity.d/env/99-fsl.sh
```

## Collection

 - Name: [mih/ohbm2018-training](https://github.com/mih/ohbm2018-training)
 - License: None

