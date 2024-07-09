def number_to_words(n):
    ones={
        0:"",
        1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'
    }
    teens={
        10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',
        15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'
    }
    tens={
        2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'
    }

    if 1<=n<10:
        return ones[n]
    elif 10<=n<20:
        return teens[n]
    elif 20<=n<100:
        return tens[n//10]+(ones[n%10] if n%10!=0 else '')
    elif 100<=n<1000:
        return ones[n//100]+'hundred'+('and'+number_to_words(n%100) if n%100!=0 else '')
    elif n==1000:
        return 'onethousand'
    return ''
    
def count_letters_in_words(limit):
    total=1000
    for i in range(1,limit+1):
        word=number_to_words(i)
        total+=len(word)
    return total
    
total=count_letters_in_words(1000)
print("Total number of letters from 1 to 1000 are", total)
