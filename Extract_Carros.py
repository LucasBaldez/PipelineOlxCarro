import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import time



class ExtractCarro():

    hoje = datetime.datetime.now()
    ano = hoje.strftime('%Y')
    
    #Função para montar o caminho da url com os filtros de estado, carro e anos desejados
    def filtros_carro(uf,carro):
        urls = []
        for number in range(1,30):
            url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-'+ uf.lower() +'?o='+ str(number)+'&q='+carro                 
            urls.append(url)
            
        return urls

    #Função para extrair os carros que foram encontrados no OLX
    def extrair_carro(urls):
        
        get_urls = urls
        venda_carros = []
        headers = {'user-agent': 'Chrome/115.0.5790.171'}
        
        for url in get_urls:

            response = requests.get(url, headers=headers)
            site = BeautifulSoup(response.content, 'html.parser')
            time.sleep(3)
            carros = site.find_all('section', attrs={'class': 'horizontal undefined sc-ejGVNB jrGpJY'})            

            for carro in carros:
                titulo = carro.find('h2').text
                link = carro.find('a')['href']
                if carro.find('h3') == None:
                    preco = ''
                else:
                    preco = carro.find('h3').text
                local = carro.find('p', attrs={'class': 'sc-ifAKCX iOyFmS'}).text
                pagina = url

                #armazena os registros dos carros a venda em um dicionário
                info_carros ={
                    'titulo' : titulo,
                    'preco' : preco,
                    'local' : local,
                    'link' : link,
                    'pagina' : pagina
                
                }
                #armazena todos os registro dos carros na lista venda_carros
                venda_carros.append(info_carros)
            
        #cria dataframe com os dados
        df_carros = pd.DataFrame(venda_carros)
        df_carros.to_excel('Planilhas/carrosOLX.xlsx', index=False)
           
                

if __name__ == '__main__':
    paths = ExtractCarro.filtros_carro('DF','Palio')
    #print(paths[0])
    ExtractCarro.extrair_carro(paths)

    
    

