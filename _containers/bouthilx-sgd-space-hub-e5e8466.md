---
id: 5076
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "e5e8466"
commit: "7fdc1872db32067933f0361b0cb560a427ed3373"
version: "f8a9bb549ee2fc8c1257ebfdd9d14783"
build_date: "2018-10-02T03:38:11.485Z"
size_mb: 1932
size: 862294047
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e5e8466/2018-10-02-7fdc1872-f8a9bb54/f8a9bb549ee2fc8c1257ebfdd9d14783.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e5e8466/2018-10-02-7fdc1872-f8a9bb54/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e5e8466/2018-10-02-7fdc1872-f8a9bb54/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:e5e8466

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:e5e8466
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
        git reset --hard e5e8466

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

