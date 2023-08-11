from Extract_Carros import ExtractCarro 



if __name__ == '__main__':
    urls = ExtractCarro.filtros_carro('DF','Corolla')
    ExtractCarro.extrair_carro(urls)
