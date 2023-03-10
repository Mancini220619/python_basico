import os
import win32security
import html

# pasta a ser analisada
#folder = r"\\servidor\compartilhamento\pasta"
folder = r"\\172.20.11.10\c$\Users\ADM341307403\Downloads"

# obter as ACLs da pasta
sd = win32security.GetFileSecurity(folder, win32security.DACL_SECURITY_INFORMATION)

# obter lista de ACEs (entradas de controle de acesso)
dacl = sd.GetSecurityDescriptorDacl()
aces = [dacl.GetAce(i) for i in range(dacl.GetAceCount())]

# agrupar ACEs por tipo de permissão
read_aces = [ace for ace in aces if ace[0].AccessMask & win32security.FILE_GENERIC_READ]
write_aces = [ace for ace in aces if ace[0].AccessMask & win32security.FILE_GENERIC_WRITE]

# gerar arquivo HTML
html_str = "<html><head><title>Permissões da pasta</title></head><body>"
html_str += "<h1>Permissões de Leitura</h1>"
for ace in read_aces:
    trustee_name, trustee_domain, trustee_type = win32security.LookupAccountSid(None, ace[1])
    html_str += f"<p>{trustee_domain}\\{trustee_name}</p>"
html_str += "<h1>Permissões de Modificação</h1>"
for ace in write_aces:
    trustee_name, trustee_domain, trustee_type = win32security.LookupAccountSid(None, ace[1])
    html_str += f"<p>{trustee_domain}\\{trustee_name}</p>"
html_str += "</body></html>"

# salvar arquivo HTML
with open("permissões.html", "w") as f:
    f.write(html_str)
