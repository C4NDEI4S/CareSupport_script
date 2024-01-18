from github import Github
import base64

def upload_to_github(username, password, repo_name, file_path, commit_message):
    # Autenticação no GitHub
    g = Github(username, password)

    # Obtém o repositório desejado
    repo = g.get_user().get_repo(repo_name)

    # Obtém o conteúdo atual do arquivo no repositório
    try:
        contents = repo.get_contents(file_path)
        current_content = base64.b64decode(contents.content).decode("utf-8")
    except Exception:
        current_content = ""

    # Leitura do conteúdo do arquivo local
    with open(file_path, 'r') as file:
        new_content = file.read()

    # Verifica se o conteúdo é diferente antes de fazer upload
    if new_content != current_content:
        # Faz o upload do novo conteúdo
        repo.update_file(file_path, commit_message, new_content, contents.sha)
        print("Arquivo atualizado no repositório do GitHub.")
    else:
        print("O conteúdo do arquivo não foi alterado. Nenhum upload necessário.")

if __name__ == "__main__":
    # Substitua as informações abaixo com suas credenciais e detalhes do arquivo
    github_username = "seu-usuario-github"
    github_password = "sua-senha-github"
    repository_name = "nome-do-repositorio"
    local_file_path = "caminho/do/arquivo/no/seu/computador/arquivo.txt"
    commit_msg = "Atualizando arquivo no repositório"

    upload_to_github(github_username, github_password, repository_name, local_file_path, commit_msg)
