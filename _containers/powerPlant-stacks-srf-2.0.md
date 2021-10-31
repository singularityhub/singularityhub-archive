---
id: 6786
name: "powerPlant/stacks-srf"
branch: "master"
tag: "2.0"
commit: "33410b18016b0e23c1ca40f7c31fb740ff74a8bc"
version: "afb168079c009d2c803700fc27840cd6"
build_date: "2019-02-12T21:37:58.844Z"
size_mb: 645
size: 184164383
sif: "https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.0/2019-02-12-33410b18-afb16807/afb168079c009d2c803700fc27840cd6.simg"
url: https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.0/2019-02-12-33410b18-afb16807/
recipe: https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.0/2019-02-12-33410b18-afb16807/Singularity
collection: powerPlant/stacks-srf
---

# powerPlant/stacks-srf:2.0

```bash
$ singularity pull shub://powerPlant/stacks-srf:2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:29

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2.0

%post
  ## Download build prerequisites
  dnf -y install gcc gcc-c++ libgomp make perl wget zlib-devel

  wget http://catchenlab.life.illinois.edu/stacks/source/stacks-2.0.tar.gz

  tar -xvf stacks-2.0.tar.gz
  cd stacks-2.0
  ./configure
  make
  make install
  
  ## Cleanup
  dnf -y remove wget zlib-devel
  dnf -y clean all
  rm -rf /stacks*

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"$SINGULARITY_NAME <cmd>\" or \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec ls /usr/local/bin
else
  exec "$@"
fi
```

## Collection

 - Name: [powerPlant/stacks-srf](https://github.com/powerPlant/stacks-srf)
 - License: None

