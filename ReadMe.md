# このソフトウェアについて

GitHubアップローダDB作成外部呼出のリファクタリング。

# 前回まで

* https://github.com/ytyaru/GitHub.Upload.ByPython.Add.Database.Create.Callable.201703251122

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite](https://www.sqlite.org/) 3.8.2

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

1. GitHubリポジトリにしたいディレクトリを用意する
1. 1に`up.sh`をコピーする
1. `up.sh`を任意に設定する

```
USER=ytyaru
DESCRIPTION="説明文。"
HOMEPAGE=http://abc
PATH_SCRIPT=/home/${USER}/automation/GitHubUploader/hup.py
```

# 実行

```sh
bash up.sh
```

`up.sh`を使わない場合は以下。
```sh
python3 hup.py `pwd` -u username -d "リポジトリ説明文。" -l http://リポジトリHomepage
```

# 結果

* 初回に限りDBを作成する
    * `./database/res/db`配下にDBファイルが作成される
* アップローダCUI対話が表示される

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[pytz](https://github.com/newvem/pytz)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2003-2005 Stuart Bishop <stuart@stuartbishop.net>](https://github.com/newvem/pytz/blob/master/LICENSE.txt)

