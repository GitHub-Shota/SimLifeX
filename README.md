# SimLifeX

# STEP1: gitの使い方

## 0. gitをインストールする
[https://gitforwindows.org/](https://gitforwindows.org/) でインストーラをダウンロードし、指示に従ってgitをインストールする。

Vscodeを使用している場合などは、コミットを見やすくするなどの拡張機能を導入してもよい。

## 1. gitで共有したリポジトリの保存(コピー)方法
以下、プログラムはgitのリポジトリを複製したい階層にて実行。
**cmd想定**

```
$ git clone (gitの共有先のURL)
```

これにより、自身のPCの任意のディレクトリに共有したいgitのリポジトリが作製(コピー)される。

- **HTTPS**: HTTPSでの転送。認証機能あり。
- **SSH**: SSHでの転送。認証機能あり。
- **GitHub CLI**: Gitのプロトコルでの転送。認証機能なし。

## 2. 各自編集した内容をGitに上げる/引っ張る、状態を確認する

### リモートの状態確認

```
$ git fetch
$ git log origin/main
```

これを実行することで、コミットログの閲覧が可能。

### Gitに上げる(Push)

```
$ git add .
$ git commit -m "[編集内容などを短文で]"
$ git push origin main
```

主にアプリケーションの更新作業をしたときに使用。リモートリポジトリをローカルリポジトリに同期する。

### Gitから引っ張る(Pull)

```
$ git pull origin main
```

主に本番環境にてアプリケーションを配置するときに使用。ローカルリポジトリ（＝作業ディレクトリ）をリモートリポジトリと同期する。

# STEP2: Python環境の再現

## 1. Pythonのインストール

### Pythonのバージョンを表示して確認
以下を確認:
- インストールされていること
- 環境変数が通っていること（＝任意のディレクトリで実行可能である）

```
$ python --version
```

バージョンが確認できなければ、Microsoft Storeなどからインストールをする。インストールウィザードの途中で `Add Python 3.X. to PATH` にチェックを入れて環境変数を追記させる。

## 2. pipのインストール

pip のバージョンを確認し、インストールされていることを確認する。

```
$ python -m pip --version
```

※ Python 3.4以降は標準で付属。

## 3. パッケージのインストール

使用しているパッケージ一覧を書き出した`requirements.txt`を参照して、パッケージを一括インストールする。

```
$ pip install -r requirements.txt
```

仮想環境を構築している場合、仮想環境を起動した状態で一括インストールすること。

仮想環境を停止した状態で`pip list`を実行してもインストールしたパッケージは表示されない。

```
(venv) $ pip install -r requirements.txt
```

## 4. 仮想環境の設定（任意、スキップ可能）

今回のアプリ用に独立したPythonの仮想環境を用意する。個人で使っているPythonのパッケージ関連を汚さないメリットがある。

### 仮想環境の配置

任意のディレクトリ、もしくは`/SimLifeX`で仮想環境を構築する。

※ 必ず仮想環境名を`venv`とすること。`SimLifeX`では`/venv`ディレクトリのみ非同期とするよう`.gitignore`を作成している。

```
$ python -m venv venv
```

仮想環境名を`venv`以外にすると、生成物が各リポジトリで同期されるため名称に注意。

### 仮想環境の起動

構築した仮想環境は、上記の設定コマンドを実行した際に生成されるディレクトリ内の`activate`を実行することで起動できる。

起動した状態で`$ python`を実行した場合は、任意のディレクトリで生成された`/venv`内に格納されたPythonを参照するモードとなる。

- **Windows PowerShellの場合**:
  ```
  > .\venv\Scripts\Activate.ps1
  ```

- **Windows cmdの場合**:
  ```
  > .\venv\Scripts\activate
  ```

- **Linux/Macの場合**:
  ```
  $ source venv/bin/activate
  ```
  または
  ```
  $ source venv/Scripts/activate
  ```

### 仮想環境の停止

仮想環境を停止する。venvを起動した階層で実行。停止した状態ではPython、パッケージなどは各端末の環境準拠となる。

```
(venv) $ deactivate
```

## 5. 作業ディレクトリ（リポジトリ）と仮想環境の従属関係について

仮想環境は実行したいアプリ（例: flaskr）と同階層で構築する必要はない。

あくまで仮想環境を起動した状態で参照するPythonファイルの保管場所なので、`activate`が実行しやすい位置であれば`SimLifeX`内外は問わない。

便宜上、リポジトリ直下の`/SimLifeX`で環境名`venv`を構築することをスタンダードと設定する。`.gitignore`では`/venv`を非追跡とするように記入しているため注意。

## その他: 個人の環境でFlaskアプリを実行する方法

私たちは、`flaskr/run.py`や`flaskr/main.py`で実行が確認できなかった（Webサーバが立てられなかった）ため、以下のコードで実行した。

```
$ flask --app flaskr run --port 80 --host 0.0.0.0
```

おそらく**超危険**と思われる。
