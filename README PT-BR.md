# ETL de um arquivo Excel (XLS)

ETL - Extract, Transform and Load, é o nome dado ao processo de extração de dados, transformação/formatação dos mesmos e, por fim, alimentar algum sistema de inteligência com esses dados.

### Sobre o projeto

Serviço freelance feito para uma empresa de consultoria de negócios em Foz do Iguaçu/Brasil que consistiu em automatizar a captura de dados financeiros e fluxo de caixa para carregar em uma plataforma de Business Intelligence.

### Etapa1 - Compreender como era feito o processo de analise de dados antes da automatização

Em reunião com os analistas financeiros da empresa de consultoria foi  mostrando que os mesmos de conectavam remotamente no computador  principal da Padaria e Cafeteria, acessavam o ERP (Sistema Comercial) do cliente e tiravam um relatório em XLS/Excel. Sendo assim, a partir disso era feita a análise e tratamento dos dados visualmente e manualmente para uma segunda planilha que posteriormente seria  lida por uma plataforma de business intelligence.

### Etapa2 - Minhas propostas de solução para automatizar a captura e formatação dos dados.

#### Melhor proposta para a automatização

Conversar com a empresa terceirizada que administrava o ERP do cliente para uma tentativa de obter acesso direto ao banco de dados com um usuário que apenas permitiria fazer SELECT QUERY. Posteriormente estudar as relações das tabelas e encontrar os dados, preparar um script query que seria implementado futuramente em Python que se conectaria diretamente ao servidor do banco de dados. Sendo assim, tendo uma automatização da captura de dados desde sua fonte.

#### Contraproposta caso a primeira não fosse possível

Negado a proposta (como foi o caso) pela a outra empresa terceirizada que detinha a administração do banco de dados, foi sugerido por mim que automatizássemos a partir do que já teriam controle, que foi explicado já na **Etapa1** deste mesmo README. Em outras palavras, foi desenvolvido um software em Python que teria como entrada o arquivo financeiro e de fluxo de caixa da Padaria e Cafeteria que era gerado por meio do ERP pelos analistas financeiros.

### Etapa3 - Entendendo os dados do arquivo XLS

Em reunião com os analistas financeiros, perguntei quais dados do relatório gerado pelo ERP eram pertinentes. Na imagem seguinte eu destaquei em **verde** as informações que me foram apontadas como importantes. 

#### Formato de Entrada:

![worksheetPart1](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/part1.png)

![worksheetPart2](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/part2.png)

**OBS:** O relatório original é inteiramente em português, eu traduzi propositalmente pro inglês para fins de tornar público de forma universal esse projeto.

**OBS²:** Os relatórios originais continham de 3000 a 4000 KBs (em torno de 30mil linhas de dados financeiros mensais), o arquivo disposto neste GitHub é apenas um exemplo com apenas 69 KBs.

![originalDiff](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/exemploKB.png)

#### Formato de Saída:

A saída foram dois arquivos em formato CSV para serem lidos automaticamente pela plataforma de business intelligence que a empresa de consultoria utiliza. 

O primeiro arquivo **Vendas por Produto.csv** (Sales by Product.csv) contendo respectivamente as seguintes informações: **código do produto** ; **descrição do produto** ; **unidade de medida** ; **data da emissão da venda** ; **hora da venda** ; **código do documento** ; **quantidade do item vendido** ; **preço do produto por unidade** ; **desconto no preço** ; **adição no preço** ; **valor final pelo produto**.

O segundo arquivo **Informação de Pagamento por Venda.csv** (Payment Info by Sales.csv) contendo respectivamente as seguintes informações: **data da emissão da venda** ; **hora da venda** ; **código do documento** ; **método de pagamento adotado** ; **valor pago neste método escolhido**.

Em ambos os arquivos encontra-se o campo **código do documento** para manter o relacionamento entre os dados.

### Etapa4 - Desenvolvimento do código em Python

Basicamente o software tem dois arquivos de código principais (por enquanto), o **`import_data.py`**, dentro do diretório /python_files, e o **`main.py`** no diretório raiz.

O primeiro arquivo citado é uma função geral que recebe como argumento o caminho do arquivo XLS, que contem todas as regras de captura dos dados, tal como outras funções locais mantendo organização do código e boas práticas para futuras manutenções facilitadas.

Já o segundo arquivo (**`main.py`**) contem as regras de escrita e saída do arquivo final depois que recebe o retorno do resultado da função inserida no **`import_data.py`**. Sim, pra manter a legibilidade e boas práticas, eu poderia ter criado outro arquivo Python com funções de escrita do arquivo de saída, mas como o programa é pequeno, não achei pertinente.

Dentro desse projeto será encontrado um arquivo chamado **`pers.py`** dentro do diretório /config que eu usaria pra comunicar com o banco de dados caso a empresa terceirizada tivesse fornecido o acesso de consulta ao banco diretamente.

### Etapa5 - Arquivos de saída em CSV

Como já foi explanado na **Etapa3**/Formato de Saída desde README, os arquivos de saída deveriam sair na ordem pedida pelos analistas financeiros da empresa de consultoria, eis o resultado, da forma que foi solicitado:

**Vendas por Produto.csv** (Sales by Product.csv)

![individual_output](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/individual_output.png)



**Informação de Pagamento por Venda.csv** (Payment Info by Sales.csv)

![payment_output](https://github.com/thplira/ETL-from-XLS-Excel-File-BakeryCoffeeShop-/blob/master/github-img/payment_output.png)



Ambos arquivos, apesar da imagem mostrar em planilha (por conta da regra do CSV), são arquivos texto puros. Sendo assim, não contendo nenhum meta-dado que normalmente planilhas em XLS/XLSX contêm e aumentando a velocidade de processamento das plataformas de business intelligence lerem seu conteúdo.



### Etapa6 - Possíveis próximos passos

Caso eu consiga o acesso direto ao banco de dados do cliente, poderei trabalhar numa função paralela a aquela que captura os dados do XLS e implementarei SELECT QUERYs direto no Python em comunicação com o banco de dados para tratar os dados direto da fonte. Assim, diminuindo ainda mais a necessidade de interação homem-maquina, que atualmente ainda retiram o relatório do ERP "manualmente".

