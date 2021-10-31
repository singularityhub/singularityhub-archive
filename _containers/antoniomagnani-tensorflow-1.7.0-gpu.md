---
id: 7445
name: "antoniomagnani/tensorflow"
branch: "master"
tag: "1.7.0-gpu"
commit: "b6ebe4ed78b7ba95ee5fd8cbb801f182391c54a6"
version: "610593cad945148bebaa924e028ff970"
build_date: "2019-02-25T20:22:55.944Z"
size_mb: 2598
size: 1176948767
sif: "https://datasets.datalad.org/shub/antoniomagnani/tensorflow/1.7.0-gpu/2019-02-25-b6ebe4ed-610593ca/610593cad945148bebaa924e028ff970.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/antoniomagnani/tensorflow/1.7.0-gpu/2019-02-25-b6ebe4ed-610593ca/
recipe: https://datasets.datalad.org/shub/antoniomagnani/tensorflow/1.7.0-gpu/2019-02-25-b6ebe4ed-610593ca/Singularity
collection: antoniomagnani/tensorflow
---

# antoniomagnani/tensorflow:1.7.0-gpu

```bash
$ singularity pull shub://antoniomagnani/tensorflow:1.7.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.7.0-gpu

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

