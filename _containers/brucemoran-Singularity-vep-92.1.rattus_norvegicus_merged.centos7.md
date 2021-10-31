---
id: 7188
name: "brucemoran/Singularity"
branch: "master"
tag: "vep-92.1.rattus_norvegicus_merged.centos7"
commit: "48ec65f9f707842f1dda7e97bb0bcb4b0205d961"
version: "9f70e837016b5e70b5e0175330ed3ae3"
build_date: "2019-02-13T20:23:56.944Z"
size_mb: 2260
size: 1158631455
sif: "https://datasets.datalad.org/shub/brucemoran/Singularity/vep-92.1.rattus_norvegicus_merged.centos7/2019-02-13-48ec65f9-9f70e837/9f70e837016b5e70b5e0175330ed3ae3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/brucemoran/Singularity/vep-92.1.rattus_norvegicus_merged.centos7/2019-02-13-48ec65f9-9f70e837/
recipe: https://datasets.datalad.org/shub/brucemoran/Singularity/vep-92.1.rattus_norvegicus_merged.centos7/2019-02-13-48ec65f9-9f70e837/Singularity
collection: brucemoran/Singularity
---

# brucemoran/Singularity:vep-92.1.rattus_norvegicus_merged.centos7

```bash
$ singularity pull shub://brucemoran/Singularity:vep-92.1.rattus_norvegicus_merged.centos7
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:brucemoran/Singularity:vep-92.1.centos7

%help
    Container for VEP_92.1 rattus_norvegicus_merged cache

%post

    ##install cache
    cd /usr/local/ensembl-vep
    perl ./INSTALL.pl --AUTO ac \
                      --CACHEDIR "/usr/local/ensembl-vep/cache" \
                      --SPECIES "rattus_norvegicus_merged" \
                      --NO_UPDATE \
                      --NO_HTSLIB \
                      --PLUGINS "dbNSFP,RefSeqHGVS"

    ln -s /usr/local/ensembl-vep/* /usr/local/bin/
```

## Collection

 - Name: [brucemoran/Singularity](https://github.com/brucemoran/Singularity)
 - License: None

