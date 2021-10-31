---
id: 13459
name: "ravi-0841/singularity-tensorflow-spg"
branch: "master"
tag: "latest"
commit: "16112a0480b7f172dda54a04211d2b869abd6e8e"
version: "4b2ad6cdb7701137f8c5c934c6e2a7a0"
build_date: "2021-03-25T04:00:55.492Z"
size_mb: 4522.0
size: 2433589279
sif: "https://datasets.datalad.org/shub/ravi-0841/singularity-tensorflow-spg/latest/2021-03-25-16112a04-4b2ad6cd/4b2ad6cdb7701137f8c5c934c6e2a7a0.sif"
url: https://datasets.datalad.org/shub/ravi-0841/singularity-tensorflow-spg/latest/2021-03-25-16112a04-4b2ad6cd/
recipe: https://datasets.datalad.org/shub/ravi-0841/singularity-tensorflow-spg/latest/2021-03-25-16112a04-4b2ad6cd/Singularity
collection: ravi-0841/singularity-tensorflow-spg
---

# ravi-0841/singularity-tensorflow-spg:latest

```bash
$ singularity pull shub://ravi-0841/singularity-tensorflow-spg:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.14.0-gpu-py3

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
  apt-get install -y libmagic-dev
  apt-get install -y libsndfile1
  pip install opencv-contrib-python
  pip install wrapt==1.12.0
  pip install pyyaml
  pip install joblib==0.11.0
  pip install llvmlite==0.31.0
  pip install numba==0.44.1
  pip install librosa==0.7.0
  pip install pep8==1.7.0
  pip install nose==1.3.7
  pip install hyperopt==0.2.3
  pip install hyperas
  pip install tqdm
  pip install pyAudioAnalysis
  pip install hmmlearn==0.2.3
  pip install simplejson==3.17.0
  pip install eyed3
  pip install pydub
  pip install webrtcvad==2.0.10
  pip install soundfile
  pip install ffmpeg-python
  pip install pyworld
  pip install autograd
  pip install pomegranate==0.12.0
  pip install crepe==0.0.10
  pip install pycwt
  pip install unidecode
  pip install inflect==0.2.5

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [ravi-0841/singularity-tensorflow-spg](https://github.com/ravi-0841/singularity-tensorflow-spg)
 - License: [MIT License](https://api.github.com/licenses/mit)

