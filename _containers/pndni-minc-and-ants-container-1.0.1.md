---
id: 8254
name: "pndni/minc-and-ants-container"
branch: "1.0.1"
tag: "1.0.1"
commit: "4262ff7c0c915358d98845123ff716a50599a9db"
version: "193bb48f2e0a08739d86f970776c6e05"
build_date: "2019-04-05T20:12:12.671Z"
size_mb: 6860
size: 1341337631
sif: "https://datasets.datalad.org/shub/pndni/minc-and-ants-container/1.0.1/2019-04-05-4262ff7c-193bb48f/193bb48f2e0a08739d86f970776c6e05.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/minc-and-ants-container/1.0.1/2019-04-05-4262ff7c-193bb48f/
recipe: https://datasets.datalad.org/shub/pndni/minc-and-ants-container/1.0.1/2019-04-05-4262ff7c-193bb48f/Singularity
collection: pndni/minc-and-ants-container
---

# pndni/minc-and-ants-container:1.0.1

```bash
$ singularity pull shub://pndni/minc-and-ants-container:1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/minc-container:1.2.0

%appinstall ants
    tmpdir=$(mktemp -d)
    pushd $tmpdir
    git clone --branch v2.3.1 https://github.com/ANTsX/ANTs.git ANTs_src
    mkdir ANTs_build
    pushd ANTs_build
    /opt/cmake/bin/cmake ../ANTs_src \
    -DITK_BUILD_MINC_SUPPORT=ON
    make -j 2
    popd  # ANTs_build
    mkdir -p /opt/ants/bin
    # it doesn't look like the libraries are needed. no RPATH or
    # RUNPATH used. as determined by running
    # for i in `ls`; do if [ $(file $i | awk '{print $2}') == "ELF" ]; then objdump -x $i | awk -v FS='\n' -v RS='\n\n' '$1 == "Dynamic Section:" {print}' | grep -i path ; fi; done;
    # in /scif/apps/ants/bin
    # and the documentation doesn't say to alter LD_LIBRARY_PATH
    cp ANTs_src/Scripts/* /scif/apps/ants/bin/
    cp ANTs_build/bin/* /scif/apps/ants/bin/
    popd  # $tmpdir

%apphelp
The ANTs software is governed by the following
terms/copyright:
Copyright (c) 2009-2013 ConsortiumOfANTS
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
3. Neither the name of the consortium nor the names of its contributors
  may be used to endorse or promote products derived from this software
  without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE CONSORTIUM AND CONTRIBUTORS ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

%labels
    Maintainer Steven Tilley
    Version 1.0.1
```

## Collection

 - Name: [pndni/minc-and-ants-container](https://github.com/pndni/minc-and-ants-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

