# Data Pipeline With Apache Airflow

## Apache Airflow
É uma ferramenta que nos permite automatizar o pipeline de dados. É um orquestrador de fluxos, ou seja, com ele você é capaz de decidir qual momento e em quais condições algum programa seu irá rodar.
Podemos desenvolver nosso datapipeline no airflow e agendar sua execução de forma automática.


* Ferramenta open source
* Orquestrador de fluxos
* Cria, agenda e monitora data pipelines

### Principais características

* Dinâmico
* Extensível
* Escalável
* Elegante
* Interface Web

### Casos de uso comuns do Airflow

* Desenvolvimentos de pipelines ETL/ELT
* Treinamento de modelos de Machine Learning
* Geração de relatórios automatizada
* Backups automáticos

### Principais conceitos da ferramenta

**DAG** </br>
É um fluxo de trabalho, um pipeline de dados definido em python que trata-se de um conjunto de instruções que precisam ser executadas em uma determinada ordem. Ao definirmos um data pipeline no Airflow, este passa a ser um DAG.


**Task** </br>
É a unidade mais básica de um DAG e é utilizada para implementar uma determinada lógica no pipeline. Podemos afirmar, portanto, que um DAG também é um conjunto de tasks onde cada uma dessas tarefas corresponde a uma etapa que precisa ser realizada no pipeline de dados.

**DAG run** </br>
Ou "execução de DAG" , trata-se da execução propriamente dita de um DAG no tempo. Este DAG run inclui algumas informações sobre a execução do DAG, entra elas podemos citar o horário e tempo de execução de cada tarefa. Em suma, trata-se da instância de um DAG no tempo.

**Task instance** </br>
Ou "instância de tarefa" , é a execução de uma tarefa em um ponto específico do DAG. Além disso, quando trabalhamos com DAGs, interagimos principalmente com *_operators_* (operadores), que são os blocos de construção de um DAG. Esses operators contêm a lógica de como os dados são processados em um data pipeline e cada tarefa é definida justamente pela instanciação de um operador.

### Arquitetura do AirFlow
4 componentes principais que devem estar sempre em execução para que ele funcione corretamente

* **Web Server:** servidor em flask que serve para apresentar a interface de usuário do airflow que nos permite inspecionar, acompanhar o comportamento dos DAGs e suas tarefas;
* **Pasta de arquivos DAG:** armazena os aruqivos DAGs criados. Ela é lida pelo agendador e executor;
* **Schedule (agendador):** responsável pelo agendamento da execução das tarefas dos DAGs. Lida com o acionamento dos fluxos de trabalho (DAGs) agendados e o envio de tarefas para o executor;
* **Banco de dados:** usado pelo agendador, executor e webserver, e serve para armazenar todos os metadados e status do DAG e suas tarefas;
* **Executor:** é o mecanismo de execução das tarefas e é responsável para descobrir quais recursos são necessários para executar nossas tarefas.

Além destes principais, existem alguns componentes situacionais que são usados por alguns executores específicos apenas para executar tarefas ou fazer uso de determinados recursos. um deles:

* **Worker:** processo que executa as tarefas conforme definido pelo executor. Dependendo do executor escolhido, você pode ou não  ter workers (trabalhadores) como parte da infraestrutura do Airflow.

### Arquitetura
Todos esses componentes se relacionam de alguma maneira, formando a arquitetura do Airflow.

![Arquitetura airflow](/img/arquitetura-airflow.png)

#### Para saber mais:

[Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/2.3.2/) </br>
[Apache Airflow Project](https://airflow.apache.org/docs/apache-airflow/2.3.2/project.html) </br>
[Arquitecture Overview](https://airflow.apache.org/docs/apache-airflow/2.3.2/concepts/overview.html) </br>

