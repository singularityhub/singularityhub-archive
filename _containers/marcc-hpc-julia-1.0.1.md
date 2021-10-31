---
id: 5500
name: "marcc-hpc/julia"
branch: "master"
tag: "1.0.1"
commit: "8ba703f5eb359889b89d69b13e547875b80c3a28"
version: "ef81cd189c39c79464fa517d6d9d93b2"
build_date: "2018-11-07T13:35:05.785Z"
size_mb: 550
size: 186642463
sif: "https://datasets.datalad.org/shub/marcc-hpc/julia/1.0.1/2018-11-07-8ba703f5-ef81cd18/ef81cd189c39c79464fa517d6d9d93b2.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/julia/1.0.1/2018-11-07-8ba703f5-ef81cd18/
recipe: https://datasets.datalad.org/shub/marcc-hpc/julia/1.0.1/2018-11-07-8ba703f5-ef81cd18/Singularity
collection: marcc-hpc/julia
---

# marcc-hpc/julia:1.0.1

```bash
$ singularity pull shub://marcc-hpc/julia:1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: library/julia:1.0.1

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

