---
id: 4006
name: "mwiens91/saltant-working-example"
branch: "master"
tag: "latest"
commit: "ee2ad3efe53cd579c8c1a85612d3f68696ab0eea"
version: "ede0dc46de8824a7c46a24ffabd6472b"
build_date: "2018-08-16T01:30:06.916Z"
size_mb: 740
size: 373813279
sif: "https://datasets.datalad.org/shub/mwiens91/saltant-working-example/latest/2018-08-16-ee2ad3ef-ede0dc46/ede0dc46de8824a7c46a24ffabd6472b.simg"
url: https://datasets.datalad.org/shub/mwiens91/saltant-working-example/latest/2018-08-16-ee2ad3ef-ede0dc46/
recipe: https://datasets.datalad.org/shub/mwiens91/saltant-working-example/latest/2018-08-16-ee2ad3ef-ede0dc46/Singularity
collection: mwiens91/saltant-working-example
---

# mwiens91/saltant-working-example:latest

```bash
$ singularity pull shub://mwiens91/saltant-working-example:latest
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

 - Name: [mwiens91/saltant-working-example](https://github.com/mwiens91/saltant-working-example)
 - License: None

