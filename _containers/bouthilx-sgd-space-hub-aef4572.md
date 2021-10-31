---
id: 5125
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "aef4572"
commit: "20003a57373c8587abb64d15c8ec073069703e30"
version: "dde57273d3ec757ceb8c5a6370c75c17"
build_date: "2018-10-04T05:19:39.716Z"
size_mb: 1932
size: 862298143
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/aef4572/2018-10-04-20003a57-dde57273/dde57273d3ec757ceb8c5a6370c75c17.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/aef4572/2018-10-04-20003a57-dde57273/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/aef4572/2018-10-04-20003a57-dde57273/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:aef4572

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:aef4572
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.0.4.0

%labels
    AUTHOR xavier.bouthillier@umontreal.ca

% environment
    SGD_SPACE_DATA_PATH=/data

%post
    echo "------------------------------------------------------"
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev
        git reset --hard aef4572

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install --process-dependency-links -e sgd-space[execute,configure,deploy]

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/sgd-space-hub](https://github.com/bouthilx/sgd-space-hub)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

