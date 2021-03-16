English | [Portuguese](./README.pt-BR.md)

<h1 align="center">PLNCrawler</h1>

<div align="center">

A web crawler for datasets creation

![Python version][python-src]
![Latest commit][commit-src]
[![License][license-src]][license-href]

</div>

PLNCrawler is a web crawler focused on the automated creation of datasets to be used in natural language processing. The included sites are [Sensacionalista](https://www.sensacionalista.com.br/pais/), [The piauí Herald](https://piaui.folha.uol.com.br/herald/) and [Estadao](https://politica.estadao.com.br/ultimas), with their datasets available in this repository in the [datasets](datasets/) folder.

> ##### **About the article published with reference to this repository** – Some of the websites used previously were discontinued by: 1. Nexo Jornal having started asking for registration in order to be able to view its content and; 2. HuffPost Brasil stopped publishing content and all of its news was limited. These two websites were exchanged for Estadão #####

## Dependencies ##

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/en/master/)

## How to use ##

To make good use of this repository it is recommended to use the [pipenv](https://pypi.org/project/pipenv/) package. If you don't want to use it, install the necessary dependencies the way you want and following the versions mentioned in the [Pipfile](Pipfile) file in the packages division.

The following installation tutorial will be based on [pipenv](https://pypi.org/project/pipenv/), if you don't have it, install it with [pip](https://pip.pypa.io/en/stable/installing/).

```properties
> pip install pipenv
```

Clone or download the repository.

```sh
https://github.com/schuberty/PLNCrawler.git
```

Being in the directory where the repository was imported, install a new virtual environment with the correct dependencies from the Pipfile file with the following command:

```properties
> pipenv install --dev
```

Next, activate the Pipenv shell:

```properties
> pipenv shell
```

This will spawn a new shell subprocess, which can be deactivated by using:

```properties
(env) > exit
```

---
###### **README in development**

[python-src]: https://img.shields.io/badge/python-3.9-green.svg
[commit-src]: https://badgen.net/github/last-commit/schuberty/PLNCrawler
[license-src]: https://badgen.net/github/license/schuberty/PLNCrawler
[license-href]: LICENSE.md