# Backuper Python

Um script simples e eficiente para backup incremental de arquivos utilizando Python. Realiza backup apenas de arquivos novos ou modificados, economizando tempo e espaço em disco.

## Funcionalidades

- **Backup Incremental**: Copia apenas arquivos novos ou modificados usando hash SHA256
- **Exclusão de Padrões**: Possibilidade de excluir arquivos por padrões (ex: `*.tmp`, `__pycache__`)
- **Relatório Detalhado**: Exibe resumo com arquivos adicionados, modificados e ignorados
- **Configuração Simples**: Arquivo `config.ini` para fácil configuração

## Instalação

### Pré-requisitos

- Python 3.6 ou superior

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Backuper_python.git
cd Backuper_python
```

2. Configure o arquivo `config.ini`:
```ini
[backup]
source = caminho/da/pasta/origem
destination = caminho/da/pasta/destino
exclude = *.tmp,*.log,__pycache__
```

## Configuração

Edite o arquivo `config.ini` com as seguintes opções:

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `source` | Pasta de origem dos arquivos | `C:/Users/João/Documentos` |
| `destination` | Pasta de destino do backup | `D:/Backup/Documentos` |
| `exclude` | Padrões de arquivos a ignorar (separados por vírgula) | `*.tmp,*.log,__pycache__` |

### Exemplos de Padrões de Exclusão

```
# Excluir arquivos temporários
exclude = *.tmp,*.temp

# Exclude arquivos de log
exclude = *.log

# Excluir cache do Python
exclude = __pycache__,*.pyc

# Múltiplos padrões
exclude = *.tmp,*.log,__pycache__,.git
```

## Uso

Execute o script:

```bash
python backup.py
```

### Exemplo de Saída

```
Iniciando backup de 'C:/Users/João/Documentos' para 'D:/Backup/Documentos'
Encontrados 150 arquivos para backup

==================================================
RESUMO DO BACKUP
==================================================

[3] ARQUIVOS ADICIONADOS:
  + arquivo_novo1.txt
  + arquivo_novo2.pdf
  + imagem.png

[2] ARQUIVOS MODIFICADOS:
  ~ documento_editado.docx
  ~ config.yaml

[145] ARQUIVOS IGNORADOS

Total: 3 adicionados, 2 modificados, 145 ignorados.
```

## Manual das Funções

### `load_config()`

Carrega as configurações do arquivo `config.ini`.

**Retorna**: Dicionário com as configurações da seção `[backup]`

---

### `get_file_hash(file_path)`

Calcula o hash SHA256 de um arquivo para verificação de integridade.

**Parâmetros**:
- `file_path` (str): Caminho do arquivo

**Retorna**: String com o hash SHA256 do arquivo

---

### `get_files_to_backup(source, exclude_patterns)`

Lista todos os arquivos da pasta de origem, aplicando filtros de exclusão.

**Parâmetros**:
- `source` (str): Pasta de origem
- `exclude_patterns` (list): Lista de padrões a excluir

**Retorna**: Lista de objetos Path dos arquivos para backup

---

### `copy_file(file, source, destination)`

Copia um arquivo para o destino se ele for novo ou estiver modificado.

**Parâmetros**:
- `file` (Path): Arquivo a ser copiado
- `source` (str): Pasta de origem
- `destination` (str): Pasta de destino

**Retorna**: Tupla `(status, caminho_destino)` onde:
- `status` pode ser `'added'`, `'modified'` ou `'ignored'`
- `caminho_destino` é o caminho do arquivo no destino

---

### `main()`

Função principal que orchestrar todo o processo de backup.

1. Carrega configurações
2. Lista arquivos da origem
3. Copia arquivos novos/modificados
4. Exibe resumo do backup

---

## Como Funciona

1. **Leitura da Configuração**: O script lê `source`, `destination` e `exclude` do `config.ini`
2. **Varredura de Arquivos**: Percorre recursivamente a pasta de origem
3. **Comparação por Hash**: Compara o hash SHA256 do arquivo origem com o destino
4. **Cópia Seletiva**: Copia apenas se o arquivo não existir no destino ou se o hash for diferente
5. **Relatório**: Exibe resumo com estatísticas do backup

## Estrutura do Projeto

```
Backuper_python/
├── backup.py          # Script principal
├── config.ini         # Arquivo de configuração
├── README.md          # Documentação
└── LICENSE            # Licença
```

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contribuição

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.

---

Feito com Python
