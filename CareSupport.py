from github import Github

def upload_to_github(username, password, repo_name, file_path, commit_message):
    # Autenticação no GitHub
    g = Github(username, password)

    # Obtém o repositório desejado (substitua 'your-username' pelo seu nome de usuário e 'your-repo' pelo nome do repositório)
    repo = g.get_user().get_repo(repo_name)

    # Leitura do conteúdo do arquivo
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Cria um novo arquivo no repositório do GitHub
    repo.create_file(file_path, commit_message, file_content)

if __name__ == "__main__":
    # Substitua as informações abaixo com suas credenciais e detalhes do arquivo
    github_username = "seu-usuario-github"
    github_password = "sua-senha-github"
    repository_name = "nome-do-repositorio"
    local_file_path = "caminho/do/arquivo/no/seu/computador/arquivo.txt"
    commit_msg = "Adicionando arquivo ao repositório"

    upload_to_github(github_username, github_password, repository_name, local_file_path, commit_msg)
