---
id: 7831
name: "elimoss/metagenomics_workflows"
branch: "master"
tag: "quickmerge"
commit: "881308b293350e84dd6db27fd3f250a7c812f4cd"
version: "629832687e24e9d46ae97bb96437068a"
build_date: "2019-03-19T05:26:45.228Z"
size_mb: 966
size: 396791839
sif: "https://datasets.datalad.org/shub/elimoss/metagenomics_workflows/quickmerge/2019-03-19-881308b2-62983268/629832687e24e9d46ae97bb96437068a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/elimoss/metagenomics_workflows/quickmerge/2019-03-19-881308b2-62983268/
recipe: https://datasets.datalad.org/shub/elimoss/metagenomics_workflows/quickmerge/2019-03-19-881308b2-62983268/Singularity
collection: elimoss/metagenomics_workflows
---

# elimoss/metagenomics_workflows:quickmerge

```bash
$ singularity pull shub://elimoss/metagenomics_workflows:quickmerge
```

## Singularity Recipe

```singularity
# Metagenomics Singularity environment definition for long read workflow
# Eli Moss
# elimoss@stanford.edu
# January 2019

# build this environment with `sudo singularity build bhatt_meta_singularity.img bhatt_meta_singularity.def`
# for development, build with sudo singularity build --sandbox bhatt_meta_singularity bhatt_meta_singularity.def,
# and then modify with sudo singularity shell --writable bhatt_meta_singularity/
# When complete, use sudo singularity build bhatt_meta.simg bhatt_meta_singularity/

# This environment is used in practice by adding --with-singularity shub://elimoss/metagenomics_workflows:longread
# to the snakemake command.

bootstrap: docker
from: ubuntu:19.04

# this command assumes at least singularity 2.3
%environment
    PATH="/usr/local/anaconda/bin:$PATH"
		PATH="/usr/bin/quickmerge/:$PATH"
		PATH="/usr/local/anaconda/bin:$PATH"
%post
    apt-get update
    apt-get install -y eatmydata
    eatmydata apt-get install -y wget bzip2 \
      ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
      git bc rsync zlib1g-dev libbz2-dev liblzma-dev autoconf
    apt-get clean

    apt-get install -y build-essential

   #install quickmerge
   wget https://github.com/mahulchak/quickmerge/archive/v0.2.tar.gz
   tar -zxf v0.2.tar.gz
	 mv quickmerge-0.2/ quickmerge
	 cd quickmerge/
   bash make_merger.sh
	 ln -s merger/quickmerge
	 (echo '#!/usr/bin/env python'; sed '1d' merge_wrapper.py ) > tmp
	 mv tmp merge_wrapper.py
	 chmod a+x merge_wrapper.py
	 cd ..
	 mv quickmerge /usr/bin/



    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
		export PATH="/usr/local/anaconda/bin:$PATH"

		conda install -c bioconda mummer
```

## Collection

 - Name: [elimoss/metagenomics_workflows](https://github.com/elimoss/metagenomics_workflows)
 - License: None

