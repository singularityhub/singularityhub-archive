---
id: 7629
name: "tikk3r/lofar-h5plot"
branch: "master"
tag: "latest"
commit: "77b91efe94a4174e0f137a0c36e657dfd8ef8b5a"
version: "c3590fafcad697c1a4910572c801ea40c7bcdf25c4ab9ce094a56ebd09ddfd65"
build_date: "2021-03-09T11:37:28.627Z"
size_mb: 528.6953125
size: 554377216
sif: "https://datasets.datalad.org/shub/tikk3r/lofar-h5plot/latest/2021-03-09-77b91efe-c3590faf/c3590fafcad697c1a4910572c801ea40c7bcdf25c4ab9ce094a56ebd09ddfd65.sif"
url: https://datasets.datalad.org/shub/tikk3r/lofar-h5plot/latest/2021-03-09-77b91efe-c3590faf/
recipe: https://datasets.datalad.org/shub/tikk3r/lofar-h5plot/latest/2021-03-09-77b91efe-c3590faf/Singularity
collection: tikk3r/lofar-h5plot
---

# tikk3r/lofar-h5plot:latest

```bash
$ singularity pull shub://tikk3r/lofar-h5plot:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
    export INSTALLDIR=/opt/h5plot
    export PATH=$INSTALLDIR:$PATH

%post
    export INSTALLDIR=/opt/h5plot
    mkdir -p $INSTALLDIR && cd $INSTALLDIR

    apt-get update
    apt-get install -y git python3-pip
    apt-get install -y libgl1-mesa-glx qt5-default

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade https://github.com/revoltek/losoto/archive/master.zip
    python3 -m pip install lofar-h5plot

%runscript
    export INSTALLDIR=/opt/h5plot
    export PATH=$INSTALLDIR:$PATH
    alias python='python3'
    h5plot "$@"

%help
    This Singularity image contains lofar-h5plot (https://github.com/tikk3r/lofar-h5plot).
```

## Collection

 - Name: [tikk3r/lofar-h5plot](https://github.com/tikk3r/lofar-h5plot)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

