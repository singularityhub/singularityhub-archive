---
id: 5840
name: "datalad/datalad"
branch: "master"
tag: "0.11.1"
commit: "c937353c79e6d399dee042480677412183adc77d"
version: "6fde03cabb3addac99fbe3764ed08322"
build_date: "2020-06-13T03:52:48.505Z"
size_mb: 651
size: 217698335
sif: "https://datasets.datalad.org/shub/datalad/datalad/0.11.1/2020-06-13-c937353c-6fde03ca/6fde03cabb3addac99fbe3764ed08322.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/datalad/datalad/0.11.1/2020-06-13-c937353c-6fde03ca/
recipe: https://datasets.datalad.org/shub/datalad/datalad/0.11.1/2020-06-13-c937353c-6fde03ca/Singularity
collection: datalad/datalad
---

# datalad/datalad:0.11.1

```bash
$ singularity pull shub://datalad/datalad:0.11.1
```

## Singularity Recipe

```singularity
#
# This container provides a full Python3-based installation of DataLad
# (http://datalad.org) using DataLad's latest development state at the
# time the container is built.
#
# Changelog
# ---------
# 0.11.1
#  - Update to get a fresh build, also with fixed up git-annex.
#    Starting from this build, we would freeze APT repos, to make
#    build reproducible.  The state of APT repos might be after the release
#    to absorb fixes in other packages such as git-annex-standalone.
# 0.10.2
#  - Update after initial "burn-in" time for 0.10 series
# 0.10.rc5
#  - Pre-release
#
#######################################################################


Bootstrap:docker
From:neurodebian:latest

%post
    nd_freeze 20181209
    echo "Configuring the environment"
    apt-get -y update

    # setup the container sources themselves
    apt-get -y install eatmydata
    eatmydata apt-get -y install gnupg wget locales

    # we need a UTF locale for DataLad to work properly
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen

    # bare essentials to pull everything else in
    eatmydata apt-get -y install --no-install-recommends git git-annex-standalone python3-pip datalad python-datalad python3-datalad

    eatmydata apt-get -y install --no-install-recommends python3-setuptools python3-wheel less rsync git-remote-gcrypt aria2 libexempi3

    # just for scrapy
    eatmydata apt-get -y install --no-install-recommends python3-twisted


    # clean up
    apt-get clean


%environments
    unset PYTHONPATH

%runscript
    datalad "$@"
```

## Collection

 - Name: [datalad/datalad](https://github.com/datalad/datalad)
 - License: [Other](None)

