# 🚗 DM Cars: Sistema Web para Gestão de Revenda de Carros 🚗

<div align="center">
<img src="https://github.com/patresio/dm-cars/raw/master/.gitassets/capa.png" width="350" />  <div data-badges>
    <img src="https://img.shields.io/github/stars/patresio/dm-cars?style=for-the-badge" alt="GitHub stars" />
    <img src="https://img.shields.io/github/forks/patresio/dm-cars?style=for-the-badge" alt="GitHub forks" />
    <img src="https://img.shields.io/github/issues/patresio/dm-cars?style=for-the-badge" alt="GitHub issues" />
</div>

<div data-badges>
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt="python" />
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
    <img src="https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
    <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="bootstrap" />
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS" />
</div>
</div>

DM Cars é um sistema web completo e intuitivo, desenvolvido com Django para otimizar a gestão de revendas de carros.  Hospedado na AWS e utilizando PostgreSQL como banco de dados, o sistema oferece controle total do seu estoque e processos de venda, garantindo mais eficiência e organização para o seu negócio.

O objetivo principal do projeto é fornecer uma ferramenta robusta e fácil de usar para revendedores gerenciarem seus veículos, clientes, vendas e finanças de forma eficiente, permitindo que eles foquem no crescimento de seus negócios.

## 🖥️ Como rodar este projeto (Desenvolvimento Local) 🖥️

### Requisitos:

-   [Python](https://www.python.org/) instalado (versão X.X ou superior)
-   [pip](https://pip.pypa.io/en/stable/) (gerenciador de pacotes do Python)
-   [PostgreSQL](https://www.postgresql.org/) instalado

### Execução:

1.  Clone este repositório:

    ```sh
    git clone [https://github.com/patresio/dm-cars](https://www.google.com/search?q=https://github.com/patresio/dm-cars)
    ```

2.  Acesse o diretório do projeto:

    ```sh
    cd dm-cars
    ```

3.  Crie e ative um ambiente virtual:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # No Linux/Mac
    venv\Scripts\activate     # No Windows
    ```

4.  Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

5.  Configure o banco de dados PostgreSQL:

    -   Crie um banco de dados no PostgreSQL.
    -   Configure as variáveis de ambiente (ou o arquivo `settings.py`) do Django com as informações de conexão do banco de dados (nome, usuário, senha, host, porta).

6.  Execute as migrações do Django:

    ```sh
    python manage.py migrate
    ```

7.  Crie um superusuário (administrador):

    ```sh
    python manage.py createsuperuser
    ```

8.  Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

9.  Acesse o projeto em [http://localhost:8000](http://localhost:8000).

## 🗒️ Features do projeto 🗒️

-   Cadastro e gerenciamento detalhado de veículos (marca, modelo, ano, cor, quilometragem, etc.)
-   Controle de estoque completo (entrada, saída, disponibilidade, status, etc.)
-   Gestão eficiente de clientes (cadastro, histórico de compras, informações de contato)
-   Registro e acompanhamento preciso de vendas (data, valor, vendedor, forma de pagamento)
-   Geração de orçamentos e contratos personalizados
-   Relatórios abrangentes de estoque, vendas e desempenho (com filtros e exportação)
-   Controle financeiro básico (receitas, despesas, fluxo de caixa)
-   Gestão de usuários e permissões (controle de acesso baseado em funções)

<div align="center">
<img src="https://github.com/patresio/dm-cars/raw/master/.gitassets/2.jpg" width="80%" />  
</div>

## 💎 Links úteis 💎

-   [Documentação do Django](https://docs.djangoproject.com/en/4.2/)