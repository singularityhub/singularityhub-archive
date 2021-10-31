---
id: 1865
name: "jasongallant/singularity_demo"
branch: "master"
tag: "latest"
commit: "7626f34acd475edf976a5d1fec0822a171840929"
version: "6e392d1ff06a071053f64125c7cc5559"
build_date: "2018-02-26T16:06:31.492Z"
size_mb: 234
size: 97132575
sif: "https://datasets.datalad.org/shub/jasongallant/singularity_demo/latest/2018-02-26-7626f34a-6e392d1f/6e392d1ff06a071053f64125c7cc5559.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jasongallant/singularity_demo/latest/2018-02-26-7626f34a-6e392d1f/
recipe: https://datasets.datalad.org/shub/jasongallant/singularity_demo/latest/2018-02-26-7626f34a-6e392d1f/Singularity
collection: jasongallant/singularity_demo
---

# jasongallant/singularity_demo:latest

```bash
$ singularity pull shub://jasongallant/singularity_demo:latest
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

 - Name: [jasongallant/singularity_demo](https://github.com/jasongallant/singularity_demo)
 - License: None

