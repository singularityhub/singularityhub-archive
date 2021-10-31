---
id: 15816
name: "hariszaf/darn"
branch: "main"
tag: "latest"
commit: "f006e99b3ecd267ea69b4d5539dc7561d5d1de82"
version: "e73c678f47bfec96b98f7cf5fe715110"
build_date: "2021-03-29T01:34:04.398Z"
size_mb: 2053.0
size: 979054623
sif: "https://datasets.datalad.org/shub/hariszaf/darn/latest/2021-03-29-f006e99b-e73c678f/e73c678f47bfec96b98f7cf5fe715110.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/hariszaf/darn/latest/2021-03-29-f006e99b-e73c678f/
recipe: https://datasets.datalad.org/shub/hariszaf/darn/latest/2021-03-29-f006e99b-e73c678f/Singularity
collection: hariszaf/darn
---

# hariszaf/darn:latest

```bash
$ singularity pull shub://hariszaf/darn:latest
```

## Singularity Recipe

```singularity
# Set base image
Bootstrap: docker
From: hariszaf/darn:latest

# Set the maintainer
%labels
   Maintainer Haris Zafeiropoulos

# Set Singularity environment
%post
   export WORKDIR="/home"
   echo "export WORKDIR=$WORKDIR" >> $SINGULARITY_ENVIRONMENT
   mkdir -p $WORKDIR
   echo "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" >> $SINGULARITY_ENVIRONMENT 

# Set basecommnad; run PEMA analysis
%runscript
   bash /home/darn.sh "$@"

# Singularity container complete
```

## Collection

 - Name: [hariszaf/darn](https://github.com/hariszaf/darn)
 - License: None

