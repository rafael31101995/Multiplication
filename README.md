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
* Essa lista é ajustada, incluindo 0 para cada um dos espaços em branco. O exemplo refeito abaixo.
       
       
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

    