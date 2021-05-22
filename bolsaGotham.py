ref_arquivo = open("gotham_op.txt","r")
print("\nLinhas inválidas:")
ticker_list = dict()
erro=0

for line in ref_arquivo:
    #PROCESSING
    original_line=line.rstrip('\n')
    line = line.split(';')
    line = [i.split(':') for i in line]
    side=line[0][1]
    qty=line[1][1]
    ticker=line[2][1].rstrip('\n')
    
    ticker_error=0
    qty_error1=0
    qty_error2=0
    qty_error3=0
    side_error=0

    #VERIFY TICKER
    if(len(ticker)==5 or len(ticker)==6):
        if(ticker[:4].isalpha()==False or ticker[4:].isnumeric()==False): ticker_error=1
    else:
        ticker_error=1

    #VERIFY QTY 
    if(qty.isnumeric()):
        if(int(qty)%10!=0):
            qty_error1=1
        if(int(qty)<=0):
            qty_error2=1
    else:
       qty_error3=1 

    #VERIFY SIDE && ADD QTY
    if(side!='BUY' and side!='SELL'):
        side_error=1

    if(ticker_error==0 and qty_error1==0 and qty_error2==0 and side_error==0):
        if ticker in ticker_list:
            if(side=='BUY'): ticker_list[ticker]+=int(qty)
            if(side=='SELL'): ticker_list[ticker]-=int(qty)
        else:
            if(side=='BUY'): ticker_list[ticker]=int(qty)
            if(side=='SELL'): ticker_list[ticker]=-int(qty)
    else:
        erro=1
        print("•",original_line,"\n"," ◦",end="")
        if(side_error!=0):
            print(" Valor inválido de SIDE;", end="")
        if(qty_error2!=0):
            print(" QTY não é positivo;", end="")
        if(qty_error1!=0):
            print(" QTY não é múltiplo de 10;", end="")
        if(qty_error3!=0):
            print(" QTY não é um número;", end="")
        if(ticker_error!=0):
            print(" TICKER mal formatado;", end="")
        print("")

if (erro==0): print("Nenhuma")
print("\nTotal de compra e venda por ativo:")
for key in ticker_list:
    print("•",key,":", ticker_list[key])
print("")

ref_arquivo.close()
