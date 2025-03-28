tol, bozorg, koochak = map(int, input().split())

if bozorg + koochak <= tol or koochak + tol <= bozorg or tol + bozorg <= koochak:
    print('Invalid triangle.')
else:
    nim_mohit = (tol + bozorg + koochak) / 2
    masahat = (nim_mohit * (nim_mohit - tol) * (nim_mohit - bozorg) * (nim_mohit - koochak)) ** 0.5
    masahat = round(masahat, 2)
    print(f'The area of the triangle is: {masahat:.2f}')

    if tol == bozorg == koochak:
        print('The triangle is a(n) equilateral triangle.')
    elif tol == bozorg or tol == koochak or bozorg == koochak:
        print('The triangle is a(n) isosceles triangle.')
    else:
        print('The triangle is a(n) scalene triangle.')

    if tol ** 2 == bozorg ** 2 + koochak ** 2 or bozorg ** 2 == tol ** 2 + koochak ** 2 or koochak ** 2 == tol ** 2 + bozorg ** 2:
        print('The triangle is also a right-angled triangle.')
    else:
        print('The triangle is not a right-angled triangle.')
