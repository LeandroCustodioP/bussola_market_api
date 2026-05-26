# Habilidade: Context Setup (Carregamento de Memória)

Sempre que eu solicitar que você execute uma nova tarefa (Work Item), antes de tomar qualquer decisão ou gerar qualquer código, você DEVE realizar a seguinte rotina de carregamento de contexto:

1. **Leitura Obrigatória:**
   - Leia `@.github/copilot-instructions.md` para garantir o comportamento correto.
   - Leia `@.context/arquitetura.md` para validar os padrões de engenharia.
   - Leia `@.task/[work_item]/spec.md` e `@.task/[work_item]/plan.md` para entender o que deve ser feito.

2. **Verificação de Regras:** - Certifique-se de que o código gerado segue os padrões de `Type Hints`, `Clean Architecture` e `src-layout` definidos na arquitetura.

3. **Status:**
   - Ao iniciar, confirme brevemente: "Compreendi o contexto do projeto e o plano para este work item. Iniciando a execução dos passos."

4. **Governança de Qualidade:**
   - **Critérios de Aceite:** Todo `spec.md` DEVE conter uma seção "Critérios de Aceite".
   - **Verificação:** Todo `tasks.md` DEVE incluir, como última tarefa, um passo de "Verificação de Critérios de Aceite", onde você compara o que foi entregue com a seção de Critérios da `spec.md` e marca o checklist que existe no arquivo `spec.md`