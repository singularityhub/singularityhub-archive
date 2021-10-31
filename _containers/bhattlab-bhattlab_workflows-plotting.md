---
id: 7785
name: "bhattlab/bhattlab_workflows"
branch: "singularity"
tag: "plotting"
commit: "f444516e8a44d456b95313bb1dc95ee23510bbc4"
version: "60baa094086622695b3ac47d0f1814f3"
build_date: "2021-04-14T03:38:36.691Z"
size_mb: 1202
size: 535547935
sif: "https://datasets.datalad.org/shub/bhattlab/bhattlab_workflows/plotting/2021-04-14-f444516e-60baa094/60baa094086622695b3ac47d0f1814f3.simg"
url: https://datasets.datalad.org/shub/bhattlab/bhattlab_workflows/plotting/2021-04-14-f444516e-60baa094/
recipe: https://datasets.datalad.org/shub/bhattlab/bhattlab_workflows/plotting/2021-04-14-f444516e-60baa094/Singularity
collection: bhattlab/bhattlab_workflows
---

# bhattlab/bhattlab_workflows:plotting

```bash
$ singularity pull shub://bhattlab/bhattlab_workflows:plotting
```

## Singularity Recipe

```singularity
# Singularity environment definition for plotting in R
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

		 conda install -y -c conda-forge -c bioconda -c r \
       r r-ggplot2 r-reshape2 r-rcolorbrewer \
			 readline=6.2



			 #add more stuff here if needed for plotting stuff with this container
```

## Collection

 - Name: [bhattlab/bhattlab_workflows](https://github.com/bhattlab/bhattlab_workflows)
 - License: None

