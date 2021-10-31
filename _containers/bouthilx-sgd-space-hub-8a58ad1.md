---
id: 5048
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "8a58ad1"
commit: "2758ba86a09deb7aa192e180729fc4445cec3d72"
version: "eb798b39e8a13237983adda60b8a1282"
build_date: "2018-09-30T22:17:17.753Z"
size_mb: 1932
size: 862253087
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8a58ad1/2018-09-30-2758ba86-eb798b39/eb798b39e8a13237983adda60b8a1282.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8a58ad1/2018-09-30-2758ba86-eb798b39/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8a58ad1/2018-09-30-2758ba86-eb798b39/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:8a58ad1

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:8a58ad1
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
        git reset --hard 8a58ad1

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

