---
id: 15150
name: "Gresliebear/test_example_singularity_hub"
branch: "main"
tag: "tag_name"
commit: "fd7106ff4b9c21296e5abe7ec1c3c7b0012325ef"
version: "fa66c81055ec1848d9e3ca34de768ddf5ccfb87a7722da09368099a0fdd06fb9"
build_date: "2020-12-20T03:41:53.492Z"
size_mb: 2029.96484375
size: 2128572416
sif: "https://datasets.datalad.org/shub/Gresliebear/test_example_singularity_hub/tag_name/2020-12-20-fd7106ff-fa66c810/fa66c81055ec1848d9e3ca34de768ddf5ccfb87a7722da09368099a0fdd06fb9.sif"
url: https://datasets.datalad.org/shub/Gresliebear/test_example_singularity_hub/tag_name/2020-12-20-fd7106ff-fa66c810/
recipe: https://datasets.datalad.org/shub/Gresliebear/test_example_singularity_hub/tag_name/2020-12-20-fd7106ff-fa66c810/Singularity
collection: Gresliebear/test_example_singularity_hub
---

# Gresliebear/test_example_singularity_hub:tag_name

```bash
$ singularity pull shub://Gresliebear/test_example_singularity_hub:tag_name
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Author: Leslie M. Wubbel
    Maintainer: Leslie M. Wubbel
    Version: v0.0.1
    
%post
    apt-get update -y
    apt-get install wget -y
    apt-get install git -y

       ## Basic installations 
    apt-get update -y
    apt install software-properties-common -y 
    apt-add-repository universe -y
    apt install python3.7 -y

    apt-get install python3-pip -y
    pip3 install --upgrade pip 
    pip3 install --upgrade setuptools
    pip3 install wheel
    pip3 install scikit-learn
    pip3 install opencv-python
    pip3 install absl-py==0.9.0
    pip3 install appdirs==1.4.4
    pip3 install attrs==19.3.0
    pip3 install black==19.10b0
    pip3 install cachetools==4.1.1
    pip3 install certifi==2020.6.20
    pip3 install chardet==3.0.4
    pip3 install click==7.1.2
    pip3 install coverage==5.2.1
    pip3 install cycler==0.10.0
    pip3 install decorator==4.4.2
    pip3 install dill==0.3.2
    pip3 install filelock==3.0.12
    pip3 install flake8==3.8.3
    pip3 install flake8-bugbear==20.1.4
    pip3 install flake8-comprehensions==3.2.3
    pip3 install flake8-executable==2.0.3
    pip3 install flake8-polyfill==1.0.2
    pip3 install flake8-pyi==20.5.0
    pip3 install future==0.18.2
    pip3 install gdown==3.12.0
    pip3 install google-auth==1.20.1
    pip3 install google-auth-oauthlib==0.4.1
    pip3 install grpcio==1.31.0
    pip3 install h5py==2.10.0
    pip3 install idna==2.10
    pip3 install imageio==2.9.0
    pip3 install importlab==0.5.1
    pip3 install importlib-metadata==1.7.0
    pip3 install isort==5.3.2
    pip3 install joblib==0.16.0
    pip3 install kiwisolver==1.2.0
    pip3 install Markdown==3.2.2
    pip3 install matplotlib==3.3.0
    pip3 install mccabe==0.6.1
    pip3 install meshio==4.0.16
    pip3 install monai==0.2.0
    pip3 install mypy==0.782
    pip3 install mypy-extensions==0.4.3
    pip3 install networkx==2.4
    pip3 install nibabel==3.1.1
    pip3 install ninja==1.10.0.post1
    pip3 install numpy==1.19.1
```

## Collection

 - Name: [Gresliebear/test_example_singularity_hub](https://github.com/Gresliebear/test_example_singularity_hub)
 - License: None

