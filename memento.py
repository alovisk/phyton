class Memento:
  estadoTexto = ""
  def setMemento(self,string):
    if(string != ""):
      self.estadoTexto = string
  def getTextoSalvo(self):
    return self.estadoTexto

class TakerCareText:
  estados = []
  def adicionarMemento(self, memento):
        self.estados.append(memento)
  def getUltimoEstadoSalvo(self):
        if (len(self.estados) <= 0):
            return Memento()
        else:
          estadoSalvo = self.estados.pop()
          return estadoSalvo

class Texto:
    def __init__(self):
      self.caretaker = TakerCareText()
      self.texto = ""
    def escreverTexto(self,novoTexto):
        memento = Memento()
        memento.setMemento(self.texto)
        self.caretaker.adicionarMemento(memento)
        self.texto += novoTexto
    def desfazerEscrita(self):
        self.texto = self.caretaker.getUltimoEstadoSalvo().getTextoSalvo();
    def mostrarTexto(self):
        print(self.texto)
        
texto = Texto()
texto.escreverTexto("Primeira linha do texto\n");
texto.escreverTexto("Segunda linha do texto\n");
texto.escreverTexto("Terceira linha do texto\n");
texto.mostrarTexto();
texto.desfazerEscrita();
texto.mostrarTexto();
texto.desfazerEscrita();
texto.mostrarTexto();
texto.desfazerEscrita();
texto.mostrarTexto();
texto.desfazerEscrita();
texto.mostrarTexto();
texto.escreverTexto("Primeira linha do texto\n");
texto.escreverTexto("Segunda linha do texto\n");
texto.escreverTexto("Terceira linha do texto\n");
texto.mostrarTexto();
texto.escreverTexto("Terceira linha do texto\n");
texto.mostrarTexto();
texto.desfazerEscrita();
texto.mostrarTexto();
texto.desfazerEscrita();
texto.mostrarTexto();