---
id: 10694
name: "AASHISHAG1/test"
branch: "master"
tag: "kaldi"
commit: "b82805376d9d434fbfa93ee5ea163041546a1037"
version: "47ef5008810c31cfd9e5b26e319ffbc12509bb5aa6f5818fbb8e64af87fb4c86"
build_date: "2021-04-07T17:29:20.584Z"
size_mb: 606.140625
size: 635584512
sif: "https://datasets.datalad.org/shub/AASHISHAG1/test/kaldi/2021-04-07-b8280537-47ef5008/47ef5008810c31cfd9e5b26e319ffbc12509bb5aa6f5818fbb8e64af87fb4c86.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/AASHISHAG1/test/kaldi/2021-04-07-b8280537-47ef5008/
recipe: https://datasets.datalad.org/shub/AASHISHAG1/test/kaldi/2021-04-07-b8280537-47ef5008/Singularity
collection: AASHISHAG1/test
---

# AASHISHAG1/test:kaldi

```bash
$ singularity pull shub://AASHISHAG1/test:kaldi
```

## Singularity Recipe

```rpm
Bootstrap:docker
From:ubuntu:latest

%labels
        MAINTAINER Agarwal-Aashish

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
        apt-get update
		apt-get install -y zlib1g-dev jq automake autoconf unzip sox libtool subversion python2.7 python3  libpcre3 libpcre3-dev gfortran build-essential git zlib1g-dev libtool curl vim python-pip screen gstreamer1.0-plugins-bad gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-pulseaudio gstreamer1.0-plugins-ugly gstreamer1.0-tools libgstreamer1.0-dev libjansson-dev python-gi wget python3-pip libsndfile1 software-properties-common ffmpeg
		pip install --upgrade ws4py==0.3.2 pyyaml tornado soundfile webrtcvad wave
		pip3 install sox python_speech_features pyxdg bs4 six requests tables attrdict setuptools librosa flask wave soundfile flask_cors webrtcvad
		curl -sL https://deb.nodesource.com/setup_12.x | bash -
		apt-get install nodejs
		npm install -g @angular/cli
		npm install @angular/cli --save
		npm install @angular/compiler-cli --save
		npm install --save-dev @angular-devkit/build-angular
		npm install @angular-devkit/core --save-dev
		
%runscript
        echo "Successfully installed the dependencies."
```

## Collection

 - Name: [AASHISHAG1/test](https://github.com/AASHISHAG1/test)
 - License: None

