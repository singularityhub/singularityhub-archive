---
id: 14015
name: "MariusCausemann/brain-inversion"
branch: "master"
tag: "latest"
commit: "883a736a184433b45dbdfcdb2a567ffe52a4b84b"
version: "718548d07d62afedfda9e6f5849b659a"
build_date: "2020-08-22T16:53:13.331Z"
size_mb: 2497.0
size: 675348511
sif: "https://datasets.datalad.org/shub/MariusCausemann/brain-inversion/latest/2020-08-22-883a736a-718548d0/718548d07d62afedfda9e6f5849b659a.sif"
url: https://datasets.datalad.org/shub/MariusCausemann/brain-inversion/latest/2020-08-22-883a736a-718548d0/
recipe: https://datasets.datalad.org/shub/MariusCausemann/brain-inversion/latest/2020-08-22-883a736a-718548d0/Singularity
collection: MariusCausemann/brain-inversion
---

# MariusCausemann/brain-inversion:latest

```bash
$ singularity pull shub://MariusCausemann/brain-inversion:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: multiphenics/multiphenics

%environment
    PYTHONPATH=/usr/local/lib/python3/dist-packages/gmsh-4.6.0-Linux64-sdk/lib/
    export PYTHONPATH

%post
    chmod -R 777 var/*
    apt-get -q update && 
    apt-get install -q -y libgl1-mesa-dev libglu1-mesa-dev libxcursor-dev libxinerama-dev python3-h5py
    apt-get clean
    pip3 -q install --upgrade --no-cache-dir pip meshio==4.0.13 jdata pyvista gmsh pygmsh pyyaml
```

## Collection

 - Name: [MariusCausemann/brain-inversion](https://github.com/MariusCausemann/brain-inversion)
 - License: None

