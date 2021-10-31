---
id: 7538
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "pp2"
commit: "d2a1a8b6133b38de5c45e0d295d4333ab6b83bbd"
version: "27aed9dbe65d046c702ec8185972b417"
build_date: "2019-02-28T22:42:32.015Z"
size_mb: 1219
size: 467443743
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/pp2/2019-02-28-d2a1a8b6-27aed9db/27aed9dbe65d046c702ec8185972b417.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/pp2/2019-02-28-d2a1a8b6-27aed9db/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/pp2/2019-02-28-d2a1a8b6-27aed9db/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:pp2

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:pp2
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: ubuntu:18.04

%runscript
  export PATH=/usr/local/bin:$PATH
  export XDG_RUNTIME_DIR=/tmp/.jupyter_$(uuidgen)
  /usr/bin/env python2 $@

%environment
  export PYTHONNOUSERSITE=True

%post
export DEBIAN_FRONTEND=noninteractive
#  echo 'PYTHONNOUSERSITE=True' >> $SINGULARITY_ENVIRONMENT

  apt-get update && apt-get install -y python-dev  python-pip  python-tk \
                            build-essential bash-completion less uuid-runtime libopenblas-dev csh openssh-client rsh-client \
                            gawk mc vim cython sqlite  && rm -rf /var/lib/apt/lists/*

  
/usr/bin/env python2 -m  pip install --upgrade pip
/usr/bin/env python2 -m  pip install --upgrade ase
/usr/bin/env python2 -m  pip install --upgrade pymatgen
/usr/bin/env python2 -m  pip install --upgrade phonopy
/usr/bin/env python2 -m  pip install --upgrade lxml
/usr/bin/env python2 -m  pip install --upgrade numba
/usr/bin/env python2 -m  pip install --upgrade pp
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

