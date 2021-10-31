---
id: 7615
name: "giovannipizzi/singularity-quantum-espresso"
branch: "master"
tag: "apt-5.1"
commit: "9d192bfcdca44c3d86663e7f46200521b3c183dc"
version: "f42117d3e55fbb49cbaf0fc9514bae2e"
build_date: "2019-03-06T12:46:34.208Z"
size_mb: 296
size: 132423711
sif: "https://datasets.datalad.org/shub/giovannipizzi/singularity-quantum-espresso/apt-5.1/2019-03-06-9d192bfc-f42117d3/f42117d3e55fbb49cbaf0fc9514bae2e.simg"
url: https://datasets.datalad.org/shub/giovannipizzi/singularity-quantum-espresso/apt-5.1/2019-03-06-9d192bfc-f42117d3/
recipe: https://datasets.datalad.org/shub/giovannipizzi/singularity-quantum-espresso/apt-5.1/2019-03-06-9d192bfc-f42117d3/Singularity
collection: giovannipizzi/singularity-quantum-espresso
---

# giovannipizzi/singularity-quantum-espresso:apt-5.1

```bash
$ singularity pull shub://giovannipizzi/singularity-quantum-espresso:apt-5.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install quantum-espresso
    apt-get -y clean

%environment
    export LC_ALL=en_US.UTF-8

%runscript
    echo "Quantum ESPRESSO 5.1 is installed (via APT on ubuntu 16.04) in this singularity file. Just run pw.x or one of the other Quantum ESPRESSO codes."
```

## Collection

 - Name: [giovannipizzi/singularity-quantum-espresso](https://github.com/giovannipizzi/singularity-quantum-espresso)
 - License: None

