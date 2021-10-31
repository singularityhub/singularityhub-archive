---
id: 10266
name: "researchapps/quantum_state_diffusion"
branch: "master"
tag: "latest"
commit: "a5088d0bc58100eb0114f7adb154b01c4a5b18b2"
version: "ddb71b99942674f3a838f48d81ef1290"
build_date: "2021-03-09T01:21:58.101Z"
size_mb: 2929.0
size: 1243815967
sif: "https://datasets.datalad.org/shub/researchapps/quantum_state_diffusion/latest/2021-03-09-a5088d0b-ddb71b99/ddb71b99942674f3a838f48d81ef1290.sif"
url: https://datasets.datalad.org/shub/researchapps/quantum_state_diffusion/latest/2021-03-09-a5088d0b-ddb71b99/
recipe: https://datasets.datalad.org/shub/researchapps/quantum_state_diffusion/latest/2021-03-09-a5088d0b-ddb71b99/Singularity
collection: researchapps/quantum_state_diffusion
---

# researchapps/quantum_state_diffusion:latest

```bash
$ singularity pull shub://researchapps/quantum_state_diffusion:latest
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

