# 📁 Pasta de Templates (`/templates`)

Este diretório é o coração da interface visual da aplicação. Ele contém todos os arquivos HTML que são renderizados pelo Flask e exibidos aos usuários.

---

## 🇧🇷 Português (PT-BR)

### 🎯 Propósito

A pasta `/templates` armazena a estrutura visual do projeto. O Flask, por padrão, procura arquivos HTML nesta pasta para renderizar as páginas. A organização e a padronização dos templates são cruciais para a manutenibilidade e a consistência do design.

### 🏛️ Arquitetura de Templates: Herança com `model.html`

Para evitar a repetição de código (como `head`, `navbar` e `footer`), utilizamos um sistema de **herança de templates** do Jinja2.

-   **`model.html`**: É o arquivo **pai**. Ele define a estrutura HTML completa que é comum a todas as páginas.
-   **Outras Páginas (`.html`)**: São os arquivos **filhos**. Eles herdam a estrutura do `model.html` e preenchem apenas as seções específicas de conteúdo.

### 🧱 Blocos Obrigatórios e Estrutura

Toda nova página criada **deve** herdar de `model.html` e utilizar os blocos de conteúdo definidos.

#### Estrutura Mínima Obrigatória:

```html
{% extends "model.html" %}

{% block content %}
    <!-- 
      Todo o conteúdo principal da sua página vai aqui.
      Ex: seções, artigos, formulários, etc.
    -->
{% endblock %}
```

#### Blocos Disponíveis em `model.html`:

-   `{% block title %}`: Permite definir um título específico para a página na tag `<title>`. Se não for definido, o título padrão será usado.
-   `{% block hero %}`: Uma seção opcional para criar um cabeçalho de destaque (hero banner) abaixo da barra de navegação. Ideal para títulos de página impactantes.
-   `{% block content %}`: **(Obrigatório)** O bloco principal onde todo o conteúdo da página deve ser inserido.
-   `{% block scripts %}`: Permite adicionar scripts JavaScript específicos para uma página no final do `<body>`.

#### Exemplo de Uso Completo:

```html
{% extends "model.html" %}

{% block title %}Página de Exemplo{% endblock %}

{% block hero %}
<div class="hero">
    <h1>Bem-vindo à Página de Exemplo</h1>
</div>
{% endblock %}

{% block content %}
<div class="container mt-5">
    <p>Este é o conteúdo principal da minha página.</p>
</div>
{% endblock %}

{% block scripts %}
    {{ super() }} <!-- Mantém os scripts do pai -->
    <script src="/path/to/meu-script-especifico.js"></script>
{% endblock %}
```

### ✅ Regras e Boas Práticas

1.  **Herança é Obrigatória**: Todas as novas páginas devem usar `{% extends "model.html" %}`.
2.  **Use o Bloco `content`**: O conteúdo principal deve estar dentro do `{% block content %}`.
3.  **Bootstrap como Base**: Utilize componentes e classes do Bootstrap para garantir a consistência visual.
4.  **Organização**: Páginas de certificações devem ficar dentro da subpasta `/certifications`.
5.  **Apenas HTML**: Este diretório deve conter exclusivamente arquivos `.html`.

---

## 🇺🇸 English (EN-US)

### 🎯 Purpose

The `/templates` folder stores the project's visual structure. By default, Flask looks for HTML files in this folder to render pages. The organization and standardization of templates are crucial for maintainability and design consistency.

### 🏛️ Template Architecture: Inheritance with `model.html`

To avoid code repetition (like `head`, `navbar`, and `footer`), we use Jinja2's **template inheritance** system.

-   **`model.html`**: This is the **parent** file. It defines the complete HTML structure common to all pages.
-   **Other Pages (`.html`)**: These are the **child** files. They inherit the structure from `model.html` and only fill in the specific content sections.

### 🧱 Required Blocks and Structure

Every new page created **must** inherit from `model.html` and use the defined content blocks.

#### Minimum Required Structure:

```html
{% extends "model.html" %}

{% block content %}
    <!-- 
      All the main content of your page goes here.
      Ex: sections, articles, forms, etc.
    -->
{% endblock %}
```

#### Available Blocks in `model.html`:

-   `{% block title %}`: Allows setting a specific title for the page in the `<title>` tag. If not defined, the default title will be used.
-   `{% block hero %}`: An optional section to create a hero banner below the navigation bar. Ideal for impactful page titles.
-   `{% block content %}`: **(Required)** The main block where all page content must be inserted.
-   `{% block scripts %}`: Allows adding page-specific JavaScript scripts at the end of the `<body>`.

#### Full Usage Example:

```html
{% extends "model.html" %}

{% block title %}Example Page{% endblock %}

{% block hero %}
<div class="hero">
    <h1>Welcome to the Example Page</h1>
</div>
{% endblock %}

{% block content %}
<div class="container mt-5">
    <p>This is the main content of my page.</p>
</div>
{% endblock %}

{% block scripts %}
    {{ super() }} <!-- Keeps the parent's scripts -->
    <script src="/path/to/my-specific-script.js"></script>
{% endblock %}
```

### ✅ Rules and Best Practices

1.  **Inheritance is Mandatory**: All new pages must use `{% extends "model.html" %}`.
2.  **Use the `content` Block**: The main content must be inside `{% block content %}`.
3.  **Bootstrap as a Base**: Use Bootstrap components and classes to ensure visual consistency.
4.  **Organization**: Certification pages should be placed inside the `/certifications` subfolder.
5.  **HTML Only**: This directory should contain exclusively `.html` files.