# Mulplicação em formato escolar

#### Proposta
Abaixo temos o formato "escolar", a proposta do programa é copiar
a lógica do calculo, passo a passo.

          98765
        x 12345
    -----------
         493825
        395060
       296295
      197530
      98765
    -----------
     1219253925
     
#### Lógica, parte por parte
A lógica é bem parecida com o da proposta, porem com algumas alterações\ 
leves para facilitar a soma dos valores.

*  A multiplicação é feita normalmente, número por número. Ao final da multiplicação\
é gerada uma lista com os 5 números, ainda utilizando o exemplo na parte de proposta.
* Essa lista é ajustada, incluindo 0 para cada um dos espaços em branco.
O exemplo refeito abaixo.
       
Exemplo:       
       
          98765
        x 12345
    -----------
         493825
        3950600
       29629500
      197530000
      987650000
    -----------
     1219253925
     
* Feito isso, a lista é ordenada para que os maiores valores sejam os primeiros a serem somados. 
* A soma é sempre feita de dois em dois, ao final da soma, o resultado é incluido em uma nova lista\
porém, menor que a lista original pois os dois numeros somados não são inclusos nesta nova lista.\
Este processo é realizado varias vezes até a lista possuir um unico número, no caso o resultado.\
* Lembrando que ao longo do processo é realizado a soma invertida do valor.

#### As funções
Abaixo é listada as funções do programa e suas "funções".

* multiplication
    * Esta é a função principal, ela é utilizada para chamar as outras funções, para que os números sejam\
    calculados corretamente de acordo com a logica. Recebe dois parametros, o multiplicador e o multiplicando.
* check_if_is_negative
    * O nome é bem descritivo, porém ela vai um pouco além. Ela também nos da o resultado da multiplicação\
    de sinais, caso seja negativo com negativo, o resultado será positivo, caso seja negativo com positivo, o resultado,\
    será negativo.
* multipling_logic
    * Esta função tem toda a logica de multiplicação, nela é feita a multiplicação passo a passo, e seu retorno\
    será uma lista com o resultado de cada valor multiplicado.
* adjusting_list
    * Serve para incluir na lista que foi retornada pela função anterior, zeros ao final que cada número, exceto o primeiro da lista.
* making_sum
    * Esta função recebe a lista de valores, inverte a ordem dela e faz a soma de dois em dois e nos dá o resultado final.
* inverting_number_of_list
    * Inverte cada número da lista que recebe, e retorna uma lista com cada número invertido.
    
#### TDD - Test Driven Development
Ao final do programa temos os testes. O criterios de cada teste estão descritos a seguir.

* Teste de números exageradamente grandes.
* Teste de um número grande por zero.
* Teste do primeiro número negativo por um segundo número positivo.
* Teste de dois números negativos, resultado positivo.
* Teste de x < y. Primeiro número pequeno por um segundo número grande. 