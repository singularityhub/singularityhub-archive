---
id: 2620
name: "bouthilx/qtrack"
branch: "master"
tag: "61064c1"
commit: "9bdad0b586cafa7eccb8a2e560e5674d8bebe714"
version: "5772e0db9afb0b27b8dda33406d854a8"
build_date: "2018-04-23T19:13:10.338Z"
size_mb: 2217
size: 1013272607
sif: "https://datasets.datalad.org/shub/bouthilx/qtrack/61064c1/2018-04-23-9bdad0b5-5772e0db/5772e0db9afb0b27b8dda33406d854a8.simg"
url: https://datasets.datalad.org/shub/bouthilx/qtrack/61064c1/2018-04-23-9bdad0b5-5772e0db/
recipe: https://datasets.datalad.org/shub/bouthilx/qtrack/61064c1/2018-04-23-9bdad0b5-5772e0db/Singularity
collection: bouthilx/qtrack
---

# bouthilx/qtrack:61064c1

```bash
$ singularity pull shub://bouthilx/qtrack:61064c1
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
        git reset --hard 61064c1
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

