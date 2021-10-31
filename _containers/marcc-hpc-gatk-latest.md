---
id: 1299
name: "marcc-hpc/gatk"
branch: "4.0.0"
tag: "latest"
commit: "62b0fdf8e558960687f42b47475f7d75be63bf7b"
version: "1abacda4cb0339fb4a217218c80e4748"
build_date: "2021-03-15T08:55:38.125Z"
size_mb: 5016
size: 2487083039
sif: "https://datasets.datalad.org/shub/marcc-hpc/gatk/latest/2021-03-15-62b0fdf8-1abacda4/1abacda4cb0339fb4a217218c80e4748.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/gatk/latest/2021-03-15-62b0fdf8-1abacda4/
recipe: https://datasets.datalad.org/shub/marcc-hpc/gatk/latest/2021-03-15-62b0fdf8-1abacda4/Singularity
collection: marcc-hpc/gatk
---

# marcc-hpc/gatk:latest

```bash
$ singularity pull shub://marcc-hpc/gatk:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: broadinstitute/gatk
IncludeCmd: yes

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir -p /scratch /data 

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/gatk](https://github.com/marcc-hpc/gatk)
 - License: [MIT License](https://api.github.com/licenses/mit)

