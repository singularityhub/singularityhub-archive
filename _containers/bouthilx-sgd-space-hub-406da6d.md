---
id: 5306
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "406da6d"
commit: "72594da624775dde539c806035bef33cb048ccd1"
version: "b903a87395d34b3250f2fbc8d4ae4784"
build_date: "2018-10-22T21:27:18.759Z"
size_mb: 1932
size: 862335007
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/406da6d/2018-10-22-72594da6-b903a873/b903a87395d34b3250f2fbc8d4ae4784.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/406da6d/2018-10-22-72594da6-b903a873/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/406da6d/2018-10-22-72594da6-b903a873/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:406da6d

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:406da6d
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
        git reset --hard 406da6d

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

