---
id: 6070
name: "jcreinhold/NiftiSynth.jl"
branch: "master"
tag: "latest"
commit: "c6e0c86b1073398a46153e0ce4e999d2a822f458"
version: "f6666b257d1df2deccc1f121743f66b0"
build_date: "2018-12-29T03:55:59.450Z"
size_mb: 579
size: 196526111
sif: "https://datasets.datalad.org/shub/jcreinhold/NiftiSynth.jl/latest/2018-12-29-c6e0c86b-f6666b25/f6666b257d1df2deccc1f121743f66b0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jcreinhold/NiftiSynth.jl/latest/2018-12-29-c6e0c86b-f6666b25/
recipe: https://datasets.datalad.org/shub/jcreinhold/NiftiSynth.jl/latest/2018-12-29-c6e0c86b-f6666b25/Singularity
collection: jcreinhold/NiftiSynth.jl
---

# jcreinhold/NiftiSynth.jl:latest

```bash
$ singularity pull shub://jcreinhold/NiftiSynth.jl:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: library/julia:1.0.3

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
  apt-get install -y zlib1g-dev
  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command
  exec /usr/local/julia/bin/julia  "$@"

%test
  # test that script is a success
```

## Collection

 - Name: [jcreinhold/NiftiSynth.jl](https://github.com/jcreinhold/NiftiSynth.jl)
 - License: None

