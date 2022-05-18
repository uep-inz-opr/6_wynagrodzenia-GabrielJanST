class Pracownik:
  def __init__(self, imie, wynagrodzenie, skladki, koszt):
    self.imie = imie
    self.wynagrodzenie = wynagrodzenie
    self.skladki = skladki
    self.koszt = koszt
    sum(wynagrodzenie)
  
  def __repr__(self):
    wynik = "{self.liczba} {self.nazwa} {self.wynagrodzenie} {self.skladki} {self.koszt}"
    if sum > 0:
      wynik += sum
    else:
        sum = 0
    return wynik

  def __gt__(self, obj):
    return self.dlugosc > obj.dlugosc

  def __eq__(self, obj):
    return self.dlugosc == obj.dlugosc

  def __len__(self):
    return self.dlugosc

#wstawic petle z pracownikami jako print
