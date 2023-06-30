Readme

Padrão Decorator - O que é.

O padrão Decorator é um padrão de design de software que permite adicionar 
funcionalidades a um objeto existente de forma dinâmica, sem alterar a estrutura 
básica desse objeto. Ele pertence à categoria dos padrões de design estruturais 
e é amplamente utilizado na programação orientada a objetos. 

Quando usar o Padrão Decorator?

O padrão Decorator é usado quando você quer adicionar funcionalidades extras 
a um objeto sem modificar sua estrutura básica. 
Ele permite estender as funcionalidades de um objeto de forma flexível, 
combinando diferentes decoradores. Isso evita a criação de muitas subclasses 
e preserva a interface original do objeto. 
É útil quando você precisa adicionar funcionalidades dinamicamente, 
de forma incremental e reutilizável.


Quais os Componentes do Padrão Decorator?

No padrão Decorator, temos quatro componentes principais: 
A interface, a classe original, o decorador abstrato e os decoradores concretos. 

1 - A interface define o contrato, 
2 - A classe original contém a lógica básica, 
3 - O decorador abstrato adiciona funcionalidades extras,
4 - Os decoradores concretos implementam essas funcionalidades. 

Os decoradores podem ser combinados para adicionar funcionalidades de forma flexível ao objeto decorado.

Prós

O padrão Decorator oferece flexibilidade na adição de funcionalidades, 
extensibilidade modular, preservação da interface original, reutilização 
de código e separação de preocupações.

Contras

O padrão Decorator pode adicionar complexidade ao código, resultar em muitos 
objetos pequenos, tornar difícil remover funcionalidades, causar efeitos colaterais 
indesejados e complicar o código base.

