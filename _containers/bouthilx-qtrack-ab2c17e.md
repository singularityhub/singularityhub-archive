---
id: 2546
name: "bouthilx/qtrack"
branch: "master"
tag: "ab2c17e"
commit: "bc8e8d9fd76ca061346e37ca18a3b65ca770fdac"
version: "7fa360a2cf5a9b3fb6e74b04d1859092"
build_date: "2018-04-16T12:51:45.090Z"
size_mb: 2216
size: 1013145631
sif: "https://datasets.datalad.org/shub/bouthilx/qtrack/ab2c17e/2018-04-16-bc8e8d9f-7fa360a2/7fa360a2cf5a9b3fb6e74b04d1859092.simg"
url: https://datasets.datalad.org/shub/bouthilx/qtrack/ab2c17e/2018-04-16-bc8e8d9f-7fa360a2/
recipe: https://datasets.datalad.org/shub/bouthilx/qtrack/ab2c17e/2018-04-16-bc8e8d9f-7fa360a2/Singularity
collection: bouthilx/qtrack
---

# bouthilx/qtrack:ab2c17e

```bash
$ singularity pull shub://bouthilx/qtrack:ab2c17e
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.0.3.1

%labels
   AUTHOR xavier.bouthillier@umontreal.ca

%post
	export GITHUB_TOKEN="e209b24443c2fefa895c81d80957b838df6c68d7"

    echo "------------------------------------------------------"
    echo "Installing Tensorflow for tensor-board"
    echo "------------------------------------------------------"
	pip3 install tensorflow==1.5

    echo "------------------------------------------------------"
    echo "Installing custom Sacred"
    echo "------------------------------------------------------"
    cd /repos
	git clone https://${GITHUB_TOKEN}@github.com/bouthilx/impn.git qtrack
    cd qtrack
        git fetch
        git checkout --track origin/qtrack
        git reset --hard ab2c17e
        git submodule init
        git submodule update
        cd protopt
            git submodule init
            git submodule update
        cd ..

        pip3 install protopt/sacred

        echo "------------------------------------------------------"
        echo "Installing custom SmartDispatch"
        echo "------------------------------------------------------"

        pip3 install protopt/smartdispatch

    cd ..

    echo "------------------------------------------------------"
    echo "Installing Protopt"
    echo "------------------------------------------------------"
    pip3 install qtrack/protopt

    echo "------------------------------------------------------"
    echo "Installing IMPN"
    echo "------------------------------------------------------"
    pip3 install qtrack/

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/qtrack](https://github.com/bouthilx/qtrack)
 - License: None

