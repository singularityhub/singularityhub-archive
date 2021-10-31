---
id: 15035
name: "TomHarrop/phase-honeybee-vcf"
branch: "master"
tag: "phase_honeybee_vcf_v0.0.2"
commit: "9f96a884d3cacf2c7070239099cb0672d604faed"
version: "5af932d302d204533c8cc9fa6bf828de22d9632f48c2214da922a5e88d83e58e"
build_date: "2020-12-12T05:30:36.187Z"
size_mb: 635.61328125
size: 666488832
sif: "https://datasets.datalad.org/shub/TomHarrop/phase-honeybee-vcf/phase_honeybee_vcf_v0.0.2/2020-12-12-9f96a884-5af932d3/5af932d302d204533c8cc9fa6bf828de22d9632f48c2214da922a5e88d83e58e.sif"
url: https://datasets.datalad.org/shub/TomHarrop/phase-honeybee-vcf/phase_honeybee_vcf_v0.0.2/2020-12-12-9f96a884-5af932d3/
recipe: https://datasets.datalad.org/shub/TomHarrop/phase-honeybee-vcf/phase_honeybee_vcf_v0.0.2/2020-12-12-9f96a884-5af932d3/Singularity
collection: TomHarrop/phase-honeybee-vcf
---

# TomHarrop/phase-honeybee-vcf:phase_honeybee_vcf_v0.0.2

```bash
$ singularity pull shub://TomHarrop/phase-honeybee-vcf:phase_honeybee_vcf_v0.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.8.6-buster

%help
    Container for phase-honeybee-vcf v0.0.2

%labels
    VERSION "phase-honeybee-vcf v0.0.2"
    MAINTAINER "Tom Harrop"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    apt-get update
    apt-get install -y \
        bcftools \
        build-essential \
        libcrypto++-dev \
        minimap2 \
        samtools \
        tabix

    /usr/local/bin/python3 -m pip \
        install --upgrade \
        pip \
        setuptools \
        wheel

    /usr/local/bin/python3 -m pip \
        install \
    	git+https://github.com/whatshap/whatshap@491ec8e

    /usr/local/bin/python3 -m pip \
        install \
        git+git://github.com/tomharrop/phase-honeybee-vcf.git@v0.0.2

%runscript
    exec /usr/local/bin/phase_honeybee_vcf "$@"
```

## Collection

 - Name: [TomHarrop/phase-honeybee-vcf](https://github.com/TomHarrop/phase-honeybee-vcf)
 - License: None

