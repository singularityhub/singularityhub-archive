---
id: 2681
name: "datalad/datalad-neuroimaging"
branch: "master"
tag: "latest"
commit: "88746668d971646b7deae17ff8556080a7107fa4"
version: "9ab8575268426a9aeaf67b9c6cb5566d"
build_date: "2020-05-13T16:56:00.781Z"
size_mb: 1295
size: 453541919
sif: "https://datasets.datalad.org/shub/datalad/datalad-neuroimaging/latest/2020-05-13-88746668-9ab85752/9ab8575268426a9aeaf67b9c6cb5566d.simg"
url: https://datasets.datalad.org/shub/datalad/datalad-neuroimaging/latest/2020-05-13-88746668-9ab85752/
recipe: https://datasets.datalad.org/shub/datalad/datalad-neuroimaging/latest/2020-05-13-88746668-9ab85752/Singularity
collection: datalad/datalad-neuroimaging
---

# datalad/datalad-neuroimaging:latest

```bash
$ singularity pull shub://datalad/datalad-neuroimaging:latest
```

## Singularity Recipe

```singularity
#
# This container provides a full Python3-based installation of DataLad
# for neuroimaging (http://datalad.org) using the latest stable release
# at the time the container is built.
#
# Copyright (c) 2018, Michael Hanke. MIT license
#
# Changelog
# ---------
# 0.1.2
#  - Test suite runs in container
#
# 0.1
#  - First official release of the DataLad extension for neuroimaging
#
#######################################################################

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

    eatmydata apt-get -y install --no-install-recommends python3-setuptools python3-wheel less rsync git-remote-gcrypt aria2 libexempi3 python3-libxmp

    # just for scrapy
    eatmydata apt-get -y install --no-install-recommends python3-twisted

    pip3 install --system datalad_neuroimaging

    # clean up
    apt-get clean


%environments
    unset PYTHONPATH

%runscript
    datalad "$@"

%help
    This is DataLad for Neuroimaging. Run with --help for more info.

%test
    datalad test datalad_neuroimaging
```

## Collection

 - Name: [datalad/datalad-neuroimaging](https://github.com/datalad/datalad-neuroimaging)
 - License: [Other](None)

