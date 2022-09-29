#test1=12353434.232
#print(str(test1))
def thous_s(test1):
    return ("{:,}".format(test1))

test1=12353434.232

print("The number after inserting commas:" + thous_s(test1))
#this method only for integer and no decimal
initial=197930775
thousand_sep = (format(initial, ',d'))
print("Number after inserting commas: " + str(thousand_sep))


print(f'{1592039502:,.2f}')