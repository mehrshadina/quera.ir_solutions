adad1, adad2 = map(int, input().split())
adad3, adad4 = map(int, input().split())

if (adad1.bit_length() > 4 or
    adad2.bit_length() > 4 or
    adad3.bit_length() > 4 or
    adad4.bit_length() > 4):
    print("ghar foro mirizad!")

kamtarin_zarb = min(adad1 * adad3, adad1 * adad4, adad2 * adad3, adad2 * adad4)
bishtarin_zarb = max(adad1 * adad3, adad1 * adad4, adad2 * adad3, adad2 * adad4)

niro = (1 >> (bishtarin_zarb & kamtarin_zarb)) | (bishtarin_zarb ^ kamtarin_zarb)

maghsom_bar_3 = (niro % 3 == 0)
tavane_2 = (niro & (niro - 1)) == 0 and niro > 0

natije = bishtarin_zarb * kamtarin_zarb if maghsom_bar_3 else abs(bishtarin_zarb - kamtarin_zarb) if tavane_2 else 0
print(natije)
