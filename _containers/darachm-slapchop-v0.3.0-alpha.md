---
id: 8424
name: "darachm/slapchop"
branch: "master"
tag: "v0.3.0-alpha"
commit: "529d60e121e8bdac5b086554ab88b392c654c7b8"
version: "ae8906aa994f44df21e92c490f10eac0"
build_date: "2019-12-27T03:43:55.192Z"
size_mb: 608
size: 240873503
sif: "https://datasets.datalad.org/shub/darachm/slapchop/v0.3.0-alpha/2019-12-27-529d60e1-ae8906aa/ae8906aa994f44df21e92c490f10eac0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/darachm/slapchop/v0.3.0-alpha/2019-12-27-529d60e1-ae8906aa/
recipe: https://datasets.datalad.org/shub/darachm/slapchop/v0.3.0-alpha/2019-12-27-529d60e1-ae8906aa/Singularity
collection: darachm/slapchop
---

# darachm/slapchop:v0.3.0-alpha

```bash
$ singularity pull shub://darachm/slapchop:v0.3.0-alpha
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
MAINTAINER darachm

%help

    This container just has 'slapchop.py' and dependencies in it.
    The 'runscript' is just running that script in python3.
    
    For options, do:

        singularity run this-container-name -h

    To run it, do something like:

        singularity exec shub://darachm/slapchop:latest \
            exec python3 /slapchop.py \
            data/raw.fastq output-basename \
            --processes 3 \
            -o "Sample:  input   > (?P<sample>[ATCG]{5})(?P<fixed1>GTCCACGAGGTC){e<=1}(?P<rest>TCT.*){e<=1}" \
            -o "Strain:  rest    > (?P<tag>TCT){e<=1}(?P<strain>[ATCG]{10,26})CGTACGCTGCAGGTCGAC" \
            -o "UMITail: rest    > (?P<fixed2>CGTACGCTGCAGGTC)(?<UMItail>GAC[ATCG]G[ATCG]A[ATCG]G[ATCG]G[ATCG]G[ATCG]GAT){s<=2}" \
            -o "UMI:     UMItail > (GAC(?P<umi1>[ATCG])G(?<umi2>[ATCG])A(?<umi3>[ATCG])G(?<umi4>[ATCG])G(?<umi5>[ATCG])G(?<umi6>[ATCG])G){e<=2}" \
            --output-seq "sample+spacer+strain" \
            --output-id "input.id+'_umi='+umi1.seq+umi2.seq+umi3.seq+ \
                umi4.seq+umi5.seq+umi6.seq+'_sample='+sample.seq" \
            --filter "sample_length == 5 and rest_start >= 16" \
            --verbose --verbose

%runscript

    exec /usr/bin/python3 /slapchop.py "$@"

%files

    slapchop.py

%post

    apt-get -y update
    apt-get -y install apt-utils
    apt-get -y install python3 python3-biopython python3-pip

    pip3 install regex==2019.02.18

%test

    /usr/bin/python3 /slapchop.py -h
```

## Collection

 - Name: [darachm/slapchop](https://github.com/darachm/slapchop)
 - License: [BSD 2-Clause "Simplified" License](https://api.github.com/licenses/bsd-2-clause)

