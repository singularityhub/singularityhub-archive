---
id: 3665
name: "mlampros/singularity_containers"
branch: "master"
tag: "fuzzywuzzy_python"
commit: "6b047e8f8e520cbdc55cf29b346c1984ec4a1d14"
version: "ecd6f730760a946bb1cb8b8ae19482f7"
build_date: "2018-07-25T23:56:14.665Z"
size_mb: 659
size: 241815583
sif: "https://datasets.datalad.org/shub/mlampros/singularity_containers/fuzzywuzzy_python/2018-07-25-6b047e8f-ecd6f730/ecd6f730760a946bb1cb8b8ae19482f7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mlampros/singularity_containers/fuzzywuzzy_python/2018-07-25-6b047e8f-ecd6f730/
recipe: https://datasets.datalad.org/shub/mlampros/singularity_containers/fuzzywuzzy_python/2018-07-25-6b047e8f-ecd6f730/Singularity
collection: mlampros/singularity_containers
---

# mlampros/singularity_containers:fuzzywuzzy_python

```bash
$ singularity pull shub://mlampros/singularity_containers:fuzzywuzzy_python
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
  pip3 install --upgrade pip==9.0.3                               # do this due to a problem with 'python-pip' ( SEE : https://github.com/pypa/pip/issues/5240#issuecomment-381673100 )
  pip3 install jupyter
  pip3 install numpy
  pip3 install fuzzywuzzy
  pip3 install python-Levenshtein

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

