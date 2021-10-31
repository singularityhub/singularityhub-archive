---
id: 740
name: "expfactory-experiments/breath-counting-task"
branch: "master"
tag: "latest"
commit: "3c08d3f8a251be96c5a4948a4564f2996c3c29a7"
version: "544839f00ade3fe68afa6863b9bb2e1f"
build_date: "2017-11-09T13:22:23.803Z"
size_mb: 546
size: 182603807
sif: "https://datasets.datalad.org/shub/expfactory-experiments/breath-counting-task/latest/2017-11-09-3c08d3f8-544839f0/544839f00ade3fe68afa6863b9bb2e1f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/expfactory-experiments/breath-counting-task/latest/2017-11-09-3c08d3f8-544839f0/
recipe: https://datasets.datalad.org/shub/expfactory-experiments/breath-counting-task/latest/2017-11-09-3c08d3f8-544839f0/Singularity
collection: expfactory-experiments/breath-counting-task
---

# expfactory-experiments/breath-counting-task:latest

```bash
$ singularity pull shub://expfactory-experiments/breath-counting-task:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

########################################
# Configure
########################################

%environment
    EXPFACTORY_STUDY_ID=expfactory
    EXPFACTORY_SERVER=localhost
    export EXPFACTORY_STUDY_ID \
           EXPFACTORY_SERVER


########################################
# Install No need to touch below here
########################################

    EXPFACTORY_CONTAINER=true
    EXPFACTORY_DATA=/scif/data
    EXPFACTORY_DATABASE=filesystem 
    EXPFACTORY_BASE=/scif/apps
    export EXPFACTORY_BASE EXPFACTORY_DATA \
           EXPFACTORY_DATABASE \
           EXPFACTORY_CONTAINER

%help

If you want to see experiments available:
    singularity apps expfactory.img

To build your image (sandbox for testing)
    sudo singularity build --sandbox [expfactory] Singularity

To build your image (production)
    sudo singularity build expfactory.simg Singularity

To serve your battery
    sudo singularity instance.start expfactory.simg web1

%startscript
    service nginx start
    gunicorn --bind 0.0.0.0:5000 expfactory.wsgi:app
    service nginx restart

%post
    apt-get update && apt-get install -y nginx git python3-pip python3-dev
    cd /opt && git clone https://www.github.com/expfactory/expfactory
    cd expfactory && cp script/nginx.gunicorn.conf /etc/nginx/sites-enabled/default
    cp script/nginx.conf /etc/nginx/nginx.conf
    mkdir -p /scif/apps
    python3 -m pip install gunicorn
    cp expfactory/config_dummy.py expfactory/config.py
    chmod u+x /opt/expfactory/script/generate_key.sh
    /bin/bash /opt/expfactory/script/generate_key.sh /opt/expfactory/expfactory/config.py
    python3 setup.py install


########################################
# Install Experiments
########################################

%labels
    APPLICATION EXPFACTORY    

%appinstall breath-counting-task
    cd .. && expfactory install -f https://github.com/expfactory-experiments/breath-counting-task
```

## Collection

 - Name: [expfactory-experiments/breath-counting-task](https://github.com/expfactory-experiments/breath-counting-task)
 - License: [MIT License](https://api.github.com/licenses/mit)

