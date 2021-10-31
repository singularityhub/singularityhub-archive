---
id: 4682
name: "SebastianM-C/singularity"
branch: "master"
tag: "0.7"
commit: "66b4698da14b06f3739af602377db8e9d9059599"
version: "0a7090958aeddd6b92743c357dce6fbe"
build_date: "2018-09-07T02:36:49.039Z"
size_mb: 2426
size: 1257775135
sif: "https://datasets.datalad.org/shub/SebastianM-C/singularity/0.7/2018-09-07-66b4698d-0a709095/0a7090958aeddd6b92743c357dce6fbe.simg"
url: https://datasets.datalad.org/shub/SebastianM-C/singularity/0.7/2018-09-07-66b4698d-0a709095/
recipe: https://datasets.datalad.org/shub/SebastianM-C/singularity/0.7/2018-09-07-66b4698d-0a709095/Singularity
collection: SebastianM-C/singularity
---

# SebastianM-C/singularity:0.7

```bash
$ singularity pull shub://SebastianM-C/singularity:0.7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: julia:0.7

%environment
	JULIA_DEPOT_PATH=/mnt/storage/.julia
	PYTHON=/usr/lib/x86_64-linux-gnu/
        export JULIA_DEPOT_PATH
	export PYTHON
        export XDG_RUNTIME_DIR=""

%runscript
        export JULIA_NUM_THREADS="$(( `nproc` / 2 ))"
        exec /usr/local/julia/bin/julia -O 3 "$@"

%post
	apt update
	apt install -y python3 python3-pip \
		vim \
		ffmpeg hdf5-tools libcairo2 pdf2svg imagemagick \
		libczmq-dev

	# Other dependencies
#        yum -y install cairo pdf2svg gtk3 ImageMagick poppler-utils
#        yum -y install gettext-libs gsl-devel

        # Python
#        dnf -y install python3-numpy python3-scipy python3-matplotlib python3-ipython \
#                python3-pandas python3-sympy python3-nose atlas-devel notebook

	# JuptyerLab (experimental)
        pip3 install jupyterlab

        # LaTeX
        apt install -y texlive-latex-base \
		texlive-latex-recommended \
                texlive-luatex \
                texlive-generic-extra \
                texlive-science

	# MS fonts
	echo \
"deb http://deb.debian.org/debian stretch main contrib non-free
deb-src http://deb.debian.org/debian stretch main contrib non-free

deb http://security.debian.org/debian-security/ stretch/updates main contrib non-free
deb-src http://security.debian.org/debian-security/ stretch/updates main contrib non-free

deb http://deb.debian.org/debian stretch-updates main contrib non-free
deb-src http://deb.debian.org/debian stretch-updates main contrib non-free" \
	> /etc/apt/sources.list
	apt update
	apt install -y msttcorefonts
```

## Collection

 - Name: [SebastianM-C/singularity](https://github.com/SebastianM-C/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

