---
id: 1096
name: "marcc-hpc/apache-spark"
branch: "2.2.0"
tag: "latest"
commit: "ad74fe7db6b66faf0878f24e859f425367815dbb"
version: "2b53c051a98cfe12620c9fed2cc35b3f"
build_date: "2019-09-23T05:01:37.420Z"
size_mb: 4598
size: 2312183839
sif: "https://datasets.datalad.org/shub/marcc-hpc/apache-spark/latest/2019-09-23-ad74fe7d-2b53c051/2b53c051a98cfe12620c9fed2cc35b3f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/apache-spark/latest/2019-09-23-ad74fe7d-2b53c051/
recipe: https://datasets.datalad.org/shub/marcc-hpc/apache-spark/latest/2019-09-23-ad74fe7d-2b53c051/Singularity
collection: marcc-hpc/apache-spark
---

# marcc-hpc/apache-spark:latest

```bash
$ singularity pull shub://marcc-hpc/apache-spark:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: singularities/spark:latest

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /scratch /data 
  
  # add log mount path location
  mkdir /usr/local/hadoop-2.8.2/logs

  # set localhost as default for the configuration
  sed -i.bak "s|\[NAMENODE_HOST\]|localhost|g" /usr/local/hadoop-2.8.2/etc/hadoop/core-site.xml
  
  # add additional python packages
  apt-get update
  
  # perhaps one wants 'ps' and 'kill' and 'git' and 'vim'
  apt-get --yes install procps git vim
  
  apt-get --yes install python-numpy python-scipy python-matplotlib ipython python-pandas python-sympy python-nose
  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/apache-spark](https://github.com/marcc-hpc/apache-spark)
 - License: [MIT License](https://api.github.com/licenses/mit)

