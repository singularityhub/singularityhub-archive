---
id: 14476
name: "zhinoos/TestWebinar"
branch: "master"
tag: "latest"
commit: "d9bb7f6994d81c9fabe9176be0b29ac3a9aeb4aa"
version: "b490cd22bc020d783ae8eb1858cdf0064151a37ac4a69dac0ee8d238a86a7036"
build_date: "2021-02-08T08:43:13.553Z"
size_mb: 314.734375
size: 330022912
sif: "https://datasets.datalad.org/shub/zhinoos/TestWebinar/latest/2021-02-08-d9bb7f69-b490cd22/b490cd22bc020d783ae8eb1858cdf0064151a37ac4a69dac0ee8d238a86a7036.sif"
url: https://datasets.datalad.org/shub/zhinoos/TestWebinar/latest/2021-02-08-d9bb7f69-b490cd22/
recipe: https://datasets.datalad.org/shub/zhinoos/TestWebinar/latest/2021-02-08-d9bb7f69-b490cd22/Singularity
collection: zhinoos/TestWebinar
---

# zhinoos/TestWebinar:latest

```bash
$ singularity pull shub://zhinoos/TestWebinar:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
	CREATER Shengg
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

 - Name: [zhinoos/TestWebinar](https://github.com/zhinoos/TestWebinar)
 - License: None

