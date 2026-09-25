# Importa a classe Path, usada para representar caminhos de arquivo de forma portável (Windows/Linux).
from pathlib import Path
# Importa o módulo json, usado para analisar e manipular dados JSON.
import json

# Define a função load_jsonl. Recebe o caminho do arquivo e retorna os valores
# JSON encontrados em suas linhas não vazias, preservando a ordem.
def load_jsonl(arquivo: Path) -> list[object]:
    """Lê os valores JSON de um arquivo JSONL, mantendo a ordem das linhas."""
    # Abre o arquivo em modo leitura ("r") com codificação UTF-8. 
    # with é usado para garantir que o arquivo seja fechado após o bloco ser executado.
    with open(arquivo, 'r', encoding='utf-8') as file:
        # List comprehension: percorre o arquivo linha a linha, na ordem original.
        # if line.strip() ignora linhas vazias (só espaços ou \n), que quebrariam o JSON.
        # json.loads(line) converte o texto JSON em um valor Python. Esse valor
        # pode ser um dicionário, uma lista, um texto, um número, True, False ou None.
        # A compreensão de lista reúne os valores e preserva a ordem do arquivo.
        return [json.loads(line) for line in file if line.strip()]

def verifica_tipo(evento: object) -> list[str]:
    """Verifica se o valor recebido é um objeto JSON (um dicionário Python)."""
    # No Python, um objeto JSON é representado por um dicionário.
    if not isinstance(evento, dict):
        return ["O evento precisa ser um objeto JSON."]
    return []

def verifica_chaves(evento: dict[str, object]) -> list[str]:
    """Verifica se o evento tem as chaves necessárias."""
    obrigatorias = ['event_id', 'event_time', 'source', 'service', 'event_type', 'attributes']
    faltando = [chave for chave in obrigatorias if chave not in evento]
    # Verifica se o evento tem as chaves necessárias.
    if faltando:
        return [f"O evento precisa ter as chaves {faltando}."]
    return []


if __name__ == "__main__":
    # Testa a função load_jsonl com o JSONL do cenário slow_db.
    
    # Retorna a pasta Projeto (raiz do repositório).
    raiz = Path(__file__).resolve().parent.parent

    # A partir da raiz, entra nas pastas: simulator → fixtures → slow_db → events.jsonl.
    # O / do Path junta pastas; não é divisão.
    eventos = load_jsonl(raiz / "simulator" / "fixtures" / "slow_db" / "events.jsonl")
    
    for evento in eventos:
        # Primeira etapa: confirma que o valor é um objeto JSON.
        erros = verifica_tipo(evento)

        if not erros:
            # Segunda etapa: verifica se todas as chaves obrigatórias existem.
            erros = verifica_chaves(evento)
            if erros:
                print(erros)
            else:
                print("Tudo certo!")
        else:
            print(erros)
    
    #print(verifica_tipo(eventos))
    # Imprime o número de eventos lidos.
    #print(f"Lidos {len(eventos)} eventos.")
    # Imprime os primeiros eventos.
    #print(eventos[:3])
