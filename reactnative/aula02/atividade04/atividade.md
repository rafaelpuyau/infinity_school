# Atividade 02

## [ __EASY__ ]

### a. Criar um componente chamado __MeuComponente.js__ na raiz do projeto

- A estrutura desse componente será um card com o título _Infinity School_ e com o texto _Criando aplicações mobile para Android e iOS_
- Dentro da constante _**styles**_ colocar as propriedades abaixo:
    - card:
        - backgroundColor: #F4EBDF
        - padding: 12
        - borderRadius: 3
        - marginVertical: 7
    - cardTitle:
        - fontSize: 18
        - fontWeight: bold
    - cardText:
        - color: #777777
        - fontSize: 14

### b. Depois do componente devidamente criado, importar o componente ScrollView do módulo react-native e MeuComponente de MeuComponente.js dentro de App.js

- Colocar a Status Bar com style light
- Colocar um título como _Meu App_ com a tag Text:
    - title:
        - color: #FFFFFF
        - fontSize: 24
        - marginBottom: 24
- Inserir apenas uma vez o MeuComponente
- Depois inserir 12x o MeuComponente e observar o comportamento dentro da ScrollView. 
    __OBS__: para efeitos didáticos, troque de ScrollView para apenas View e já o que acontece.