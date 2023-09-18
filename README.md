# Sistema Hidrômetro Digital - API

API do Sistema de Hidrômetros Digitais.

## Dependências

* python3;
* Dependências python contidas em `requirements.txt`;

### Desenvolvimento

Caso não tenha o `virtualenv` instalado, instale através do seguinte comando:

```sh
$ pip3 install virtualenv
```

Para rodar o projeto em desenvolvimento crie um ambiente virtual python para não "sujar" o seu ambiente atual.

```sh
$ virtualenv venv
```

Em seguida, ative o ambiente virtual:

```sh
$ sourve venv/bin/activate
```

Instale as dependências do projeto:

```sh
$ pip3 install -r requirements.txt
```

Para rodar o projeto, execute o seguinte comando:

```sh
$ python3 -m uvicorn main:app --reload
```

### Rotas

#### Leituras

Rota para resgatar a última leitura do dispositivo por `id`:

```
/leitura/{id}
```

* Tipo: **GET**
* Recebe: nada
* Retorna: `{"id": id, "timestamp": unix timestamp, "leitura": leitura em litros}`
* Teste:

```
curl -X GET http://localhost:8000/leitura/2
```

Rota para setar a última leitura do dispositivo por `id`:

```
/leitura/{id}
```

* Tipo: **POST**
* Recebe: `{"timestamp", unix timestamp, "leitura": leitura em litros}`
* Retorna: `{"status": "OK" ou "FAILED"}`
* Teste: esta requisição seta os dados `{"timestamp": "1625862265", "leitura": 10.00 }` para o dispositivo de `id=2`.
```
curl -d '{"timestamp": "1625862265", "leitura": 10.00 }' -H "Content-Type: application/json" -X POST http://localhost:8000/leitura/2
```

## Desenvolvedor

| ![](https://github.com/calebe94.png)                                       |
|:---------------------------------------------------------------------------:|
| [Edimar Calebe Castanho(calebe94@disroot.org)](https://github.com/Calebe94) |

## Licença

Todo este software é coberto pela [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
