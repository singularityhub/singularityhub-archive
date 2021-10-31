---
id: 5129
name: "psychoinformatics-de/cbbs-toolbox"
branch: "master"
tag: "mridefacer"
commit: "7868b694995464925f0a200f11293d08872ff8c9"
version: "43552f641fd9b518a8c4179a4d816e8e"
build_date: "2018-12-03T17:26:27.744Z"
size_mb: 740
size: 304050207
sif: "https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/mridefacer/2018-12-03-7868b694-43552f64/43552f641fd9b518a8c4179a4d816e8e.simg"
url: https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/mridefacer/2018-12-03-7868b694-43552f64/
recipe: https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/mridefacer/2018-12-03-7868b694-43552f64/Singularity
collection: psychoinformatics-de/cbbs-toolbox
---

# psychoinformatics-de/cbbs-toolbox:mridefacer

```bash
$ singularity pull shub://psychoinformatics-de/cbbs-toolbox:mridefacer
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

    # get needed tools
    eatmydata apt-get -y install git make help2man num-utils
    # clean up
    apt-get clean

    # inject FSL setup
    ln -fs /etc/fsl/5.0/fsl.sh /.singularity.d/env/99-fsl.sh


    # get mridefacer
    git clone https://github.com/mih/mridefacer.git
    make -C mridefacer install
```

## Collection

 - Name: [psychoinformatics-de/cbbs-toolbox](https://github.com/psychoinformatics-de/cbbs-toolbox)
 - License: None

