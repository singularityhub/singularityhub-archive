---
id: 14604
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "open3d_user"
commit: "590d2ff4af115a836a1222d005feef7bad8b31dd"
version: "227209f125f7682bbfc59c46fe87e7de246e19a152145f85ca703222c6ecf3fb"
build_date: "2020-10-13T17:51:36.123Z"
size_mb: 2927.515625
size: 3069722624
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/open3d_user/2020-10-13-590d2ff4-227209f1/227209f125f7682bbfc59c46fe87e7de246e19a152145f85ca703222c6ecf3fb.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/open3d_user/2020-10-13-590d2ff4-227209f1/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/open3d_user/2020-10-13-590d2ff4-227209f1/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:open3d_user

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:open3d_user
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:continuumio/miniconda3:4.8.2

%labels
MAINTAINER Thomas Green

%environment
# Do not use unknown user installs.
PYTHONNOUSERSITE=1
export PYTHONNOUSERSITE

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch
mkdir /apps

# Brings in conda.
. /etc/profile
cd /tmp

# Useful for testing visualisation
apt-get install -y mesa-utils

# Might be useful for visualisation.
wget https://netix.dl.sourceforge.net/project/virtualgl/2.6.4/virtualgl_2.6.4_amd64.deb
apt install -y ./virtualgl_2.6.4_amd64.deb

conda update -n base -c defaults conda

# Use user environment file (remove all versions and Windows)
cat >test.yml<<EOF
name: base
channels:
  - pytorch
  - open3d-admin
  - defaults
dependencies:
  - argon2-cffi
  - async_generator
  - attrs
  - backcall
  - blas
  - bleach
  - brotlipy
  - ca-certificates
  - certifi
  - cffi
  - chardet
  - colorama
  - cryptography
  - cudatoolkit
  - decorator
  - defusedxml
  - entrypoints
  - freetype
  - idna
  - importlib-metadata
  - importlib_metadata
  - intel-openmp
  - ipykernel
  - ipython
  - ipython_genutils
  - ipywidgets
  - jedi
  - jinja2
  - jpeg
  - json5
  - jsonschema
  - jupyter_client
  - jupyter_core
  - jupyterlab
  - jupyterlab_pygments
  - jupyterlab_server
  - libpng
  - libsodium
  - libtiff
  - lz4-c
  - markupsafe
  - mistune
  - mkl
  - mkl-service
  - mkl_fft
  - mkl_random
  - nbclient
  - nbconvert
  - nbformat
  - nest-asyncio
  - ninja
  - notebook
  - numpy
  - numpy-base
  - olefile
  - open3d
  - openssl
  - packaging
  - pandoc
  - pandocfilters
  - parso
  - pickleshare
  - pillow
  - pip
  - prometheus_client
  - prompt-toolkit
  - pycparser
  - pygments
  - pyopenssl
  - pyparsing
  - pyrsistent
  - pysocks
  - python
  - python-dateutil
  - pytorch
  - pyzmq
  - requests
  - send2trash
  - setuptools
  - six
  - sqlite
  - terminado
  - testpath
  - tk
  - torchvision
  - tornado
  - traitlets
  - urllib3
  - wcwidth
  - webencodings
  - wheel
  - widgetsnbextension
  - xz
  - zeromq
  - zipp
  - zlib
  - zstd
EOF

conda env update -n base -f test.yml
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

