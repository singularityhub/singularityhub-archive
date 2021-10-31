---
id: 8244
name: "C3BI-pasteur-fr/craw"
branch: "master"
tag: "1.0"
commit: "4907eea840b76a39745436e58774f896f8ced812"
version: "88199eb14a78cc6ff075d13d70db7f07"
build_date: "2019-04-05T20:03:06.664Z"
size_mb: 865
size: 368074783
sif: "https://datasets.datalad.org/shub/C3BI-pasteur-fr/craw/1.0/2019-04-05-4907eea8-88199eb1/88199eb14a78cc6ff075d13d70db7f07.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/C3BI-pasteur-fr/craw/1.0/2019-04-05-4907eea8-88199eb1/
recipe: https://datasets.datalad.org/shub/C3BI-pasteur-fr/craw/1.0/2019-04-05-4907eea8-88199eb1/Singularity
collection: C3BI-pasteur-fr/craw
---

# C3BI-pasteur-fr/craw:1.0

```bash
$ singularity pull shub://C3BI-pasteur-fr/craw:1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
from: ubuntu:bionic


%labels
	maintainer Bertrand Neron <bneron@pasteur.fr>
    package.name craw
    package.version 1.0
    package.homepage https://gitlab.pasteur.fr/bneron/craw
    package.license GPLv3
  
%post
    ####################################
    #         Installing system        #
    ####################################

    apt-get update -y
    apt-get install -y --no-install-recommends python3 python3-tk
    apt-get install -y git
    apt-get install -y python3-pip

    #################################
    #        installing craw        #
    #################################
	pip3 install craw==1.0

    #################################
    #        cleaning image         #
    #################################
	apt-get purge -y git
	apt-get autoremove -y
    apt-get clean -y

%test
    mkdir /test_craw
    cd /test_craw
    pip3 download --no-deps craw==1.0.0
    tar -xzf craw-1.0.0.tar.gz
    /usr/bin/python3 craw-1.0.0/tests/run_tests.py -vv
    cd /
    rm -Rf /test_craw
%help
    This singularity image contains the Counter RNAseq Window (CRAW) package.
    Two commands are available \"coverage\" and \"htmp\.
    To run command:
         ./craw.img [coverage|htmp] [options]... [args]... .

    To get help about each command ./craw.img [coverage|htmp] --help.
    The detailed documentation is accessible here: http://bneron.pages.pasteur.fr/craw/

%runscript

# the following syntax allow to get the command and args
# in POSIX manner so compliant with dash which
# is the debian/ubuntu /bin/sh shell

CMD="$1"
shift
ARGS=${@}

case ${CMD} in
	coverage )
		exec /usr/local/bin/craw_coverage ${ARGS} ;;
	htmp )
		exec /usr/local/bin/craw_htmp ${ARGS} ;;
	* )
		echo "command \"${CMD}\" is not supported. available commands: \"coverage\"|\"htmp\"" 
    exit 127
    ;;
esac
```

## Collection

 - Name: [C3BI-pasteur-fr/craw](https://github.com/C3BI-pasteur-fr/craw)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

