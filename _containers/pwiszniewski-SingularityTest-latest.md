---
id: 14869
name: "pwiszniewski/SingularityTest"
branch: "master"
tag: "latest"
commit: "36f3993c70f9e1cc85e71469dcfcb01c7e94a552"
version: "d7d3d1e3a5190c73aa44ca631379604c"
build_date: "2020-11-12T16:25:57.410Z"
size_mb: 770.0
size: 331079711
sif: "https://datasets.datalad.org/shub/pwiszniewski/SingularityTest/latest/2020-11-12-36f3993c-d7d3d1e3/d7d3d1e3a5190c73aa44ca631379604c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pwiszniewski/SingularityTest/latest/2020-11-12-36f3993c-d7d3d1e3/
recipe: https://datasets.datalad.org/shub/pwiszniewski/SingularityTest/latest/2020-11-12-36f3993c-d7d3d1e3/Singularity
collection: pwiszniewski/SingularityTest
---

# pwiszniewski/SingularityTest:latest

```bash
$ singularity pull shub://pwiszniewski/SingularityTest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
	CREATER pwiszniewski
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

 - Name: [pwiszniewski/SingularityTest](https://github.com/pwiszniewski/SingularityTest)
 - License: None

