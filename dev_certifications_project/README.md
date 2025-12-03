# 🚀 Projeto CertDev 🚀

## 🇧🇷 Português (PT-BR)

O **CertDev** é uma aplicação web desenvolvida para ser um guia centralizado de certificações de tecnologia para desenvolvedores. O projeto oferece informações detalhadas sobre certificações relevantes, como AWS Cloud Practitioner, Google Analytics e PCEP, além de integrar um assistente inteligente (Google Gemini) para responder a perguntas dos usuários.

### ✨ Funcionalidades

- **Páginas Detalhadas de Certificações**: Informações claras e organizadas sobre as principais certificações de TI.
- **Assistente Inteligente**: Integração com a API do Google Gemini para responder a perguntas sobre tecnologia e carreira.
- **Interface Moderna e Responsiva**: Layout limpo e amigável para o usuário, construído com Bootstrap.
- **Navegação Intuitiva**: Estrutura de navegação simples para encontrar rapidamente as informações desejadas.

### 🛠️ Tecnologias Utilizadas

| Categoria    | Tecnologia | Descrição |
|:-------------| :--- | :--- |
| **Backend**  | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Linguagem principal para a lógica do servidor. |
| **Backend**  | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | Micro-framework web para construir a aplicação. |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | Estrutura semântica das páginas. |
| **Frontend** | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | Estilização personalizada e design. |
| **Frontend** | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | Interatividade e lógica no lado do cliente. |
| **Website**  | ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) | Framework para design responsivo e componentes de UI. |
| **API**      | ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E44AD?style=for-the-badge&logo=google&logoColor=white) | Modelo de IA para o assistente inteligente. |

### 📁 Estrutura do Projeto

```
dev_certifications_project/
│
├── 📄 app.py                # Arquivo principal da aplicação Flask (rotas e lógica)
│
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 style.css      # Folha de estilos principal
│   └── 📁 img/               # Imagens e ícones utilizados no site
│
└── 📁 templates/
    ├── 📄 model.html         # Template base com a estrutura principal (navbar, footer)
    ├── 📄 index.html         # Página inicial
    ├── 📄 gemini_page.html    # Página do assistente Gemini
    └── 📁 certifications/
        ├── 📄 aws_cloud.html
        ├── 📄 google_analytics.html
        └── 📄 pcep.html
```

### 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd dev_certifications_project
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Observação: Crie um arquivo `requirements.txt` com as dependências listadas abaixo).*
4.  **Configure a chave da API:**
    Crie um arquivo `.env` e adicione sua chave da API do Google Gemini:
    ```
    GEMINI_API_KEY="SUA_CHAVE_AQUI"
    ```
5.  **Execute a aplicação:**
    ```bash
    flask run
    ```
Acesse `http://127.0.0.1:5000` no seu navegador.

### 📦 Dependências

-   **flask**: Para o servidor web.
-   **google-generativeai**: Para interagir com a API do Gemini.
-   **python-dotenv**: Para gerenciar as variáveis de ambiente.
-   **markdown**: Para converter o texto de resposta do Gemini em HTML.


Instale todas com:
```bash
pip install flask google-generativeai python-dotenv markdown
```

***

## 🇺🇸 English (EN-US)

**CertDev** is a web application designed as a centralized guide for developer technology certifications. The project provides detailed information on relevant certifications such as AWS Cloud Practitioner, Google Analytics, and PCEP, and integrates an intelligent assistant (Google Gemini) to answer user questions.

### ✨ Features

- **Detailed Certification Pages**: Clear and organized information on key IT certifications.
- **Intelligent Assistant**: Integration with the Google Gemini API to answer questions about technology and careers.
- **Modern and Responsive Interface**: Clean, user-friendly layout built with Bootstrap.
- **Intuitive Navigation**: Simple navigation structure to quickly find desired information.

### 🛠️ Technologies Used

| Category     | Technology | Description |
|:-------------| :--- | :--- |
| **Backend**  | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Main language for server-side logic. |
| **Backend**  | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | Web micro-framework to build the application. |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | Semantic structure of the pages. |
| **Frontend** | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | Custom styling and design. |
| **Frontend** | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | Client-side interactivity and logic. |
| **Website**  | ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) | Framework for responsive design and UI components. |
| **API**      | ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E44AD?style=for-the-badge&logo=google&logoColor=white) | AI model for the intelligent assistant. |

### 📁 Project Structure

```
dev_certifications_project/
│
├── 📄 app.py                # Main Flask application file (routes and logic)
│
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 style.css      # Main stylesheet
│   └── 📁 img/               # Images and icons used on the site
│
└── 📁 templates/
    ├── 📄 model.html         # Base template with main structure (navbar, footer)
    ├── 📄 index.html         # Homepage
    ├── 📄 gemini_page.html    # Gemini assistant page
    └── 📁 certifications/
        ├── 📄 aws_cloud.html
        ├── 📄 google_analytics.html
        └── 📄 pcep.html
```

### 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone <REPOSITORY_URL>
    cd dev_certifications_project
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file with the dependencies listed below).*
4.  **Set up the API key:**
    Create a `.env` file and add your Google Gemini API key:
    ```
    GEMINI_API_KEY="YOUR_KEY_HERE"
    ```
5.  **Run the application:**
    ```bash
    flask run
    ```
Access `http://127.0.0.1:5000` in your browser.

### 📦 Dependencies

-   **flask**: For the web server.
-   **google-generativeai**: To interact with the Gemini API.
-   **python-dotenv**: To manage environment variables.
-   **markdown**: To convert Gemini's response text into HTML.

Install them all with:
```bash
pip install flask google-generativeai python-dotenv markdown
```