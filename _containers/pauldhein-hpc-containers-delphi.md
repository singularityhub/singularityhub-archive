---
id: 9208
name: "pauldhein/hpc-containers"
branch: "master"
tag: "delphi"
commit: "d580bc9b2e04f2ba8b945c3cd618d7b6fb214ba1"
version: "bf0b2c4d2b048025fe788c1a893f1384"
build_date: "2019-06-06T15:55:37.587Z"
size_mb: 4749
size: 3062181919
sif: "https://datasets.datalad.org/shub/pauldhein/hpc-containers/delphi/2019-06-06-d580bc9b-bf0b2c4d/bf0b2c4d2b048025fe788c1a893f1384.simg"
url: https://datasets.datalad.org/shub/pauldhein/hpc-containers/delphi/2019-06-06-d580bc9b-bf0b2c4d/
recipe: https://datasets.datalad.org/shub/pauldhein/hpc-containers/delphi/2019-06-06-d580bc9b-bf0b2c4d/Singularity
collection: pauldhein/hpc-containers
---

# pauldhein/hpc-containers:delphi

```bash
$ singularity pull shub://pauldhein/hpc-containers:delphi
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ml4ai/UA-hpc-containers:pytorch

%help
  Temporary container for delphi with PyTorch support

%post
  # in-container bind points for shared filesystems
  mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local
  apt-get -y update
  apt-get -y install git
  apt-get -y install graphviz libgraphviz-dev pkg-config
  # git clone https://github.com/ml4ai/delphi.git
  # cd delphi/
  # pip install -e .
  pip install torch==1.0.1 indra tqdm numpy scipy pandas future networkx cython dataclasses python-dateutil salib sympy plotly matplotlib seaborn>=0.9.0 flask SQLAlchemy flask-sqlalchemy jupyter jupyter-contrib-nbextensions flask-WTF flask-codemirror pygments
```

## Collection

 - Name: [pauldhein/hpc-containers](https://github.com/pauldhein/hpc-containers)
 - License: None

