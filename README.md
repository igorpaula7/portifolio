# Portifolio

![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-639?logo=css&logoColor=fff)

## Escopo do Projeto

Desenvolvimento de portifolio usando o framework Django para exibição de meus projetos.

## Tecnologias Utilizadas

(em desenvolvimento)

## Como Usar

(em desenvolvimento)

## Principais Funcionalidades

- CRUD de projetos;
- Manutenção do portifolio via django admin

## Requisitos

(em desenvolvimento)

## Modelagem de dados

```mermaid
classDiagram

    class Projeto {
        +str titulo
        +str descricao
        +str link_repositorio
        +int linguagem_id
    }

    class Linguagem {
      +str titulo
      +str cor_hexadecimal
    }

  Projeto <|-- Linguagem

  note for Linguagem "um projeto pode ter várias linguagens"
```

## Links Úteis

(em desenvolvimento)
