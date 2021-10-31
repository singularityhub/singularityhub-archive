---
id: 8962
name: "bouthilx/hpop-hub"
branch: "master"
tag: "75dd126"
commit: "ecc8aa894eb29994225f531375875dbce1e3d68d"
version: "a13f94f9ec53b81a67d99f75141181c5"
build_date: "2019-05-09T08:14:52.581Z"
size_mb: 2748
size: 1752088607
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/75dd126/2019-05-09-ecc8aa89-a13f94f9/a13f94f9ec53b81a67d99f75141181c5.simg"
url: https://datasets.datalad.org/shub/bouthilx/hpop-hub/75dd126/2019-05-09-ecc8aa89-a13f94f9/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/75dd126/2019-05-09-ecc8aa89-a13f94f9/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:75dd126

```bash
$ singularity pull shub://bouthilx/hpop-hub:75dd126
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
            git reset --hard 75dd126

        cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install --process-dependency-links -e repro[coco,mini]

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

