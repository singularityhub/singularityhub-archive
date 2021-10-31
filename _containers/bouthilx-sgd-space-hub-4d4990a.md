---
id: 5297
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "4d4990a"
commit: "97cf5a3aa6c8d71bd58e6b691e3240cfa553ecaf"
version: "0f150fc47f2ddb4f076a9ff7af603550"
build_date: "2018-10-22T21:27:18.806Z"
size_mb: 1932
size: 862318623
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4d4990a/2018-10-22-97cf5a3a-0f150fc4/0f150fc47f2ddb4f076a9ff7af603550.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4d4990a/2018-10-22-97cf5a3a-0f150fc4/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4d4990a/2018-10-22-97cf5a3a-0f150fc4/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:4d4990a

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:4d4990a
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
        git reset --hard 4d4990a

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

