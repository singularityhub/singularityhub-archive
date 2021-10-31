---
id: 8243
name: "C3BI-pasteur-fr/craw"
branch: "master"
tag: "latest"
commit: "4907eea840b76a39745436e58774f896f8ced812"
version: "fa19d8fd41e325cbaa5f8590ebc46d70"
build_date: "2019-04-05T20:03:06.671Z"
size_mb: 933
size: 440500255
sif: "https://datasets.datalad.org/shub/C3BI-pasteur-fr/craw/latest/2019-04-05-4907eea8-fa19d8fd/fa19d8fd41e325cbaa5f8590ebc46d70.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/C3BI-pasteur-fr/craw/latest/2019-04-05-4907eea8-fa19d8fd/
recipe: https://datasets.datalad.org/shub/C3BI-pasteur-fr/craw/latest/2019-04-05-4907eea8-fa19d8fd/Singularity
collection: C3BI-pasteur-fr/craw
---

# C3BI-pasteur-fr/craw:latest

```bash
$ singularity pull shub://C3BI-pasteur-fr/craw:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
from: ubuntu:bionic


%labels
	maintainer Bertrand Neron <bneron@pasteur.fr>
    package.name craw
    package.version latest
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
    cd /usr/local/src
	git clone https://gitlab.pasteur.fr/bneron/craw/
	cd craw
	pip3 install .

	mkdir /craw
    mv tests /craw/

    #################################
    #        cleaning image         #
    #################################
	apt-get purge -y git
	apt-get autoremove -y
    apt-get clean -y

%test
    /usr/bin/python3 /craw/tests/run_tests.py -vv

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

