---
id: 14324
name: "UniversalDataTool/universal-data-tool"
branch: "master"
tag: "latest"
commit: "e10c7b8e9db3febb75de32382aa204eb0bfcb334"
version: "42a2aefcd48e24f0e203a249f37f81d2"
build_date: "2020-10-30T04:17:20.023Z"
size_mb: 3870.0
size: 1197137951
sif: "https://datasets.datalad.org/shub/UniversalDataTool/universal-data-tool/latest/2020-10-30-e10c7b8e-42a2aefc/42a2aefcd48e24f0e203a249f37f81d2.sif"
url: https://datasets.datalad.org/shub/UniversalDataTool/universal-data-tool/latest/2020-10-30-e10c7b8e-42a2aefc/
recipe: https://datasets.datalad.org/shub/UniversalDataTool/universal-data-tool/latest/2020-10-30-e10c7b8e-42a2aefc/Singularity
collection: UniversalDataTool/universal-data-tool
---

# UniversalDataTool/universal-data-tool:latest

```bash
$ singularity pull shub://UniversalDataTool/universal-data-tool:latest
```

## Singularity Recipe

```singularity
# A singularity container recipe file for the UNIVERSAL-DATA-TOOL
Bootstrap: docker
From: node:12

%environment
    export LISTEN_PORT=3000

%post

    # Clone the repository
    bash -c "cd / \
        && git clone https://github.com/UniversalDataTool/universal-data-tool.git \
        && mv universal-data-tool/ /opt/"

    # Install the package
    npm install -g serv
    bash -c "cd /opt/universal-data-tool \
        && npm install \
        && npm run build"

%startscript
    npx serve -s "/opt/universal-data-tool/build" -p $LISTEN_PORT

%runscript
    npx serve -s /opt/universal-data-tool/build -p $LISTEN_PORT

%help
    A singularity container for running the UNIVERSAL-DATA-TOOL. For more information
    see https://github.com/UniversalDataTool/universal-data-tool/.

%labels
    Maintainer: Rick Staa
    Github: https://github.com/UniversalDataTool/universal-data-tool/
    Version: v1.0.0
    Type: Public
```

## Collection

 - Name: [UniversalDataTool/universal-data-tool](https://github.com/UniversalDataTool/universal-data-tool)
 - License: [MIT License](https://api.github.com/licenses/mit)

