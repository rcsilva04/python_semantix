from pyspark import SparkConf, SparkContext
from operator import add

sc = spark.sparkContext

julho= sc.textFile('NASA_access_log_Jul95')
julho = julho.cache()

agosto = sc.textFile('NASA_access_log_Aug95')
agosto = agosto.cache()

# Quantidade de Hosts únicos
julho_hosts = julho.flatMap(lambda line: line.split(' ')[0]).distinct().count() # Realiza o split, aplica o distinct e Conta quantidade
agosto_hosts = agosto.flatMap(lambda line: line.split(' ')[0]).distinct().count()
total_hosts = julho_hosts + agosto_hosts # Soma as 2 variaveis acima

print('Quantidade de Hosts: %s' % total_hosts)

# Função para contar quantidade de erro 404
def func_erro_404(line):
    try:
        code = line.split(' ')[-2]
        if code == '404':
            return True
    except:
        pass
    return False

julho_404 = julho.filter(func_erro_404).cache()
agosto_404 = agosto.filter(func_erro_404).cache()

total_404 = julho_404 + agosto_404

print('Quantidade de Erro 404: %s' % total_404.count())


# Funcção para identificar 5 Endpoints que mais apresentou erro 404
def func_top5(z):
    endpoints = z.map(lambda line: line.split("u'")[0].split(' ')[0])
    contador = endpoints.map(lambda endpoint: (endpoint, 1)).reduceByKey(add)
    top = contador.sortBy(lambda pair: -pair[1]).take(5)
    
    print('Os 5 endpoints com mais erros 404')
    for endpoint, count in top:
        print(endpoint, count)
    return top


# Função para contar a quantidade de erros 404 por dia
def func_erros_dia(x):
    dias = x.map(lambda line: line.split('[')[1].split(':')[0])
    contador_dia = dias.map(lambda day: (day, 1)).reduceByKey(add).collect()
    
    print('Quantidade de erros 404 por dia:')
    for day, count in contador_dia:
        print(day, count)
    return contador_dia



# Função para contar o total de bytes
#def func_conta_bytes (y)
#    byte_julho = julho.map(lambda line: line.split(' ')[9])
#    byte_agosto = agosto.map(lambda line: line.split(' ')[9])

#    conta_bytes = byte_julho.flatMap(byte_julho).reduce(add)
    
#    print('Quantidade de bytes:')
#    for conta_bytes in contador:
#        print(conta_bytes)
#    return contador


func_top5(total_404) # Chama a funçao que apresenta os Top5 de Endpoints que apresentaram erro 404
func_erros_dia(total_404) # Executa a função para contar quantos erros 404 por dia
#func_conta_bytes()

sc.stop()