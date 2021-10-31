---
id: 14241
name: "ggruszczynski/singularity_recipies"
branch: "master"
tag: "latest"
commit: "32bd16d3ee9e3c1871cdfb50549087f4265da732"
version: "91e7354ff63c9f2472d315f8b0e0b89f"
build_date: "2020-09-10T17:56:43.590Z"
size_mb: 172.0
size: 66048031
sif: "https://datasets.datalad.org/shub/ggruszczynski/singularity_recipies/latest/2020-09-10-32bd16d3-91e7354f/91e7354ff63c9f2472d315f8b0e0b89f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ggruszczynski/singularity_recipies/latest/2020-09-10-32bd16d3-91e7354f/
recipe: https://datasets.datalad.org/shub/ggruszczynski/singularity_recipies/latest/2020-09-10-32bd16d3-91e7354f/Singularity
collection: ggruszczynski/singularity_recipies
---

# ggruszczynski/singularity_recipies:latest

```bash
$ singularity pull shub://ggruszczynski/singularity_recipies:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:20.04

%labels
MAINTAINER Vanessasaur
SPECIES Dinosaur

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the image!" 
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
apt update
apt-get install -y vim  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [ggruszczynski/singularity_recipies](https://github.com/ggruszczynski/singularity_recipies)
 - License: None

