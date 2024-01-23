from github import Github
import base64

def upload_to_github(token, repo_name, file_path, commit_message):
    # Autenticação no GitHub usando token de acesso pessoal
    g = Github(token)

    # Obtém o repositório desejado (cria se não existir)
    user = g.get_user()
    repo = None
    try:
        repo = user.get_repo(repo_name)
    except Exception:
        print(f"O repositório '{repo_name}' não existe. Criando um novo.")
        repo = user.create_repo(repo_name)

    # Tenta obter o conteúdo atual do arquivo no repositório
    try:
        contents = repo.get_contents(file_path)
        current_content = base64.b64decode(contents.content).decode("utf-8")
    except Exception:
        # Se o arquivo não existir, cria um novo e define o conteúdo atual como vazio
        print(f"O arquivo '{file_path}' não existe. Criando um novo.")
        repo.create_file(file_path, commit_message, "")
        current_content = ""

    # Leitura do conteúdo do arquivo local
    with open(file_path, 'r') as file:
        new_content = file.read()

    # Verifica se o conteúdo é diferente antes de fazer upload
    if current_content != new_content:
        # Faz o upload do novo conteúdo
        repo.update_file(file_path, commit_message, new_content, contents.sha)
        print("Arquivo atualizado no repositório do GitHub.")
    else:
        print("O conteúdo do arquivo não foi alterado. Nenhum upload necessário.")

if __name__ == "__main__":
    # Substitua as informações abaixo com seu token de acesso pessoal e detalhes do arquivo
    github_token = "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"
    repository_name = "CareSupport"
    local_file_path = "C:\\Users\\trsnc\\Documents\\miband-heartrate-2.1.0\\miband-heartrate-2.1.0\\heartrate.csv"
    commit_msg = "A atualizar o arquivo no repositório"

    # Chamada para o método de upload
    upload_to_github(github_token, repository_name, local_file_path, commit_msg)
