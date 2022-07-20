mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"21f3002717@student.onlinedegree.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = process.env.PORT||8000 \n\
" > ~/.streamlit/config.toml
