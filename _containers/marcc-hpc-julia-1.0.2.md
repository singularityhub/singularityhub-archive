---
id: 5753
name: "marcc-hpc/julia"
branch: "master"
tag: "1.0.2"
commit: "5bdbe29c0d35281776355e0c926dd0ce513639ae"
version: "a9e9d6a3a94147eac1474345536d4450"
build_date: "2019-12-13T04:40:43.683Z"
size_mb: 551
size: 187093023
sif: "https://datasets.datalad.org/shub/marcc-hpc/julia/1.0.2/2019-12-13-5bdbe29c-a9e9d6a3/a9e9d6a3a94147eac1474345536d4450.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/julia/1.0.2/2019-12-13-5bdbe29c-a9e9d6a3/
recipe: https://datasets.datalad.org/shub/marcc-hpc/julia/1.0.2/2019-12-13-5bdbe29c-a9e9d6a3/Singularity
collection: marcc-hpc/julia
---

# marcc-hpc/julia:1.0.2

```bash
$ singularity pull shub://marcc-hpc/julia:1.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: library/julia:1.0.2

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

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

