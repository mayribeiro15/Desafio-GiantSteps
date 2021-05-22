def validate_line(ticker, side, qty):
    cod_error=[0,0,0,0,0]

    if(side!='BUY' and side!='SELL'):
        cod_error[0]=1

    if(qty.isnumeric()):
        if(int(qty)<=0):
            cod_error[1]=1
        if(int(qty)%10!=0):
            cod_error[2]=1
    else:
       cod_error[3]=1

    if(len(ticker)==5 or len(ticker)==6):
        if(ticker[:4].isalpha()==False or ticker[4:].isnumeric()==False): cod_error[4]=1
    else:
        cod_error[4]=1

    return cod_error

def print_results(ticker_list, error_list):
    print("\nTotal de compra e venda por ativo:")
    for key in ticker_list:
        print("•",key,":", ticker_list[key])
    print("\nLinhas inválidas:")
    if (error_list==[]): print("Nenhuma")
    for key in error_list:
        original_line=key[0]
        cod_error=key[1]
        print("•",original_line,"\n"," ◦",end="")
        if(cod_error[0]==1):
            print(" Valor inválido de SIDE;", end="")
        if(cod_error[1]==1):
            print(" QTY não é positivo;", end="")
        if(cod_error[2]==1):
            print(" QTY não é múltiplo de 10;", end="")
        if(cod_error[3]==1):
            print(" QTY não é um número;", end="")
        if(cod_error[4]==1):
            print(" TICKER mal formatado;", end="")
        print("")
    print("")

ref_arquivo = open("gotham_op.txt","r")
ticker_list = dict()
error_list = []

for line in ref_arquivo:
    line = line.rstrip('\n')
    strings = line.split(';')
    strings = [i.split(':') for i in strings]
    
    side=strings[0][1]
    qty=strings[1][1]
    ticker=strings[2][1]

    cod_error=validate_line(ticker, side, qty)

    if(cod_error==[0,0,0,0,0]):
        if ticker in ticker_list:
            if(side=='BUY'): ticker_list[ticker]+=int(qty)
            if(side=='SELL'): ticker_list[ticker]-=int(qty)
        else:
            if(side=='BUY'): ticker_list[ticker]=int(qty)
            if(side=='SELL'): ticker_list[ticker]=-int(qty)
    else:
        error_list.append([line,cod_error])

print_results(ticker_list, error_list)

ref_arquivo.close()
