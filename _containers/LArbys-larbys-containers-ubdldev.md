---
id: 7732
name: "LArbys/larbys-containers"
branch: "master"
tag: "ubdldev"
commit: "94f99842cc966637b3a8ba8bec085aa7ea245dd8"
version: "fdbaaa429957d0a313f5a64ea5446961"
build_date: "2019-03-13T03:34:54.636Z"
size_mb: 10837
size: 4729229343
sif: "https://datasets.datalad.org/shub/LArbys/larbys-containers/ubdldev/2019-03-13-94f99842-fdbaaa42/fdbaaa429957d0a313f5a64ea5446961.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/LArbys/larbys-containers/ubdldev/2019-03-13-94f99842-fdbaaa42/
recipe: https://datasets.datalad.org/shub/LArbys/larbys-containers/ubdldev/2019-03-13-94f99842-fdbaaa42/Singularity
collection: LArbys/larbys-containers
---

# LArbys/larbys-containers:ubdldev

```bash
$ singularity pull shub://LArbys/larbys-containers:ubdldev
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: larbys/ubdl:ubuntu16.04

%post
	apt update -y
	apt install -y emacs vim
	apt autoremove -y && apt clean -y
	mkdir -p /cluster/home
	mkdir -p /cluster/kappa
	mkdir -p /cluster/shared
	mkdir -p /opt/shared
```

## Collection

 - Name: [LArbys/larbys-containers](https://github.com/LArbys/larbys-containers)
 - License: None

