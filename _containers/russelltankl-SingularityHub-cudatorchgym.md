---
id: 8850
name: "russelltankl/SingularityHub"
branch: "master"
tag: "cudatorchgym"
commit: "91ab6aac22ffc4357ebd9131b4986cd718b67904"
version: "f2004efc5767f07a664d329bd99e66ca"
build_date: "2019-05-06T04:14:38.918Z"
size_mb: 9404
size: 4297314335
sif: "https://datasets.datalad.org/shub/russelltankl/SingularityHub/cudatorchgym/2019-05-06-91ab6aac-f2004efc/f2004efc5767f07a664d329bd99e66ca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/russelltankl/SingularityHub/cudatorchgym/2019-05-06-91ab6aac-f2004efc/
recipe: https://datasets.datalad.org/shub/russelltankl/SingularityHub/cudatorchgym/2019-05-06-91ab6aac-f2004efc/Singularity
collection: russelltankl/SingularityHub
---

# russelltankl/SingularityHub:cudatorchgym

```bash
$ singularity pull shub://russelltankl/SingularityHub:cudatorchgym
```

## Singularity Recipe

```singularity
bootstrap: docker
From: itamtao/pytorch-mpi:cuda9

%labels

MAINTAINER baditya@iastate.edu

%post
      # load environment variables
    . /environment

    # use bash as default shell
    echo "\n #Using bash as default shell \n" >> /environment
    echo 'SHELL=/bin/bash' >> /environment

    # make environment file executable
    chmod +x /environment

    # default mount paths
    which python
    /home/lin/conda/envs/pytorch-py3.6/bin/pip --no-cache-dir install setproctitle
    git clone https://github.com/openai/gym.git
    cd gym
    /home/lin/conda/bin/conda clean -pt --yes --all
    /home/lin/conda/envs/pytorch-py3.6/bin/pip --no-cache-dir install -e .
    /home/lin/conda/envs/pytorch-py3.6/bin/pip --no-cache-dir install gym[atari]
    cd ..
    git clone https://github.com/openai/baselines.git
    cd baselines
    /home/lin/conda/envs/pytorch-py3.6/bin/pip --no-cache-dir install tensorflow
    /home/lin/conda/envs/pytorch-py3.6/bin/pip --no-cache-dir install -e .
```

## Collection

 - Name: [russelltankl/SingularityHub](https://github.com/russelltankl/SingularityHub)
 - License: None

