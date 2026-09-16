============================================================
ROADMAP DO PROGRAMA
============================================================

Objetivo
--------
Estabilizar a base do programa, melhorar a segurança e a
experiência de uso, adicionar testes e preparar o projeto para
uma primeira versão distribuível.

A implementação deve seguir a ordem das fases abaixo, evitando
adicionar recursos avançados antes que os recursos fundamentais
estejam estáveis e testados.


============================================================
FASE 1 — FUNDAMENTOS E USABILIDADE
============================================================

1. VALIDAR OS DADOS CADASTRADOS
--------------------------------

Arquivos envolvidos:
- app/modulos/sites.py
- app/modulos/programas.py
- app/modulos/pastas.py
- app/modulos/navegador_padrao.py

Melhorias:
- Bloquear códigos vazios.
- Bloquear códigos duplicados.
- Remover espaços extras das entradas.
- Validar nomes vazios.
- Validar caminhos inexistentes.
- Validar links inválidos.
- Melhorar e padronizar as mensagens de erro.
- Impedir sobrescritas acidentais.

Resultado esperado:
Nenhum cadastro inválido deve ser aceito e nenhum cadastro
existente deve ser sobrescrito sem confirmação.


2. CORRIGIR O FLUXO DE COMANDOS
-------------------------------

Arquivo principal:
- app/core.py

Melhorias:
- Corrigir o comando "limpar <código>" para utilizar
  corretamente o código informado.
- Permitir editar diretamente pelo código.
- Permitir excluir diretamente pelo código.
- Exibir mensagem de ajuda quando um comando for utilizado
  incorretamente.
- Aceitar entradas com letras maiúsculas e espaços extras.
- Solicitar confirmação antes de substituir um cadastro existente.
- Disponibilizar "ajuda" como alternativa aos comandos de ajuda
  existentes.
- Padronizar o tratamento de comandos inválidos.

Resultado esperado:
Os comandos devem ser previsíveis, consistentes e fáceis de
entender.


3. MELHORAR O ARMAZENAMENTO DOS DADOS
--------------------------------------

Arquivo:
- app/banco.py

Melhorias:
- Validar a estrutura do arquivo JSON antes de utilizá-lo.
- Criar backup automático antes de sobrescrever os dados.
- Permitir recuperação a partir do backup caso o JSON esteja
  corrompido.
- Utilizar escrita atômica do arquivo.
- Adicionar uma versão ao formato dos dados para permitir futuras
  migrações.
- Definir corretamente o diretório de armazenamento de dados de
  acordo com o sistema operacional.

Resultado esperado:
Reduzir significativamente o risco de perda ou corrupção dos
cadastros.


============================================================
FASE 2 — SEGURANÇA
============================================================

4. TORNAR A EXECUÇÃO DE PROGRAMAS MAIS SEGURA
-----------------------------------------------

Arquivo principal:
- app/modulos/programas.py

Situação atual:
A utilização de "shell=True", combinada com bloqueios baseados
apenas na identificação textual de comandos perigosos, não
oferece proteção suficiente.

Melhorias:
- Evitar "shell=True" sempre que possível.
- Separar o executável de seus argumentos.
- Permitir somente programas ou caminhos previamente autorizados.
- Exibir informações claras sobre o programa que será executado.
- Solicitar confirmação para programas desconhecidos.
- Não permitir comandos administrativos por padrão.
- Criar uma lista de programas confiáveis.
- Registrar falhas de execução.
- Tratar erros de execução de maneira segura.

Resultado esperado:
Reduzir o risco de execução de comandos destrutivos,
inesperados ou não autorizados.


5. PROTEGER A FUNÇÃO DE LIMPEZA DE PASTAS
------------------------------------------

Arquivo principal:
- app/modulos/pastas.py

Melhorias:
- Bloquear pastas críticas do sistema.
- Bloquear a raiz do disco.
- Bloquear a pasta onde o próprio programa está instalado.
- Exibir uma prévia dos primeiros arquivos que serão removidos.
- Solicitar confirmação explícita antes da exclusão.
- Utilizar confirmação digitando o nome da pasta quando necessário.
- Criar um modo de simulação (dry-run), sem apagar arquivos.
- Permitir o envio de itens para a Lixeira quando essa opção
  estiver disponível.
- Impedir operações perigosas mesmo quando solicitadas
  acidentalmente.

Resultado esperado:
Evitar exclusões acidentais e reduzir a possibilidade de perda
irreversível de arquivos.


============================================================
FASE 3 — TESTES E QUALIDADE
============================================================

6. CRIAR TESTES AUTOMATIZADOS
-----------------------------

Nova pasta:
- tests/

Criar testes para:
- Cadastro de sites.
- Cadastro de programas.
- Cadastro de pastas.
- Edição de cadastros.
- Exclusão de cadastros.
- Persistência em JSON.
- Recuperação de dados corrompidos.
- Detecção de códigos duplicados.
- Expansão de variáveis de ambiente, como %TEMP%.
- Tratamento de comandos inválidos.
- Bloqueio de ações perigosas.
- Casos de entrada vazia ou inválida.

Resultado esperado:
Permitir alterações no código sem comprometer funcionalidades
que já estejam funcionando.


7. CRIAR TESTES MANUAIS DE ACEITAÇÃO
-------------------------------------

Definir e executar uma lista de cenários de uso:

- Iniciar o programa sem um arquivo de dados.
- Cadastrar um site.
- Abrir o site cadastrado.
- Editar o site.
- Excluir o site.
- Cadastrar uma pasta válida.
- Tentar cadastrar uma pasta inexistente.
- Cadastrar um navegador.
- Definir o navegador padrão.
- Fechar o programa.
- Reabrir o programa.
- Confirmar que os dados continuam salvos.
- Testar entradas vazias.
- Testar entradas inválidas.
- Testar códigos duplicados.
- Testar comandos inexistentes.
- Testar operações potencialmente perigosas.

Resultado esperado:
Validar o comportamento do programa sob a perspectiva real
do usuário.


============================================================
FASE 4 — INTERFACE E EXPERIÊNCIA DO USUÁRIO
============================================================

8. MELHORAR A INTERFACE DO TERMINAL
------------------------------------

Arquivos envolvidos:
- app/menu.py
- app/terminal.py

Melhorias:
- Padronizar os menus.
- Tornar a navegação consistente.
- Utilizar cores no terminal quando houver compatibilidade.
- Padronizar títulos e seções.
- Exibir indicadores claros de operação concluída.
- Destacar mensagens de erro.
- Tratar corretamente Ctrl+C.
- Tratar entradas vazias.
- Disponibilizar uma opção de voltar em todas as telas.
- Evitar a limpeza excessiva da tela.
- Manter informações importantes visíveis durante as operações.

Resultado esperado:
Oferecer uma experiência de terminal mais organizada,
profissional e previsível.


9. MELHORAR A LISTAGEM DE CADASTROS
------------------------------------

Adicionar:
- Ordenação por nome.
- Ordenação por código.
- Busca por texto.
- Filtros por tipo.
- Exibição organizada em tabela.
- Mensagem clara quando não existirem registros.
- Possibilidade de exportar os cadastros.

Resultado esperado:
Permitir que o usuário encontre rapidamente qualquer item
cadastrado.


============================================================
FASE 5 — DOCUMENTAÇÃO E DISTRIBUIÇÃO
============================================================

10. CRIAR A DOCUMENTAÇÃO DO PROJETO
------------------------------------

Arquivo:
- README.md

O README deve conter:
- Objetivo do programa.
- Requisitos.
- Processo de instalação.
- Como executar.
- Lista de comandos.
- Exemplos de utilização.
- Local de armazenamento dos dados.
- Informações sobre backups.
- Avisos relacionados à execução de programas.
- Avisos relacionados à exclusão de pastas.
- Solução para problemas comuns.

Resultado esperado:
Permitir que outra pessoa consiga instalar, configurar e utilizar
o programa sem depender de assistência externa.


11. PREPARAR A CONFIGURAÇÃO DE EXECUÇÃO
-----------------------------------------

Adicionar, conforme necessário:
- requirements.txt, caso existam bibliotecas externas.
- .gitignore.
- Arquivo de versão.
- Script de execução para Windows.
- Configuração adequada para diferentes sistemas operacionais,
  quando aplicável.
- Possibilidade de gerar um executável .exe utilizando PyInstaller.
- Ícone definitivo.
- Nome definitivo do aplicativo.

Resultado esperado:
Facilitar a distribuição do programa, inclusive para usuários
que não possuem Python instalado.


============================================================
FASE 6 — RECURSOS ADICIONAIS
============================================================

Os recursos desta fase só devem ser implementados depois que
as funcionalidades principais estiverem estáveis, protegidas
e testadas.

Possíveis recursos futuros:
- Atalhos de teclado.
- Favoritos.
- Categorias para programas, sites e pastas.
- Importação de dados.
- Exportação de dados.
- Backup manual.
- Restauração de backup.
- Interface gráfica utilizando Tkinter, PySide ou outra biblioteca.
- Inicialização automática com o Windows.
- Histórico de ações.
- Sistema de logs.
- Perfis de usuário.
- Sincronização opcional dos dados.


============================================================
ORDEM RECOMENDADA DE IMPLEMENTAÇÃO
============================================================

PRIORIDADE ALTA
---------------

1. Validação dos cadastros.
2. Correção do comando "limpar".
3. Proteção da limpeza de pastas.
4. Remoção ou redução do uso de "shell=True".
5. Validação e backup do arquivo JSON.
6. Recuperação de dados corrompidos.
7. Testes automatizados básicos.
8. Tratamento dos principais erros de execução.


PRIORIDADE MÉDIA
----------------

1. Melhorias nos menus.
2. Tratamento de Ctrl+C.
3. Tratamento de entradas inválidas.
4. Busca e ordenação dos cadastros.
5. Melhorias na apresentação das listagens.
6. Documentação completa no README.md.
7. Testes manuais completos.
8. Preparação inicial para distribuição.


PRIORIDADE BAIXA
----------------

1. Exportação e importação de dados.
2. Interface gráfica.
3. Sistema avançado de logs.
4. Empacotamento como .exe.
5. Favoritos.
6. Categorias.
7. Histórico de ações.
8. Outros recursos avançados.


============================================================
CRITÉRIO DE CONCLUSÃO — PRIMEIRA VERSÃO DISTRIBUÍVEL
============================================================

O programa poderá ser considerado pronto para uma primeira
versão distribuível quando todos os requisitos abaixo forem
atendidos:

[x] Cadastros inválidos são rejeitados corretamente.

[x] Códigos vazios ou duplicados não são aceitos.

[ ] Nenhum cadastro existente pode ser sobrescrito
    acidentalmente.

[ ] O comando "limpar <código>" funciona corretamente.

[ ] A limpeza de pastas possui proteção contra locais críticos.

[ ] A execução de programas possui controles de segurança
    adequados.

[ ] O uso de shell=True foi eliminado ou reduzido a situações
    justificadas e controladas.

[ ] O arquivo JSON possui validação e mecanismo de backup.

[ ] Existe recuperação em caso de corrupção dos dados.

[ ] Os principais fluxos possuem testes automatizados.

[ ] Os principais fluxos foram validados manualmente.

[ ] O programa trata entradas inválidas e interrupções
    adequadamente.

[ ] Existe documentação de instalação e utilização.

[ ] O programa mantém os dados corretamente após ser fechado
    e reaberto.

[ ] Existe uma forma simples de distribuir o programa ao
    usuário final.


============================================================
META FINAL
============================================================

Transformar o programa de uma ferramenta funcional em uma
aplicação estável, segura, testável, documentada e preparada
para distribuição.

A prioridade deve ser:

ESTABILIDADE
    ↓
SEGURANÇA
    ↓
TESTES
    ↓
USABILIDADE
    ↓
DOCUMENTAÇÃO
    ↓
DISTRIBUIÇÃO
    ↓
RECURSOS AVANÇADOS

Novos recursos não devem comprometer a estabilidade ou a
segurança das funcionalidades já existentes.
============================================================