---
id: 5305
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "eaf7075"
commit: "75c9354b87cc1fcc7df2e9211d1d62f45cd49316"
version: "463015a3b3ab0ad0e935d556d810bb34"
build_date: "2018-10-22T21:27:18.766Z"
size_mb: 1932
size: 862330911
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/eaf7075/2018-10-22-75c9354b-463015a3/463015a3b3ab0ad0e935d556d810bb34.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/eaf7075/2018-10-22-75c9354b-463015a3/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/eaf7075/2018-10-22-75c9354b-463015a3/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:eaf7075

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:eaf7075
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
        git reset --hard eaf7075

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

