---
id: 2843
name: "mih/ohbm2018-training"
branch: "master"
tag: "heudiconv"
commit: "26e3d45906599405744cc3c53b163bf0318b415f"
version: "7b4fbd4f19d91225dc2aa3b7e3e78bff"
build_date: "2018-05-20T23:46:11.258Z"
size_mb: 457
size: 168771615
sif: "https://datasets.datalad.org/shub/mih/ohbm2018-training/heudiconv/2018-05-20-26e3d459-7b4fbd4f/7b4fbd4f19d91225dc2aa3b7e3e78bff.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mih/ohbm2018-training/heudiconv/2018-05-20-26e3d459-7b4fbd4f/
recipe: https://datasets.datalad.org/shub/mih/ohbm2018-training/heudiconv/2018-05-20-26e3d459-7b4fbd4f/Singularity
collection: mih/ohbm2018-training
---

# mih/ohbm2018-training:heudiconv

```bash
$ singularity pull shub://mih/ohbm2018-training:heudiconv
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

 - Name: [mih/ohbm2018-training](https://github.com/mih/ohbm2018-training)
 - License: None

