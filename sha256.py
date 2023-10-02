from hashlib import sha256, sha512, md5
import streamlit as st

st.set_page_config(
    layout='wide',
    page_title="Hashing",
    page_icon="🖥️"
)

st.write("""
<h1> HASHING </h1>
<img width="50" height="50" src="https://icongr.am/octicons/file-binary.svg?size=128&color=ffffff" />
""", unsafe_allow_html=True)

with st.expander(":red[**O QUE É?**]"):
    st.markdown("""
    #### É uma tecnica que pode ser usada para validação de informações,
    #### consulta de valores ou criptografar dados com tamanhos variaveis e 
    #### então transformalos em um codigo de tamanho fixo chamado de ‘valor hash’
    #### ou simplestente ‘hash’.
    """)
with st.expander(":blue[**POR QUE UTILIZAR?**]"):
    st.markdown("""
    #### A utilização das tecnicas de hashing são boas para verificar
    #### a integridade de arquivos e garantir a segurança de senhas,
    #### dos arquivos e das informações armazenadas dentro de um banco
    #### de dados ou para consultar valores duplicados.
    """)
with st.expander(":green[**FORMAS DE USO**]"):
    st.markdown("""
    #### Podemos utilizar o hash em bancos de dados na hora de armazenar dados sensiveis que só
    #### necessitem de uma validação do usuario e que o(s) gerenciador(es) do banco não necessita
    #### saber dela, senhas por exemplo.
    #### Consulta de informações, criase uma chave hash para cada informação.
    #### Tambem é possivel verifcar se um arquivo foi ou não alterado comparando o codigo hash
    #### dele antes e depois, pode-se utilizar sites como o VirusTotal que gera um codigo hash
    #### ao escanear um arquivo, onde podemos ver se o arquivo continua o mesmo.
    """)
with st.expander(":orange[**COMO UTILIZAR**]"):
    st.markdown("""
    #### A utilização de codigos hash podem ser facilmente implememntada em codigos
    #### de sistemas em diversas linguagens de programação seja Python, Java, C, etc.
    #### Ou diretamente pelo usuario em sites e sistemas que façam essa conversão.
    """)
    st.subheader(":gray[**==CODIGO EM PYTHON==**]")
    st.write("""
            <div display = "inline">
            <img width="50" height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />            
            </div>
""",
             unsafe_allow_html=True)
    st.code(language='python',
            body=r"""
                    import hashlib
                    m = hashlib.sha256()
                    m.update(b"Nobody inspects")
                    m.update(b" the spammish repetition")
                    m.digest()
                    #RESULTADO BINARIO
                    '\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
                    m.hexdigest()
                    #RESULTADO FINAL
                    '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
            """
            )

with st.expander(":violet[**FORMA COMO SERIA ARMAZENADA NO BANCO DE DADOS**]"):
    st.subheader("EXEMPLOS DAS FORMAS CRIPTOGRAFADA DE UMA INFORMAÇÃO COM FUNÇÕES HASH")
    st.text_input("Digite seu nome", key="NOME")
    st.text_input("Digite seu CPF", key="CPF")
    st.text_input("Digite uma Senha", key="SENHA")
    st.subheader("Função Hash SHA256", divider='rainbow')
    st.markdown('SHA-256 é usado como parte do processo de autenticação '
                 'de pacotes de software Debian GNU/Linux e no '
                 'padrão DKIM de assinatura de mensagens;')
    if st.session_state['NOME'] != '' and st.session_state['CPF'] != "" and st.session_state['SENHA'] != "":
        dicionario = {
            "Nome": st.session_state['NOME'],
            "CPF": sha256(f"{st.session_state['CPF']}".encode()).hexdigest(),
            "SENHA": sha256(f"{st.session_state['SENHA']}".encode()).hexdigest()
        }
        st.json(dicionario)

    st.subheader("Função Hash SHA512", divider='rainbow')
    if st.session_state['NOME'] != '' and st.session_state['CPF'] != "" and st.session_state['SENHA'] != "":
        dicionario = {
            "Nome": st.session_state['NOME'],
            "CPF": sha512(f"{st.session_state['CPF']}".encode()).hexdigest(),
            "SENHA": sha512(f"{st.session_state['SENHA']}".encode()).hexdigest()
        }
        st.json(dicionario)

    st.subheader("Função Hash MD5", divider='rainbow')
    if st.session_state['NOME'] != '' and st.session_state['CPF'] != "" and st.session_state['SENHA'] != "":
        dicionario = {
            "Nome": st.session_state['NOME'],
            "CPF": md5(f"{st.session_state['CPF']}".encode()).hexdigest(),
            "SENHA": md5(f"{st.session_state['SENHA']}".encode()).hexdigest()
        }
        st.json(dicionario)
