---
id: 5482
name: "nelsonihc/singularity"
branch: "master"
tag: "nightly"
commit: "77e6b0804a2f01c142633e2bec448226f6449d23"
version: "4ffe96eadc354b931bb96a78b325f76f"
build_date: "2018-11-15T01:37:41.740Z"
size_mb: 7514
size: 3728261151
sif: "https://datasets.datalad.org/shub/nelsonihc/singularity/nightly/2018-11-15-77e6b080-4ffe96ea/4ffe96eadc354b931bb96a78b325f76f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nelsonihc/singularity/nightly/2018-11-15-77e6b080-4ffe96ea/
recipe: https://datasets.datalad.org/shub/nelsonihc/singularity/nightly/2018-11-15-77e6b080-4ffe96ea/Singularity
collection: nelsonihc/singularity
---

# nelsonihc/singularity:nightly

```bash
$ singularity pull shub://nelsonihc/singularity:nightly
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nelsonihc/singularity:base1804

%environment

%post
    . /opt/conda/etc/profile.d/conda.sh
    conda activate

    conda install -y pytorch-nightly cuda92 -c pytorch

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

