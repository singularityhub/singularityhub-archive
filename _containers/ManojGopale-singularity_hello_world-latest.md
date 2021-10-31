---
id: 2609
name: "ManojGopale/singularity_hello_world"
branch: "master"
tag: "latest"
commit: "a9f6f7fb5fa481cf2a3d90678197cf97fbc8b51d"
version: "69da3c3bc7ac1eae97b9ae558a02abf5"
build_date: "2021-03-01T14:01:21.802Z"
size_mb: 235
size: 97300511
sif: "https://datasets.datalad.org/shub/ManojGopale/singularity_hello_world/latest/2021-03-01-a9f6f7fb-69da3c3b/69da3c3bc7ac1eae97b9ae558a02abf5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ManojGopale/singularity_hello_world/latest/2021-03-01-a9f6f7fb-69da3c3b/
recipe: https://datasets.datalad.org/shub/ManojGopale/singularity_hello_world/latest/2021-03-01-a9f6f7fb-69da3c3b/Singularity
collection: ManojGopale/singularity_hello_world
---

# ManojGopale/singularity_hello_world:latest

```bash
$ singularity pull shub://ManojGopale/singularity_hello_world:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%runscript

    echo "I can put here whatever I want to happen when the user runs my container!"
    exec echo "Hello Monsoir Meatball" "$@"

%post
 
   echo "Here we are installing software and other dependencies for the container!"
   apt-get update
   apt-get install -y git
```

## Collection

 - Name: [ManojGopale/singularity_hello_world](https://github.com/ManojGopale/singularity_hello_world)
 - License: None

