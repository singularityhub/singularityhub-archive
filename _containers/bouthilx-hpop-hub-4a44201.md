---
id: 8928
name: "bouthilx/hpop-hub"
branch: "master"
tag: "4a44201"
commit: "5581f54d0d48005d7b9393e529510ab51a897694"
version: "36217e994de7aa6b40cca84dbbe279af"
build_date: "2019-05-08T15:10:10.705Z"
size_mb: 2766
size: 1763622943
sif: "https://datasets.datalad.org/shub/bouthilx/hpop-hub/4a44201/2019-05-08-5581f54d-36217e99/36217e994de7aa6b40cca84dbbe279af.simg"
url: https://datasets.datalad.org/shub/bouthilx/hpop-hub/4a44201/2019-05-08-5581f54d-36217e99/
recipe: https://datasets.datalad.org/shub/bouthilx/hpop-hub/4a44201/2019-05-08-5581f54d-36217e99/Singularity
collection: bouthilx/hpop-hub
---

# bouthilx/hpop-hub:4a44201

```bash
$ singularity pull shub://bouthilx/hpop-hub:4a44201
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
            git reset --hard 4a44201

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

