---
id: 1916
name: "marcc-hpc/tensorflow"
branch: "1.4.0-gpu-py3"
tag: "1.4.0-gpu-py3"
commit: "1519407453591e441fa7bbe13c02cd141685098f"
version: "8a600f55a8890a35e59ce158a2fb56af"
build_date: "2018-03-02T21:00:30.596Z"
size_mb: 3294
size: 1568882719
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.4.0-gpu-py3/2018-03-02-15194074-8a600f55/8a600f55a8890a35e59ce158a2fb56af.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.4.0-gpu-py3/2018-03-02-15194074-8a600f55/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.4.0-gpu-py3/2018-03-02-15194074-8a600f55/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.4.0-gpu-py3

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.4.0-gpu-py3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.4.0-gpu-py3

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

 - Name: [marcc-hpc/tensorflow](https://github.com/marcc-hpc/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

