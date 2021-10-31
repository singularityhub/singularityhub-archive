---
id: 7444
name: "antoniomagnani/tensorflow"
branch: "master"
tag: "1.8.0-gpu"
commit: "9cbd82b4b509311a0de5ba80f3da961a8d25699b"
version: "e1ac866030647d8279433bbdcd9ec0c7"
build_date: "2019-02-25T20:22:55.953Z"
size_mb: 2598
size: 1176944671
sif: "https://datasets.datalad.org/shub/antoniomagnani/tensorflow/1.8.0-gpu/2019-02-25-9cbd82b4-e1ac8660/e1ac866030647d8279433bbdcd9ec0c7.simg"
url: https://datasets.datalad.org/shub/antoniomagnani/tensorflow/1.8.0-gpu/2019-02-25-9cbd82b4-e1ac8660/
recipe: https://datasets.datalad.org/shub/antoniomagnani/tensorflow/1.8.0-gpu/2019-02-25-9cbd82b4-e1ac8660/Singularity
collection: antoniomagnani/tensorflow
---

# antoniomagnani/tensorflow:1.8.0-gpu

```bash
$ singularity pull shub://antoniomagnani/tensorflow:1.8.0-gpu
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

