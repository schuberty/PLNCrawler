[English](./README.md) | Portuguese

<h1 align="center">PLNCrawler</h1>

<div align="center">

Um web crawler para criação de datasets

![Python version][python-src]
![Latest commit][commit-src]
[![License][license-src]][license-href]

</div>

PLNCrawler é um web crawler focado na criação automatizada de datasets utilizados no processamento de linguagem natural. Os sites incluídos são [Sensacionalista](https://www.sensacionalista.com.br/pais/), [The piauí Herald](https://piaui.folha.uol.com.br/herald/), [HuffPost Brasil](https://www.huffpostbrasil.com/noticias/) e [Nexo Jornal](https://www.nexojornal.com.br/tema/Sociedade)

## Dependencias
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/en/master/)

## Como usar

Para usar PLNCrawler, além deste repositório, também deveras ter as dependencias citadas acima. Elas podem ser instaladas, usando o arquivo [requirements](requirements.txt), a partir do pypi:

```sh
pip install -r requirements.txt
```

Depois de ter as dependências e o repositório, execute:
```sh
python PLNCrawler.py
```

A partir disto, as informações necessárias serão disponibilizadas após a execução.

---
###### **README em desenvolvimento**

[python-src]: https://img.shields.io/badge/python-3.8-green.svg
[commit-src]: https://badgen.net/github/last-commit/schuberty/PLNCrawler
[license-src]: https://badgen.net/github/license/schuberty/PLNCrawler
[license-href]: LICENSE.md
