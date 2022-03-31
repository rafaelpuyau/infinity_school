# Estilizando o Botão no React Native

O componente `<Button />` aceita poucas propriedades como o `title` e o `onPress`, mas **NÃO** aceita a 
propriedade `style`, o que torna a estilização deste componente muito difícil.

O máximo que conseguimos fazer, em termos de estilização é mexer na cor com a propriedade `color`.

Então, para criarmos um botão com estilo personalizavel, devemos utilizar o componente `<Pressable />`. Este
sim, é **totalmente** personalizavel, além de nos permitir, também, personalizar seu comportamento.

Vale lembrar que o estilo aplicado a este componente será o mesmo para dispositivos *Android*, *iOS* e na *web*,
o que permite uma aparência consistente em todas as plataformas.

