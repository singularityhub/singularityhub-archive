---
id: 1138
name: "SebastianM-C/singularity"
branch: "master"
tag: "python"
commit: "dea1a7d87b7843248009b71d09e6b22c9a1c1c0a"
version: "c0938a86d71275133aaab491314c6469"
build_date: "2018-01-02T11:44:24.460Z"
size_mb: 6881
size: 2410332191
sif: "https://datasets.datalad.org/shub/SebastianM-C/singularity/python/2018-01-02-dea1a7d8-c0938a86/c0938a86d71275133aaab491314c6469.simg"
url: https://datasets.datalad.org/shub/SebastianM-C/singularity/python/2018-01-02-dea1a7d8-c0938a86/
recipe: https://datasets.datalad.org/shub/SebastianM-C/singularity/python/2018-01-02-dea1a7d8-c0938a86/Singularity
collection: SebastianM-C/singularity
---

# SebastianM-C/singularity:python

```bash
$ singularity pull shub://SebastianM-C/singularity:python
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu


%runscript

        exec /opt/intel/intelpython3/bin/python "$@"

%post

        apt-get update
      	apt-get install -y wget libncurses5 libncurses5-dev libncursesw5
      	apt-get install -y dvipng
        apt-get install -y texlive texlive-latex-extra
      	wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
      	apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
      	# wget https://apt.repos.intel.com/setup/intelproducts.list -O /etc/apt/sources.list.d/intelproducts.list
      	apt-get update
      	# apt-get install -y intel-mkl-64bit-2018.1-038
        # apt-get install -y intel-ipp-64bit-2018.1-038
      	# apt-get install -y intel-tbb-2018.0-033
      	# apt-get install -y intel-daal-64bit-2018.1-038
      	# apt-get install -y intelpython3
        # Workaround
        wget https://apt.repos.intel.com/intelpython/binary/intelpython3-2018.1-023_amd64.deb
        dpkg -i ./intelpython3-2018.1-023_amd64.deb
        rm ./intelpython3-2018.1-023_amd64.deb
```

## Collection

 - Name: [SebastianM-C/singularity](https://github.com/SebastianM-C/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

