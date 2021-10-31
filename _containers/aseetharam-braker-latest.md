---
id: 14582
name: "aseetharam/braker"
branch: "master"
tag: "latest"
commit: "f97c667493e940e71674bec7705f305d063f23a4"
version: "300ebf2e0d568e0ffd74565977d6271b"
build_date: "2021-04-16T21:27:56.100Z"
size_mb: 1075.0
size: 294858783
sif: "https://datasets.datalad.org/shub/aseetharam/braker/latest/2021-04-16-f97c6674-300ebf2e/300ebf2e0d568e0ffd74565977d6271b.sif"
url: https://datasets.datalad.org/shub/aseetharam/braker/latest/2021-04-16-f97c6674-300ebf2e/
recipe: https://datasets.datalad.org/shub/aseetharam/braker/latest/2021-04-16-f97c6674-300ebf2e/Singularity
collection: aseetharam/braker
---

# aseetharam/braker:latest

```bash
$ singularity pull shub://aseetharam/braker:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/biocontainers/braker2:2.1.6--hdfd78af_2

%environment
    export PATH=/opt/gmes_linux_64/ProtHint/bin/:${PATH}
    export AUGUSTUS_SCRIPTS_PATH=/usr/local/bin
    export AUGUSTUS_BIN_PATH=/usr/local/bin
    export GENEMARK_PATH=/opt/gmes_linux_64
    export ALIGNMENT_TOOL_PATH=/usr/local/bin/

# Register for GeneMark-ES/ET/EP at http://exon.gatech.edu/GeneMark/license_download.cgi (tested with ver 4.65)
# NOTE: the bundled license key expires after 200 days

%post
    set -o pipefail -o errexit
    readonly GENEMARK_DOWNLOAD_URL=http://topaz.gatech.edu/GeneMark/tmp/GMtool_v3gNp/gmes_linux_64.tar.gz
    wget -O - ${GENEMARK_DOWNLOAD_URL} | gzip -dc | tar -C /opt -xf -
    mkdir /opt/gm_key
    mv /opt/gmes_linux_64/gm_key /opt/gm_key/.gm_key
    cd /opt/gmes_linux_64
    perl change_path_in_perl_scripts.pl "/usr/bin/env perl"

    # https://github.com/gatech-genemark/ProtHint/issues/27
    sed -i.bak 's/grep -P/grep/' /opt/gmes_linux_64/ProtHint/bin/prothint.py
    sed -i.bak -e 's/readlink -e/realpath/' -e 's/stat --printf/stat -c/' /opt/gmes_linux_64/ProtHint/bin/spalnBatch.sh
   

%runscript
    exec braker.pl "$@"
```

## Collection

 - Name: [aseetharam/braker](https://github.com/aseetharam/braker)
 - License: None

