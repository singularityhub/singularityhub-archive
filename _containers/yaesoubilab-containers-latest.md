---
id: 7669
name: "yaesoubilab/containers"
branch: "master"
tag: "latest"
commit: "611ad111d2d98d5ad53d024133dcd8151112e33c"
version: "2223f5a3691f0cd147a4d951676c0e84"
build_date: "2019-04-23T20:55:38.011Z"
size_mb: 1495
size: 481300511
sif: "https://datasets.datalad.org/shub/yaesoubilab/containers/latest/2019-04-23-611ad111-2223f5a3/2223f5a3691f0cd147a4d951676c0e84.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yaesoubilab/containers/latest/2019-04-23-611ad111-2223f5a3/
recipe: https://datasets.datalad.org/shub/yaesoubilab/containers/latest/2019-04-23-611ad111-2223f5a3/Singularity
collection: yaesoubilab/containers
---

# yaesoubilab/containers:latest

```bash
$ singularity pull shub://yaesoubilab/containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%setup
    # mkdir ${SINGULARITY_ROOTFS}/repos
    # mkdir ${SINGULARITY_ROOTFS}/repos/StatisticalDistributionsLib
    # mkdir ${SINGULARITY_ROOTFS}/repos/SimulationLib
    # mkdir ${SINGULARITY_ROOTFS}/repos/TBABM
    mkdir ${SINGULARITY_ROOTFS}/params_bucket

%files

%environment

%post
    apt-get update
    apt-get -y install cmake make git libeigen3-dev libboost-all-dev clang python-pip
    pip install csvkit
    export CC=/usr/bin/clang
    export CXX=/usr/bin/clang++
    git clone https://github.com/yaesoubilab/StatisticalDistributionsLib repos/StatisticalDistributionsLib/
    git clone https://github.com/yaesoubilab/SimulationLib repos/SimulationLib/
    git clone https://github.com/yaesoubilab/TBABM repos/TBABM/
    cd repos/StatisticalDistributionsLib && cmake . && make install && cd ..
    cd SimulationLib/SimulationLib && cmake . && make install && cd ../..
    cd TBABM && git checkout new-tb-initialization && cmake . && make && cd ../..
    NOW=`date`
    echo "export NOW=\"${NOW}\"" >> $SINGULARITY_ENVIRONMENT

# With this post section, it should be possible to simply cp the TBABM
# directory over, go to params/ and run ./updateJSONs.sh, and then run
# the simulation as normal

%runscript
    echo "Container was created $NOW"
    echo "Arguments received: $*"
    # exec cd ${SINGULARITY_ROOTFS}/repos/TBABM/src && ./TBABM "$@"

%startscript
    nc -lp $LISTEN_PORT

%test
    grep -q NAME=\"Ubuntu\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is Ubuntu as expected."
    else
        echo "Container base is not Ubuntu."
    fi

%labels
    Author marcus.russi@yale.edu
    Version v0.0.1
    URL https://github.com/yaesoubilab

%help
    This is a production container used for cluster-based runs of TBABM
```

## Collection

 - Name: [yaesoubilab/containers](https://github.com/yaesoubilab/containers)
 - License: None

