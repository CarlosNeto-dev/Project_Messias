# 📁 Pasta de Arquivos Estáticos (`/static`)

Este diretório contém todos os recursos que são servidos diretamente ao navegador do usuário, sem processamento pelo servidor Flask. A correta organização e utilização desta pasta são fundamentais para o funcionamento da interface do site.

---

## 🇧🇷 Português (PT-BR)

### 🎯 Propósito

A pasta `/static` é o local padrão onde o Flask procura por arquivos como CSS, JavaScript, imagens, fontes, etc. Diferente dos templates, que são processados pelo Jinja2, os arquivos aqui são enviados "como estão" para o cliente.

### 📂 Estrutura de Subpastas

Para manter o projeto organizado, utilizamos a seguinte estrutura:

-   `static/`
    -   `css/`: Contém todas as folhas de estilo (`.css`). O arquivo principal é o `style.css`.
    -   `img/`: Contém todos os recursos visuais, como logotipos, ícones e imagens de certificação.

### 🔗 Como Referenciar Arquivos Estáticos (MUITO IMPORTANTE)

Nunca crie links para arquivos estáticos manualmente (ex: `href="static/css/style.css"`). A maneira correta e robusta em Flask é usar a função `url_for()`.

A função `url_for()` gera dinamicamente a URL para um arquivo estático. O primeiro argumento é sempre `'static'`, e o segundo argumento é `filename`, que deve conter o caminho do arquivo *a partir da pasta `static`*.

#### Exemplo para CSS:

No `<head>` do seu template `model.html`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

#### Exemplo para Imagens:

Em qualquer template, para exibir uma imagem:

```html
<img src="{{ url_for('static', filename='img/nome_da_imagem.png') }}" alt="Descrição da Imagem">
```

#### Vantagens de usar `url_for()`:

1.  **Flexibilidade**: Se você decidir mudar a rota onde os arquivos estáticos são servidos, não precisará alterar nenhum link nos templates.
2.  **Performance**: O Flask pode ser configurado para adicionar hashes aos nomes dos arquivos para controle de cache, e `url_for()` lidará com isso automaticamente.
3.  **Consistência**: Garante que os links sempre funcionarão, independentemente de como a aplicação é implantada.

### ✅ Regras e Boas Práticas

1.  **Sempre use `url_for()`**: É a regra mais importante para esta pasta.
2.  **Mantenha a Estrutura**: Adicione novos arquivos CSS em `/css` e novas imagens em `/img`.
3.  **Otimize as Imagens**: Antes de adicionar imagens, comprima-as para garantir que o site carregue rapidamente.

---

## 🇺🇸 English (EN-US)

### 🎯 Purpose

The `/static` folder is the default location where Flask looks for files such as CSS, JavaScript, images, fonts, etc. Unlike templates, which are processed by Jinja2, the files here are sent "as is" to the client.

### 📂 Subfolder Structure

To keep the project organized, we use the following structure:

-   `static/`
    -   `css/`: Contains all stylesheets (`.css`). The main file is `style.css`.
    -   `img/`: Contains all visual assets, such as logos, icons, and certification images.

### 🔗 How to Reference Static Files (VERY IMPORTANT)

Never create links to static files manually (e.g., `href="static/css/style.css"`). The correct and robust way in Flask is to use the `url_for()` function.

The `url_for()` function dynamically generates the URL for a static file. The first argument is always `'static'`, and the second argument is `filename`, which must contain the path to the file *from within the `static` folder*.

#### Example for CSS:

In the `<head>` of your `model.html` template:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

#### Example for Images:

In any template, to display an image:

```html
<img src="{{ url_for('static', filename='img/image_name.png') }}" alt="Image Description">
```

#### Advantages of using `url_for()`:

1.  **Flexibility**: If you decide to change the route where static files are served, you won't need to change any links in the templates.
2.  **Performance**: Flask can be configured to add hashes to filenames for cache control, and `url_for()` will handle this automatically.
3.  **Consistency**: Ensures that links will always work, regardless of how the application is deployed.

### ✅ Rules and Best Practices

1.  **Always use `url_for()`**: This is the most important rule for this folder.
2.  **Maintain the Structure**: Add new CSS files to `/css` and new images to `/img`.
3.  **Optimize Images**: Before adding images, compress them to ensure the site loads quickly.