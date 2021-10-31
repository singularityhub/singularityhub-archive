---
id: 5434
name: "datalad/datalad-htcondor"
branch: "master"
tag: "latest"
commit: "ba55265e5813d992421358c11e87945a531e2c97"
version: "8ff8961e04fb8f562c695a25d8cb4ebe"
build_date: "2018-11-16T10:50:08.072Z"
size_mb: 596
size: 214872095
sif: "https://datasets.datalad.org/shub/datalad/datalad-htcondor/latest/2018-11-16-ba55265e-8ff8961e/8ff8961e04fb8f562c695a25d8cb4ebe.simg"
url: https://datasets.datalad.org/shub/datalad/datalad-htcondor/latest/2018-11-16-ba55265e-8ff8961e/
recipe: https://datasets.datalad.org/shub/datalad/datalad-htcondor/latest/2018-11-16-ba55265e-8ff8961e/Singularity
collection: datalad/datalad-htcondor
---

# datalad/datalad-htcondor:latest

```bash
$ singularity pull shub://datalad/datalad-htcondor:latest
```

## Singularity Recipe

```singularity
#
# This container provides a Python3-based DataLad (http://datalad.org)
# installation for use in the pre- and post-flight stages of remote
# job execution.
#
# Changelog
# ---------
# 0.1
#  - Pre-release
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
    # netbase is needed to have meaningful protocoll definitions
    eatmydata apt-get -y install --no-install-recommends git git-annex-standalone python3-pip netbase

    eatmydata apt-get -y install --no-install-recommends python3-setuptools python3-wheel less rsync git-remote-gcrypt aria2

    # we are using revolution as the entry point
    pip3 install datalad-revolution

    # clean up
    apt-get clean


%environments
    # keep the host environment out, to some degree
    unset PYTHONPATH

%runscript
    datalad "$@"
```

## Collection

 - Name: [datalad/datalad-htcondor](https://github.com/datalad/datalad-htcondor)
 - License: [Other](None)

