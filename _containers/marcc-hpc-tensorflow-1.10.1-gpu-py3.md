---
id: 4738
name: "marcc-hpc/tensorflow"
branch: "1.10.1-gpu-py3"
tag: "1.10.1-gpu-py3"
commit: "540f93135c8ea030c806a3a69fd060abdd103b2f"
version: "58fdf2a39756797243f8c77322db8016"
build_date: "2019-07-16T15:58:19.955Z"
size_mb: 3214
size: 1558552607
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.1-gpu-py3/2019-07-16-540f9313-58fdf2a3/58fdf2a39756797243f8c77322db8016.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.1-gpu-py3/2019-07-16-540f9313-58fdf2a3/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.1-gpu-py3/2019-07-16-540f9313-58fdf2a3/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.10.1-gpu-py3

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.10.1-gpu-py3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.10.1-gpu-py3

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

