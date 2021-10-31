---
id: 15882
name: "dcgc-bfx/dcgc-jupyter-rstudio"
branch: "main"
tag: "0.2.1"
commit: "ebbfaca23a86f4177565bec2e3ee015ebe91dcba"
version: "8b3e0c1b68444938bb1d732d20309994b3d20b1acd48b3302c3a0f50220f84e2"
build_date: "2021-04-12T09:03:07.573Z"
size_mb: 1539.01171875
size: 1613770752
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.2.1/2021-04-12-ebbfaca2-8b3e0c1b/8b3e0c1b68444938bb1d732d20309994b3d20b1acd48b3302c3a0f50220f84e2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.2.1/2021-04-12-ebbfaca2-8b3e0c1b/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.2.1/2021-04-12-ebbfaca2-8b3e0c1b/Singularity
collection: dcgc-bfx/dcgc-jupyter-rstudio
---

# dcgc-bfx/dcgc-jupyter-rstudio:0.2.1

```bash
$ singularity pull shub://dcgc-bfx/dcgc-jupyter-rstudio:0.2.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: dcgc-bfx/dcgc-base-conda:0.1.1

%labels
  Author fabian.rost@tu-dresden.de
  Organisation DcGC
  Version latest

%help
  Start jupyter lab:
    singularity run --writable-tmpfs --app jupyter library://fabianrost84/dcgc/single-cell.sif

  Start rstudio server listening on port 8787:
    singularity run --writable-tmpfs --app rserver library://fabianrost84/dcgc/single-cell.sif 8787

%files
  files/jupyter_notebook_config.json /opt/conda/etc/jupyter/
  files/rserver.conf /etc/rstudio/rserver.conf

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
  mamba clean -ai --quiet --yes

  # jupyterlab extensions
  jupyter labextension install "@jupyterlab/toc"

  # rstudio server
  apt-get update --fix-missing -q
  apt-get install -y -q \
    gdebi-core \
    uuid

  wget --no-verbose https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.4.1106-amd64.deb
  gdebi -q -n rstudio-server-1.4.1106-amd64.deb
  rm rstudio-server-1.4.1106-amd64.deb
  chmod -R a+rw /var/lib/rstudio-server

  apt-get clean -q
  rm -rf /var/lib/apt/lists/*

  # for running rstudio server with conda R
  git clone https://github.com/grst/rstudio-server-conda.git

  chmod -R a+w /opt

####################
## rstudio server ##
####################

%apprun rserver
  bash <<-EOF
	source activate /opt/conda
	/rstudio-server-conda/start_rstudio_server.sh "${@}"
EOF

#################
## jupyter lab ##
#################

%apprun jupyter
  bash <<-EOF
	source activate /opt/conda
	jupyter lab --no-browser "${@}"
EOF
```

## Collection

 - Name: [dcgc-bfx/dcgc-jupyter-rstudio](https://github.com/dcgc-bfx/dcgc-jupyter-rstudio)
 - License: None

