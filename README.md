# project-jerseys-control
Stock management system built with Django to manage football jersey sales and inventory

Checklist:

- Requisitos

- Criar o MER

- Fazer diagrama UML

- Protótipagem no Figma

- Criação do backlog (quebrar em partes menores)

- Codificação

Requisitos funcionais do projeto:


O sistema não precisaria de login a principio. A ideia é que o usuário comum possa utilizar o sistema como uma espécie de catálogo. Por outro lado, o admin terá o seu login para que ele possa ter acesso a funcionalidades especificas.

O admin terá acesso a aba de dashboards, onde seria possível filtrar o período (ultimos 8 7 dias, ultimos 20 dias..), ver o valor em estoque, entradas no período e saídas no período. Ainda, abaixo desses KPIs, será possível visualizar as saídas diárias (no período filtrado) por meio de um gráfico de barras. Abaixo do gráfico de barras, seria possível ver os produtos que estão com estoque baixo (<= 2), os produtos estagnados (ou seja, que não tem nenhuma saída nos últimos 20 dias) e também os 3 produtos mais vendidos.

Na aba Clubes, o admin poderá criar clubes (categorias) e colocar dentro de cada um deles, os produtos referentes àquele clube. Isso é importante pois assim na aba de produtos, poderá ter o filtro de clube. SOMENTE O ADMIN TERÁ ACESSO A ESSA PARTE

Na aba Produtos, teriam os cards dos produtos, com imagens. O usuário poderá clicar no card para visualizar detalhes do produto, como descrição, tipo, preço e dentre outros. Além disso, ao clicar no card do produto, teriam videos ou então mais imagens do produto. O usuário poderia filtrar o clube que ele quer ver a camisa. 

O admin poderá adicionar produtos, que terão clube, modelo, tamanho, tipo (Casa ou fora) quantidade e preço da venda. Além disso, cada produto terá uma imagem ou então um video associada a ele. O admin poderá ainda editar os dados de um produto, sendo primordial que ele possa editar a quantidade e o preço. O admin também poderá excluir um produto ou então ocultá-lo se quiser. Quando um produto tiver acabado a quantidade, a imagem do seu card ficará cinza

Na aba movimentação, o admin poderá ver uma listagem com as movimentações, onde seria possível ter a Data, o tipo (saida ou entrada), o produto, a quantidade e o valor unitário. Nessa aba teria o filtro de data para visualizar a data da movimentação e até mesmo o filtro de Clube, para ver as movimentações de camisa de determinado clube. Nessa aba ainda teria um botão onde seria possível realizar uma nova movimentação (entrada ou saída), que deverá atualizar a quantidade do produto lá na aba Produtos, além de atualizar os dados na aba de dashboard. Além disso, se ao realizar um nova movimentação, a quantidade de produtos que sairem for maior que a quantidade de produtos disponiveis, terá que levantar um erro


A ideia é que além de ser uma gestão de estoque, que seja como uma especie de catálogo para os usuários comuns poderem olhar os produtos
