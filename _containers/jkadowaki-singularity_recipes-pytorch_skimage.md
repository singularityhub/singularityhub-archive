---
id: 8732
name: "jkadowaki/singularity_recipes"
branch: "master"
tag: "pytorch_skimage"
commit: "cffc65c54d447f4a79e87d8b3621617479795257"
version: "6c2adff8642a6843d13c72f0161fe692"
build_date: "2019-12-05T11:10:42.105Z"
size_mb: 3567
size: 2344149023
sif: "https://datasets.datalad.org/shub/jkadowaki/singularity_recipes/pytorch_skimage/2019-12-05-cffc65c5-6c2adff8/6c2adff8642a6843d13c72f0161fe692.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jkadowaki/singularity_recipes/pytorch_skimage/2019-12-05-cffc65c5-6c2adff8/
recipe: https://datasets.datalad.org/shub/jkadowaki/singularity_recipes/pytorch_skimage/2019-12-05-cffc65c5-6c2adff8/Singularity
collection: jkadowaki/singularity_recipes
---

# jkadowaki/singularity_recipes:pytorch_skimage

```bash
$ singularity pull shub://jkadowaki/singularity_recipes:pytorch_skimage
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ml4ai/UA-hpc-containers:cuda9_py36

%help
  This recipe builds a singularity container from an Nividia Docker container for the PyTorch neural network framework.

%post
  # in-container bind points for shared filesystems
  mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local
  pip install torch torchvision torchtext
  pip install tqdm scikit-learn
  pip install scikit-image
```

## Collection

 - Name: [jkadowaki/singularity_recipes](https://github.com/jkadowaki/singularity_recipes)
 - License: None

