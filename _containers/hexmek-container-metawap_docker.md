---
id: 15903
name: "hexmek/container"
branch: "master"
tag: "metawap_docker"
commit: "5ae21ec240f9a753af23f945582705fdd1c5bc59"
version: "c92bed2e10dfdb8a8e2df41aba49ac18ed9c54f8f7179faf4a937fdd0b2e5f49"
build_date: "2021-04-15T08:45:34.895Z"
size_mb: 1279.08984375
size: 1341222912
sif: "https://datasets.datalad.org/shub/hexmek/container/metawap_docker/2021-04-15-5ae21ec2-c92bed2e/c92bed2e10dfdb8a8e2df41aba49ac18ed9c54f8f7179faf4a937fdd0b2e5f49.sif"
url: https://datasets.datalad.org/shub/hexmek/container/metawap_docker/2021-04-15-5ae21ec2-c92bed2e/
recipe: https://datasets.datalad.org/shub/hexmek/container/metawap_docker/2021-04-15-5ae21ec2-c92bed2e/Singularity
collection: hexmek/container
---

# hexmek/container:metawap_docker

```bash
$ singularity pull shub://hexmek/container:metawap_docker
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/biocontainers/metawrap:1.2--hdfd78af_2 


%post
    CONFFILE=$(which config-metawrap)
    echo """# Paths to custon pipelines and scripts of metaWRAP
SOFT=/usr/local/bin/metawrap-scripts
PIPES=/usr/local/bin/metawrap-modules

# OPTIONAL databases (see 'Databases' section of metaWRAP README for details)
# path to kraken standard database
KRAKEN_DB=/path/to/database

# path to indexed human genome (see metaWRAP website for guide). This includes files hg38.bitmask and hg38.srprism.*
BMTAGGER_DB=/hps/research/finn/saary/database/metawrap/bmtagger

# paths to BLAST databases
BLASTDB=/path/to/database/NCBI_nt
TAXDUMP=/hps/research/finn/saary/database/metawrap/NCBI_tax""" > $CONFFILE

%environment
    export LC_ALL=C
```

## Collection

 - Name: [hexmek/container](https://github.com/hexmek/container)
 - License: None

