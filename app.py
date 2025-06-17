import streamlit as st
import google.generativeai as genai
import re 

#COnfigura Gemini
api_keys =  st.secrets("API_KEY")
genai.configure(api_key=api_keys)
model = genai.GenerativeModel("gemini-2.0-flash")

#Passa intruções para o Gemini
def get_movie_suggestions(user_input):
    """
    Gera sugestões de filmes com base na entrada do usuário usando o modelo Gemini.
    O prompt é projetado para encorajar uma saída estruturada para facilitar a análise.
    """
    prompt = f"""Sugira até 3 filmes com base na seguinte descrição ou preferência: '{user_input}'.
    Para cada filme, forneça o Título, Gênero e um Resumo.
    Formate cada sugestão exatamente como no exemplo abaixo, usando marcadores claros.
    Certifique-se de que cada seção (Título, Gênero, Resumo) comece com o marcador correspondente.

    Título: [Nome do Filme]
    Gênero: [Gênero do Filme]
    Resumo: [Breve Resumo do Filme]
    ---
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar sugestões de filmes: {str(e)}"

#Interface
#Título da aba
st.set_page_config(page_title="IA de Sugestão de Filmes", page_icon="🎬")

#Título da página
st.title("IA de Sugestão de Filmes")
# Descrição da aplicação
st.markdown("""
    Em dúvida de qual filme assistir!
    Peça uma sugestão a IA de sugestão de filmes integrada gemini!
""")

# Instrução para o usuário
user_preference = st.text_area(
    "Descreva o tipo de filme que você gostaria de assistir:",
    placeholder="Exemplo: Filmes do Romance",
    height=100
)

#Inicia a busca
if st.button("Buscar"):
    # Verifica se o usuário forneceu uma descrição
    if user_preference:
            #Busca sugestões de filmes
            raw_suggestions_text = get_movie_suggestions(user_preference)

            if "Erro" in raw_suggestions_text:
                st.error(raw_suggestions_text)
            else:
                st.subheader("Aqui estão algumas sugestões para você:")

                # Divide as sugestões usando o delimitador "---"
                # Filtra quaisquer strings vazias que possam resultar da divisão
                individual_suggestions = [s.strip() for s in raw_suggestions_text.split("---") if s.strip()]
                
                # Verifica se a IA retornou sugestões
                if not individual_suggestions:
                    st.warning("Não foi possível encontrar sugestões de filmes com base na sua descrição. Tente ser mais específico!")

                for suggestion_block in individual_suggestions:
                    # Exibe cada sugestão em uma caixinha separado
                    with st.container(border=True):
                        # Coloca o Título, Gênero e Resumo em seus devidos campos
                        title_match = re.search(r"Título:\s*(.*)", suggestion_block, re.IGNORECASE)
                        genre_match = re.search(r"Gênero:\s*(.*)", suggestion_block, re.IGNORECASE)
                        summary_match = re.search(r"Resumo:\s*(.*)", suggestion_block, re.IGNORECASE | re.DOTALL)

                        title = title_match.group(1).strip()
                        genre = genre_match.group(1).strip()
                        summary = summary_match.group(1).strip()

                        st.markdown(f"**Título:** {title}")
                        st.markdown(f"**Gênero:** {genre}")
                        st.markdown(f"**Resumo:** {summary}")
