PIPELINE DE DADOS 
Documents/data-engineer/apache-airflow/orquestrando-pipeline1/data-pipeline/airflow-alura
um pipeline de dados, ou datapipeline, é uma série de etapas de processamento de dados.
Sendo que, cada etapa fornece uma saída que é a entrada para a próxima etapa. Isso vai acontecendo
até que o pipeline seja concluído. Além disso, também podem existir etapas independentes a serem 
executadas em paralelo.
A maioria dos pipelines possuem três elementos principais: a origem, uma ou mais etapas de processamento 
e o destino. Mas os pipelines de dados podem ser arquitetados de várias maneiras diferentes e tudo
vai depender do caso de uso.
O pipeline de dados que estamos desenvolvendo nesse projeto é simples e possui poucas etapas. No entanto,
os pipelines podem ficar bem complexos e com diferentes etapas dependendo do processamento que precisa ser
feito.

Para se aprofundar mais nesse assunto:
[What is a data pipeline](https://hazelcast.com/glossary/data-pipeline/) - Hazelcast
[What is a data pipeline](https://www.ibm.com/topics/data-pipeline) - IBM


-- principais passos do ambiente
1 - verificar a versão do python (instalar a venv)
2 - criar ambientevirtual e ativá-lo
4 - instalar airflow (pip3 install 'apache-airflow==2.3.2' --constraint "https://raw/githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"(versao)(arquivo de restrição))
5 - colocar o airflow no pathexecutar: airflow standalone (esse comando inicia o bd, criar um usuário)


## Apache Airflow
COMANDOS APACHE AIRFLOW
* Podemos executar cada um dos componentes do airflow de forma separada, tudo de forma manual. Mas podemos tbm usar um comando para executar tudo de forma automática: <br>
<code> airflow standalone </code>

### Conhecendo a interface do AirFlow

![Interface airflow 1](/img/interface-airflow1.png)

Interface que lista os DAGs
**Runs :** mostra o status de cada uma das execuções dos DAGs
**Schedule :** mostra o intervalo de agendamento de cada um dos DAGs
**Last Run :** mostra a data e horário do ultimo Dag Run
**Next Run :** mostra a próxima data e horário que o Dag Run vai executar
**Recent Tasks :** monstram as tarefas do DAG

Para saber mais sobre:
[Outras visualizações da interface](https://airflow.apache.org/docs/apache-airflow/2.3.2/ui.html)

DAG - Directed Acyclic Graphs (Grafos Acíclicos Dirigidos) <br>
*Directed -* quer dizer que o fluxo de trabalho sempre vai se dar apenas em uma única direção. <br>
*Acyclic -* quer dizer que as tarefas não podem ter dependências entre si mesmas <br>
*Graphs -* ferramneta matemática com nós e arestas que conectam esses nós (que são as nossas tarefas)

para saber mais:
[airflow - entendendo os DAGs](https://www.alura.com.br/artigos/airflow-entendendo-dags)
[DAGs - documentação](https://airflow.apache.org/docs/apache-airflow/1.10.12/concepts.html#dags)

principal ideia do airflow é dividir uma tarfea grande em etapas.

#### OPERATORS
Operadores são classes python que encapsulam a lógica para fazer uma unidade de trabalho, ou seja, uma tarefa. Eles definem as ações que serão concluídas para cada unidade de trabalho e abstraem muito código que teríamos que escrever. Quando instanciamos um operador e passamos os parêmetros necessários, a instância desse operador passa a ser uma tarefa.

Existem muitos tipos diferentes de operadores disponíveis no Airflow e o trablaho que cada um faz varia muito. Alguns dos operadores mais usados são:
* **PythonOperator:** executa uma função python;
* **BashOperator:** executa um script bash;
* **KubernetesPodOperator:** executa uma imagem definida como imagem do docker em um pod do kubernetes;
* **SnowflakeOperator:** executa uma consulta em um banco de dados snowflake;
* **EmailOperator:** envia aum e-mail.

Um Airflow tem um conjunto muito extenso de operadores disponíveis. No entanto, se não existir um operador para seu caso de uso, você pode também criar os seus próprios operadores.

##### Características de um operador

Um operador possui 3 características principais:
1. **Idempotência:** independentemente de quantas vezes uma tarefa for executada com os mesmos parâmetros, o resultado final deve ser sempre o mesmo.
2. **Isolamento:** a tarefa não compartilha recursos com outras tarefas de qualquer outro operador.
3. **Atomicidade:** a tarefa é um processo indivisível e bem determinado.

Para mais informações sobre operators:
[Sobre operators](https://airflow.apache.org/docs/apache-airflow/2.3.2/concepts/operators.html)

##### Agendamento no Airflow
Um dos recursos mais fundamentais do Apache Airflow é a capacidade de agendar trabalhos. Dessa forma, é importante conhecermos alguns termos do Airflow que são relacionados ao agendamento:

* **Data de início (start date):** data em que o DAG começa a ser agendado. Essa data é o início do intervalo de dados que você deseja processar;

* **Intervalo de agendamento (schedule interval):** define o intervalo de tempo em que o DAG é acionado. Por exemplo, "@daily" significa que o DAG deve ser acionado todos os dias à meia-noite;

* **Intervalo de dados (data interval):** propriedade de cada DAG Run que representa o intervalo de tempo em que cada tarefa deve operar. Por exemplo, para um DAG agendado de dia em dia, cada intervalo de dados começará no início (00:00) e terminará no final do dia (23:59). A execução do DAG acontece no final do intervalo de dados;

* **Data lógica (logical date):** é a mesma do início do intervalo de dados. Não representa quando o DAG será realmente executado. Antes do Airflow 2.2, era chamada de data de execução.

É importante ressaltar que o DAG só é acionado após a data de início + o intervalo de agendamento, ou seja, no final do intervalo de dados. Por exemplo: se temos um DAG com a data de início igual a 13/09 e com o schedule interval igual a "@daily", indicando que ele deve ser executado todos os dias à meia noite, sua dinâmica de execução vai ser a seguinte:

![Scheduler](/img/dag-run-img.png)

Para mais informações:
[Scheduler](https://airflow.apache.org/docs/apache-airflow/2.2.3/concepts/scheduler.html)
[DAG Runs](https://airflow.apache.org/docs/apache-airflow/2.2.3/dag-run.html)


##### Jinja Templates - Templates Reference
É uma estrutura de modelagem em Python utilizada pelo Airflow como seu mecanismo de modelagem, o que nos transmite ter acesso à informação em tempo de execução. Há diversas variáveis que podem nos trazer dados em tempo de execução.

[Sobre variáveis dinâmicas](https://airflow.apache.org/docs/apache-airflow/2.3.2/templates-ref.html)

##### CRON Expressions

Quando queremos definir intervalos de tempo um pouco mais complexos para a execução do nosso DAG, o Airflow permite a utilização das chamadas Cron Expressions. A sintaxe delas consiste em 5 componentes:

![Cron Expression](/img/cron-expressions.png)

Sendo os valores possíveis para cada um desses componentes:

* minuto: 0-59;
* hora: 0-23;
* dia do mês: 1-31;
* mês: 1-12;
* dia da semana: 0-6 representando de domingo a sábado.

Se queremos que um DAG seja executado toda segunda-feira do mês, às 00h00. Por isso, passamos a seguinte Cron Expression para o parâmetro schedule_interval:
<code>schedule_interval = 0 0 * * 1</code>

Para saber mais:
[CRON Expression](https://en.wikipedia.org/wiki/Cron#CRON_expression)






