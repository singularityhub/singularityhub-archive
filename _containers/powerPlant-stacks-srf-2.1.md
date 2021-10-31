---
id: 6787
name: "powerPlant/stacks-srf"
branch: "master"
tag: "2.1"
commit: "33410b18016b0e23c1ca40f7c31fb740ff74a8bc"
version: "b0e2f280f2f144f2d825395fb72cfc19"
build_date: "2019-02-12T21:37:58.837Z"
size_mb: 645
size: 184270879
sif: "https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.1/2019-02-12-33410b18-b0e2f280/b0e2f280f2f144f2d825395fb72cfc19.simg"
url: https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.1/2019-02-12-33410b18-b0e2f280/
recipe: https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.1/2019-02-12-33410b18-b0e2f280/Singularity
collection: powerPlant/stacks-srf
---

# powerPlant/stacks-srf:2.1

```bash
$ singularity pull shub://powerPlant/stacks-srf:2.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:29

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2.1

%post
  ## Download build prerequisites
  dnf -y install gcc gcc-c++ libgomp make perl wget zlib-devel

  wget http://catchenlab.life.illinois.edu/stacks/source/stacks-2.1.tar.gz

  tar -xvf stacks-2.1.tar.gz
  cd stacks-2.1
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

