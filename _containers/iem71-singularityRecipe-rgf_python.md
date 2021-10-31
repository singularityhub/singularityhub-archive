---
id: 9164
name: "iem71/singularityRecipe"
branch: "master"
tag: "rgf_python"
commit: "870053a66a52df908d84c9d509b71f922d0d37b9"
version: "38c360a00bf3c36103744c5f4ffe3513"
build_date: "2019-05-19T19:13:25.835Z"
size_mb: None
size: 394895391
sif: "https://datasets.datalad.org/shub/iem71/singularityRecipe/rgf_python/2019-05-19-870053a6-38c360a0/38c360a00bf3c36103744c5f4ffe3513.simg"
url: https://datasets.datalad.org/shub/iem71/singularityRecipe/rgf_python/2019-05-19-870053a6-38c360a0/
recipe: https://datasets.datalad.org/shub/iem71/singularityRecipe/rgf_python/2019-05-19-870053a6-38c360a0/Singularity
collection: iem71/singularityRecipe
---

# iem71/singularityRecipe:rgf_python

```bash
$ singularity pull shub://iem71/singularityRecipe:rgf_python
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04


%labels
  Maintainer Lampros Mouselimis
  NOTES Based on info of the following web-sites : https://www.sylabs.io/guides/2.5.1/user-guide.pdf, https://github.com/singularityhub/jupyter, https://vsoch.github.io/2016/singularity-web/, https://bwlewis.github.io/r-and-singularity/


%post

  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  
  # to solve the "locale.Error: unsupported locale setting" error [https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting ]
  export LC_ALL=C

  apt-get -y update && apt-get -y upgrade
  apt-get install -y python3 vim wget
  apt-get install -y python3-pip
  pip3 install --upgrade pip==9.0.3                                                                        # do this due to a problem with 'python-pip' ( SEE : https://github.com/pypa/pip/issues/5240#issuecomment-381673100 )
  pip3 install jupyter
  pip3 install -U numpy
  apt-get install -y nano git cmake gfortran g++ curl wget autoconf bzip2 libtool libtool-bin sudo         # "sudo" is not installed by default in containers like docker, singularity
  pip3 install --upgrade setuptools
  pip3 install --upgrade scipy
  pip3 install -U scikit-learn

  sudo pip3 install rgf_python                                                                             # requires "sudo" [ system-wide installation ]

  # clean tmp files
  apt-get autoremove -y
  apt-get clean



%runscript
    
  # command to be executed when the container runs
  echo "The web-browser runs on localhost:8888"
  exec /usr/local/bin/jupyter notebook --allow-root --ip='*' --port=8888 --no-browser
```

## Collection

 - Name: [iem71/singularityRecipe](https://github.com/iem71/singularityRecipe)
 - License: None

