# SrRecon

![](https://img.shields.io/badge/SrRecon-1.3B-blue.svg)
![](https://img.shields.io/pypi/pyversions/requests.svg?label=python)
![](https://img.shields.io/badge/update-20/05/2019-blue.svg)
![](https://img.shields.io/badge/last_update-20/05/2019-blue.svg)
![](https://img.shields.io/conda/pn/conda-forge/python.svg?color=blue&label=Plataformas&logo=blue&logoColor=blue)

- SrRecon é uma ferramenta de reconhecimento e scan de Sites. Esse scan analiza e mostra para o utilizador as portas abertas, CMS, Pagina Admin, Localização do servidor, tipo de servidor, qual linguagem que o servidor uitliza, e os Domínios que o servidor possui. Esse scan é poderoso que pode ser modificado por qual quer pessoa devido ter uma syntax 100% legível e Indentada.

# AVISO
   - Se achar algun erro ou poblema [Click aqui](https://github.com/Srblu3/SrRecon/issues "Click aqui") e crie um ISSUES!
   - Qual quer pobleminha crie um ISSUE. com o link acima.

# Imagem

![SrRecon Funcionando](https://i.imgur.com/Lc9gnHx.jpg "SrRecon Funcionando")


# Características

- Pega servidor primario DNS
- Verifica tipo de servidor ( privado ou aberto )
- HTTPS/HTTP detector
- Detecta SSL
- Detecta o tipo de criptrografia SSL
- Linguagem que é utilizada pelo host
- Tipo de servidor que é utilizado pela host
- Detecta CMS
- Detector de Portas
- Localiza a Host
- Admin finder
- SubDominio finder



# Instalação

- Baixe diretamente do github com:
- git clone https://github.com/Srblu3/SrRecon.git
- ou click aqui: [SrRecon](https://github.com/Srblu3/SrRecon/archive/master.zip "SrRecon")



# Uso

|         OS       | LINHA DE COMANDO                 |
| ---------------- | -------------------------------- |
|      Linux:      | python3 SrRecon.py [IP/URL]      |
|      Windows     | python SrRecon.py [IP/URL]       |
|     MAC OR OTHER | python SrRecon.py [IP/URL]       |



# Requerimentos

- Bibliotecas [Socket](ttps://pypi.org/project/sockets/ "Socket"), Sys, OS, [Requests](https://pypi.org/project/requests/ "Requests"), [OpenSSL](https://pypi.org/project/pyOpenSSL/ "OpenSSL"), [SSL](https://pypi.org/project/ssl/ "SSL").
- Python versão 2.x | 3.x.



# ChatLogs

   ```bash
    [18/05/2019] Correção do bug CMS.
    [18/05/2019] Correção bug SSL.
    [18/05/2019] Adicionado a Função HTTPS/HTTP detect.
    [18/05/2019] Adicionado a Função de Versão SSL.
    [18/05/2019] Adicionado a Admin Finder.
    [18/05/2019] Otimizado Admin Finder.
    [18/05/2019] Bug removido do SSL detect.
    [19/05/2019] Adicionado SubDominios Detect.
    [19/05/2019] Removido Bug do SSL detect².
    [19/05/2019] Adicionado mais SubDominios para serem detectados.
    [19/05/2019] Removido Bug do SubDomain Finder.
    [19/05/2019] Otimizado SubDomain Finder.
    [19/05/2019] Detectando Redirecionamento.
    [19/05/2019] Update 1.3 BETA.
    [19/05/2019] Adicionado novo banner, criado por Gabriel Paiva.
    [19/05/2019] Otimizado SubDomain Finder²
    [20/05/2019] Adicionado nova lista para SubDomain Finder.
    [20/05/2019] Adicionado nova lista para Admin Finder.
    [20/05/2019] Passando algumas funções para "def".
    [20/05/2019] Retirado biblioteca "Signal" devido não estar utilizando.
    
```
