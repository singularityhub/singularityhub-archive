---
id: 4868
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "62351cf"
commit: "bbdac895ec8e541739bdda6fee28fbfe72723136"
version: "2306e41dd96e918ab0b5a35fdfda05e4"
build_date: "2018-09-18T06:26:29.903Z"
size_mb: 1857
size: 830668831
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/62351cf/2018-09-18-bbdac895-2306e41d/2306e41dd96e918ab0b5a35fdfda05e4.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/62351cf/2018-09-18-bbdac895-2306e41d/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/62351cf/2018-09-18-bbdac895-2306e41d/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:62351cf

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:62351cf
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
    echo "Installing kleio prototype"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/epistimio/kleio.git@prototype

    echo "------------------------------------------------------"
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev
        git reset --hard 62351cf

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install -e sgd-space

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

