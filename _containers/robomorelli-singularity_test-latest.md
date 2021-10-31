---
id: 15305
name: "robomorelli/singularity_test"
branch: "main"
tag: "latest"
commit: "3dffee4eb1b318c0e28c5d8eaf4891ce586d7ceb"
version: "309e50f99fb7263f7ea22d0ed1bd91be"
build_date: "2021-03-20T19:32:13.860Z"
size_mb: 96.0
size: 37068831
sif: "https://datasets.datalad.org/shub/robomorelli/singularity_test/latest/2021-03-20-3dffee4e-309e50f9/309e50f99fb7263f7ea22d0ed1bd91be.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/robomorelli/singularity_test/latest/2021-03-20-3dffee4e-309e50f9/
recipe: https://datasets.datalad.org/shub/robomorelli/singularity_test/latest/2021-03-20-3dffee4e-309e50f9/Singularity
collection: robomorelli/singularity_test
---

# robomorelli/singularity_test:latest

```bash
$ singularity pull shub://robomorelli/singularity_test:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:16.04

%labels
MAINTAINER Vanessasaur
SPECIES Dinosaur

%environment
RAWR_BASE=/code
export RAWR_BASE


%runscript
echo "This gets run when you run the image!"
exec /bin/bash /code/rawr.sh "$@"


%post
echo "This section happens once after bootstrap to build the image."
mkdir -p /code
#apt-get install vim
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [robomorelli/singularity_test](https://github.com/robomorelli/singularity_test)
 - License: None

