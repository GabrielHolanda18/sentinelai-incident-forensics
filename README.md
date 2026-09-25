# Investigando a lentidão em um sistema de pedidos

**Projeto educacional do SentinelAI**

Este projeto explora, com dados fictícios, como investigar por que um sistema de pedidos fica lento e algumas solicitações falham. Enquanto funciona, um programa faz anotações automáticas sobre o que aconteceu; essas informações ajudam a entender problemas.

## O que a aplicação faz

Na versão atual, o programa em Python, executado no terminal, lê um arquivo de exemplo com 10 registros criados para este estudo. Para cada registro, ele confere se:

- as informações têm a estrutura esperada, como um conjunto de campos e valores;
- os campos obrigatórios estão presentes.

Quando as verificações passam, a aplicação mostra `Tudo certo!`. Se encontrar um problema de formato, mostra uma mensagem de erro.

Por enquanto, o programa trabalha com dados fictícios e faz apenas essas conferências básicas. A investigação automática de causas e o uso de inteligência artificial são etapas futuras, ainda não implementadas.

## Cenário de exemplo

O exemplo representa um sistema fictício de pedidos. Um banco de dados guarda as informações dos pedidos, e uma API — um serviço que recebe solicitações de outros programas — encaminha operações como consultar ou criar um pedido.

Nos registros de exemplo, algumas operações no banco começam a demorar mais. Em seguida, certas solicitações à API levam tempo demais para responder e terminam com um erro de timeout. **Timeout** significa que o programa parou de esperar porque a resposta não chegou dentro do limite de tempo.

Essa sequência ajuda a investigar se a lentidão do banco pode estar relacionada às falhas da API. Ela é uma hipótese didática: a ordem dos acontecimentos, sozinha, não prova a causa em um sistema real.

## Como executar

Com o Python 3.9 ou mais recente instalado, abra um terminal na pasta principal do projeto e execute:

```bash
python forensic_engine/ingestion.py
```

Com os dados atuais, a mensagem `Tudo certo!` aparece uma vez para cada um dos 10 registros. A leitura usa apenas recursos incluídos no Python; não é necessário instalar bibliotecas adicionais.

## Dados e arquivos principais

Os dados são **sintéticos**: foram criados para o exercício e não vieram de usuários ou de um sistema real. O arquivo `events.jsonl` contém um registro por linha. JSONL é um arquivo de texto em que cada linha contém um registro no formato JSON, uma maneira comum de organizar informações em campos e valores.

| Arquivo ou campo | Explicação |
| --- | --- |
| `forensic_engine/ingestion.py` | Código que lê os registros e confere seu formato básico. |
| `simulator/fixtures/slow_db/events.jsonl` | Os 10 registros fictícios do cenário. |
| `simulator/fixtures/slow_db/manifest.json` | A descrição da situação preparada para o exercício. O programa atual não lê esse arquivo. |
| `event_id` | Identificador do registro. |
| `event_time` | Data e horário do acontecimento; UTC é um horário de referência usado no mundo todo. |
| `source` | Tipo de origem, como banco de dados ou aplicação. |
| `service` | Componente relacionado, como `orders-db` ou `orders-api`. |
| `event_type` | Tipo de acontecimento, como uma operação no banco ou uma solicitação à API. |
| `attributes` | Detalhes adicionais, como a duração da operação ou o código de resposta. |

## Situação do projeto

**Já funciona:** ler os registros, confirmar que cada um tem a estrutura básica esperada e verificar a presença dos campos obrigatórios.

**Próximas etapas:** conferir se os valores de cada campo têm o formato esperado; organizar os acontecimentos em uma linha do tempo; e, depois, estudar maneiras de destacar períodos fora do padrão.

## Palavras usadas neste projeto

| Palavra | Em termos simples |
| --- | --- |
| Registro ou log | Anotação automática sobre algo que aconteceu no programa. |
| Banco de dados | Lugar onde o sistema guarda informações, como os pedidos. |
| API | Serviço que permite a outros programas solicitar operações. |
| Timeout | Fim da espera porque uma resposta demorou além do limite definido. |
| Dados sintéticos | Dados inventados para estudo, sem representar usuários reais. |

## Referência técnica opcional

Alguns nomes usados para descrever medições foram inspirados nas convenções do OpenTelemetry, um projeto aberto com padrões para registrar o comportamento de sistemas. Os dados deste exercício usam um formato simplificado; não são um arquivo oficial de exportação do OpenTelemetry.

- [Convenções para medições de banco de dados](https://opentelemetry.io/docs/specs/semconv/db/database-metrics/)
- [Convenções para medições HTTP](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/)
