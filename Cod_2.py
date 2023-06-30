from abc import ABC, abstractmethod

# Componente base (interface do café)
class Cafe(ABC):
    @abstractmethod
    def getDescricao(self):
        pass
    
    @abstractmethod
    def getCusto(self):
        pass

# Implementação do Café Preto
class CafePreto(Cafe):
    def getDescricao(self):
        return "Café Preto"
    
    def getCusto(self):
        return 2.0

# Implementação do Café da Casa
class CafeDaCasa(Cafe):
    def getDescricao(self):
        return "Café da Casa"
    
    def getCusto(self):
        return 3.0

# Decorator base
class CafeDecorator(Cafe):
    def __init__(self, cafe):
        self.cafe = cafe
    
    def getDescricao(self):
        return self.cafe.getDescricao()
    
    def getCusto(self):
        return self.cafe.getCusto()

# Decorator de leite
class LeiteDecorator(CafeDecorator):
    def __init__(self, cafe):
        super().__init__(cafe)
    
    def getDescricao(self):
        return super().getDescricao() + ", Leite"
    
    def getCusto(self):
        return super().getCusto() + 0.5

# Decorator de açúcar
class AcucarDecorator(CafeDecorator):
    def __init__(self, cafe):
        super().__init__(cafe)
    
    def getDescricao(self):
        return super().getDescricao() + ", Açúcar"
    
    def getCusto(self):
        return super().getCusto() + 0.25

# Novo tipo de café: Café com Canela
class CafeComCanela(Cafe):
    def getDescricao(self):
        return "Café com Canela"
    
    def getCusto(self):
        return 3.5

# Exemplo de uso
if __name__ == '__main__':
    cafe = CafePreto()
    print(f"Descrição: {cafe.getDescricao()}")
    print(f"Custo: R${cafe.getCusto()}")

    cafe = CafeDaCasa()
    cafe = LeiteDecorator(cafe)
    cafe = AcucarDecorator(cafe)
    print(f"Descrição: {cafe.getDescricao()}")
    print(f"Custo: R${cafe.getCusto()}")

    cafe = CafeComCanela()
    cafe = LeiteDecorator(cafe)
    print(f"Descrição: {cafe.getDescricao()}")
    print(f"Custo: R${cafe.getCusto()}")
