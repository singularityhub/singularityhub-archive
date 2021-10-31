---
id: 8333
name: "ivana-m/singularity_image_recipes"
branch: "master"
tag: "dvs6_py36"
commit: "03b18aa43955434f164034d446188eeff520bab8"
version: "585b0c5f354f81e681da07f89aeff251"
build_date: "2019-04-10T18:24:19.207Z"
size_mb: 1042
size: 344715295
sif: "https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/dvs6_py36/2019-04-10-03b18aa4-585b0c5f/585b0c5f354f81e681da07f89aeff251.simg"
url: https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/dvs6_py36/2019-04-10-03b18aa4-585b0c5f/
recipe: https://datasets.datalad.org/shub/ivana-m/singularity_image_recipes/dvs6_py36/2019-04-10-03b18aa4-585b0c5f/Singularity
collection: ivana-m/singularity_image_recipes
---

# ivana-m/singularity_image_recipes:dvs6_py36

```bash
$ singularity pull shub://ivana-m/singularity_image_recipes:dvs6_py36
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_image_recipes:devtoolset6

%post
   # install python36
   yum install -y https://centos7.iuscommunity.org/ius-release.rpm
   yum update -y
   yum install -y python36u python36u-libs python36u-devel python36u-pip
```

## Collection

 - Name: [ivana-m/singularity_image_recipes](https://github.com/ivana-m/singularity_image_recipes)
 - License: None

