x = 10
y = 20
ergebnis = 0 # globabe Variablen müssen AUSSERHALB der class sein (nicht wie globale var in c#)
class TestGlobalVariable:##  ha ha phython kann nix
    #x = 10   ###  sssoooooo nicht
    #y = 20
   # ergebnis = 0


    def Mannomann():
       ergebnis = x + y ## geht nicht da Variablen aussserhalb der func nicht gelesen werden können c# gewinnt....
       return ergebnis  ## geht wenn sie AUSSERHALB der Class sind - fucking shit confusing schittischeissssss

    print (Mannomann())
## muss mit __init___ oder so gemacht werden - das ist kacke