---
id: 14086
name: "kiwiroy/gtf-to-gff3"
branch: "master"
tag: "0.1.0"
commit: "907ea3b597d30fed7cfd02f6a84625d757503a5c"
version: "af61ae12dd9770d1837aec1c3b97df78310441cf3e41874b12dcec3212c03cc3"
build_date: "2020-12-22T01:07:46.673Z"
size_mb: 29.8515625
size: 31301632
sif: "https://datasets.datalad.org/shub/kiwiroy/gtf-to-gff3/0.1.0/2020-12-22-907ea3b5-af61ae12/af61ae12dd9770d1837aec1c3b97df78310441cf3e41874b12dcec3212c03cc3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/kiwiroy/gtf-to-gff3/0.1.0/2020-12-22-907ea3b5-af61ae12/
recipe: https://datasets.datalad.org/shub/kiwiroy/gtf-to-gff3/0.1.0/2020-12-22-907ea3b5-af61ae12/Singularity
collection: kiwiroy/gtf-to-gff3
---

# kiwiroy/gtf-to-gff3:0.1.0

```bash
$ singularity pull shub://kiwiroy/gtf-to-gff3:0.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: zakame/perl:5.32-alpine

%files
  cpanfile /opt/src/cpanfile
  scripts/augustus-to-fa /opt/local/bin/augustus-to-fa
  scripts/gtf-to-gff3 /opt/local/bin/gtf-to-gff3
  t /opt/local/share/gtf-to-gff3/tests

%environment
  export LC_ALL=C.UTF-8
  export PERL5OPT=-I/opt/local/lib/perl5
  export PATH=/opt/local/bin:$PATH
  
%post
  cd /opt/src

  ### install / update system dependencies
  apk add --virtual .build-deps build-base curl git make openssl openssl-dev xz zlib-dev && \
    apk add --no-cache ca-certificates git make openssl tar zlib

  ## Build
  git clone -b release/101 https://github.com/Ensembl/ensembl-io.git ensembl-io
  rm -rf ensembl-io/modules/t
  perl -MExtUtils::Install -e 'install([ from_to => {@ARGV}, uninstall_shadows => 0, dir_mode => 755 ]);' -- \
    ./ensembl-io/modules /opt/local/lib/perl5
  git clone -b release/101 https://github.com/Ensembl/ensembl.git ensembl
  rm -rf ensembl/modules/t
  perl -MExtUtils::Install -e 'install([ from_to => {@ARGV}, uninstall_shadows => 0, dir_mode => 755 ]);' -- \
    ./ensembl/modules /opt/local/lib/perl5
  cpanm -L/opt/local --installdeps -n -q .

  ## allowed
  install -d /opt/local/share/gtf-to-gff3
  echo augustus-to-fa > /opt/local/share/gtf-to-gff3/commands
  echo gtf-to-gff3   >> /opt/local/share/gtf-to-gff3/commands

  ## cleanup
  apk del .build-deps && rm -rf /opt/src

%runscript
  SINGULARITY_BASENAME=$(basename $SINGULARITY_NAME)

  if echo $SINGULARITY_BASENAME | grep -qxf /opt/local/share/gtf-to-gff3/commands; then
    if [ -x /opt/local/bin/$SINGULARITY_BASENAME ]; then
      exec /opt/local/bin/$SINGULARITY_NAME "$@"
    else
      /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
      exec cat /opt/local/share/gtf-to-gff3/commands
    fi
  fi

%test
  ## build stage?
  if test -z "$SINGULARITY_CONTAINER"; then
    export LC_ALL=C.UTF-8
    export PERL5OPT=-I/opt/local/lib/perl5
    export PATH=/opt/local/bin:/usr/local/bin:$PATH
    export SINGULARITY_NAME=gtf-to-gff3
  fi
  prove -r /opt/local/share/gtf-to-gff3/tests
```

## Collection

 - Name: [kiwiroy/gtf-to-gff3](https://github.com/kiwiroy/gtf-to-gff3)
 - License: None

