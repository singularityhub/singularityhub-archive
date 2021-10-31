---
id: 2725
name: "marcc-hpc/tensorflow"
branch: "1.8.0-gpu"
tag: "1.8.0-gpu"
commit: "41ed15d51fbd7f5ebad1c722d0e38112f58a6684"
version: "619d1921c9013b433b0efdaed1957756"
build_date: "2020-11-03T07:27:39.626Z"
size_mb: 3073
size: 1411014687
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.8.0-gpu/2020-11-03-41ed15d5-619d1921/619d1921c9013b433b0efdaed1957756.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/tensorflow/1.8.0-gpu/2020-11-03-41ed15d5-619d1921/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.8.0-gpu/2020-11-03-41ed15d5-619d1921/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.8.0-gpu

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.8.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.8.0-gpu

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

  # additional packages
  apt-get update
  apt-get install -y python-tk
  apt-get install -y libsm6 libxext6
  pip install selenium
  pip install moviepy
  pip install lmdb
  pip install opencv-contrib-python
  pip install cryptography

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/tensorflow](https://github.com/marcc-hpc/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

