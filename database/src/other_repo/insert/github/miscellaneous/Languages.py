#!python3
#encoding:utf-8
import dataset
import database.src.other_repo.insert.github.api.repositories.Repositories
import time
class Languages:
    def __init__(self, db_path_repo, req_param):
        self.req = req_param
        self.db_path_repo = db_path_repo
        self.db_repo = dataset.connect('sqlite:///' + db_path_repo)
        self.api = database.src.other_repo.insert.github.api.repositories.Repositories.Repositories(req_param)
        self.page = database.src.other_repo.insert.github.api.Pagenation.Pagenation(req_param)

    """
    まだ言語情報が存在しないリポジトリの言語情報のみ取得し登録する。
    """
    def filling(self):
        self.db_repo.begin()
        repos = self.db_repo['Repositories'].find(order_by='CreatedAt')
        for repo in repos:
            if None is not self.db_repo['Repositories'].find_one(repo['Id']):
                continue
            time.sleep(2)
            langs = self.api.list_languages(repo['Name'])
            if langs is None:
                continue
            self.insert(repo['Id'], langs)
        self.db_repo.commit()

    """
    言語情報を取得してローカルDBを更新する。
    """
    def update_local_db(self):
        self.db_repo.begin()
        repos = self.db_repo['Repositories'].find(order_by='CreatedAt')
        for repo in repos:
            time.sleep(2)
            langs = self.api.list_languages(repo['Name'])
            if langs is None:
                continue
            self.db_repo['Languages'].delete(RepositoryId=repo['Id'])
            self.insert(repo['Id'], langs)
        self.db_repo.commit()

    def insert(self, repo_id, langs):
        for key in langs.keys():
            self.db_repo['Languages'].insert(dict(
                RepositoryId=repo_id, 
                Language=key, 
                Size=langs[key]))
