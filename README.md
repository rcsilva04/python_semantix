### Qual o objetivo do comando cache em Spark?
A função `cache()` tem como objetivo armazenar em memoria o RDD criado no passo anterior. Como `chache()` é uma operação em lazy, o Spark não armazenará de imediato os dados na memória sendo alocados apenas após uma ação ser realizada no RDD. 
O uso correto agilizará o processamento, pois o Spark não precisará recalcular os RDDs anteriores caso venha a utiliza-lo novamente, e também é útil para caso de falha de alguma partição precisando reconstruir somente as partes faltantes.


### O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?
O Spark é maioria das vezes mais rápido que o MapReduce devido a forma de processamento. O MapReduce trabalha nas seguintes etapas, lê os dados do cluster, executa a operação e escreve o resultado de volta no cluster. Necessitando do alto uso da CPU e Disco, e para cada processo MapReduce é iniciado uma nova instância JVM.
Já o Spark utiliza a memória para fazer todo o processamento de dados reduzindo a necessidade de escrita e leitura em disco, chegando a proximidade de processamento real-time e trabalhando com a JVM de cada nó, já em execução.


### Qual é a função do SparkContext?
É o elo entre o programa e o cluster sendo objeto que conecta o Spark. Podendo ser acessado por uma variável dentro do programa para utilização das configurações dos seus recursos, como memória e processadores.


### Explique com suas palavras o que é Resilient Distributed Datasets (RDD)
RDD é unidade fundamental do Spark. É uma coleção de objetos distribuídos para apenas leitura e são imutáveis. O "R" vem de Resilient, onde os dados da memória que são perdidos podem ser recriados, ou seja, são tolerantes as falhas. O primeiro "D" é de Distribute e significa que os dados são armazenados na memória em diferentes nós através do cluster. O segundo "D" é de Dataset e quer dizer que os dados iniciais podem vir de um arquivo ou serem criados por meio de um programa. Há 3 formas de criar um RDD, podendo ser de um arquivo, da memória ou de outro RDD. E existem dois tipos de operações, o de Transformação que são operações que retornam um novo RDD utilizando Lazy Evolution como: função map, filter, distinct, union, subtract. E o segundo tipo de operação é de Ação, onde é retornado um valor para o driver ou escrever no storage. 


### GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
A forma de processamento é diferente entre ambos, quando há um grande dataset fica mais nítido essa diferença. No GroupByKey, os dados nas partições são embaralhados com todos os pares de chaves para formar uma lista de valores e depois agrupa-los. Já o ReduceByKey agregará os pares antes de embaralhar. O ReduceByKey combinará todos os seus pares de valores em outro valor exatamente do mesmo tipo em cada partição, tendo apenas uma saída para uma chave a ser enviado pela rede.


### Explique o que o código Scala abaixo faz.
1. *val textFile = sc.textFile("/home/usr_cec/Juzete/iris.csv")*
2. *val counts = textFile.flatMap(line => line.split(" "))*
3. *map(word => (word, 1))*
4. *reduceByKey(_ + _)*
5. *counts.saveAsTextFile("/home/usr_cec/Juzete/teste_scala.csv")*


Na linha 1 é utilizada uma variável imutável para vai receber os  dados do arquivo.
Na linha 2 também se faz uso de variável imutável que receberá da função `FlatMap()` um reduce no array multidimensional e retornará um array unidimensional havendo quebra de linha quando existir espaço.
Na linha 3 é usado a `função map()` que para cada Chave é recebido o Valor 1.
Na linha 4 a função `reduceByKey()` para combinar todos os seus pares de valores para obter apenas uma saída para cada Chave.
Na linha 5 é gravado em um arquivo as alterações realizadas pelo programa, como as quebras de linha.
