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

### Raspar evento
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

### Raspar Temporada

Para raspar os dados de uma temporada é necessário que o parâmetro do nome da temporada seja fornecido. Para isso, visite a página da temporada no OddsPortal e copie da url da página o nome que representa a temporada, isto é, a parte do texto sublinhada na imagem abaixo. Acompanhado do parâmetro referente ao número de páginas presentes nos resultados da temporada.

![Nome da temporada na url da página da temporada](https://drive.google.com/uc?export=view&id=1LSrFLYm6oz6LPXQmI6Nzgc-IX1VctCbq)

O comando deverá ser como os apresentados abaixo. 

```
python run_season.py nba-2018-2019 28
```

O comando acima acessa os dados da temporada 2018/2019 da NBA.

```
python run_season.py nba-2020-2021 25
```

O comando acima acessa os dados da temporada 2020/2021 da NBA.

# Autoria

Programa desenvolvido por **Alaide Lisandra Melo Carvalho** (<mendie73@gmail.com>), [addnomes] como projeto para a disciplina de *Simulação e Modelagem* de 2021.2.

&copy; IMD/UFRN 2022.
