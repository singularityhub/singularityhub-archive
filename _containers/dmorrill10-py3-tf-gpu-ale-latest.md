---
id: 1786
name: "dmorrill10/py3-tf-gpu-ale"
branch: "master"
tag: "latest"
commit: "c8e1090ea47759c8668ad9e6072729dcde12f9b6"
version: "157c0032987bee79bc4bb53a5aadc761"
build_date: "2018-02-22T21:43:25.911Z"
size_mb: 2949
size: 1226223647
sif: "https://datasets.datalad.org/shub/dmorrill10/py3-tf-gpu-ale/latest/2018-02-22-c8e1090e-157c0032/157c0032987bee79bc4bb53a5aadc761.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dmorrill10/py3-tf-gpu-ale/latest/2018-02-22-c8e1090e-157c0032/
recipe: https://datasets.datalad.org/shub/dmorrill10/py3-tf-gpu-ale/latest/2018-02-22-c8e1090e-157c0032/Singularity
collection: dmorrill10/py3-tf-gpu-ale
---

# dmorrill10/py3-tf-gpu-ale:latest

```bash
$ singularity pull shub://dmorrill10/py3-tf-gpu-ale:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.5.0-gpu-py3

%help

To install python libraries after this image is built, create a virtual environment that uses the system packages with `virtualenv --system-site-packages venv && source venv/bin/activate`, then use `pip` as usual.


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
  chmod +x /environment

  # default mount paths
  mkdir -p /scratch /data /usr/bin

  apt-get update
  apt-get install -y cmake libcupti-dev libyaml-dev wget unzip locales
  apt-get clean
  locale-gen en_US.UTF-8

  pip3 install --upgrade pip
  pip3 install numpy tqdm virtualenv

  wget https://github.com/mgbellemare/Arcade-Learning-Environment/archive/v0.6.0.zip
  unzip v0.6.0.zip
  cd Arcade-Learning-Environment-0.6.0
  rm -rf build
  mkdir build
  cd build
  cmake -DUSE_SDL=OFF -DUSE_RLGLUE=OFF -DBUILD_EXAMPLES=OFF ..
  make -j 4

  cd ../
  pip3 install .

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [dmorrill10/py3-tf-gpu-ale](https://github.com/dmorrill10/py3-tf-gpu-ale)
 - License: [MIT License](https://api.github.com/licenses/mit)

