class Memento:
  def __init__(self,string):
    self.string = string
  def getString(self):
    return self.string

class TakerCareText:
  estados = []
  def TextoCareTaker(self):
        estados = []
 
  def adicionarMemento(self, memento):
        self.estados.push(memento);
  
  def getUltimoEstadoSalvo(self):
        if (self.estados.size() <= 0):
            return ""
        else:
          estadoSalvo = self.estados.get(estados.size() - 1);
          self.estados.remove(self.estados.size() - 1);
          return estadoSalvo;

