---
id: 2749
name: "bbrito/singularity_images"
branch: "master"
tag: "1.9"
commit: "a869d53ba2a5e17130e78c356d630886aa5d6e89"
version: "11f135965edd200f6bb598154e28cf0d"
build_date: "2018-05-10T14:15:21.605Z"
size_mb: 7046
size: 2097410079
sif: "https://datasets.datalad.org/shub/bbrito/singularity_images/1.9/2018-05-10-a869d53b-11f13596/11f135965edd200f6bb598154e28cf0d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bbrito/singularity_images/1.9/2018-05-10-a869d53b-11f13596/
recipe: https://datasets.datalad.org/shub/bbrito/singularity_images/1.9/2018-05-10-a869d53b-11f13596/Singularity
collection: bbrito/singularity_images
---

# bbrito/singularity_images:1.9

```bash
$ singularity pull shub://bbrito/singularity_images:1.9
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: bbrito/singularity_images:1.8


%post
    echo "Hello from inside the container"
    mkdir -p /home/bdebrito_sing
    apt-get update
    apt-get install -y \
        python-wstool \
        ssh
        
    cd /home/bdebrito_sing
    wstool init .
    wstool merge https://raw.githubusercontent.com/bbrito/social-lstm-tf/master/social_lstm.rosinstall
    wstool update

%runscript
    echo "This is what happens when you run the container..."
```

## Collection

 - Name: [bbrito/singularity_images](https://github.com/bbrito/singularity_images)
 - License: None

