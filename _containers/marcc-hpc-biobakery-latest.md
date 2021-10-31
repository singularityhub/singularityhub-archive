---
id: 1703
name: "marcc-hpc/biobakery"
branch: "master"
tag: "latest"
commit: "ee378bf54c65fe544337315ecf1bcf78270f020b"
version: "ad88ff07845498ebb23df92d8398b393"
build_date: "2020-02-12T17:15:52.753Z"
size_mb: 11265
size: 5572186143
sif: "https://datasets.datalad.org/shub/marcc-hpc/biobakery/latest/2020-02-12-ee378bf5-ad88ff07/ad88ff07845498ebb23df92d8398b393.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/biobakery/latest/2020-02-12-ee378bf5-ad88ff07/
recipe: https://datasets.datalad.org/shub/marcc-hpc/biobakery/latest/2020-02-12-ee378bf5-ad88ff07/Singularity
collection: marcc-hpc/biobakery
---

# marcc-hpc/biobakery:latest

```bash
$ singularity pull shub://marcc-hpc/biobakery:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: biobakery/biobakery:latest

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
  mkdir /scratch /data 

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/biobakery](https://github.com/marcc-hpc/biobakery)
 - License: [MIT License](https://api.github.com/licenses/mit)

