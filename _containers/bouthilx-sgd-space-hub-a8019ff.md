---
id: 5301
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "a8019ff"
commit: "645936fe7def0d84d423e10771228512e2b15629"
version: "50614547188090706685100841f2289e"
build_date: "2018-10-22T21:27:18.792Z"
size_mb: 1932
size: 862326815
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a8019ff/2018-10-22-645936fe-50614547/50614547188090706685100841f2289e.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a8019ff/2018-10-22-645936fe-50614547/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a8019ff/2018-10-22-645936fe-50614547/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:a8019ff

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:a8019ff
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
        git reset --hard a8019ff

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

