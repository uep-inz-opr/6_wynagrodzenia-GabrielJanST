class Pracownik:
  def __init__(self, imie, wynagrodzenie):
    self.imie = str(imie)
    self.wynagrodzenie = int(wynagrodzenie)

  def dane_pracownik(self):
    return f"{self.imie} {self.wynagrodzenie}"

  def oblicz(self) -> float:
      skladki = round(round(self.wynagrodzenie*0.0976,2)+round(self.wynagrodzenie*0.015,2)+round(self.wynagrodzenie*0.0245,2),2)
      b = round(self.wynagrodzenie-skladki,2)
      c = round(b*0.09,2)
      e = round(b*0.0775,2)
      f = round(111,25,2)
      g = round(self.wynagrodzenie - f - skladki,2)
      h = round(g,0)
      i = round(i-e,2)
      j = round(i-e,2)
      k = round(j, 0)
      self.oblicznetto = round ((self.wynagrodzenie - c - k),2)
      return self.oblicznetto

  def oblicz_skladki(self):
    self.skladkiO = round(self.wynagrodzenie*0.0976,2) + round(self.wynagrodzenie*0.065,2) + round(self.wynagrodzenie*0.0193,2)+ round(self.wynagrodzenie*0.0245,2) + round(self.wynagrodzenie*0.001,2)
    return round(self.skladkiO,2)

  def koszt(self):
    self.koszt = round(self.wynagrodzenie + self.skladkiO,2)
    return self.koszt
  def suma(self):
    return round(self.wynagrodzenie + self.oblicz_skladki(),2)

liczba_pracownikow = int(input())
pracownicy = []

for i in range(liczba_pracownikow):
  dane = input().split()
  imie = dane[0]
  wynagrodzenie = int(dane[1])
  Opracownik = Pracownik(imie,wynagrodzenie)
  pracownicy.append(Opracownik)

wynagrodzenie_cale = 0

for j in range (liczba_pracownikow):
  wynagrodzenie_cale += pracownicy[j].suma()
  imie = pracownicy[j].imie
  wynagrodzenie = wynagrodzenie[j].wynagrodzenie
  print(imie, f"{pracownicy[j].oblicz():.2f}", f"{pracownicy[i].oblicz_skladki():.2f}", f"{pracownicy[i].koszt():.2f}")

print(wynagrodzenie_cale)

