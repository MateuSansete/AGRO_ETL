# Padrão de Commits

Este projeto segue o padrão [**Conventional Commits**](https://www.conventionalcommits.org/), que define uma convenção simples e legível para os nomes dos commits.

---

## Estrutura do Commit

<tipo>(escopo opcional): <descrição breve>

**Exemplo:**

fix(pipeline): corrige erro na transformação de dados nulos
feat(api): adiciona endpoint para consulta de métricas

---

## Tipos de Commits

| Tipo | Descrição | Exemplo |
|------|------------|----------|
| **feat** | Adição de nova funcionalidade | `feat(etl): adiciona extração de dados do S3` |
| **fix** | Correção de erros ou bugs | `fix(transform): corrige erro de tipagem no pandas ou no arquivo do jupyter` |
| **docs** | Alterações em documentação | `docs(readme): adiciona instruções de execução do pipeline` |
| **style** | Mudanças de formatação ou estilo (sem alterar código funcional) | `style: formata código com black` |
| **refactor** | Refatoração de código sem mudar comportamento | `refactor(load): melhora função de carga no Redshift` |
| **test** | Adição ou ajuste de testes automatizados | `test: adiciona testes para função de limpeza de dados` |
| **chore** | Tarefas diversas que não afetam o código (build, deps, configs) | `chore: atualiza dependências do requirements.txt` |
| **perf** | Melhoria de performance | `perf: otimiza leitura de arquivos CSV grandes` |




---

## Referências

- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/)




