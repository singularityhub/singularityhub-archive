---
id: 5968
name: "psychoinformatics-de/cbbs-toolbox"
branch: "master"
tag: "fsl"
commit: "8fa2822797f001f1da216855a332d7878c5fa8b7"
version: "4984c01e667b38d206a9a36acf5721be"
build_date: "2018-12-14T10:38:28.275Z"
size_mb: 647
size: 273367071
sif: "https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/fsl/2018-12-14-8fa28227-4984c01e/4984c01e667b38d206a9a36acf5721be.simg"
url: https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/fsl/2018-12-14-8fa28227-4984c01e/
recipe: https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/fsl/2018-12-14-8fa28227-4984c01e/Singularity
collection: psychoinformatics-de/cbbs-toolbox
---

# psychoinformatics-de/cbbs-toolbox:fsl

```bash
$ singularity pull shub://psychoinformatics-de/cbbs-toolbox:fsl
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
    # Note: (ben) Not sure. Taken from github.com/myyoda/ohbm-training/blob/master/section23/environments/Singularity.fsl
    ln -fs /etc/fsl/5.0/fsl.sh /.singularity.d/env/99-fsl.sh
```

## Collection

 - Name: [psychoinformatics-de/cbbs-toolbox](https://github.com/psychoinformatics-de/cbbs-toolbox)
 - License: None

