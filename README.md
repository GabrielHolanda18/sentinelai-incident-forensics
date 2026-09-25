# SentinelAI - primeiro incremento

O MVP começa como um laboratório pequeno de investigação de incidentes. O primeiro cenário é uma lentidão no banco de pedidos seguida de timeouts na API.

## Hipótese do cenário

No cenário sintético controlado, um aumento persistente da duração das operações no banco é seguido por mais timeouts na API. Após a recuperação do banco, a API volta a responder com sucesso.

A ordem dos sinais permite investigar essa hipótese. Ela não prova, por si só, causalidade em dados reais.

## Contrato mínimo dos eventos

O arquivo `simulator/fixtures/slow_db/events.jsonl` tem um objeto JSON por linha. Cada evento usa estes campos:

| Campo | Significado |
| --- | --- |
| `event_id` | Identificador único e estável do evento |
| `event_time` | Horário em que ocorreu, em UTC e formato ISO 8601 |
| `source` | Fonte do dado, como `database` ou `application` |
| `service` | Componente associado, como `orders-db` ou `orders-api` |
| `event_type` | Tipo da observação |
| `attributes` | Medições e detalhes específicos |

Os nomes dentro de `attributes` seguem como referência as convenções do OpenTelemetry: `db.client.operation.duration` em segundos para operações no banco; `http.server.request.duration` em segundos e `http.response.status_code` para requisições HTTP; `error.type` descreve uma falha, como `timeout`.

Este é um formato simples do projeto, inspirado nessas convenções. Ele não é um arquivo de exportação OTLP. Fontes: [convenções de métricas de banco](https://opentelemetry.io/docs/specs/semconv/db/database-metrics/) e [convenções de métricas HTTP](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/).

## Separação das respostas conhecidas

`simulator/fixtures/slow_db/manifest.json` registra o que foi injetado no cenário. Ele representa o gabarito do avaliador e não deve ser lido pelo motor de ingestão ou pelo detector.

## Primeiro exercício prático

Implemente `load_jsonl(path)` em `forensic_engine/ingestion.py` para:

1. Abrir o arquivo como UTF-8.
2. Interpretar cada linha não vazia como JSON.
3. Devolver os eventos na ordem do arquivo.

Neste exercício, mantenha o escopo na leitura. Validação do contrato, ordenação temporal, pandas, banco de dados e API serão incrementos posteriores. Ao terminar, traga seu código ou a mensagem de erro; revisaremos juntos antes de avançar.
