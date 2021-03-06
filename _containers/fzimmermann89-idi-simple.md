---
id: 14475
name: "fzimmermann89/idi"
branch: "master"
tag: "simple"
commit: "43d5e8ea99941e9553c3d93d67c99ae48fdfe4f8"
version: "05d1271988079a6dd0c572562f2629601a6a002d6d7439fb184af1816351b9ad"
build_date: "2021-01-22T03:39:45.947Z"
size_mb: 3943.7890625
size: 4135362560
sif: "https://datasets.datalad.org/shub/fzimmermann89/idi/simple/2021-01-22-43d5e8ea-05d12719/05d1271988079a6dd0c572562f2629601a6a002d6d7439fb184af1816351b9ad.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fzimmermann89/idi/simple/2021-01-22-43d5e8ea-05d12719/
recipe: https://datasets.datalad.org/shub/fzimmermann89/idi/simple/2021-01-22-43d5e8ea-05d12719/Singularity
collection: fzimmermann89/idi
---

# fzimmermann89/idi:simple

```bash
$ singularity pull shub://fzimmermann89/idi:simple
```

## Singularity Recipe

```singularity
Bootstrap: library
From: fzimmermann89/idi/latest

%post
#upgrade base
yum update -y && yum upgrade -y

. /etc/profile.d/conda.sh
conda activate

#ensure (frozen) package versions
conda config  --file /opt/anaconda3/.condarc --append channels plotly --append channels conda-forge 
conda config  --file /opt/anaconda3/.condarc --set channel_priority flexible
conda install -q -y -c conda-forge mamba
mamba install -q -y  _libgcc_mutex=0.1 _openmp_mutex=4.5 aiohttp=3.7.3 ansi2html=1.6.0 appdirs=1.4.4 argon2-cffi=20.1.0 asteval=0.9.16 async-timeout=3.0.1 async_generator=1.10 attrs=20.3.0 backcall=0.2.0 black=19.10b0 blas=1.0 bleach=3.2.1 blosc=1.20.1 bqplot=0.12.18 brotli=1.0.9 brotli-python=1.0.9 bzip2=1.0.8 ca-certificates=2020.12.5 certifi=2020.12.5 cffi=1.14.0 chardet=3.0.4 charls=2.1.0 click=7.1.2 cloudpickle=1.6.0 colorama=0.4.4 conda=4.9.2 conda-package-handling=1.6.1 cryptography=2.9.2 cycler=0.10.0 cython=0.29.21 cytoolz=0.11.0 dash=1.18.1 dash-core-components=1.14.1 dash-html-components=1.1.1 dash-renderer=1.8.3 dash-table=4.11.1 dask-core=2020.12.0 dbus=1.13.18 debugpy=1.2.1 decorator=4.4.2 defusedxml=0.6.0 dill=0.3.3 entrypoints=0.3 expat=2.2.10 fastrlock=0.5 flask=1.1.2 flask-compress=1.8.0 fontconfig=2.13.1 freetype=2.10.4 future=0.18.2 gettext=0.19.8.1 giflib=5.1.4 gitdb=4.0.5 gitpython=3.1.11 glib=2.66.4 gst-plugins-base=1.14.5 gstreamer=1.18.2 hdf5=1.10.6 h5py=2.10 icu=68.1  idna=2.9 imagecodecs=2020.5.30 imageio=2.9.0 importlib-metadata=2.0.0 importlib_metadata=2.0.0 intel-openmp=2020.2 ipydatawidgets=4.1.0 ipykernel=5.3.4 ipympl=0.5.8 ipython=7.19.0 ipython_genutils=0.2.0 ipyvolume=0.6.0a6 ipywebrtc=0.5.0 ipywidgets=7.6.0 isort=5.6.4 itsdangerous=1.1.0 jedi=0.17.2 jinja2=2.11.2 joblib=1.0.0 jpeg=9d json5=0.9.5 jsonschema=3.2.0 jupyter=1.0.0 jupyter-dash=0.3.1 jupyter-server-proxy=1.5.2 jupyter_client=6.1.7 jupyter_console=6.2.0 jupyter_core=4.7.0 jupyterlab=2.2.6   jupyterlab-latex=2.0.0 jupyterlab_pygments=0.1.2 jupyterlab_server=1.2.0 jxrlib=1.1 kiwisolver=1.3.0 krb5=1.17.1 lcms2=2.11 ld_impl_linux-64=2.33.1 libaec=1.0.4 libclang=11.0.0 libedit=3.1.20181209 libevent=2.1.10 libffi=3.3 libgcc-ng=9.3.0 libgfortran-ng=7.3.0 libglib=2.66.4 libgomp=9.3.0 libiconv=1.16 libllvm10=10.0.1 libllvm11=11.0.0 libpng=1.6.37 libpq=12.3 libsodium=1.0.18 libstdcxx-ng=9.3.0 libtiff=4.1.0 libuuid=2.32.1 libuv=1.40.0 libwebp=1.0.1 libxcb=1.14 libxkbcommon=1.0.3 libxml2=2.9.10 libzopfli=1.0.3 line_profiler=2.1.2 llvmlite=0.34.0 lmfit=1.0.1 lz4-c=1.9.2 mako=1.1.3 markupsafe=1.1.1 matplotlib=3.3.2 matplotlib-base=3.3.2 memory_profiler=0.58.0 mistune=0.8.4 mkl=2020.2 mkl-devel=2020.2 mkl-service=2.3.0 mkl_fft=1.2.0 mkl_random=1.1.1 multidict=5.1.0 multiprocess=0.70.11.1 mypy_extensions=0.4.3 mysql-common=8.0.22 mysql-libs=8.0.22 nbclient=0.5.1 nbconvert=6.0.7 nbdime=2.1.0 nbformat=5.0.8 ncurses=6.2 nest-asyncio=1.4.3 networkx=2.5 ninja=1.10.2 nodejs=15.3.0 notebook=6.1.6 nspr=4.29 nss=3.60 numba=0.51.2 numexpr=2.7.2 numpy=1.19.2 numpy-base=1.19.2 olefile=0.46 openjpeg=2.3.0 openssl=1.1.1i packaging=20.8 pandas=1.1.5 pandoc=2.11 pandocfilters=1.4.3 parso=0.7.0 pathos=0.2.7 pathspec=0.7.0 pcre=8.44 pexpect=4.8.0 pickleshare=0.7.5 pillow=8.0.1 pip=20.3.3 plotly=4.14.1 pox=0.2.9 ppft=1.6.6.3 prometheus_client=0.9.0 prompt-toolkit=3.0.8 prompt_toolkit=3.0.8 psutil=5.7.2 ptvsd=4.3.2 ptyprocess=0.6.0 pycosat=0.6.3 pycparser=2.20  pygments=2.7.3 pyopenssl=19.1.0 pyparsing=2.4.7 pyqt=5.12.3 pyqt-impl=5.12.3 pyqt5-sip=4.19.18 pyqtchart=5.12 pyqtwebengine=5.12.1 pyrsistent=0.17.3 pysocks=1.7.1 python=3.7.7 python-dateutil=2.8.1 python_abi=3.7 pythreejs=2.2.1 pytools=2020.4.4 pytz=2020.5 pywavelets=1.1.1 pyyaml=5.3.1 pyzmq=20.0.0 qt=5.12.9 qtconsole=4.7.7 qtpy=1.9.0 readline=8.0 regex=2020.11.13 requests=2.23.0 retrying=1.3.3 ruamel_yaml=0.15.87 scikit-image=0.17.2 scikit-learn=0.23.2 scipy=1.5.2 seaborn=0.11.1 send2trash=1.5.0 setuptools=51.0.0 simpervisor=0.3 sip=4.19.8 six=1.15.0 smmap=3.0.4 snappy=1.1.8 sqlite=3.34.0 tbb=2020.3 terminado=0.9.1 testpath=0.4.4 threadpoolctl=2.1.0 tifffile=2020.12.8 tk=8.6.8 toml=0.10.1 toolz=0.11.1 tornado=6.1 tqdm=4.46.0 traitlets=4.3.3 traittypes=0.2.1 typed-ast=1.4.1 typing-extensions=3.7.4.3 typing_extensions=3.7.4.3 uncertainties=3.1.5 urllib3=1.25.8 wcwidth=0.2.5 webencodings=0.5.1 werkzeug=1.0.1 wheel=0.34.2 widgetsnbextension=3.5.1 xeus=0.25.3 xeus-python=0.9.4 xz=5.2.5 yaml=0.1.7 yarl=1.6.3 zeromq=4.3.3 zipp=3.4.0 zlib=1.2.11 zstd=1.4.5
LIBRARY_PATH=/usr/local/cuda/lib64/stubs CPATH=/usr/local/cuda/include CUDA_ROOT=/usr/local/cuda pip install -q jupyterlab-code-formatter==1.3.8   jupyterlab-git==0.23.3   jupyterlab-latex==2.0.0    mkl-include==2021.1.1  pycuda==2020.1  cupy-cuda102

echo 'install idi' && pip install git+https://github.com/fzimmermann89/idi

#cleanup
conda clean -a -y
pip cache purge
rm -rf /root/.conda | true
rm -rf /root/.npm | true
rm -rf /root/.cache | true
rm -rf /tmp/npm* | true
rm -rf /tmp/texlive* | true
rm -rf /tmp/yarn* | true
rm -rf /var/cache/* | true

%labels
    Maintainer zimmf
    Version 0.1-200910
        
%runscript
exec /opt/runscript.sh python "$@"

%startscript
exec /opt/runscript.sh jupyter lab "$@"

%apprun jupyter
exec /opt/runscript.sh jupyter "$@"

%apprun ipython
exec /opt/runscript.sh ipython "$@"

%apprun pdftex
exec pdftex "$@"


%help
Centos7 with conda python, jupyter, latex, cuda and mkl




%environment
CUDA_ROOT=/usr/local/cuda
export CUDA_ROOT
SINGULARITY_SHELL=/bin/zsh
export SINGULARITY_SHELL
MKLROOT=/opt/intel/compilers_and_libraries/linux/mkl
export MKLROOT
TBBROOT=/opt/intel/compilers_and_libraries/linux/tbb
export TBBROOT
INTEL_LICENSE_FILE=/opt/intel/compilers_and_libraries/linux/licenses
export INTEL_LICENSE_FILE
LIBRARY_PATH=$LIBRARY_PATH:/opt/intel/compilers_and_libraries/linux/compiler/lib/intel64_lin:/opt/intel/compilers_and_libraries/linux/mkl/lib/intel64_lin:/opt/intel/compilers_and_libraries/linux/tbb/lib/intel64/gcc4.8:/opt/intel/compilers_and_libraries/linux/tbb/lib/intel64/gcc4.8
export LIBRARY_PATH
CPATH=$CPATH:/opt/intel/compilers_and_libraries/linux/mkl/include:/opt/intel/compilers_and_libraries/linux/tbb/include:/opt/intel/compilers_and_libraries/linux/tbb/include
export CPATH
PATH=$PATH:/opt/anaconda3/bin:/usr/local/texlive/bin/x86_64-linux:/usr/local/cuda/bin
PATH=$PATH:/opt/intel/compilers_and_libraries/linux/bin/intel64:/opt/intel/compilers_and_libraries/linux/bin
export PATH
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/intel/compilers_and_libraries/linux/mkl/bin/pkgconfig
export PKG_CONFIG_PATH
LD_PRELOAD=/usr/local/lib64/mklpatch.so
export LD_PRELOAD
```

## Collection

 - Name: [fzimmermann89/idi](https://github.com/fzimmermann89/idi)
 - License: None

