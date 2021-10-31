---
id: 5077
name: "psychoinformatics-de/cbbs-toolbox"
branch: "master"
tag: "heudiconv"
commit: "4b7f29a6d8862c228f1967f56f6fe3cba546bc76"
version: "a029c642a135cb4aa4141f87da886cab"
build_date: "2018-10-02T17:15:58.777Z"
size_mb: 455
size: 164098079
sif: "https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/heudiconv/2018-10-02-4b7f29a6-a029c642/a029c642a135cb4aa4141f87da886cab.simg"
url: https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/heudiconv/2018-10-02-4b7f29a6-a029c642/
recipe: https://datasets.datalad.org/shub/psychoinformatics-de/cbbs-toolbox/heudiconv/2018-10-02-4b7f29a6-a029c642/Singularity
collection: psychoinformatics-de/cbbs-toolbox
---

# psychoinformatics-de/cbbs-toolbox:heudiconv

```bash
$ singularity pull shub://psychoinformatics-de/cbbs-toolbox:heudiconv
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:neurodebian:latest

%post
    echo "Configuring the environment"
    apt-get -y update

    # setup the container sources themselves
    apt-get -y install eatmydata
    # proper locale setup for UTF8
    eatmydata apt-get -y install locales
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen

    # bare essentials to pull everything else in
    eatmydata apt-get -y install --no-install-recommends python3-pip python3-setuptools python3-wheel wget

    # non-python and a few other bits to avoid having to build everything
    eatmydata apt-get -y install --no-install-recommends dcm2niix python3-numpy python3-six python3-traits python3-scipy pigz

    # little dance to avoid having to install the entire git stack
    # fancified dcmstack version needed
    wget https://github.com/mvdoc/dcmstack/archive/bf/importsys.zip
    pip3 install --system importsys.zip
    rm -f importsys.zip

    wget https://github.com/nipy/heudiconv/archive/master.zip
    pip3 install --system master.zip
    rm -f master.zip

    # clean up
    apt-get clean
```

## Collection

 - Name: [psychoinformatics-de/cbbs-toolbox](https://github.com/psychoinformatics-de/cbbs-toolbox)
 - License: None

