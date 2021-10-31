---
id: 5304
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "06b787f"
commit: "a96478a6d845fe0825f464f6a018967070541bdb"
version: "66b33ef125a85e674623ad6533c0ea8e"
build_date: "2018-10-22T21:27:18.773Z"
size_mb: 1932
size: 862330911
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/06b787f/2018-10-22-a96478a6-66b33ef1/66b33ef125a85e674623ad6533c0ea8e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/06b787f/2018-10-22-a96478a6-66b33ef1/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/06b787f/2018-10-22-a96478a6-66b33ef1/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:06b787f

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:06b787f
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
        git reset --hard 06b787f

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

