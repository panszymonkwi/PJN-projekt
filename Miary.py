def Wyswietlenie_miar():
    print("\n------------------------------------ MIARY I WZORY ------------------------------------")
    print("Miary określające efektywność ekstrakcji informacji:")
    print("  Dokładność (ang. accuracy) - miara określająca jaka część ze zbioru wszystkich obiektów, które mogą być informacjami\
    została poprawnie zaklasyfikowana.")
    print(
        "  Precyzja (ang. precision) - miara określająca jaka część wydobytych informacji jest zgodna z rzeczywistością, czyli jest wydobyta poprawnie.")
    print(
        "  Czułość (ang. recall) - określa jaka część ze wszystkich poprawnych wyników została otrzymana w procesie wydobywania informacji.")
    print(
        "  Swoistość (ang. specificity) - określa jaką część ujemnych wyników wykrył klasyfikator. Swoistość jest odpowiednikiem czułości dla przypadków ujemnych.")
    print("  Wynik F1 (ang. F1-score)jest średnią harmoniczną precyzji i czułości, tworzy zrównoważony pomiar\
    dobrze określający wydajność modelu. Wynik F1 osiąga najlepszą wartość przy 1, a najgorszą przy 0.")

    print(
        "\nPojedynczy wynik testu - to określenie czy informacja należy do danej kategorii (wynik: dodatni), lub nie należy do niej (wynik: ujemny).")
    print(
        "Logiczne wyniki są rezultatem kombinacji dwóch możliwych wyników obserwacji oraz dwóch możliwych oczekiwanych wyników:")
    print("TP - wynik prawdziwie dodatni (true positive) oznacza, że w wyniku klasyfikacji dany obiekt został uznany za przynależący do danej kategorii\
    i w rzeczywistości faktycznie należy do tej kategorii.")
    print("FP - wynik fałszywie dodatni (false positive) oznacza , że w wyniku klasyfikacji dany obiekt został uznany za przynależący do danej kategorii,\
    ale w rzeczywistości do niej nie należy.")
    print("FN - wynik fałszywie ujemny (false negative) oznacza, że w wyniku klasyfikacji obiekt został uznany za nie przynależny do danej kategorii,\
    ale w rzeczywistości do niej należy. ")
    print("TN - wynik prawdziwie ujemny (true negative) oznacza, że w wyniku klasyfikacji obiekt został uznany za nie przynależący do danej kategorii,\
    co pokrywa się z faktycznym stanem w rzeczywistości")
    print("\nWZORY:")
    print("        accuracy    = (TP + TN)/(TP + TN + FP + FN)")
    print("        precision   = TP /(TP + FP)")
    print("        recall      = TP /(TP + FN)")
    print("        specificity = TN /(TN + FP)")
    print("        F1-score    = 2*(precision * recall)/(precision + recall)")
    print("\nPodsumowanie wyników testów")
    print("Wartości FP i FN są takie same , bo każda niepoprawnie wydobyta informacja oznacza jeden wynik fałszywie dodatni\
    i jeden wynik fałszywie ujemny, więc wartości precyzji i czułości też są takie same. ")
    print(
        "Przy wartości miary precyzji równej mierze czułości, wartość miary F1 jest równa miarom precyzji i czułości.")
    print("       precision =  recall = F1-score     w przypadku ekstrakcji informacji w danym projekcie")
    print("---------------------------------------------------------------------------------------")