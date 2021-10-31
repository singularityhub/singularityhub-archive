---
id: 5119
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "e537456"
commit: "85815086ee65e84c18b0ee6fb17adc70bb368dfb"
version: "e260a06f46f98df14a2bf2595ae94edd"
build_date: "2018-10-04T05:19:39.736Z"
size_mb: 1932
size: 862294047
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e537456/2018-10-04-85815086-e260a06f/e260a06f46f98df14a2bf2595ae94edd.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e537456/2018-10-04-85815086-e260a06f/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e537456/2018-10-04-85815086-e260a06f/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:e537456

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:e537456
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
        git reset --hard e537456

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

