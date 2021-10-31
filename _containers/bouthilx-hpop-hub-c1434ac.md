---
id: 8886
name: "bouthilx/hpop-hub"
branch: "master"
tag: "c1434ac"
commit: "72ab9bb4f4893771c1738efbfde793c64e9d60e5"
version: "4e57a2e82ef093ce49b42548f3ccf87c"
build_date: "2019-05-07T14:45:54.298Z"
size_mb: 2723
size: 1742999583
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/c1434ac/2019-05-07-72ab9bb4-4e57a2e8/4e57a2e82ef093ce49b42548f3ccf87c.simg"
url: https://datasets.datalad.org/shub/bouthilx/hpop-hub/c1434ac/2019-05-07-72ab9bb4-4e57a2e8/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/c1434ac/2019-05-07-72ab9bb4-4e57a2e8/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:c1434ac

```bash
$ singularity pull shub://bouthilx/hpop-hub:c1434ac
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.1.0.0

%labels
    AUTHOR xavier.bouthillier@umontreal.ca

% environment
    REPRO_DATA_PATH=/data

%post
    echo "------------------------------------------------------"
    echo "Updating setuptools"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'

    echo "------------------------------------------------------"
    echo "Installing coco"
    echo "------------------------------------------------------"
    pip3 install numpy scipy
    cd /repos
      git clone https://github.com/numbbo/coco.git
      cd coco
          python3.6 do.py run-python
      cd ..

    echo "------------------------------------------------------"
    echo "Installing mahler"
    echo "------------------------------------------------------"
    pip3 install --upgrade git+https://github.com/bouthilx/mahler.git
    pip3 install --upgrade git+https://github.com/bouthilx/mahler.registry.mongodb.git

    echo "------------------------------------------------------"
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
        git clone https://gitlab.com/bouthilx/repro.git
        cd repro
            git fetch
            git checkout --track origin/dev
            git reset --hard c1434ac

        cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install --process-dependency-links -e repro[coco]

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/hpop-hub](https://github.com/bouthilx/hpop-hub)
 - License: None

