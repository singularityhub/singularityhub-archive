---
id: 1381
name: "sci-f/container.scif"
branch: "master"
tag: "latest"
commit: "98502a9f75ff3f919b58d5326721045dcb485bf4"
version: "d89149dfc5fc33c46ee82212e8962b27"
build_date: "2021-04-14T04:00:51.915Z"
size_mb: 2486
size: 917303327
sif: "https://datasets.datalad.org/shub/sci-f/container.scif/latest/2021-04-14-98502a9f-d89149df/d89149dfc5fc33c46ee82212e8962b27.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sci-f/container.scif/latest/2021-04-14-98502a9f-d89149df/
recipe: https://datasets.datalad.org/shub/sci-f/container.scif/latest/2021-04-14-98502a9f-d89149df/Singularity
collection: sci-f/container.scif
---

# sci-f/container.scif:latest

```bash
$ singularity pull shub://sci-f/container.scif:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%help
This container will say hello-world (in dinosaur)!

Examples:

     # See all installed languages
     ./<container> apps

     # See help for a specific language
     ./<container> help <language> Or

     # Run a specific languages
     ./<container> run <language>

%runscript
    exec /opt/conda/bin/scif "$@"

%post
    apt-get update && apt-get install -y wget vim curl unzip git build-essential
    apt-get install -y cpp gcc g++

    /opt/conda/bin/pip install scif
    /opt/conda/bin/scif install /hello-world.scif

%files
    hello-world.scif
    helpers /opt
    data

%environment
    # Here I have global variables for each app section to access
    DEBIAN_FRONTEND=noninteractive
    export DEBIAN_FRONTEND
```

## Collection

 - Name: [sci-f/container.scif](https://github.com/sci-f/container.scif)
 - License: [BSD 3-clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

