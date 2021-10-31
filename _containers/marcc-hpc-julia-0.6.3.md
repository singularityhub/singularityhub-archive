---
id: 3419
name: "marcc-hpc/julia"
branch: "master"
tag: "0.6.3"
commit: "3dfcadfe683537fd5b0fce38f632f846875fc8f5"
version: "925a080f3157fd24bc2f0ead2e71adc4"
build_date: "2018-07-10T16:54:21.178Z"
size_mb: 465
size: 167043103
sif: "https://datasets.datalad.org/shub/marcc-hpc/julia/0.6.3/2018-07-10-3dfcadfe-925a080f/925a080f3157fd24bc2f0ead2e71adc4.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/julia/0.6.3/2018-07-10-3dfcadfe-925a080f/
recipe: https://datasets.datalad.org/shub/marcc-hpc/julia/0.6.3/2018-07-10-3dfcadfe-925a080f/Singularity
collection: marcc-hpc/julia
---

# marcc-hpc/julia:0.6.3

```bash
$ singularity pull shub://marcc-hpc/julia:0.6.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: library/julia:0.6.3

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

