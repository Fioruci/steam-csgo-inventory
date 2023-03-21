import jinja2, create_html

def render_html(dict_dados):
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    

    conteudo = create_html(dict_dados)
    xo = open("Template/index.html", 'w', encoding="utf-8")
    xo.write(conteudo)
    xo.close()

    template_file = "Template/index.html"
    template = template_env.get_template(template_file)
    output_text = template.render(dict_dados)


    html_path = f'{dict_dados["nome_amigo"]}.html'
    html_file = open(html_path, 'w', encoding="utf-8")
    html_file.write(output_text)
    html_file.close()

# render_html("Fioruci")