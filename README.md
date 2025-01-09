# SimLifeX

STEP1.gitの使い方

0.gitをインストールする
https://gitforwindows.org/　でインストーラをダウンロードし、指示に従ってgitをインストールする。
Vscodeを使用している場合などは、コミットを見やすくするなどの拡張機能を導入してもよい。


1.gitで共有したリポジトリの保存(コピー)方法
以下、プログラムはgitのリポジトリを複製したい階層にて実行。
cmd想定

$git clone (gitの共有先のURL)

で、自身のPCの任意のディレクトリに共有したいgitのリポジトリが作製(コピー)される。
HTTPS：HTTPSでの転送。認証機能あり。
SSH：SSHでの転送。認証機能あり。
GitHub CLI：Gitのプロトコルでの転送。認証機能なし。

2.各自編集した内容をGitに上げる/引っ張る、状態を確認する

・リモートの状態確認

$git fetch
$git log origin/main

を実行することでコミットログの閲覧が可能。

・Gitに上げる(Push)

$ git add .
$ git commit -m "[編集内容などを短文で]"
$ git push origin main

を実行。
主にアプリケーションの更新作業をしたときに使用。
リモートリポジトリをローカルリポジトリに同期する。

・Gitから引っ張る(pull)

$ git pull origin main

を実行。
主に、本番環境にてアプリケーションを配置するときに使用
ローカルリポジトリ（＝作業ディレクトリ）をリモートリポジトリと同期する。

Step2: python環境の再現

Pythonのインストール
pythonのバージョンを表示する
同時に
    インストールされていること
    環境変数が通っていること（＝任意のディレクトリで実行可能である）
以上2点を確認する
$ python --version

バージョンが確認できなければmicrosoft storeなどからインストールをする.
インストールウィザードの途中で□ Add Python 3.X. to PATHにチェックを入れて環境変数を追記させる．

pipのインストール
pip のバージョンを確認しながら, インストールされていることを確認する. 
※ Python 3.4以降は標準で付属
$ python -m pip –version

パッケージのインストール
使用しているパッケージ一覧を書き出したrequirements.txtを参照して, パッケージを一括インストールする.
/SimLifeX$ pip install -r requirements.txt

後述の仮想環境を構築している場合, 仮想環境を起動した状態で一括インストール仮想環境を停止deactivateしてpip listするとおそらくインストールしたパッケージは表示されない
(venv)/SimLifeX$ pip install -r requirements.txt

［任意，skip可能］仮想環境の設定
今回のアプリ用に独立したpython の仮想環境を用意する. 
個人で使っているpython のパッケージ関連を汚さないメリットがある.

仮想環境の配置
任意のディレクトリ, もしくは/SimLifeX で仮想環境を構築する. 
※ 必ず仮想環境名をvenvとすること. 
SimLifeXでは/venv ディレクトリのみ非同期とする .gitignore を作成した. 
環境名をvenv以外とした場合, 生成物が各リポジトリで同期されるため名称に注意
/SimLifeX$ python -m venv venv

仮想環境の起動
構築した仮想環境は上記の設定コマンドを実行した際に生成されるディレクトリの中のactivate を実行することで起動できる. 起動した状態で$ python を実行した場合は, 任意のディレクトリで生成された/venv 内に格納されたpython を参照するモードとなる.

windows pawershell の場合
\SimLifeX> .\venv\Scripts\Activate.ps1

windows cmd の場合
\SimLifeX> .\venv\Scripts\activate

linux/macの場合
/SimLifeX$ source venv/bin/activate

もしくは
/SimLifeX$ source venv/Scripts/activate

仮想環境の停止
仮想環境を停止する. 停止した状態ではpython, パッケージなどは各端末の環境準拠となる.
(venv)/SimLifeX$ deactivate

作業ディレクトリ（リポジトリ）と仮想環境の従属関係について
仮想環境は実行したいアプリ（flaskr）と同階層で構築する必要はない. あくまで仮想環境を起動した状態で参照するpython ファイルの保管場所なのでactivate が実行しやすい位置であれば, SimLifeX内外は問わない. 便宜上リポジトリ直下の/SimLifeX で環境名venv を構築することをスタンダードと設定する. .gitignore では/venv を非追跡とするように記入しているため注意.


その他：個人の環境でflaskアプリを実行する方法について
・私たちは、flaskr/run.pyやflaskr/main.pyで実行が確認できなかった(Webサーバが立てられなかった)ため、以下のコードで実行した。

\SimLifeX> flask --app flaskr run --port 80 --host 0.0.0.0

おそらく超危険？っぽい。






