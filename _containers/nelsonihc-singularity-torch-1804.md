---
id: 7193
name: "nelsonihc/singularity"
branch: "master"
tag: "torch-1804"
commit: "339db7ad07d1c13c798bc6a9dc4274dfb9733420"
version: "f2c73428ed4515836368c634e5559277"
build_date: "2019-02-13T20:23:56.833Z"
size_mb: 8382
size: 4320624671
sif: "https://datasets.datalad.org/shub/nelsonihc/singularity/torch-1804/2019-02-13-339db7ad-f2c73428/f2c73428ed4515836368c634e5559277.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nelsonihc/singularity/torch-1804/2019-02-13-339db7ad-f2c73428/
recipe: https://datasets.datalad.org/shub/nelsonihc/singularity/torch-1804/2019-02-13-339db7ad-f2c73428/Singularity
collection: nelsonihc/singularity
---

# nelsonihc/singularity:torch-1804

```bash
$ singularity pull shub://nelsonihc/singularity:torch-1804
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nelsonihc/singularity:base1804

%environment

%post
    . /opt/conda/etc/profile.d/conda.sh
    conda activate

    conda install -y pytorch cuda92 -c pytorch

    pip install \
        augmentor \
        PyHamcrest \
        pretrainedmodels \
        PyYAML \
        pycocotools \
        tensorboard \
        tensorboardX \
        tqdm \
        pybind11 \
        cppimport

    ldconfig /usr/local/cuda/lib64/stubs

    cd /tmp && \
    git clone https://github.com/uber/horovod.git && \
    cd horovod && HOROVOD_GPU_ALLREDUCE=NCCL python setup.py install --prefix=/opt/conda && \
    rm -r /tmp/horovod

    cd /tmp && \
    git clone https://github.com/pytorch/ignite.git && \
    cd ignite && python setup.py install --prefix=/opt/conda && \
    rm -r /tmp/ignite

    ldconfig

    # extra pips
```

## Collection

 - Name: [nelsonihc/singularity](https://github.com/nelsonihc/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

