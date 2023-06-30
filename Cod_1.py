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

# Exemplo de uso
if __name__ == '__main__':
    cafe = CafePreto()
    print(f"Descrição: {cafe.getDescricao()}")
    print(f"Custo: R${cafe.getCusto()}")

    cafe = CafeDaCasa()
    print(f"Descrição: {cafe.getDescricao()}")
    print(f"Custo: R${cafe.getCusto()}")