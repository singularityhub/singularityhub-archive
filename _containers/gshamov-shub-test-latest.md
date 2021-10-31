---
id: 893
name: "gshamov/shub-test"
branch: "master"
tag: "latest"
commit: "80023392a11487b84fa7ea1a6d96ab3102159f63"
version: "d40159bf7de42b5174b57704f504f64a"
build_date: "2019-10-14T14:06:37.550Z"
size_mb: 1013
size: 327229471
sif: "https://datasets.datalad.org/shub/gshamov/shub-test/latest/2019-10-14-80023392-d40159bf/d40159bf7de42b5174b57704f504f64a.simg"
url: https://datasets.datalad.org/shub/gshamov/shub-test/latest/2019-10-14-80023392-d40159bf/
recipe: https://datasets.datalad.org/shub/gshamov/shub-test/latest/2019-10-14-80023392-d40159bf/Singularity
collection: gshamov/shub-test
---

# gshamov/shub-test:latest

```bash
$ singularity pull shub://gshamov/shub-test:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.10

%help
   A container to have Ubuntu 16.10 (Yakkety Yak) build environment.
   The environment should be enough to build AlmaBTE as per
   http://www.almabte.eu/index.php/user-manual/

%runscript
    echo "This is what happens when you run the container..."


%post
    echo "Hello from inside the container"
    apt-get -y update
    apt-get -y --force-yes install vim mc build-essential cmake libboost-all-dev libhdf5-dev wget
```

## Collection

 - Name: [gshamov/shub-test](https://github.com/gshamov/shub-test)
 - License: None

