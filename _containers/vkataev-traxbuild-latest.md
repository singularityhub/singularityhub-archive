---
id: 11849
name: "vkataev/traxbuild"
branch: "master"
tag: "latest"
commit: "e26491f51c7d97d93fb76178320d47a9fcdacd6b"
version: "29142a09303117bc0305a69e0025f94b"
build_date: "2020-01-17T10:11:20.191Z"
size_mb: 1660.0
size: 701403167
sif: "https://datasets.datalad.org/shub/vkataev/traxbuild/latest/2020-01-17-e26491f5-29142a09/29142a09303117bc0305a69e0025f94b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/vkataev/traxbuild/latest/2020-01-17-e26491f5-29142a09/
recipe: https://datasets.datalad.org/shub/vkataev/traxbuild/latest/2020-01-17-e26491f5-29142a09/Singularity
collection: vkataev/traxbuild
---

# vkataev/traxbuild:latest

```bash
$ singularity pull shub://vkataev/traxbuild:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest
#From: tensorflow/tensorflow:latest

%runscript
 
    exec /venv/bin/python "$@"

%post

    export LC_ALL=C
    export PATH=/bin:/sbin:/usr/bin:/usr/sbin:$PATH

    echo "S: Update and install pip + virtualenv packages"
    apt update -y
    apt install -y python3-dev python3-pip
    pip3 install -U virtualenv

    echo "S: Create a virtual environment"
    virtualenv --system-site-packages -p python3 /venv

#    echo "S: Enter virtualenv"
#    source ./venv/bin/activate

    echo "S: Upgrade pip"
    /venv/bin/pip install --upgrade pip

    echo "S: Install tensorflow package"
    /venv/bin/pip install --upgrade tensorflow

    echo "S: Verify tensorflow"
    /venv/bin/python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([100, 100])))"

    echo "S: Install trax"
    /venv/bin/pip install --upgrade trax

%post

    echo "S: Install matplotlib"
    /venv/bin/pip install --upgrade matplotlib

#   echo "S: Install dev env"
#   apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip
#   echo "S: Install dependencies"
#   pip3 install -U pip six numpy wheel setuptools mock 'future>=0.17.1'
#   pip3 install keras_applications --no-deps
#   pip3 install keras_preprocessing --no-deps
#   echo "S: Install tensorflow"
#   pip3 install tensorflow:latest
#   echo "S: Install tensorflow"

%labels

AUTHOR Vadim Kataev
```

## Collection

 - Name: [vkataev/traxbuild](https://github.com/vkataev/traxbuild)
 - License: [MIT License](https://api.github.com/licenses/mit)

