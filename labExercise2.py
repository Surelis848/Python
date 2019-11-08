integer=int(input('Enter an integer: '))
binary=''
new_integer=0
to_the_power=0

if (integer >= 0):
    while integer>0:
        number=integer%2
        binary=str(number)+binary
        integer=integer//2
print(binary)

for item in reversed(binary):
    new_integer+=(int(binary[-1]))*(2**to_the_power)
    to_the_power+=1
    binary=binary[:-1]
print(new_integer)