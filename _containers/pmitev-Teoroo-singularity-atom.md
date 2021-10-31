---
id: 11875
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "atom"
commit: "e5749e9abbd4b97751fd449a3e09b1f90a9071f2"
version: "950cc88954d79ef020bec3e1182f2f32"
build_date: "2019-12-19T13:47:06.927Z"
size_mb: 1034.0
size: 310579231
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/atom/2019-12-19-e5749e9a-950cc889/950cc88954d79ef020bec3e1182f2f32.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/atom/2019-12-19-e5749e9a-950cc889/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/atom/2019-12-19-e5749e9a-950cc889/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:atom

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:atom
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: ubuntu:18.04

%runscript
  /usr/bin/atom $@ 

%setup

%files

%environment


%post
  export DEBIAN_FRONTEND=noninteractive
  export ATOM_VERSION=v1.42.0

  apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      fakeroot \
      gconf2 \
      gconf-service \
      git \
      gvfs-bin \
      libasound2 \
      libcap2 \
      libgconf-2-4 \
      libgcrypt20 \
      libgtk2.0-0 \
      libgtk-3-0 \
      libnotify4 \
      libnss3 \
      libx11-xcb1 \
      libxkbfile1 \
      libxss1 \
      libxtst6 \
      libgl1-mesa-glx \
      libgl1-mesa-dri \
      policykit-1 \
      python \
      xdg-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    curl -L https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom-amd64.deb > /tmp/atom.deb && \
    dpkg -i /tmp/atom.deb && \
    rm -f /tmp/atom.deb
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

