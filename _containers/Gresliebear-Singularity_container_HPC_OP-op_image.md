---
id: 15099
name: "Gresliebear/Singularity_container_HPC_OP"
branch: "main"
tag: "op_image"
commit: "26f11e6521cbfead0bbfedeedde6651723ccd545"
version: "b8f64c23fee168da8773af8e1d56f54930715fccdbc91bd307fce21e9d395657"
build_date: "2021-03-23T20:33:38.039Z"
size_mb: 3222.05859375
size: 3378573312
sif: "https://datasets.datalad.org/shub/Gresliebear/Singularity_container_HPC_OP/op_image/2021-03-23-26f11e65-b8f64c23/b8f64c23fee168da8773af8e1d56f54930715fccdbc91bd307fce21e9d395657.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Gresliebear/Singularity_container_HPC_OP/op_image/2021-03-23-26f11e65-b8f64c23/
recipe: https://datasets.datalad.org/shub/Gresliebear/Singularity_container_HPC_OP/op_image/2021-03-23-26f11e65-b8f64c23/Singularity
collection: Gresliebear/Singularity_container_HPC_OP
---

# Gresliebear/Singularity_container_HPC_OP:op_image

```bash
$ singularity pull shub://Gresliebear/Singularity_container_HPC_OP:op_image
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Author: Leslie M. Wubbel
    Maintainer: Leslie M. Wubbel
    Version: v0.0.0
    
%post
    apt-get update -y
    apt-get install wget -y
    apt-get install git -y
    
    ## Software needed to run OpenCV
    apt-get update -y
    apt install software-properties-common -y 
    apt-add-repository universe -y
    ## Software needed to run OpenCV
    apt install libgl1-mesa-glx libgl1-mesa-dev libdbus-1-3 libdbus-1-dev \
        libnss3 libxcomp3 libxcomposite1 libxcomposite-dev libxcursor1 \
        libxcursor-dev libxi6 libxi-dev libxtst6 libxtst-dev libxt6 \
        libxt-dev libasound2 -y
    apt install python3.7 -y

    ## pip install requirements 
    ##
    ##
    # Initialize environment and update conda
    #export PATH=/usr/local/miniconda/bin:${PATH}
    #export LD_LIBRARY_PATH=/usr/local/miniconda/lib:${LD_LIBRARY_PATH}

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
    pip3 install oauthlib==3.1.0
    pip3 install opencv-python==4.4.0.46
    pip3 install packaging==20.4
    pip3 install pandas==1.1.0
    pip3 install parameterized==0.7.4
    pip3 install pathspec==0.8.0
    pip3 install pep8-naming==0.11.1
    pip3 install Pillow==7.2.0
    pip3 install plotly==4.9.0
    pip3 install protobuf==3.12.4
    pip3 install pyasn1==0.4.8
    pip3 install pyasn1-modules==0.2.8
    pip3 install pycodestyle==2.6.0
    pip3 install pydicom==2.0.0
    pip3 install pyflakes==2.2.0
    pip3 install pyparsing==2.4.7
    pip3 install PySocks==1.7.1
    pip3 install python-dateutil==2.8.1
    pip3 install pytorch-ignite==0.3.0
    pip3 install pytype==2020.8.10
    pip3 install pytz==2020.1
    pip3 install pyvista==0.25.3
    pip3 install PyWavelets==1.1.1
    pip3 install PyYAML==5.3.1
    pip3 install redis==3.5.3
    pip3 install regex==2020.7.14
    pip3 install requests==2.24.0
    pip3 install requests-oauthlib==1.3.0
    pip3 install retrying==1.3.3
    pip3 install rsa==4.6
    pip3 install scikit-image==0.17.2
    pip3 install scikit-learn==0.23.1
    pip3 install scipy==1.5.2
    pip3 install scooby==0.5.6
    pip3 install SimpleITK==2.0.1
    pip3 install six==1.15.0
    pip3 install sklearn==0.0
    pip3 install tensorboard==2.3.0
    pip3 install tensorboard-plugin-wit==1.7.0
    pip3 install threadpoolctl==2.1.0
    pip3 install tifffile==2020.7.24
    pip3 install toml==0.10.1
    pip3 install torch==1.6.0
    pip3 install torchvision==0.7.0
    pip3 install tqdm==4.48.2
    pip3 install typed-ast==1.4.1
    pip3 install typing-extensions==3.7.4.2
    pip3 install urllib3==1.25.10
    pip3 install vtk==8.1.2
    pip3 install Werkzeug==1.0.1
    pip3 install wget==3.2
    pip3 install zipp==3.1.0

%help
    If you run into issues regarding the
    use of this container then please
    contact the ICDS i-ASK center
    at iask@ics.psu.edu
%test
    grep -q NAME=\"Ubuntu\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is Ubuntu as expected."
    else
        echo "Container base is not Ubuntu."
        exit 1
    fi
```

## Collection

 - Name: [Gresliebear/Singularity_container_HPC_OP](https://github.com/Gresliebear/Singularity_container_HPC_OP)
 - License: [MIT License](https://api.github.com/licenses/mit)

