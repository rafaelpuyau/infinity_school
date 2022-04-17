# Atividade 01

## [ __HARD__ ]

### a. Crie 2 componentes, um Header (Header.js) e um Footer (Footer.js)

- Estrutura de diretórios:
    - `src/components`
- Estilização:
    - Header:
        - container:
            - paddingTop: 50
            - paddingBottom: 20
            - backgroundColor: navy
            - alignItems: center
        - headerText:
            - fontSize: 20
            - fontWeight: bold
            - color: #FFFFFF
    - Footer:
        - container:
            - backgroundColor: tomato
        - footer:
            - fontSize: 12
            - color: #FFFFFF
            - textAlign: center
            - paddingVertical: 16

### b. Importe esse 2 componentes para dentro do App.js deixando o Header no topo e o Footer na base da tela

- Status Bar como light
- Use a tag fragment
- Estilização do App.js:
    - container:
        - flex: 1
        - backgroundColor: #464646
        - alignItems: center
        - justifyContent: center