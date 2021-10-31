---
id: 15680
name: "dcgc-bfx/dcgc-jupyter-rstudio"
branch: "main"
tag: "0.1"
commit: "6194806611d1cb8b4009c25126773b45db9dc674"
version: "cf430352b34d22f382e43cd08b153a8aeed9f518b9e9eadc2bc658a23a6c6e07"
build_date: "2021-04-01T14:46:09.210Z"
size_mb: 1552.15625
size: 1627553792
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.1/2021-04-01-61948066-cf430352/cf430352b34d22f382e43cd08b153a8aeed9f518b9e9eadc2bc658a23a6c6e07.sif"
url: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.1/2021-04-01-61948066-cf430352/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.1/2021-04-01-61948066-cf430352/Singularity
collection: dcgc-bfx/dcgc-jupyter-rstudio
---

# dcgc-bfx/dcgc-jupyter-rstudio:0.1

```bash
$ singularity pull shub://dcgc-bfx/dcgc-jupyter-rstudio:0.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: dcgc-bfx/dcgc-base-conda:0.1

%labels
  Author fabian.rost@tu-dresden.de
  Organisation DcGC
  Version v0.1

%help
  Start jupyter lab:
    singularity run --writable-tmpfs --app jupyter library://fabianrost84/dcgc/single-cell.sif

  Start rstudio server listening on port 8787:
    singularity run --writable-tmpfs --app rserver library://fabianrost84/dcgc/single-cell.sif 8787

%files
  jupyter_notebook_config.json /opt/conda/etc/jupyter/

%environment
  DEBIAN_FRONTEND=noninteractive

%post
  chmod -R a+w /opt
  export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

  mamba install --quiet --yes \
    ipykernel \
    jupyter_nbextensions_configurator \
    jupyterlab \
    nodejs \
    r-irkernel

  # clean conda cache
  mamba clean -ai

  # jupyterlab extensions
  jupyter labextension install "@jupyterlab/toc"

  # rstudio server
  apt-get update
  apt-get install -y \
    gdebi-core \
    uuid

  wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.3.1093-amd64.deb
  gdebi -n rstudio-server-1.3.1093-amd64.deb
  rm rstudio-server-1.3.1093-amd64.deb

  apt-get clean
  rm -rf /var/lib/apt/lists/*

  # for running rstudio server with conda R
  git clone https://github.com/grst/rstudio-server-conda.git

  ####################
  ## rstudio server ##
  ####################

%apprun rserver
  conda run --no-capture-output -p /opt/conda /rstudio-server-conda/start_rstudio_server.sh "${@}"

#################
## jupyter lab ##
#################

%apprun jupyter
  conda run --no-capture-output -p /opt/conda jupyter lab --no-browser "${@}"
```

## Collection

 - Name: [dcgc-bfx/dcgc-jupyter-rstudio](https://github.com/dcgc-bfx/dcgc-jupyter-rstudio)
 - License: None

