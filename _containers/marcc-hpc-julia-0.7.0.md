---
id: 3868
name: "marcc-hpc/julia"
branch: "master"
tag: "0.7.0"
commit: "e6e46d6c5359d71b15e52eb69831b174a56be176"
version: "6246a644e085113484d42bf52fdbd6c0"
build_date: "2018-09-04T20:03:29.936Z"
size_mb: 558
size: 188452895
sif: "https://datasets.datalad.org/shub/marcc-hpc/julia/0.7.0/2018-09-04-e6e46d6c-6246a644/6246a644e085113484d42bf52fdbd6c0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/julia/0.7.0/2018-09-04-e6e46d6c-6246a644/
recipe: https://datasets.datalad.org/shub/marcc-hpc/julia/0.7.0/2018-09-04-e6e46d6c-6246a644/Singularity
collection: marcc-hpc/julia
---

# marcc-hpc/julia:0.7.0

```bash
$ singularity pull shub://marcc-hpc/julia:0.7.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: library/julia:0.7.0

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
  
  apt-get update
  
  apt-get install -y libcairo2
  apt-get install -y libfontconfig1
  apt-get install -y libpango1.0-0
  apt-get install -y libglib2.0-0
  apt-get install -y libpng16-16
  apt-get install -y libpixman-1-0
  apt-get install -y gettext
  
  apt-get install -y hdf5-tools
  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command
  exec /usr/local/julia/bin/julia  "$@"

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/julia](https://github.com/marcc-hpc/julia)
 - License: [MIT License](https://api.github.com/licenses/mit)

