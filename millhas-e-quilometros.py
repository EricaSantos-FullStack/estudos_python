#Tendo em mente que 1 quilómetro é aproximadamente igual a 0,6214 milhas, e que 1 milha é aproximadamente igual a 1.61 complete o programa no editor para que ele converta:

#milhas para quilómetros;
#quilómetros para milhas.

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles  / 0.62137
kilometers_to_miles = kilometers * 0.62137

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Output
#7.38 miles is 11.88 kilometers
#12.25 kilometers is 7.61 miles

#usando o round para arredondar e 2 para o numero de casas do float
