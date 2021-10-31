---
id: 15838
name: "dcgc-bfx/dcgc-jupyter-rstudio"
branch: "main"
tag: "0.2.0"
commit: "cde94455cd158bebace3d9999be303f77cffbdd8"
version: "0aa3b48740b146b64481595e334e127119c93a66146eba6949480da87fa97117"
build_date: "2021-04-09T22:35:14.341Z"
size_mb: 1558.37890625
size: 1634078720
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.2.0/2021-04-09-cde94455-0aa3b487/0aa3b48740b146b64481595e334e127119c93a66146eba6949480da87fa97117.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.2.0/2021-04-09-cde94455-0aa3b487/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-jupyter-rstudio/0.2.0/2021-04-09-cde94455-0aa3b487/Singularity
collection: dcgc-bfx/dcgc-jupyter-rstudio
---

# dcgc-bfx/dcgc-jupyter-rstudio:0.2.0

```bash
$ singularity pull shub://dcgc-bfx/dcgc-jupyter-rstudio:0.2.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: dcgc-bfx/dcgc-base-conda:0.1

%labels
  Author fabian.rost@tu-dresden.de
  Organisation DcGC
  Version v0.2.0

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
  mamba clean -ai --quiet --yes

  # jupyterlab extensions
  jupyter labextension install "@jupyterlab/toc"

  # rstudio server
  apt-get update --fix-missing -q
  apt-get install -y -q \
    gdebi-core \
    uuid

  wget --no-verbose https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.3.1093-amd64.deb
  gdebi -q -n rstudio-server-1.3.1093-amd64.deb
  rm rstudio-server-1.3.1093-amd64.deb

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

