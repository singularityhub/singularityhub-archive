---
id: 13079
name: "ftabaro/singularity-coderefinery2020"
branch: "master"
tag: "latest"
commit: "c3352cd91e569d7bf6d31c22c3671b2b2a61751c"
version: "720e2a592f4d663ab895995d2b83a58b2e1e1d42d7852880d439ba9f85c93804"
build_date: "2020-05-25T16:21:57.397Z"
size_mb: 1898.1953125
size: 1990402048
sif: "https://datasets.datalad.org/shub/ftabaro/singularity-coderefinery2020/latest/2020-05-25-c3352cd9-720e2a59/720e2a592f4d663ab895995d2b83a58b2e1e1d42d7852880d439ba9f85c93804.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ftabaro/singularity-coderefinery2020/latest/2020-05-25-c3352cd9-720e2a59/
recipe: https://datasets.datalad.org/shub/ftabaro/singularity-coderefinery2020/latest/2020-05-25-c3352cd9-720e2a59/Singularity
collection: ftabaro/singularity-coderefinery2020
---

# ftabaro/singularity-coderefinery2020:latest

```bash
$ singularity pull shub://ftabaro/singularity-coderefinery2020:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: jupyter/datascience-notebook:latest

%help
  Extended jupyter/datascience-notebook with packages for CodeRefinery workshop.

  How to start Jupyter Lab IDE:
    - with default options:                  ./coderefinery.sif
    - with custom options:                   ./coderefinery.sif --port=9876 --no-browser
    - with bind mount(s):                    singularity run -B /my/custom/path coderefinery.sif
    - with bind mount(s) and custom options: singularity run -B /my/custom/path coderefinery.sif --port=9876 --no-browser

%labels
  Author francesco.tabaro@tuni.fi
  Version 0.1.1

%post
  BUILDDATE=$(date -I)
  VERSION="0.1.1"
  echo "export BUILDDATE=\"${BUILDDATE}\"" >> $SINGULARITY_ENVIRONMENT
  echo "export VERSION=\"${VERSION}\"" >> $SINGULARITY_ENVIRONMENT
  PATH=/opt/conda/bin:$PATH && \
  apt-get update && apt-get install -y -q vim && \
  conda install --quiet --yes sphinx sphinx_rtd_theme pytest pycodestyle && \
  conda install --quiet --yes -c conda-forge jupyterlab-git nbdime ipywidgets && \
  conda clean --all -f && \
  pip install jupyterlab_github && \
  jupyter lab build && \
  jupyter labextension install @jupyterlab/github

%environment
  export PATH=/opt/conda/bin:$PATH
  
%runscript
  echo "CodeRefinery 2020 Singularity container v$VERSION-$BUILDDATE"
  echo "Starting Jupyter Lab..."
  exec jupyter lab $@
```

## Collection

 - Name: [ftabaro/singularity-coderefinery2020](https://github.com/ftabaro/singularity-coderefinery2020)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

