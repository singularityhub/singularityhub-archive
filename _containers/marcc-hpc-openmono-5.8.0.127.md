---
id: 2174
name: "marcc-hpc/openmono"
branch: "5.8.0.127"
tag: "5.8.0.127"
commit: "3905916847bc2c85398f521f633718db9440e8ed"
version: "b0e1de7bd58c7684bf57afc89676f682"
build_date: "2018-03-19T17:39:30.918Z"
size_mb: 572
size: 144543775
sif: "https://datasets.datalad.org/shub/marcc-hpc/openmono/5.8.0.127/2018-03-19-39059168-b0e1de7b/b0e1de7bd58c7684bf57afc89676f682.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/openmono/5.8.0.127/2018-03-19-39059168-b0e1de7b/
recipe: https://datasets.datalad.org/shub/marcc-hpc/openmono/5.8.0.127/2018-03-19-39059168-b0e1de7b/Singularity
collection: marcc-hpc/openmono
---

# marcc-hpc/openmono:5.8.0.127

```bash
$ singularity pull shub://marcc-hpc/openmono:5.8.0.127
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: mono:5.8.0.127-slim

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /scratch /data 

  apt-get update \
  && apt-get install -y binutils curl mono-devel ca-certificates-mono fsharp mono-vbnc nuget referenceassemblies-pcl \
  && rm -rf /var/lib/apt/lists/* /tmp/*

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/openmono](https://github.com/marcc-hpc/openmono)
 - License: [MIT License](https://api.github.com/licenses/mit)

