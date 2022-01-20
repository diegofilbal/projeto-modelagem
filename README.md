# projeto-modelagem
O projeto no presente repositório foi desenvolvido durante a execução da disciplina de Simulação e Modelagem.

## Requisitos

Versão Python: o programa foi testado com o uso da versão `3.9.6` do Python.

As bibliotecas utilizadas projeto foram:
- beautifulsoup4 _(versão: 4.10.0)_;
- numpy _(versão: 1.21.1)_;
- selenium _(version: 4.1.0)_; e
- webdriver_manager _(version: 3.5.2)_.

Para instalar essas bibliotecas use o comando abaixo.

```
pip install -r /path/to/requirements.txt
```

## Executar programa

O programa de raspagem de informações de um evento deve receber a url do evento, o tipo de evento (twoway ou 1x2) e se o evento já ocorreu (past) ou ainda ocorrerá (live).

```
python main.py <url_evento> <tipo_evento> <tempo_evento>
```

Exemplo:
```
python main.py https://www.oddsportal.com/basketball/usa/nba/denver-nuggets-los-angeles-clippers-lItEBSuI/ twoway past
```
ou
```
python main.py https://www.oddsportal.com/basketball/usa/nba/denver-nuggets-los-angeles-clippers-lItEBSuI/ 1x2 live
```


# Autoria

Programa desenvolvido por **Alaide Lisandra Melo Carvalho** (<mendie73@gmail.com>), [addnomes] como projeto para a disciplina de *Simulação e Modelagem* de 2021.2.

&copy; IMD/UFRN 2022.
