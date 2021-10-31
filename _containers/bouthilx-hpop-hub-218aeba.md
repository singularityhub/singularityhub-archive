---
id: 8927
name: "bouthilx/hpop-hub"
branch: "master"
tag: "218aeba"
commit: "c56381dea513018bf7b8c60582381c5b2d2ad1a5"
version: "866fa5ec8fe65172fde8f2d73d9aba9d"
build_date: "2019-05-08T15:10:10.713Z"
size_mb: 2723
size: 1743126559
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/218aeba/2019-05-08-c56381de-866fa5ec/866fa5ec8fe65172fde8f2d73d9aba9d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/hpop-hub/218aeba/2019-05-08-c56381de-866fa5ec/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/218aeba/2019-05-08-c56381de-866fa5ec/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:218aeba

```bash
$ singularity pull shub://bouthilx/hpop-hub:218aeba
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
            git reset --hard 218aeba

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

