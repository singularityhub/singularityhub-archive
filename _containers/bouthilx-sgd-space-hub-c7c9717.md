---
id: 5051
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "c7c9717"
commit: "3950d31f4b06ca143237ec46723b8bcf07d949f2"
version: "4b2467058b986ad0312f5042d53c9924"
build_date: "2018-10-01T08:41:33.965Z"
size_mb: 1932
size: 862253087
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/c7c9717/2018-10-01-3950d31f-4b246705/4b2467058b986ad0312f5042d53c9924.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/c7c9717/2018-10-01-3950d31f-4b246705/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/c7c9717/2018-10-01-3950d31f-4b246705/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:c7c9717

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:c7c9717
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
        git reset --hard c7c9717

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

