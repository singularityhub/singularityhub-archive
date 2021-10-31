---
id: 7786
name: "bhattlab/bhattlab_workflows"
branch: "singularity"
tag: "align"
commit: "c04c1e48806a0d5de6f8adb6680564923f51b32a"
version: "e2a9f73a872f9eddc5b69ee562f9da4a"
build_date: "2020-01-24T23:05:15.446Z"
size_mb: 731
size: 301707295
sif: "https://datasets.datalad.org/shub/bhattlab/bhattlab_workflows/align/2020-01-24-c04c1e48-e2a9f73a/e2a9f73a872f9eddc5b69ee562f9da4a.simg"
url: https://datasets.datalad.org/shub/bhattlab/bhattlab_workflows/align/2020-01-24-c04c1e48-e2a9f73a/
recipe: https://datasets.datalad.org/shub/bhattlab/bhattlab_workflows/align/2020-01-24-c04c1e48-e2a9f73a/Singularity
collection: bhattlab/bhattlab_workflows
---

# bhattlab/bhattlab_workflows:align

```bash
$ singularity pull shub://bhattlab/bhattlab_workflows:align
```

## Singularity Recipe

```singularity
# Singularity environment definition for aligning and processing reads
# Eli Moss
# elimoss@stanford.edu

bootstrap: docker
from: ubuntu:19.04

# this command assumes at least singularity 2.3
%environment
    PATH="/usr/local/anaconda/bin:$PATH"
%post
    apt-get update
		apt-get install -y wget bzip2 \
      ca-certificates
    apt-get clean

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
		export PATH="/usr/local/anaconda/bin:$PATH"

		conda config --set remote_read_timeout_secs 600


		#install plotting stuff

		 conda install -y -c conda-forge -c bioconda \
		 bwa samtools
```

## Collection

 - Name: [bhattlab/bhattlab_workflows](https://github.com/bhattlab/bhattlab_workflows)
 - License: None

