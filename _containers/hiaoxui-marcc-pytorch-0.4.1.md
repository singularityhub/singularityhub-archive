---
id: 4104
name: "hiaoxui/marcc-pytorch"
branch: "master"
tag: "0.4.1"
commit: "0aad269a9041844ff1df079d6e9dfec065fdec20"
version: "0f391f35535435d045fe2e6560220f21"
build_date: "2018-08-21T21:25:53.545Z"
size_mb: 8887
size: 4650422303
sif: "https://datasets.datalad.org/shub/hiaoxui/marcc-pytorch/0.4.1/2018-08-21-0aad269a-0f391f35/0f391f35535435d045fe2e6560220f21.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hiaoxui/marcc-pytorch/0.4.1/2018-08-21-0aad269a-0f391f35/
recipe: https://datasets.datalad.org/shub/hiaoxui/marcc-pytorch/0.4.1/2018-08-21-0aad269a-0f391f35/Singularity
collection: hiaoxui/marcc-pytorch
---

# hiaoxui/marcc-pytorch:0.4.1

```bash
$ singularity pull shub://hiaoxui/marcc-pytorch:0.4.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: marcc-hpc/pytorch

%post
  # Downgrade pytorch
  /opt/conda/bin/pip install torch==0.4.1
  # Reinstall most current tensorbaordX, something magic about pip...
  /opt/conda/bin/conda install tqdm nltk colorama
```

## Collection

 - Name: [hiaoxui/marcc-pytorch](https://github.com/hiaoxui/marcc-pytorch)
 - License: None

