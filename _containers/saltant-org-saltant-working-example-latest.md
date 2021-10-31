---
id: 5190
name: "saltant-org/saltant-working-example"
branch: "master"
tag: "latest"
commit: "362d18c85cbb9bb412892664ee78acfc90742ce2"
version: "ebca4bb346f4e5a25d8ad4a2cec7f527"
build_date: "2018-10-10T10:52:36.958Z"
size_mb: 740
size: 373813279
sif: "https://datasets.datalad.org/shub/saltant-org/saltant-working-example/latest/2018-10-10-362d18c8-ebca4bb3/ebca4bb346f4e5a25d8ad4a2cec7f527.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/saltant-org/saltant-working-example/latest/2018-10-10-362d18c8-ebca4bb3/
recipe: https://datasets.datalad.org/shub/saltant-org/saltant-working-example/latest/2018-10-10-362d18c8-ebca4bb3/Singularity
collection: mwiens91/saltant-working-example
---

# saltant-org/saltant-working-example:latest

```bash
$ singularity pull shub://saltant-org/saltant-working-example:latest
```

## Singularity Recipe

```singularity
# Pull from Ubuntu 16.04 image
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

# Copy over files
%files
    main.py /
    requirements.txt /

%post
    # Create a directory to hold our scripts
    mkdir /app
    mv /main.py /app/
    mv /requirements.txt /app/

    # Make logs and results directories
    mkdir /logs
    mkdir /results

    # Install Python 3.5 and Pip
    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y python3-pip

    # Install Python requirements
    pip3 install -r /app/requirements.txt
```

## Collection

 - Name: [saltant-org/saltant-working-example](https://github.com/saltant-org/saltant-working-example)
 - License: None

