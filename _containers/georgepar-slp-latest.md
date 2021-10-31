---
id: 15877
name: "georgepar/slp"
branch: "master"
tag: "latest"
commit: "4618cf7676d110593310102d6fa76e02b62d83a8"
version: "b20cf3c7ae38bd392eff0a6632a02af0a4ac5c1c6f8387df9b02f84ac1536a3a"
build_date: "2021-04-08T16:49:47.703Z"
size_mb: 1447.875
size: 1518206976
sif: "https://datasets.datalad.org/shub/georgepar/slp/latest/2021-04-08-4618cf76-b20cf3c7/b20cf3c7ae38bd392eff0a6632a02af0a4ac5c1c6f8387df9b02f84ac1536a3a.sif"
url: https://datasets.datalad.org/shub/georgepar/slp/latest/2021-04-08-4618cf76-b20cf3c7/
recipe: https://datasets.datalad.org/shub/georgepar/slp/latest/2021-04-08-4618cf76-b20cf3c7/Singularity
collection: georgepar/slp
---

# georgepar/slp:latest

```bash
$ singularity pull shub://georgepar/slp:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%setup
    mkdir ${SINGULARITY_ROOTFS}/project

%environment
    export PYTHONPATH=$PYTHONPATH:/opt/cmusdk/

%post
    apt-get -y update
    DEBIAN_FRONTEND=noninteractive apt-get -y install python3 python3-pip ffmpeg git
    ln -s /usr/bin/python3 /usr/bin/python
    pip3 install --no-cache-dir poetry cookiecutter

    cd /project
    poetry export -f requirements.txt --output requirements.txt --without-hashes
    pip3 install --no-cache-dir -r requirements.txt
    cd /

    python -m  spacy download en_core_web_sm
    python -m  spacy download en_core_web_md
    python -m  spacy download el_core_news_sm
    python -m  spacy download el_core_news_md

    git clone https://github.com/A2Zadeh/CMU-MultimodalSDK /opt/cmusdk/

    apt-get -y remove --purge git python3-pip
    apt-get -y install python3-setuptools
    apt-get clean
    apt-get autoclean
    apt-get -y autoremove

%files
    pyproject.toml /project
    poetry.lock /project
```

## Collection

 - Name: [georgepar/slp](https://github.com/georgepar/slp)
 - License: [MIT License](https://api.github.com/licenses/mit)

