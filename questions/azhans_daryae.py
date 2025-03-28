maliat = {
    "1": 5, "2": 10, "3": 20, "4": 15 
}

code_haye_mojaz = {"12", "21", "13", "31", "41", "14", "23", "32", "34", "43"}

code = input().strip()

if code not in code_haye_mojaz:
    print("Your request was not found in the system.")
else:
    gheymat_belit = 20 + maliat[code[1]] if code in {"14", "41"} else 10 + maliat[code[1]]
    
    vazn = float(input().strip())

    if vazn > 50:
        print(f"the cost of your ticket is {gheymat_belit} $.")
        print("sorry, We are unable to accept your luggage.")
    else:
        hazine_bar = (
            0 if vazn == 0 else
            10 if vazn <= 10 else
            20 if vazn <= 20 else
            int(20 + ((vazn - 20) * 2)) if (20 + ((vazn - 20) * 2)) % 1 == 0 else float(f"{20 + ((vazn - 20) * 2):.1f}")
        )
        
        hazine_nahaee = gheymat_belit + hazine_bar
        
        print(f"the cost of your ticket is {gheymat_belit} $.")
        print(f"the cost of your luggage is {hazine_bar} $.")
        print(f"you have to pay : {hazine_nahaee} $")
