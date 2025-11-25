# Templates Folder / Pasta de Templates

***

## 🇧🇷 Português (PT-BR)

### 📖 Sobre esta pasta

A pasta **/templates** armazena todas as páginas **HTML** utilizadas pela aplicação Flask.
Aqui ficam os arquivos responsáveis pela interface visual do sistema.

Todas as páginas devem seguir estes padrões:

- Utilizar **Bootstrap** como base para o layout e componentes
- Herdar o layout principal através de:

```html
{% extends "model.html" %}

{% block conteudo %}

<!-- conteúdo da página -->

{% endblock %}
```

- Manter a organização clara entre páginas principais e páginas específicas
- Somente arquivos `.html` devem permanecer aqui

Esta pasta será atualizada continuamente conforme as páginas forem sendo desenvolvidas.

***

## 🇺🇸 English (EN-US)

### 📖 About this folder

The **/templates** folder stores all the **HTML** pages used by the Flask application.
The files responsible for the system's visual interface are located here.

All pages must follow these standards:

- Use **Bootstrap** as the base for the layout and components
- Inherit the main layout using:

```html
{% extends "model.html" %}

{% block content %}

<!-- page content -->

{% endblock %}
```

- Maintain a clear organization between main pages and specific pages
- Only `.html` files should be kept here

This folder will be updated continuously as the pages are developed.