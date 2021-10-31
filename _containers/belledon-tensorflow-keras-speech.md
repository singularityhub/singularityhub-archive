---
id: 1811
name: "belledon/tensorflow-keras"
branch: "master"
tag: "speech"
commit: "2ce903844952cc36124e12d571b589cdaef69a7c"
version: "57bd279d82c600a770809c6e5bf85129"
build_date: "2020-09-10T03:23:37.982Z"
size_mb: 3323
size: 1601314847
sif: "https://datasets.datalad.org/shub/belledon/tensorflow-keras/speech/2020-09-10-2ce90384-57bd279d/57bd279d82c600a770809c6e5bf85129.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/tensorflow-keras/speech/2020-09-10-2ce90384-57bd279d/
recipe: https://datasets.datalad.org/shub/belledon/tensorflow-keras/speech/2020-09-10-2ce90384-57bd279d/Singularity
collection: belledon/tensorflow-keras
---

# belledon/tensorflow-keras:speech

```bash
$ singularity pull shub://belledon/tensorflow-keras:speech
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.3.0-gpu-py3

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y git wget python3-dev python3-pip sox
    apt-get clean

    apt-get install -y libcupti-dev
    pip3 install --upgrade pip
    pip3 install  keras \
                  lxml \
                  joblib \
                  h5py \
                  python_speech_features \
                  sox
```

## Collection

 - Name: [belledon/tensorflow-keras](https://github.com/belledon/tensorflow-keras)
 - License: None

