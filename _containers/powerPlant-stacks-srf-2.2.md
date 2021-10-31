---
id: 6788
name: "powerPlant/stacks-srf"
branch: "master"
tag: "2.2"
commit: "33410b18016b0e23c1ca40f7c31fb740ff74a8bc"
version: "5bf3f497f1c116b4f2e902b1fb28dd94"
build_date: "2019-02-12T21:37:58.830Z"
size_mb: 645
size: 184274975
sif: "https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.2/2019-02-12-33410b18-5bf3f497/5bf3f497f1c116b4f2e902b1fb28dd94.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/stacks-srf/2.2/2019-02-12-33410b18-5bf3f497/
recipe: https://datasets.datalad.org/shub/powerPlant/stacks-srf/2.2/2019-02-12-33410b18-5bf3f497/Singularity
collection: powerPlant/stacks-srf
---

# powerPlant/stacks-srf:2.2

```bash
$ singularity pull shub://powerPlant/stacks-srf:2.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:29

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2.2

%post
  ## Download build prerequisites
  dnf -y install gcc gcc-c++ libgomp make perl wget zlib-devel

  wget http://catchenlab.life.illinois.edu/stacks/source/stacks-2.2.tar.gz

  tar -xvf stacks-2.2.tar.gz
  cd stacks-2.2
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

