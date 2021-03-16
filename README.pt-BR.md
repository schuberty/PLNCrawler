[English](./README.md) | Portuguese

<h1 align="center">PLNCrawler</h1>

<div align="center">

Um web crawler para criação de datasets

![Python version][python-src]
![Latest commit][commit-src]
[![License][license-src]][license-href]

</div>

PLNCrawler é um web crawler focado na **criação automatizada de datasets** a serem utilizados no processamento de linguagem natural. Os sites incluídos são [Sensacionalista](https://www.sensacionalista.com.br/pais/), [The piauí Herald](https://piaui.folha.uol.com.br/herald/) e [Estadão](https://politica.estadao.com.br/ultimas), tendo seus datasets disponíveis neste repositório na pasta [datasets](datasets/).

> ##### **Sobre o artigo publicado com referência a este repositório** – Alguns dos websites utilizados anteriormente foram descontinuados por: 1. Nexo Jornal ter começado a pedir por inscrição para poder visualizar seu conteúdo e; 2. HuffPost Brasil parou de publicar conteúdo e todos as suas notíticas foram limitadas. Estes dois websites foram trocados pelo Estadão #####

## Dependencias ##

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/en/master/)

## Como usar ##

Para fazer o bom uso deste repositório é recomendado usar o pacote [pipenv](https://pypi.org/project/pipenv/). Caso não deseja fazer o uso do mesmo, instale as dependências necessárias da forma que deseja e seguindo as versões mencionadas no arquivo [Pipfile](Pipfile) na divisão de *packages*.

O tutorial de instalação a seguir será com base no [pipenv](https://pypi.org/project/pipenv/), caso não o tenha, instale-o com o [pip](https://pip.pypa.io/en/stable/installing/).

```sh
> pip install pipenv
```

Clone ou faça o download do repositório.

```url
https://github.com/schuberty/PLNCrawler.git
```

Estando no diretório em que o repositório foi importado, instale um novo ambiente virtual com as dependencias corretas a partir do arquivo [Pipfile](Pipfile) com o seguinte comando:

```sh
> pipenv install --dev
```

Após, ative o *Pipenv shell*:

```sh
> pipenv shell
```

Isto irá gerar um novo subprocesso shell, o qual pode ser desativado usando:

```sh
(env) > exit
```

---
###### **README em desenvolvimento** ######

[python-src]: https://img.shields.io/badge/python-3.9-green.svg
[commit-src]: https://badgen.net/github/last-commit/schuberty/PLNCrawler
[license-src]: https://badgen.net/github/license/schuberty/PLNCrawler
[license-href]: LICENSE.md
