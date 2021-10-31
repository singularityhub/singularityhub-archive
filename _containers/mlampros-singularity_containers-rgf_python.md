---
id: 3664
name: "mlampros/singularity_containers"
branch: "master"
tag: "rgf_python"
commit: "6b047e8f8e520cbdc55cf29b346c1984ec4a1d14"
version: "0c359e3a51774f7d5effea8abfa3b919"
build_date: "2020-02-28T16:02:12.777Z"
size_mb: 943
size: 359178271
sif: "https://datasets.datalad.org/shub/mlampros/singularity_containers/rgf_python/2020-02-28-6b047e8f-0c359e3a/0c359e3a51774f7d5effea8abfa3b919.simg"
url: https://datasets.datalad.org/shub/mlampros/singularity_containers/rgf_python/2020-02-28-6b047e8f-0c359e3a/
recipe: https://datasets.datalad.org/shub/mlampros/singularity_containers/rgf_python/2020-02-28-6b047e8f-0c359e3a/Singularity
collection: mlampros/singularity_containers
---

# mlampros/singularity_containers:rgf_python

```bash
$ singularity pull shub://mlampros/singularity_containers:rgf_python
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

 - Name: [mlampros/singularity_containers](https://github.com/mlampros/singularity_containers)
 - License: [Other](None)

