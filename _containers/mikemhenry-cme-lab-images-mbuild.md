---
id: 3425
name: "mikemhenry/cme-lab-images"
branch: "master"
tag: "mbuild"
commit: "13bea269668d51287e5ecaa17688a0e27128b672"
version: "be7416d36d60dbb083ed1a272bced2a3"
build_date: "2018-07-06T23:39:12.192Z"
size_mb: 3267
size: 1572511775
sif: "https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/mbuild/2018-07-06-13bea269-be7416d3/be7416d36d60dbb083ed1a272bced2a3.simg"
url: https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/mbuild/2018-07-06-13bea269-be7416d3/
recipe: https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/mbuild/2018-07-06-13bea269-be7416d3/Singularity
collection: mikemhenry/cme-lab-images
---

# mikemhenry/cme-lab-images:mbuild

```bash
$ singularity pull shub://mikemhenry/cme-lab-images:mbuild
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: shub://singularity-hub.org/mikemhenry/cme-lab-images:hoomd
%help
Base HOOMD image used in CME-Lab workflows.

http://coen.boisestate.edu/cmelab/

%setup

%files
  spec-file.txt
%labels
  Maintainer Mike Henry
  Maintaine_rEmail mikehenry@boisestate.edu
  Version v0.01

%environment

%post
  CONDA_DIR="/opt/conda"
  PATH="$CONDA_DIR/bin:$PATH"
# System deps 
  apt-get update && apt-get install -y --no-install-recommends libxrender1 libxext6 libcairo2
  conda install --file spec-file.txt -y
  #conda install -c cmelab -c mosdef -c bioconda -c glotzer -c omnia -c openbabel -y mbuild notebook gsd openbabel
  conda clean -tipsy
  nglview install
  nglview enable
  jupyter nbextension enable --py --sys-prefix widgetsnbextension
  # These are some speical forks that have merged in pedning PRs
  pip install --no-cache-dir --upgrade git+https://github.com/mikemhenry/foyer.git@f0c8d69087f9 git+https://github.com/mikemhenry/mbuild.git@ac3cea9e725a
  
%runscript
  jupyter notebook --port=9989 --ip='*' --no-browser --allow-root --NotebookApp.iopub_data_rate_limit=100000000

%test
```

## Collection

 - Name: [mikemhenry/cme-lab-images](https://github.com/mikemhenry/cme-lab-images)
 - License: None

