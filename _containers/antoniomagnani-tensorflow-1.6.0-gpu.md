---
id: 7446
name: "antoniomagnani/tensorflow"
branch: "master"
tag: "1.6.0-gpu"
commit: "a2a550085479edbd379368d021c0bdea218a8e27"
version: "a6bc03e8f5ef1ff40c0759eb5b2eab8a"
build_date: "2019-02-25T20:22:55.935Z"
size_mb: 2876
size: 1195618335
sif: "https://datasets.datalad.org/shub/antoniomagnani/tensorflow/1.6.0-gpu/2019-02-25-a2a55008-a6bc03e8/a6bc03e8f5ef1ff40c0759eb5b2eab8a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/antoniomagnani/tensorflow/1.6.0-gpu/2019-02-25-a2a55008-a6bc03e8/
recipe: https://datasets.datalad.org/shub/antoniomagnani/tensorflow/1.6.0-gpu/2019-02-25-a2a55008-a6bc03e8/Singularity
collection: antoniomagnani/tensorflow
---

# antoniomagnani/tensorflow:1.6.0-gpu

```bash
$ singularity pull shub://antoniomagnani/tensorflow:1.6.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.6.0-gpu

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

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [antoniomagnani/tensorflow](https://github.com/antoniomagnani/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

