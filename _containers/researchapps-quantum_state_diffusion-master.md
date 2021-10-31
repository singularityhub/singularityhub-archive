---
id: 180
name: "researchapps/quantum_state_diffusion"
branch: "master"
tag: "master"
commit: "d5c1c2e16a064dd47ef231538bb36f4bded3d905"
version: "d5f42d2bc86c706ca2e309fcff6f7bec"
build_date: "2017-10-17T19:50:54.058Z"
size_mb: 4890
size: 1296886265
sif: "https://datasets.datalad.org/shub/researchapps/quantum_state_diffusion/master/2017-10-17-d5c1c2e1-d5f42d2b/d5f42d2bc86c706ca2e309fcff6f7bec.img.gz"
url: https://datasets.datalad.org/shub/researchapps/quantum_state_diffusion/master/2017-10-17-d5c1c2e1-d5f42d2b/
recipe: https://datasets.datalad.org/shub/researchapps/quantum_state_diffusion/master/2017-10-17-d5c1c2e1-d5f42d2b/Singularity
collection: researchapps/quantum_state_diffusion
---

# researchapps/quantum_state_diffusion:master

```bash
$ singularity pull shub://researchapps/quantum_state_diffusion:master
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tabakg/quantum_state_diffusion
IncludeCmd: yes

%runscript

    exec /usr/local/anaconda3/bin/python /code/make_quantum_trajectory.py "$@"


% post

    mkdir -p /share/PI
    mkdir -p /scratch
    mkdir -p /local-scratch
    sudo chmod -R 777 /data
   echo "To run, ./qsd.img --help"
```

## Collection

 - Name: [researchapps/quantum_state_diffusion](https://github.com/researchapps/quantum_state_diffusion)
 - License: None

