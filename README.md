<img width="1137" alt="image" src="https://github.com/user-attachments/assets/0096b5b8-e8ea-460c-995a-bf1c002d287d" />
# 🎬 IA de Sugestão de Filmes com Streamlit + Gemini

Este é um aplicativo web simples que utiliza o modelo **Gemini** (da Google) para gerar sugestões de filmes com base nas preferências do usuário. A interface foi construída com **Streamlit**, permitindo uma experiência interativa e direta no navegador.

---

## 💡 Funcionalidades

- Entrada de texto com as preferências do usuário (ex: gênero, estilo, tema do filme)
- Integração com o modelo Gemini da Google via API
- Geração de até 3 sugestões de filmes, contendo:
  - **Título**
  - **Gênero**
  - **Resumo**

---

## 🚀 Como Executar o Projeto

1. git clone https://github.com/seu-usuario/seu-repositorio.git
2. cd seu-repositorio
3. python -m venv venv
4. source venv/bin/activate  # Linux/macOS
5. venv\Scripts\activate     # Windows
6. pip install -r requirements.txt
7. CONFIGURA A API KEY:
genai.configure(api_key="SUA_CHAVE_AQUI")
8. streamlit run seu_arquivo.py
