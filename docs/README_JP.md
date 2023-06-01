> **Note**
>
> このReadmeファイルは、このプロジェクトのmarkdown翻訳プラグインによって自動的に生成されたもので、100%正確ではない可能性があります。
>
<<<<<<< HEAD

# <img src="logo.png" width="40" > ChatGPT 学術最適化

**このプロジェクトが好きだったら、スターをつけてください。もし、より使いやすい学術用のショートカットキーまたはファンクションプラグインを発明した場合は、issueを発行するかpull requestを作成してください。また、このプロジェクト自体によって翻訳されたREADMEは[英語説明書|](docs/README_EN.md)[日本語説明書|](docs/README_JP.md)[ロシア語説明書|](docs/README_RS.md)[フランス語説明書](docs/README_FR.md)もあります。**

> **注意事項**
>
> 1. **赤色**のラベルが付いているファンクションプラグイン（ボタン）のみファイルを読み込めます。一部のプラグインはプラグインエリアのドロップダウンメニューにあります。新しいプラグインのPRを歓迎いたします！
>
> 2. このプロジェクトの各ファイルの機能は`self_analysis.md`（自己解析レポート）で詳しく説明されています。バージョンが追加されると、関連するファンクションプラグインをクリックして、GPTを呼び出して自己解析レポートを再生成することができます。一般的な質問は`wiki`にまとめられています。(`https://github.com/binary-husky/chatgpt_academic/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98`)


<div align="center">
    
機能 | 説明
--- | ---
ワンクリック整形 | 論文の文法エラーを一括で正確に修正できます。
ワンクリック日英翻訳 | 日英翻訳には、ワンクリックで対応できます。
ワンクリックコード説明 | コードの正しい表示と説明が可能です。
[カスタムショートカットキー](https://www.bilibili.com/video/BV14s4y1E7jN) | カスタムショートカットキーをサポートします。
[プロキシサーバーの設定](https://www.bilibili.com/video/BV1rc411W7Dr) | プロキシサーバーの設定をサポートします。
モジュラーデザイン | カスタム高階関数プラグインと[関数プラグイン]、プラグイン[ホット更新]のサポートが可能です。詳細は[こちら](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97)
[自己プログラム解析](https://www.bilibili.com/video/BV1cj411A7VW) | [関数プラグイン][ワンクリック理解](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A)このプロジェクトのソースコード
[プログラム解析機能](https://www.bilibili.com/video/BV1cj411A7VW) | [関数プラグイン] ワンクリックで別のPython/C/C++/Java/Lua/...プロジェクトツリーを解析できます。
論文読解 | [関数プラグイン] LaTeX論文の全文をワンクリックで解読し、要約を生成します。
LaTeX全文翻訳、整形 | [関数プラグイン] ワンクリックでLaTeX論文を翻訳または整形できます。
注釈生成 | [関数プラグイン] ワンクリックで関数の注釈を大量に生成できます。
チャット分析レポート生成 | [関数プラグイン] 実行後、まとめレポートを自動生成します。
[arxivヘルパー](https://www.bilibili.com/video/BV1LM4y1279X) | [関数プラグイン] 入力したarxivの記事URLで要約をワンクリック翻訳+PDFダウンロードができます。
[PDF論文全文翻訳機能](https://www.bilibili.com/video/BV1KT411x7Wn) | [関数プラグイン] PDF論文タイトルと要約を抽出し、全文を翻訳します（マルチスレッド）。
[Google Scholar Integratorヘルパー](https://www.bilibili.com/video/BV19L411U7ia) | [関数プラグイン] 任意のGoogle Scholar検索ページURLを指定すると、gptが興味深い記事を選択します。
数式/画像/テーブル表示 | 数式のTex形式とレンダリング形式を同時に表示できます。数式、コードのハイライトをサポートしています。
マルチスレッド関数プラグインサポート | ChatGPTをマルチスレッドで呼び出すことができ、大量のテキストやプログラムを簡単に処理できます。
ダークグラジオ[テーマ](https://github.com/binary-husky/chatgpt_academic/issues/173)の起動 | 「/?__dark-theme=true」というURLをブラウザに追加することで、ダークテーマに切り替えることができます。
[多数のLLMモデル](https://www.bilibili.com/video/BV1wT411p7yf)をサポート、[API2D](https://api2d.com/)インターフェースをサポート | GPT3.5、GPT4、[清華ChatGLM](https://github.com/THUDM/ChatGLM-6B)による同時サポートは、とても素晴らしいですね！
huggingface免科学上网[オンライン版](https://huggingface.co/spaces/qingxu98/gpt-academic) | huggingfaceにログイン後、[このスペース](https://huggingface.co/spaces/qingxu98/gpt-academic)をコピーしてください。
...... | ......


</div>


- 新しいインターフェース（config.pyのLAYOUTオプションを変更するだけで、「左右レイアウト」と「上下レイアウト」を切り替えることができます）
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230361456-61078362-a966-4eb5-b49e-3c62ef18b860.gif" width="700" >
</div>


- すべてのボタンは、functional.pyを読み込んで動的に生成されます。カスタム機能を自由に追加して、クリップボードを解放します
=======
> When installing dependencies, please strictly choose the versions specified in `requirements.txt`. 
> 
> `pip install -r requirements.txt`
>

# <img src="logo.png" width="40" > GPT 学术优化 (GPT Academic)

**もしこのプロジェクトが好きなら、星をつけてください。もしあなたがより良いアカデミックショートカットまたは機能プラグインを思いついた場合、Issueをオープンするか pull request を送信してください。私たちはこのプロジェクト自体によって翻訳された[英語 |](README_EN.md)[日本語 |](README_JP.md)[한국어 |](https://github.com/mldljyh/ko_gpt_academic)[Русский |](README_RS.md)[Français](README_FR.md)のREADMEも用意しています。
GPTを使った任意の言語にこのプロジェクトを翻訳するには、[`multi_language.py`](multi_language.py)を読んで実行してください。 (experimental)。

> **注意**
>
> 1. **赤色**で表示された関数プラグイン(ボタン)のみ、ファイルの読み取りをサポートしています。一部のプラグインは、プラグインエリアの**ドロップダウンメニュー**内にあります。また、私たちはどんな新しいプラグインのPRでも、**最優先**で歓迎し、処理します！
>
> 2. このプロジェクトの各ファイルの機能は、自己解析の詳細説明書である[`self_analysis.md`](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A)で説明されています。バージョンが進化するにつれて、関連する関数プラグインをいつでもクリックし、GPTを呼び出してプロジェクトの自己解析レポートを再生成することができます。よくある問題は[`wiki`](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)にまとめられています。[インストール方法](#installation)。

> 3. このプロジェクトは、chatglmやRWKV、パンクなど、国内の大規模自然言語モデルを利用することをサポートし、試みることを奨励します。複数のAPIキーを共存することができ、設定ファイルに`API_KEY="openai-key1,openai-key2,api2d-key3"`のように記入することができます。`API_KEY`を一時的に変更する場合は、入力エリアに一時的な`API_KEY`を入力してEnterキーを押せば、それが有効になります。


<div align="center">

機能 | 説明
--- | ---
一键校正 | 一键で校正可能、論文の文法エラーを検索することができる
一键中英翻訳 | 一键で中英翻訳可能
一键コード解説 | コードを表示し、解説し、生成し、コードに注釈をつけることができる
[自分でカスタマイズ可能なショートカットキー](https://www.bilibili.com/video/BV14s4y1E7jN) | 自分でカスタマイズ可能なショートカットキーをサポートする
モジュール化された設計 | カスタマイズ可能な[強力な関数プラグイン](https://github.com/binary-husky/chatgpt_academic/tree/master/crazy_functions)をサポートし、プラグインは[ホットアップデート](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97)に対応している
[自己プログラム解析](https://www.bilibili.com/video/BV1cj411A7VW) | [関数プラグイン] [一键読解](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A)このプロジェクトのソースコード
プログラム解析 | [関数プラグイン] 一鍵で他のPython/C/C++/Java/Lua/...プロジェクトを分析できる
論文の読み、[翻訳](https://www.bilibili.com/video/BV1KT411x7Wn) | [関数プラグイン] LaTex/ PDF論文の全文を一鍵で読み解き、要約を生成することができる
LaTex全文[翻訳](https://www.bilibili.com/video/BV1nk4y1Y7Js/)、[校正](https://www.bilibili.com/video/BV1FT411H7c5/) | [関数プラグイン] LaTex論文の翻訳または校正を一鍵で行うことができる
一括で注釈を生成 | [関数プラグイン] 一鍵で関数に注釈をつけることができる
Markdown[中英翻訳](https://www.bilibili.com/video/BV1yo4y157jV/) | [関数プラグイン] 上記の5種類の言語の[README](https://github.com/binary-husky/chatgpt_academic/blob/master/docs/README_EN.md)を見たことがありますか？
チャット分析レポート生成 | [関数プラグイン] 実行後、自動的に概要報告書を生成する
[PDF論文全文翻訳機能](https://www.bilibili.com/video/BV1KT411x7Wn) | [関数プラグイン] PDF論文からタイトルと要約を抽出し、全文を翻訳する（マルチスレッド）
[Arxivアシスタント](https://www.bilibili.com/video/BV1LM4y1279X) | [関数プラグイン] arxiv記事のURLを入力するだけで、要約を一鍵翻訳し、PDFをダウンロードできる
[Google Scholar 総合アシスタント](https://www.bilibili.com/video/BV19L411U7ia) | [関数プラグイン] 任意のGoogle Scholar検索ページURLを指定すると、gptが[related works](https://www.bilibili.com/video/BV1GP411U7Az/)を作成する
インターネット情報収集＋GPT | [関数プラグイン] まずGPTに[インターネットから情報を収集](https://www.bilibili.com/video/BV1om4y127ck)してから質問に回答させ、情報が常に最新であるようにする
数式/画像/表表示 | 数式の[tex形式とレンダリング形式](https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png)を同時に表示し、数式、コードハイライトをサポートしている
マルチスレッド関数プラグインがサポートされている | chatgptをマルチスレッドで呼び出し、[大量のテキスト](https://www.bilibili.com/video/BV1FT411H7c5/)またはプログラムを一鍵で処理できる
ダークグラジオ[テーマの起動](https://github.com/binary-husky/chatgpt_academic/issues/173) | ブラウザのURLの後ろに```/?__theme=dark```を追加すると、ダークテーマを切り替えることができます。
[多数のLLMモデル](https://www.bilibili.com/video/BV1wT411p7yf)がサポートされ、[API2D](https://api2d.com/)がサポートされている | 同時にGPT3.5、GPT4、[清華ChatGLM](https://github.com/THUDM/ChatGLM-6B)、[復旦MOSS](https://github.com/OpenLMLab/MOSS)に対応
より多くのLLMモデルが接続され、[huggingfaceデプロイ](https://huggingface.co/spaces/qingxu98/gpt-academic)がサポートされている | Newbingインターフェイス（Newbing）、清華大学の[Jittorllm](https://github.com/Jittor/JittorLLMs)のサポート[LLaMA](https://github.com/facebookresearch/llama), [RWKV](https://github.com/BlinkDL/ChatRWKV)と[盘古α](https://openi.org.cn/pangu/)
さらに多くの新機能（画像生成など）を紹介する... | この文書の最後に示す... 
</div>

- 新しいインターフェース（`config.py`のLAYOUTオプションを変更することで、「左右配置」と「上下配置」を切り替えることができます）
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230361456-61078362-a966-4eb5-b49e-3c62ef18b860.gif" width="700" >
</div>- All buttons are dynamically generated by reading functional.py, and custom functions can be freely added to free the clipboard.

>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/231975334-b4788e91-4887-412f-8b43-2b9c5f41d248.gif" width="700" >
</div>

<<<<<<< HEAD
- 色を修正/修正
=======
- Polishing/Correction

>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/231980294-f374bdcb-3309-4560-b424-38ef39f04ebd.gif" width="700" >
</div>

<<<<<<< HEAD
- 出力に数式が含まれている場合、TeX形式とレンダリング形式の両方が表示され、コピーと読み取りが容易になります
=======
- If the output contains formulas, they are displayed in both TeX and rendering forms, making it easy to copy and read.

>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png" width="700" >
</div>

<<<<<<< HEAD
- プロジェクトのコードを見るのが面倒？chatgptに整備されたプロジェクトを直接与えましょう
=======
- Don't feel like looking at the project code? Just ask chatgpt directly.

>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="700" >
</div>

<<<<<<< HEAD
- 多数の大規模言語モデルの混合呼び出し(ChatGLM + OpenAI-GPT3.5 + [API2D](https://api2d.com/)-GPT4)
=======

- Mixed calls of multiple large language models (ChatGLM + OpenAI-GPT3.5 + [API2D](https://api2d.com/)-GPT4）

>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/232537274-deca0563-7aa6-4b5d-94a2-b7c453c47794.png" width="700" >
</div>

<<<<<<< HEAD
多数の大規模言語モデルの混合呼び出し[huggingfaceテスト版](https://huggingface.co/spaces/qingxu98/academic-chatgpt-beta)(huggigface版はchatglmをサポートしていません)


---

## インストール-方法1：直接運転 (Windows、LinuxまたはMacOS)

1. プロジェクトをダウンロードします。
=======
---

# Installation

## Installation-Method 1: Directly run (Windows, Linux or MacOS)

1. Download the project.

>>>>>>> upstream/master
```sh
git clone https://github.com/binary-husky/chatgpt_academic.git
cd chatgpt_academic
```

<<<<<<< HEAD
2. API_KEYとプロキシ設定を構成する

`config.py`で、海外のProxyとOpenAI API KEYを構成して説明します。
```
1.あなたが中国にいる場合、OpenAI APIをスムーズに使用するには海外プロキシを設定する必要があります。構成の詳細については、config.py（1.その中のUSE_PROXYをTrueに変更し、2.手順に従ってプロキシを変更する）を詳細に読んでください。
2. OpenAI API KEYを構成する。OpenAIのウェブサイトでAPI KEYを取得してください。一旦API KEYを手に入れると、config.pyファイルで設定するだけです。
3.プロキシネットワークに関連する問題(ネットワークタイムアウト、プロキシが動作しない）をhttps://github.com/binary-husky/chatgpt_academic/issues/1にまとめました。
```
(P.S. プログラム実行時にconfig.pyの隣にconfig_private.pyという名前のプライバシー設定ファイルを作成し、同じ名前の設定を上書きするconfig_private.pyが存在するかどうかを優先的に確認します。そのため、私たちの構成読み取りロジックを理解できる場合は、config.pyの隣にconfig_private.pyという名前の新しい設定ファイルを作成し、その中のconfig.pyから設定を移動してください。config_private.pyはgitで保守されていないため、プライバシー情報をより安全にすることができます。)

3. 依存関係をインストールします。
```sh
# 選択肢があります。
python -m pip install -r requirements.txt


# (選択肢2) もしAnacondaを使用する場合、手順は同様です：
# (選択肢2.1) conda create -n gptac_venv python=3.11
# (選択肢2.2) conda activate gptac_venv
# (選択肢2.3) python -m pip install -r requirements.txt

# 注: 公式のpipソースまたはAlibabaのpipソースを使用してください。 別のpipソース（例：一部の大学のpip）は問題が発生する可能性があります。 一時的なソースの切り替え方法： 
# python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

もしあなたが清華ChatGLMをサポートする必要がある場合、さらに多くの依存関係をインストールする必要があります（Pythonに慣れない方やコンピューターの設定が十分でない方は、試みないことをお勧めします）：
```sh
python -m pip install -r request_llm/requirements_chatglm.txt
```

4. 実行
```sh
python main.py
```

5. 関数プラグインのテスト
```
- Pythonプロジェクト分析のテスト
    入力欄に `./crazy_functions/test_project/python/dqn` と入力し、「Pythonプロジェクト全体の解析」をクリックします。
- 自己コード解読のテスト
    「[マルチスレッドデモ] このプロジェクト自体を解析します（ソースを翻訳して解読します）」をクリックします。
- 実験的な機能テンプレート関数のテスト（GPTが「今日の歴史」に何が起こったかを回答することが求められます）。この関数をテンプレートとして使用して、より複雑な機能を実装できます。
    「[関数プラグインテンプレートデモ] 今日の歴史」をクリックします。
- 関数プラグインエリアのドロップダウンメニューには他にも選択肢があります。
```

## インストール方法2：Dockerを使用する（Linux）

1. ChatGPTのみ（大多数の人にお勧めです）
``` sh
# プロジェクトのダウンロード
git clone https://github.com/binary-husky/chatgpt_academic.git
cd chatgpt_academic
# 海外プロキシとOpenAI API KEYの設定
config.pyを任意のテキストエディタで編集する
# インストール
docker build -t gpt-academic .
# 実行
docker run --rm -it --net=host gpt-academic

# 関数プラグインのテスト
## 関数プラグインテンプレート関数のテスト（GPTが「今日の歴史」に何が起こったかを回答することが求められます）。この関数をテンプレートとして使用して、より複雑な機能を実装できます。
「[関数プラグインテンプレートデモ] 今日の歴史」をクリックします。
## Latexプロジェクトの要約を書くテスト
入力欄に./crazy_functions/test_project/latex/attentionと入力し、「テックス論文を読んで要約を書く」をクリックします。
## Pythonプロジェクト分析のテスト
入力欄に./crazy_functions/test_project/python/dqnと入力し、[Pythonプロジェクトの全解析]をクリックします。

関数プラグインエリアのドロップダウンメニューには他にも選択肢があります。
```

2. ChatGPT + ChatGLM（Dockerに非常に詳しい人+十分なコンピューター設定が必要）



```sh
# Dockerfileの編集
cd docs && nano Dockerfile+ChatGLM
# ビルド方法
docker build -t gpt-academic --network=host -f Dockerfile+ChatGLM .
# 実行方法 (1) 直接実行: 
docker run --rm -it --net=host --gpus=all gpt-academic
# 実行方法 (2) コンテナに入って調整する:
docker run --rm -it --net=host --gpus=all gpt-academic bash
```

## インストール方法3：その他のデプロイ方法

1. クラウドサーバーデプロイ
[デプロイwiki-1](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%9C%E7%A8%8B%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)

2. WSL2を使用 (Windows Subsystem for Linux)
[デプロイwiki-2](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BD%BF%E7%94%A8WSL2%EF%BC%88Windows-Subsystem-for-Linux-%E5%AD%90%E7%B3%BB%E7%BB%9F%EF%BC%89%E9%83%A8%E7%BD%B2)


## インストール-プロキシ設定
1. 通常の方法
[プロキシを設定する](https://github.com/binary-husky/chatgpt_academic/issues/1)

2. 初心者向けチュートリアル
[初心者向けチュートリアル](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BB%A3%E7%90%86%E8%BD%AF%E4%BB%B6%E9%97%AE%E9%A2%98%E7%9A%84%E6%96%B0%E6%89%8B%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%EF%BC%88%E6%96%B9%E6%B3%95%E5%8F%AA%E9%80%82%E7%94%A8%E4%BA%8E%E6%96%B0%E6%89%8B%EF%BC%89)


---

## カスタムボタンの追加(学術ショートカットキー)

`core_functional.py`を任意のテキストエディタで開き、以下のエントリーを追加し、プログラムを再起動してください。(ボタンが追加されて表示される場合、前置詞と後置詞はホット編集がサポートされているため、プログラムを再起動せずに即座に有効になります。)

例:
```
"超级英译中": {
    # 前置詞 - あなたの要求を説明するために使用されます。翻訳、コードの説明、編集など。
    "Prefix": "以下のコンテンツを中国語に翻訳して、マークダウンテーブルを使用して専門用語を説明してください。\n\n", 
    
    # 後置詞 - プレフィックスと共に使用すると、入力内容を引用符で囲むことができます。
    "Suffix": "",
},
```

=======
2. Configure the API_KEY.

Configure the API KEY and other settings in `config.py` and [special network environment settings](https://github.com/binary-husky/gpt_academic/issues/1).

(P.S. When the program is running, it will first check if there is a private configuration file named `config_private.py`, and use the configuration in it to override the same name configuration in `config.py`. Therefore, if you can understand our configuration reading logic, we strongly recommend that you create a new configuration file named `config_private.py` next to `config.py`, and transfer (copy) the configuration in `config.py` to `config_private.py`. `config_private.py` is not controlled by git and can make your privacy information more secure. P.S. The project also supports configuring most options through `environment variables`, and the writing format of environment variables refers to the `docker-compose` file. Reading priority: `environment variables` > `config_private.py` > `config.py`)

3. Install dependencies.

```sh
# （Choose I: If familiar with Python）(Python version 3.9 or above, the newer the better) Note: Use the official pip source or Ali pip source. Temporary switching source method: python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python -m pip install -r requirements.txt

# (Choose II: If not familiar with Python) Use anaconda, the steps are the same (https://www.bilibili.com/video/BV1rc411W7Dr):
conda create -n gptac_venv python=3.11    # Create anaconda environment.
conda activate gptac_venv                 # Activate the anaconda environment.
python -m pip install -r requirements.txt # This step is the same as the pip installation step.
```

<details><summary>If you need to support Tsinghua ChatGLM/Fudan MOSS as a backend, click to expand.</summary>
<p>

[Optional Steps] If you need to support Tsinghua ChatGLM/Fudan MOSS as a backend, you need to install more dependencies (precondition: familiar with Python + used Pytorch + computer configuration). Strong enough):

```sh
# Optional step I: support Tsinghua ChatGLM. Tsinghua ChatGLM remarks: If you encounter the error "Call ChatGLM fail cannot load ChatGLM parameters normally", refer to the following: 1: The version installed above is torch+cpu version, using cuda requires uninstalling torch and reinstalling torch+cuda; 2: If the model cannot be loaded due to insufficient local configuration, you can modify the model accuracy in request_llm/bridge_chatglm.py, and change AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True) to AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).
python -m pip install -r request_llm/requirements_chatglm.txt  

# Optional Step II: Support Fudan MOSS.
python -m pip install -r request_llm/requirements_moss.txt
git clone https://github.com/OpenLMLab/MOSS.git request_llm/moss  # Note that when executing this line of code, it must be in the project root.

# 【Optional Step III】Ensure that the AVAIL_LLM_MODELS in the config.py configuration file contains the expected model. Currently, all supported models are as follows (jittorllms series currently only supports the docker solution):
AVAIL_LLM_MODELS = ["gpt-3.5-turbo", "api2d-gpt-3.5-turbo", "gpt-4", "api2d-gpt-4", "chatglm", "newbing", "moss"] # + ["jittorllms_rwkv", "jittorllms_pangualpha", "jittorllms_llama"]
```

</p>
</details>



4. Run.

```sh
python main.py
```5. Testing Function Plugin
```
- Test function plugin template function (requires gpt to answer what happened today in history), you can use this function as a template to implement more complex functions
    Click "[Function Plugin Template Demo] Today in History"
```

## Installation-Methods 2: Using Docker

1. Only ChatGPT (recommended for most people)

 ``` sh
git clone https://github.com/binary-husky/chatgpt_academic.git  # Download project
cd chatgpt_academic                                 # Enter path
nano config.py                                      # Edit config.py with any text editor ‑ configure "Proxy," "API_KEY," "WEB_PORT" (e.g., 50923) and more
docker build -t gpt-academic .                      # installation

#(Last step-Option 1) In a Linux environment, `--net=host` is more convenient and quick
docker run --rm -it --net=host gpt-academic
#(Last step-Option 2) In a macOS/windows environment, the -p option must be used to expose the container port (e.g., 50923) to the port on the host.
docker run --rm -it -e WEB_PORT=50923 -p 50923:50923 gpt-academic
```

2. ChatGPT + ChatGLM + MOSS (requires familiarity with Docker)

``` sh
# Modify docker-compose.yml, delete plans 1 and 3, and retain plan 2. Modify the configuration of plan 2 in docker-compose.yml, and reference the comments for instructions.
docker-compose up
```

3. ChatGPT + LLAMA + Pangu + RWKV (requires familiarity with Docker)
``` sh
# Modify docker-compose.yml, delete plans 1 and 2, and retain plan 3. Modify the configuration of plan 3 in docker-compose.yml, and reference the comments for instructions.
docker-compose up
```


## Installation-Method 3: Other Deployment Methods

1. How to use proxy URL/Microsoft Azure API
Configure API_URL_REDIRECT according to the instructions in `config.py`.

2. Remote Cloud Server Deployment (requires cloud server knowledge and experience)
Please visit [Deployment Wiki-1](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%9C%E7%A8%8B%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)

3. Using WSL2 (Windows Subsystem for Linux Subsystem)
Please visit [Deployment Wiki-2](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BD%BF%E7%94%A8WSL2%EF%BC%88Windows-Subsystem-for-Linux-%E5%AD%90%E7%B3%BB%E7%BB%9F%EF%BC%89%E9%83%A8%E7%BD%B2)

4. How to run on a secondary URL (such as `http://localhost/subpath`)
Please visit [FastAPI Running Instructions](docs/WithFastapi.md)

5. Run with docker-compose
Please read docker-compose.yml and follow the instructions provided therein.
---
# Advanced Usage
## Customize new convenience buttons/custom function plugins

1. Custom new convenience buttons (academic shortcut keys)
Open `core_functional.py` with any text editor, add the item as follows, and restart the program. (If the button has been added successfully and is visible, the prefix and suffix support hot modification without restarting the program.)
example:
```
"Super English to Chinese Translation": {
    # Prefix, which will be added before your input. For example, used to describe your request, such as translation, code interpretation, polish, etc.
    "Prefix": "Please translate the following content into Chinese, and explain the proper nouns in the text in a markdown table one by one:\n\n", 
    
    # Suffix, which will be added after your input. For example, in combination with the prefix, you can surround your input content with quotation marks.
    "Suffix": "",
},
```
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226899272-477c2134-ed71-4326-810c-29891fe4a508.png" width="500" >
</div>

<<<<<<< HEAD

---

## いくつかの機能の例

### 画像表示：

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/228737599-bf0a9d9c-1808-4f43-ae15-dfcc7af0f295.png" width="800" >
</div>


### プログラムが自己解析できる場合：

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226936850-c77d7183-0749-4c1c-9875-fd4891842d0c.png" width="800" >
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226936618-9b487e4b-ab5b-4b6e-84c6-16942102e917.png" width="800" >
</div>

### 他のPython/Cppプロジェクトの解析：

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="800" >
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226969067-968a27c1-1b9c-486b-8b81-ab2de8d3f88a.png" width="800" >
</div>

### Latex論文の一括読解と要約生成

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/227504406-86ab97cd-f208-41c3-8e4a-7000e51cf980.png" width="800" >
</div>

### 自動報告生成

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/227503770-fe29ce2c-53fd-47b0-b0ff-93805f0c2ff4.png" height="300" >
<img src="https://user-images.githubusercontent.com/96192199/227504617-7a497bb3-0a2a-4b50-9a8a-95ae60ea7afd.png" height="300" >
<img src="https://user-images.githubusercontent.com/96192199/227504005-efeaefe0-b687-49d0-bf95-2d7b7e66c348.png" height="300" >
</div>

### モジュール化された機能デザイン

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/229288270-093643c1-0018-487a-81e6-1d7809b6e90f.png" height="400" >
<img src="https://user-images.githubusercontent.com/96192199/227504931-19955f78-45cd-4d1c-adac-e71e50957915.png" height="400" >
</div>


### ソースコードの英語翻訳

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/229720562-fe6c3508-6142-4635-a83d-21eb3669baee.png" height="400" >
</div>

## Todo およびバージョン計画:
- version 3.2+ (todo): 関数プラグインがより多くのパラメーターインターフェースをサポートするようになります。
- version 3.1: 複数のgptモデルを同時にクエリし、api2dをサポートし、複数のapikeyの負荷分散をサポートします。
- version 3.0: chatglmおよび他の小型llmのサポート
- version 2.6: プラグイン構造を再構成し、相互作用性を高め、より多くのプラグインを追加しました。
- version 2.5: 自己更新。総括的な大規模プロジェクトのソースコードをまとめた場合、テキストが長すぎる、トークンがオーバーフローする問題を解決します。
- version 2.4: (1)PDF全文翻訳機能を追加。(2)入力エリアの位置を切り替える機能を追加。(3)垂直レイアウトオプションを追加。(4)マルチスレッド関数プラグインの最適化。
- version 2.3: 多スレッドの相互作用性を向上させました。
- version 2.2: 関数プラグインでホットリロードをサポート
- version 2.1: 折りたたみ式レイアウト
- version 2.0: モジュール化された関数プラグインを導入
- version 1.0: 基本機能

## 参考および学習


以下は中国語のマークダウンファイルです。日本語に翻訳してください。既存のマークダウンコマンドを変更しないでください：

```
多くの優秀なプロジェクトの設計を参考にしています。主なものは以下の通りです：

# 参考プロジェクト1：ChuanhuChatGPTから多くのテクニックを借用
https://github.com/GaiZhenbiao/ChuanhuChatGPT

# 参考プロジェクト2：清華ChatGLM-6B：
https://github.com/THUDM/ChatGLM-6B
```

=======
2. Custom function plugins

Write powerful function plugins to perform any task you can and cannot think of.
The difficulty of writing and debugging plugins in this project is low, and as long as you have a certain amount of python basic knowledge, you can follow the template provided by us to achieve your own plugin functions.
For details, please refer to the [Function Plugin Guide](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97).

---
# Latest Update
## New feature dynamics.
1. ダイアログの保存機能。関数プラグインエリアで '現在の会話を保存' を呼び出すと、現在のダイアログを読み取り可能で復元可能なHTMLファイルとして保存できます。さらに、関数プラグインエリア（ドロップダウンメニュー）で 'ダイアログの履歴保存ファイルを読み込む' を呼び出すことで、以前の会話を復元することができます。Tips:ファイルを指定せずに 'ダイアログの履歴保存ファイルを読み込む' をクリックすることで、過去のHTML保存ファイルのキャッシュを表示することができます。'すべてのローカルダイアログの履歴を削除' をクリックすることで、すべてのHTML保存ファイルのキャッシュを削除できます。
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/235222390-24a9acc0-680f-49f5-bc81-2f3161f1e049.png" width="500">
</div>


2. 報告書を生成します。ほとんどのプラグインは、実行が終了した後に作業報告書を生成します。
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/227503770-fe29ce2c-53fd-47b0-b0ff-93805f0c2ff4.png" height="300">
<img src="https://user-images.githubusercontent.com/96192199/227504617-7a497bb3-0a2a-4b50-9a8a-95ae60ea7afd.png" height="300">
<img src="https://user-images.githubusercontent.com/96192199/227504005-efeaefe0-b687-49d0-bf95-2d7b7e66c348.png" height="300">
</div>

3. モジュール化された機能設計、簡単なインターフェースで強力な機能をサポートする。
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/229288270-093643c1-0018-487a-81e6-1d7809b6e90f.png" height="400">
<img src="https://user-images.githubusercontent.com/96192199/227504931-19955f78-45cd-4d1c-adac-e71e50957915.png" height="400">
</div>

4. 自己解決可能なオープンソースプロジェクトです。
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226936850-c77d7183-0749-4c1c-9875-fd4891842d0c.png" width="500">
</div>


5. 他のオープンソースプロジェクトの解読、容易である。
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="500">
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226969067-968a27c1-1b9c-486b-8b81-ab2de8d3f88a.png" width="500">
</div>

6. [Live2D](https://github.com/fghrsh/live2d_demo)のデコレート小機能です。（デフォルトでは閉じてますが、 `config.py`を変更する必要があります。）
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/236432361-67739153-73e8-43fe-8111-b61296edabd9.png" width="500">
</div>

7. 新たにMOSS大言語モデルのサポートを追加しました。
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/236639178-92836f37-13af-4fdd-984d-b4450fe30336.png" width="500">
</div>

8. OpenAI画像生成
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/bc7ab234-ad90-48a0-8d62-f703d9e74665" width="500">
</div>

9. OpenAIオーディオの解析とサマリー
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/709ccf95-3aee-498a-934a-e1c22d3d5d5b" width="500">
</div>

10. 全文校正されたLaTeX
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/651ccd98-02c9-4464-91e1-77a6b7d1b033" width="500">
</div>


## バージョン：
- version 3.5（作業中）：すべての関数プラグインを自然言語で呼び出すことができるようにする（高い優先度）。
- version 3.4（作業中）：chatglmのローカルモデルのマルチスレッドをサポートすることで、機能を改善する。
- version 3.3：+Web情報の総合機能
- version 3.2：関数プラグインでさらに多くのパラメータインターフェイスをサポートする（ダイアログの保存機能、任意の言語コードの解読+同時に任意のLLM組み合わせに関する問い合わせ）
- version 3.1：複数のGPTモデルを同時に質問できるようになりました！ api2dをサポートし、複数のAPIキーを均等に負荷分散することができます。
- version 3.0：chatglmとその他の小型LLMのサポート。
- version 2.6：プラグイン構造を再構築し、対話内容を高め、より多くのプラグインを追加しました。
- version 2.5：自己アップデートし、長文書やトークンのオーバーフローの問題を解決しました。
- version 2.4：（1）全文翻訳のPDF機能を追加しました。（2）入力エリアの位置切り替え機能を追加しました。（3）垂直レイアウトオプションを追加しました。（4）マルチスレッド関数プラグインを最適化しました。
- version 2.3：マルチスレッド性能の向上。
- version 2.2：関数プラグインのホットリロードをサポートする。
- version 2.1：折りたたみ式レイアウト。
- version 2.0：モジュール化された関数プラグインを導入。
- version 1.0：基本機能

gpt_academic開発者QQグループ-2：610599535

- 既知の問題
    - 一部のブラウザ翻訳プラグインが、このソフトウェアのフロントエンドの実行を妨害する
    - gradioバージョンが高すぎるか低すぎると、多くの異常が引き起こされる

## 参考学習

```
コードの中には、他の優れたプロジェクトの設計から参考にしたものがたくさん含まれています：

# プロジェクト1：清華ChatGLM-6B:
https://github.com/THUDM/ChatGLM-6B

# プロジェクト2：清華JittorLLMs:
https://github.com/Jittor/JittorLLMs

# プロジェクト3：Edge-GPT:
https://github.com/acheong08/EdgeGPT

# プロジェクト4：ChuanhuChatGPT:
https://github.com/GaiZhenbiao/ChuanhuChatGPT

# プロジェクト5：ChatPaper:
https://github.com/kaixindelele/ChatPaper

# その他：
https://github.com/gradio-app/gradio
https://github.com/fghrsh/live2d_demo
```
>>>>>>> upstream/master
