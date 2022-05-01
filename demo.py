 
#Test the push command
try:
    with open('valutor.txt','r', encoding='utf8') as f:
        radet = f.readlines()
        valuta = {}
        for rad in radet:
            rad = rad.strip('\n')
            ord = rad.split()
            if len(ord) > 0:
                if ord[0] != '#':
                    if len(ord) == 3:
                        ord.insert(1,'eur')
                    ord[2] = ord[2].strip(',')
                    ord[-1] = float(ord[-1])
                    valuta[ord[2]]= ord[-1]
        
    with open('kurser.txt','r', encoding='utf8') as f:
        radet = f.readlines()
        kurser = {}
        for rad in radet:
            rad = rad.strip('\n')
            ord = rad.split()
            if len(ord) > 0 and len(ord) >2:
                ord[0] = ord[0].strip(',')
                if len(ord) > 4:
                    ord[1] = ord[1]+' '+ord[2]
                    ord[1] = ord[1].strip(',')
                if ord[-1] == 'USD':
                    kurser[ord[0]]= [(float(ord[-2])*float(valuta[ord[-1]])), ord[1]]
                else:
                    kurser[ord[0]]= [ord[-2],ord[1]]
    
    infilnamn = input("Chose one of the persom's files")
    with open(infilnamn,'r', encoding='utf8') as f:
        radet = f.readlines()
        företag = {}
        for rad in radet:
            rad = rad.strip('\n')
            ord = rad.split()
            if len(ord) > 0:
                if ord[0] == '#':
                    namn = ord[1]
                elif len(ord) == 2:
                    företag[ord[1]]= ord[0]
        
        total = 0
        print('************************************************')
        print('Läser portfölj: ', infilnamn)
        print('************************************************')
        print('Nuvarande värde i SEK')
        print('----------------------------------------------')
        for i,j in företag.items():
            värdet = float(j) * float(kurser[i][0])
            total = total + värdet
            company = kurser[i][1]
            print(f'  {float(j):8}  {company:13}{värdet:10.2f} SEK')
        print('----------------------------------------------')
        print(f'                    Summa: {total:.2f} SEK')           
except Exception as t:
    print(t)
    print(type(t))                
            