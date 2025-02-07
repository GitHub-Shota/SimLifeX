# SimLifeX

## プロジェクトの概要

今回の開発プロジェクト「SimLifeX」は、ライフシミュレーターの開発に取り組んだものである。

**目的:** 不確実性を伴う現実世界の問題を解決する効果的な手段であるシミュレーション技術を活用し、ライフシミュレーター「SimLifeX」を開発すること。特に、高校生を対象とした理系・文系適正診断を想定している。

**アプローチ:**

- 当初はクラウド上で動くWebアプリケーションとしてAWSとPython(Flask)を用いて開発を計画していたが、予算やスケジュールなどの問題からローカル環境で動くアプリケーションに変更した。
- 確率的手法を採用し、条件付き確率とベイズの定理を用いて、質問への回答に基づいて理系への進学確率を計算するシステムを構築した。
- 質問形式は2択と3択を用意し、回答に応じて理系への進学確率を算出する。
- 事前確率として、理系と文系の性格モデルを仮定し、質問に対する回答の事前確率を設定している。例えば、「宿題は必ずやる方だ」という質問に対して、理系は「YES」と答える確率が低く、文系は「YES」と答える確率が高いというように設定している。

**システム構成:**

- ユーザーはGitHubからプログラムファイルをダウンロードし、各自のターミナルで実行する。
- プログラムは質問に答えていく形式で、回答に基づいて理系への進学確率が計算され、結果が出力される。
- 確率計算には、事前に設定した確率とベイズの定理を利用している。

**成果:**

- 質問への回答パターンと理系への進学確率の関係性をシミュレーションで確認し、パラメータ設定が意図通りに機能していることを評価した。
- 回答結果上位10パターンを表示することで、ユーザーが回答と進展確率の関係性を理解し、自己分析に役立てられるように設計されている。

**今後の展望・課題:**

- **Webアプリケーション化:** 当初計画していたWebアプリケーションとしての公開を目指し、flaskを用いたオープンアプリ化を再検討している。
- **データベース化:** 確率設定データや出力結果をデータベースで管理することを検討している。
- **GUI設計:** ユーザーインターフェースを改善し、より使いやすいアプリケーションを目指している。
- **計算量削減:** 質問数を増やした場合の計算量増加に対応するため、重要度の高い質問を抽出して質問数を絞り込むなど、計算量の削減を検討している。
- **アンケートによるパラメータ調整:** 実際にアンケートを実施し、統計データに基づいてパラメータを調整することで、シミュレーションの精度向上を目指している。
- **ライフプラン提案への発展:** 将来的には、初期パラメータ（生い立ち、学科、興味など）を入力することで、個別のライフプラン（おすすめ授業、就職先、収支予測など）を提案できるような、より高度なライフシミュレーターへの発展を目指している。

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
