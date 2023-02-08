# Data Pipeline With Apache Airflow

### Apache Airflow
É uma ferramenta que nos permite automatizar o pipeline de dados. </br>
Podemos desenvolver nosso datapipeline no airflow e agendar sua execução de forma automática.

* Ferramenta open source
* Orquestrador de fluxos
* cria, agenda e monitora data pipelines

Principais características

* Dinâmico
* Extensível
* Escalável
* Elegante
* Interface Web

Casos de uso comuns do Airflow

* Desenvolvimentos de pipelines ETL/ELT
* Treinamento de modelos de Machine Learning
* Geração de relatórios automatizada
* Backups automáticos

Principais conceitos da ferramenta

*DAG* 
é um fluxo de trabalho, um pipeline de dados definido em python que trata-se de um </br>
conjunto de instruções que precisam ser executadas em uma determinada ordem. Ao definirmos um data pipeline no Airflow, este passa a ser um DAG.


*Task*
É a unidade mais básica de um DAG e é utilizada para implementar uma determinada lógica no pipeline. Podemos afirmar, portanto, que um DAG também é um conjunto de tasks onde cada uma dessas tarefas corresponde a uma etapa que precisa ser realizada no pipeline de dados.

*DAG run*
ou "execução de DAG" , trata-se da execução propriamente dita de um DAG no tempo. Este DAG run inclui algumas informações sobre a execução do DAG, entra elas podemos citar o horário e tempo de execução de cada tarefa. Em suma, trata-se da instância de um DAG no tempo.

*Task instance*
ou "instância de tarefa" , é a execução de uma tarefa em um ponto específico do DAG. Além disso, quando trabalhamos com DAGs, interagimos principalmente com *_operators_* (operadores), que são os blocos de construção de um DAG. Esses operators contêm a lógica de como os dados são processados em um data pipeline e cada tarefa é definida justamente pela instanciação de um operador.
 

