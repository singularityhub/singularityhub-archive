---
id: 13066
name: "zhinoos/sheng"
branch: "master"
tag: "latest"
commit: "178212b415befa2bf8b0f3fd74191d1c675d09a9"
version: "bce48668b887ccd93889685360401cd5876954aff9038b5dfaf2401eeea7107f"
build_date: "2020-05-22T07:28:35.980Z"
size_mb: 326.6640625
size: 342532096
sif: "https://datasets.datalad.org/shub/zhinoos/sheng/latest/2020-05-22-178212b4-bce48668/bce48668b887ccd93889685360401cd5876954aff9038b5dfaf2401eeea7107f.sif"
url: https://datasets.datalad.org/shub/zhinoos/sheng/latest/2020-05-22-178212b4-bce48668/
recipe: https://datasets.datalad.org/shub/zhinoos/sheng/latest/2020-05-22-178212b4-bce48668/Singularity
collection: zhinoos/sheng
---

# zhinoos/sheng:latest

```bash
$ singularity pull shub://zhinoos/sheng:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
	CREATER Sheng
%post
    # Downloads the latest package lists (important).
    #apt -y install software-properties-common
    #add-apt-repository universe
    apt-get -y update
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    #DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
	apt -y install python3 
	apt install -y python3-pip
	#python3 \
	#python3-distutils \
	#python3 -m pip
        #python3-pip
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    #rm -rf /var/lib/apt/lists/*
    # Install Python modules.
    pip3 install setuptools
    #pip3 install numpy scipy pandas sklearn simplejson glob3 python-csv
    pip3 install numpy scipy pandas sklearn simplejson glob3 
    #apt-get install -y ruby-dev
    #apt-get gem install json
    #pip install simplejson
    #pip3 install -v requests -i https://pypi.python.org/simple/pdb
    #pip3 install numpy sklearn json pdb csv
```

## Collection

 - Name: [zhinoos/sheng](https://github.com/zhinoos/sheng)
 - License: None

