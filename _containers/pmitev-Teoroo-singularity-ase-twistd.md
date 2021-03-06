---
id: 7163
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "ase-twistd"
commit: "97010fdfe33d518ea2e6f2695a388365465498df"
version: "4492fd31843969158520d54539c2a4a7"
build_date: "2019-02-21T01:10:10.330Z"
size_mb: 794
size: 309796895
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/ase-twistd/2019-02-21-97010fdf-4492fd31/4492fd31843969158520d54539c2a4a7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/ase-twistd/2019-02-21-97010fdf-4492fd31/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/ase-twistd/2019-02-21-97010fdf-4492fd31/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:ase-twistd

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:ase-twistd
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: ubuntu:18.04

%runscript
  cp -a /opt/ase-db /tmp
  cd /tmp/ase-db; exec /usr/bin/twistd3 -n web --wsgi=ase.db.app.app 

%setup
  mkdir        -p ${SINGULARITY_ROOTFS}/usr/local/lib/python3.6/dist-packages/ase/db/static
  mkdir -m 777 -p ${SINGULARITY_ROOTFS}/opt/ase-db

%files
  ASE_DB_APP_CONFIG /opt/ase-db/
  test.db /opt/ase-db/
  jsmol /usr/local/lib/python3.6/dist-packages/ase/db/static

%environment
  export ASE_DB_APP_CONFIG=/opt/ase-db/ASE_DB_APP_CONFIG

%post
  env
  chmod a+r /opt/ase-db/*
  find /usr/local/lib/python3.6/dist-packages/ase/db/static  -type d -exec chmod 755 {} \;
  find /usr/local/lib/python3.6/dist-packages/ase/db/static  -type f -exec chmod 644 {} \;
  ln -s /tmp/ /opt/ase-db/tmpdir

  apt-get update && apt-get install -y  python3-pip  python3-twisted && rm -rf /var/lib/apt/lists/*
  /usr/bin/env python3 -m pip install --upgrade pip && /usr/bin/env python3 -m  pip install --upgrade ase
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

