---
id: 9918
name: "rbrewster727/brewster_pipelines"
branch: "master"
tag: "sgv_finder"
commit: "ae3f8ee3edd751d2b009ca89abdd38db67bca251"
version: "ef2357cf4fc1b64aef854afbe0b8bc2c"
build_date: "2019-06-24T14:48:03.806Z"
size_mb: 2734
size: 1247350815
sif: "https://datasets.datalad.org/shub/rbrewster727/brewster_pipelines/sgv_finder/2019-06-24-ae3f8ee3-ef2357cf/ef2357cf4fc1b64aef854afbe0b8bc2c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rbrewster727/brewster_pipelines/sgv_finder/2019-06-24-ae3f8ee3-ef2357cf/
recipe: https://datasets.datalad.org/shub/rbrewster727/brewster_pipelines/sgv_finder/2019-06-24-ae3f8ee3-ef2357cf/Singularity
collection: rbrewster727/brewster_pipelines
---

# rbrewster727/brewster_pipelines:sgv_finder

```bash
$ singularity pull shub://rbrewster727/brewster_pipelines:sgv_finder
```

## Singularity Recipe

```singularity
# Metagenomics Singularity environment definition for ICRA and SGV Finder
# Ryan Brewster
# rbrewster@stanford.edu
# June 2019

bootstrap: docker
from: ubuntu:19.04

# this command assumes at least singularity 2.3
%environment
		PATH="/usr/local/anaconda/bin:$PATH"

%post
    apt-get update
    apt-get install -y eatmydata
    eatmydata apt-get install -y wget bzip2 \
      ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
      git bc rsync zlib1g-dev libbz2-dev liblzma-dev autoconf
    apt-get clean

    apt-get install -y build-essential

    # Install anaconda

    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
    export PATH="/usr/local/anaconda/bin:$PATH"

	conda install numpy=1.13.3 ujson=1.35 pandas=0.23.4 scipy=1.1.0 bokeh=0.12.6 python=2.7.8 cython
	conda install -c conda-forge biopython=1.68 cxx-compiler

	# Install GEM-Mapper

	wget https://sourceforge.net/projects/gemlibrary/files/gem-library/Binary%20pre-release%203/GEM-binaries-Linux-x86_64-core_i3-20130406-045632.tbz2

	tar -jxvf GEM-binaries-Linux-x86_64-core_i3-20130406-045632.tbz2

	rsync -r GEM-binaries-Linux-x86_64-core_i3-20130406-045632/bin/ /usr/bin/
```

## Collection

 - Name: [rbrewster727/brewster_pipelines](https://github.com/rbrewster727/brewster_pipelines)
 - License: None

