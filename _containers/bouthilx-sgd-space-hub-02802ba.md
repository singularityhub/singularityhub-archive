---
id: 5219
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "02802ba"
commit: "5267ef0bf6f69fe1c7eb5be6abe41853f116b0b6"
version: "467f2883725826fac84ffeadb5ab3037"
build_date: "2018-10-13T22:17:37.517Z"
size_mb: 1932
size: 862314527
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/02802ba/2018-10-13-5267ef0b-467f2883/467f2883725826fac84ffeadb5ab3037.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/02802ba/2018-10-13-5267ef0b-467f2883/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/02802ba/2018-10-13-5267ef0b-467f2883/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:02802ba

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:02802ba
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
        git reset --hard 02802ba

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

