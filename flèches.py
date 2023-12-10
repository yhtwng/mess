N = [[4,1],[5,4],[1,3]]
S = [[1,4],[0,2]]
E = [[1,0],[2,3]]
O = [[4,5],[2,5]]
NE = [[3,0],[5,0]]
SO = [[0,5]]
NO = [[3,5]]
SE = [[4,3]]

from tkinter import Tk
from tkinter import Canvas

def td(n):
    tableau = []
    for i in range(n):
        for j in range(n):
            case = [i,j]
            tableau.append(case)
    cases_vides = []
    cases_pleines = N + S + E + O + NE + SO + NO + SE
    cases_jetons = []
    nb_cases_pleines = len(cases_pleines)
    for cases in cases_pleines: #cas flèche en dehors du tableau
        if cases[0]<0 or cases[0]>=n or cases[1]<0 or cases[1]>=n:
            return False
        i = 0 #cas plusieurs flèches à la même case
        for j in range (nb_cases_pleines):
            if cases_pleines[j] == cases :
                i += 1
            if i > 1:
                return False
    for cases1 in tableau :
        if cases1 not in cases_pleines:
            cases_vides.append(cases1)
    for cases in cases_vides :
        nb = 0 #nb de flèches qui le pointent
        for casesN in N : #pour le Nord
            if cases[1]==casesN[1] and cases[0]<casesN[0]:
                nb += 1
        for casesS in S : #pour le Sud
            if cases[1]==casesS[1] and cases[0]>casesS[0]:
                nb += 1
        for casesE in E : #pour l'Est
            if cases[0]==casesE[0] and cases[1]>casesE[1]:
                nb += 1
        for casesO in O : #pour l'Ouest
            if cases[0]==casesO[0] and cases[1]<casesO[1]:
                nb += 1
        for casesNE in NE : #pour le NordEst
            if cases[0]+cases[1]==casesNE[1]+casesNE[0] and cases[0]<casesNE[0] and cases[1]>casesNE[1]:
                nb += 1
        for casesSO in SO : #pour le SudOuest
            if cases[0]+cases[1]==casesSO[1]+casesSO[0] and cases[0]>casesSO[0] and cases[1]<casesSO[1]:
                nb += 1
        for casesNO in NO : #pour le NordOuest
            if cases[0]+casesNO[1]==cases[1]+casesNO[0] and cases[0]<casesNO[0] and cases[1]<casesNO[1]:
                nb += 1
        for casesSE in SE : #pour le SudEst
            if cases[0]+casesSE[1]==cases[1]+casesSE[0] and cases[0]>casesSE[0] and cases[1]>casesSE[1]:
                nb += 1
        if nb >= 3:
            cases_jetons.append(cases)
    print(cases_jetons)
        
    window = Tk()
    window.geometry("1000x1000")
    window.configure(background = "grey")
    window.title("Schéma")
    window.resizable(True, True)
 
    canvas = Canvas(width = 100*n, height = 100*n, bg = "white")
    canvas.pack(padx = 50, pady = 50)
    for case in tableau: #création des cases
        canvas.create_rectangle(case[1]*100, case[0]*100, (case[1]+1)*100, (case[0]+1)*100)
        if case in N : #création des flèches Nord
            canvas.create_line((case[1]+1/2)*100, (case[0]+1)*100, (case[1]+1/2)*100, case[0]*100, arrow='last')
        if case in S : #création des flèches Sud
            canvas.create_line((case[1]+1/2)*100, case[0]*100, (case[1]+1/2)*100, (case[0]+1)*100, arrow='last')
        if case in E : #création des flèches Sud
            canvas.create_line(case[1]*100, (case[0]+1/2)*100, (case[1]+1)*100, (case[0]+1/2)*100, arrow='last')
        if case in O : #création des flèches Ouest
            canvas.create_line((case[1]+1)*100, (case[0]+1/2)*100, (case[1])*100, (case[0]+1/2)*100, arrow='last')
        if case in NE : #création des flèches NordEst
            canvas.create_line(case[1]*100, (case[0]+1)*100, (case[1]+1)*100, (case[0])*100, arrow='last')
        if case in SO : #création des flèches SudOuest
            canvas.create_line((case[1]+1)*100, case[0]*100, case[1]*100, (case[0]+1)*100, arrow='last')
        if case in NO : #création des flèches NordOuest
            canvas.create_line((case[1]+1)*100, (case[0]+1)*100, case[1]*100, case[0]*100, arrow='last')
        if case in SE : #création des flèches SudEst
            canvas.create_line(case[1]*100, case[0]*100, (case[1]+1)*100, (case[0]+1)*100, arrow='last')
    for case in cases_jetons :
        canvas.create_oval(case[1]*100, case[0]*100, (case[1]+1)*100, (case[0]+1)*100, fill='red')
    window.mainloop()
