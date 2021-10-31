---
id: 2137
name: "psychoinformatics-de/datalad"
branch: "master"
tag: "fullmaster"
commit: "932ca626eb83d6cafaef5677af8745922b45cf54"
version: "bf289894568a8336b8dc63849ee993f7"
build_date: "2018-03-17T11:48:03.403Z"
size_mb: 984
size: 321470495
sif: "https://datasets.datalad.org/shub/psychoinformatics-de/datalad/fullmaster/2018-03-17-932ca626-bf289894/bf289894568a8336b8dc63849ee993f7.simg"
url: https://datasets.datalad.org/shub/psychoinformatics-de/datalad/fullmaster/2018-03-17-932ca626-bf289894/
recipe: https://datasets.datalad.org/shub/psychoinformatics-de/datalad/fullmaster/2018-03-17-932ca626-bf289894/Singularity
collection: psychoinformatics-de/datalad
---

# psychoinformatics-de/datalad:fullmaster

```bash
$ singularity pull shub://psychoinformatics-de/datalad:fullmaster
```

## Singularity Recipe

```singularity
#
# This container provides a full Python3-based installation of DataLad
# (http://datalad.org) using DataLad's latest development state at the
# time the container is built.
#

Bootstrap:docker
From:neurodebian:latest

%post
    echo "Configuring the environment"
    apt-get -y update

    # setup the container sources themselves
    apt-get -y install eatmydata
    eatmydata apt-get -y install gnupg wget locales

    # we need a UTF locale for DataLad to work properly
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen

    # bare essentials to pull everything else in
    eatmydata apt-get -y install --no-install-recommends git git-annex-standalone python3-pip

    eatmydata apt-get -y install --no-install-recommends python3-setuptools python3-wheel less rsync git-remote-gcrypt aria2 libexempi3

    # just for scrapy
    eatmydata apt-get -y install --no-install-recommends python3-twisted

    # little dance because pip cannot handle this url plus [full] in one go
    wget https://github.com/datalad/datalad/archive/master.zip
    pip3 install --system master.zip[full]
    rm -f master.zip

    # clean up
    apt-get clean


%environments
    unset PYTHONPATH

%runscript
    datalad "$@"
```

## Collection

 - Name: [psychoinformatics-de/datalad](https://github.com/psychoinformatics-de/datalad)
 - License: None

