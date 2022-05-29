class Pracownik:
  def __init__(self, imie, wynagrodzenie):
    self.imie = str(imie)
    self.wynagrodzenie = int(wynagrodzenie)

  def rerp(self):
    return f"{self.imie} {self.wynagrodzenie}"

    self.imie = imie
    self.skladki = skladki
    self.zdrowotnaO = wynagrodzenie - skladki
    self.zdrowotnaD = wynagrodzenie - skladki
    koszt = 111,25
    self.koszt = koszt
    self.zdrowotnaO = zdrowotnaO
    self.zdrowotnaD = zdrowotnaD
    self.skladkaDoch = skladkaDoch
    self.skladkaZdr = skladkaZdr
    self.podatek = podatek
    self.wyplata = wyplata
    self.skladkiPrac = skladkiPrac
    self.lacznyKoszt = lacznyKoszt

  def oblicz_skladki(self, skladki) -> float:
      self.skladki = round(self.wynagrodzenie*0.0976,2)+round(self.wynagrodzenie*0.065,2)+round(self.wynagrodzenie*0.0193,2)+round(self.wynagrodzenie*0.0245,2)+round(self.wynagrodzenie*0.001,2)
      return round(self.skladki,2)
  def koszt(self):
      self.skladki = round(self.wynagrodzenie + skladki, 2)
      return self.koszt

  def suma(self):
      return round(self.wynagrodzenie + self.oblicz_skladki(),2)

  def oblicz_zdrowotnaO(self, zdrowotnaO) -> float:
    return '%.2f' %({self.zdrowotna} % 9)
  def oblicz_zdrowotnaD(self, zdrowotnaD) -> float:
    return '%.2f' %({self.zdrowotna} % 7,75)
  def oblicz_skladkaDoch(self, skladkaDoch) -> float:
    return '%.2f' %({self.wynagordzenie} - {self.koszt} - {self.skladki})
  def oblicz_skladkaZdr(self, skladkaZdr) -> float:
    return '%.2f' %(({self.skladkaDoch} % 18) - 46,33)
  def oblicz_podatek(self.podatek) -> float:
    return '%.2f' %({self.skladkaZdr} - {self.oblicz_zdrowotnaD})
  def oblicz_wyplate(self.wyplata) -> float:
    return '%.2f' %({self.wynagrodzenie} - {self.oblicz_skladke} - {self.oblicz_zdrowotnaO} - {self.oblicz_podatek})
  def oblicz_skladkePrac(self, skladkiPrac) -> float:
    return '%.2f' %sum({self.wynagrodzenie} % 9,76 + {self.wynagrodzenie} % 6,5 + {self.wynagrodzenie} % 1,93 + {self.wynagrodzenie} % 2,45 + {self.wynagrodzenie} % 0,10)
  def oblicz_lacznyKoszt(self.lacznyKoszt) -> float:
    return '%.2f' %({self.wynagrodzenie} + {self.oblicz_lacznyKoszt})

liczba_pracownikow = int(input())
pracownicy = []
def suma_wynagrodzenia(self):
    wynik = "{self.wynagrodzenie} + {self.skladki} {self.wynagrodzenie} {self.skladki} {self.koszt}"
    if sum > 0:
      wynik += sum
    else:
        sum = 0
    return wynik

