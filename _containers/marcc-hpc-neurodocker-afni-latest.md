---
id: 993
name: "marcc-hpc/neurodocker-afni"
branch: "master"
tag: "latest"
commit: "b729ea1281d35f418668cbc64bd43c4e6556814d"
version: "3eace911eddf68e78addf15ce0fd0e12"
build_date: "2021-04-09T18:46:14.847Z"
size_mb: 3920
size: 1613512735
sif: "https://datasets.datalad.org/shub/marcc-hpc/neurodocker-afni/latest/2021-04-09-b729ea12-3eace911/3eace911eddf68e78addf15ce0fd0e12.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/neurodocker-afni/latest/2021-04-09-b729ea12-3eace911/
recipe: https://datasets.datalad.org/shub/marcc-hpc/neurodocker-afni/latest/2021-04-09-b729ea12-3eace911/Singularity
collection: marcc-hpc/neurodocker-afni
---

# marcc-hpc/neurodocker-afni:latest

```bash
$ singularity pull shub://marcc-hpc/neurodocker-afni:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
Registry: index.docker.io
From: neurodocker-afni
Namespace: marcchpc

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
  mkdir /scratch /data /work-zfs

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/neurodocker-afni](https://github.com/marcc-hpc/neurodocker-afni)
 - License: [MIT License](https://api.github.com/licenses/mit)

