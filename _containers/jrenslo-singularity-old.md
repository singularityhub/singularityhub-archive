---
id: 5594
name: "jrenslo/singularity"
branch: "master"
tag: "old"
commit: "7689d6e4675b556c9aa021f0fd8a9ecf3c673724"
version: "f3a7065dfb14b44be1054074bb7635d7"
build_date: "2018-11-15T18:46:13.817Z"
size_mb: 3280
size: 1668345887
sif: "https://datasets.datalad.org/shub/jrenslo/singularity/old/2018-11-15-7689d6e4-f3a7065d/f3a7065dfb14b44be1054074bb7635d7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jrenslo/singularity/old/2018-11-15-7689d6e4-f3a7065d/
recipe: https://datasets.datalad.org/shub/jrenslo/singularity/old/2018-11-15-7689d6e4-f3a7065d/Singularity
collection: jrenslo/singularity
---

# jrenslo/singularity:old

```bash
$ singularity pull shub://jrenslo/singularity:old
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
Maintainer jrenslo

%environment
alias pip=pip3
alias python=python3

%runscript
exec /bin/bash $@  # runs whichever arguments given to the script

%post
apt-get update
apt-get -y install gcc wget clang python3 vim python-dev python-pip python-tk git
git clone http://github.com/jrenslo/singularity repo
echo `which pip`
echo `which python`
cd repo
echo "Installing pip now"
#pip install --upgrade pip
pip install -r requirements.txt
python setup_script.py
python -m spacy download en_core_web_lg

#for tensorflow
#apt-get install pkg-config zip g++ zlibg-dev unzip
#wget https://github.com/bazelbuild/bazel/releases/download/0.18.1/bazel-0.18.1-installer-linux-x86_64.sh
#chmod +x bazel-0.18.1-installer-linux-x86_64.sh
#./bazel-0.18.1-installer-linux-x86_64.sh --user
#export PATH="$PATH:$HOME/bin"
#
#pip install -U --user pip six numpy wheel mock
#pip install -U --user keras_applications==1.0.5 --no-deps
#pip install -U --user keras_preprocessing==1.0.3 --no-deps
#git clone https://github.com/tensorflow/tensorflow.git
#cd tensorflow
#git checkout master  # r1.9, r1.10, etc.
## bazel test -c opt -- //tensorflow/... -//tensorflow/compiler/... -//tensorflow/contrib/lite/... # for <r1.12
#bazel test -c opt -- //tensorflow/... -//tensorflow/compiler/... -//tensorflow/lite/...
#./configure --config=monolithic
#bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
#./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
#pip install /tmp/tensorflow_pkg/tensorflow-version-tags.whl
```

## Collection

 - Name: [jrenslo/singularity](https://github.com/jrenslo/singularity)
 - License: None

