---
id: 10144
name: "kirsho/ngs2"
branch: "master"
tag: "latest"
commit: "648418e89d82ac8377d10a349ebecc7cda434242"
version: "6200bce88420eb1f7039e72b10f8b63a"
build_date: "2019-07-02T03:52:33.359Z"
size_mb: 3173
size: 1294979103
sif: "https://datasets.datalad.org/shub/kirsho/ngs2/latest/2019-07-02-648418e8-6200bce8/6200bce88420eb1f7039e72b10f8b63a.simg"
url: https://datasets.datalad.org/shub/kirsho/ngs2/latest/2019-07-02-648418e8-6200bce8/
recipe: https://datasets.datalad.org/shub/kirsho/ngs2/latest/2019-07-02-648418e8-6200bce8/Singularity
collection: kirsho/ngs2
---

# kirsho/ngs2:latest

```bash
$ singularity pull shub://kirsho/ngs2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3


%files
    ngs2.yml

%environment
    PATH=/opt/conda/envs/$(head -1  ngs2.yml | cut -d' ' -f2)/bin:$PATH				# Change $PATH

%post
    echo "Creating a Singularity Container of my ngs2 Conda Env"				# What I'm doing
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc   					# enable conda for the current 
    echo "conda activate $(head -1  ngs2.yml | cut -d' ' -f2)" >> ~/.bashrc			# will start "ngs2" conda env 
    apt-get update && apt-get -y install nano tree htop wget build-essential			# Install 
    /opt/conda/bin/conda update -n base -c defaults conda					# Update Conda
    /opt/conda/bin/conda env create -f ngs2.yml							# Conda create my env

%runscript
    exec "$@"

%labels
    Maintainer olivier.kirsh@u-paris.fr								# Merci qui?
    Version v1.0 20190701
```

## Collection

 - Name: [kirsho/ngs2](https://github.com/kirsho/ngs2)
 - License: None

