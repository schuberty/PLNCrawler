English | [Portuguese](./README.pt-BR.md)

<h1 align="center">PLNCrawler</h1>

<div align="center">

A web crawler for datasets creation

![Python version][python-src]
![Latest commit][commit-src]
[![License][license-src]][license-href]

</div>

PLNCrawler is a web crawler focused on the automated creation of datasets used in natural language processing. The included sites are [Sensacionalista](https://www.sensacionalista.com.br/pais/), [The piauí Herald](https://piaui.folha.uol.com.br/herald/), [HuffPost Brasil](https://www.huffpostbrasil.com/noticias/) and [Nexo Jornal](https://www.nexojornal.com.br/tema/Sociedade)

## Dependencies
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/en/master/)

## How to use

To use PLNCrawler, in addition to this repository, you must also have the dependencies mentioned above. They can be installed, using the [requirements](requirements.txt) file, from pypi:

```sh
pip install -r requirements.txt
```

After having the dependencies and the repository, execute:

```sh
python PLNCrawler.py 
```

After that, all the websites in [sites.json](sites.json) will be crawled and saved.

---
###### **README in development**

[python-src]: https://img.shields.io/badge/python-3.8-green.svg
[commit-src]: https://badgen.net/github/last-commit/schuberty/PLNCrawler
[license-src]: https://badgen.net/github/license/schuberty/PLNCrawler
[license-href]: LICENSE.md