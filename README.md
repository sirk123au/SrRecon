#SrRecon
![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/followers/espadrine.svg?label=Follow) ![](https://img.shields.io/pypi/pyversions/requests.svg?label=python)

- SrRecon é uma ferramenta para efetuar um reconhecimento basico de um -site, analizando as portas, pagina admin, e subdominios do site, SrRecon vem com um podereço detector, que pode ser alterado por qual quer um.

[========]
###Imagem
![SrRecon Funcionando](https://i.imgur.com/zNvNZOU.jpg "SrRecon Funcionando")

[========]
###Características
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

[========]
###Instalação

- Baixe diretamente do github com:
- git clone https://github.com/Srblu3/SrRecon.git
- ou click aqui: [SrRecon](https://github.com/Srblu3/SrRecon/archive/master.zip "SrRecon")

[========]
###Uso
| OS  | LINHA DE COMANDO|
| ------------ | ------------ |
|             Linux:    | python3 SrRecon.py [IP/URL]|
|          Windows        |         python SrRecon.py [IP/URL]       |
|          MAC OR OTHER        |         python SrRecon.py [IP/URL]       |


[========]
###Requerimentos
- Bibliotecas [Socket](ttps://pypi.org/project/sockets/ "Socket"), Sys, OS, [Requests](https://pypi.org/project/requests/ "Requests"), [OpenSSL](https://pypi.org/project/pyOpenSSL/ "OpenSSL"), [SSL](https://pypi.org/project/ssl/ "SSL"), Signal.
- Python versão 2.x | 3.x.

[========]
###ChatLogs
    [18/05/2019] Correção do bug CMS.
    [18/05/2019] Correção bug SSL.
    [18/05/2019] Adicionado a Função HTTPS/HTTP detect.
    [18/05/2019] Adicionado a Função de Versão SSL.
    [18/05/2019] Adicionado a Admin Finder.
    [18/05/2019] Otimizado Admin Finder.
    [18/05/2019] Bug removido do SSL detect.
    [19/05/2019] Adicionado SubDominios Detect.
    [19/05/2019] Removido Bug do SSL detect²

