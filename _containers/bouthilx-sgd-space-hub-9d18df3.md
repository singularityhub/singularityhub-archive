---
id: 5124
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "9d18df3"
commit: "4e0962a1eb11a1e79eaec61121a784c0cec55fb8"
version: "4bfd88153ab7ae5ead6950a55bd98a84"
build_date: "2018-10-04T05:19:39.722Z"
size_mb: 1932
size: 862298143
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9d18df3/2018-10-04-4e0962a1-4bfd8815/4bfd88153ab7ae5ead6950a55bd98a84.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9d18df3/2018-10-04-4e0962a1-4bfd8815/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9d18df3/2018-10-04-4e0962a1-4bfd8815/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:9d18df3

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:9d18df3
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
        git reset --hard 9d18df3

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

