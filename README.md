# EmojiToImage

絵文字を画像に変換して投稿し直してくれるDiscord Bot。
元の絵文字メッセージは削除されます。
ファイル構成はherokuでの運用を前提としています。

**使い方**
1. e2i_bot.pyを編集して6行目にトークンを設定する
2. imageディレクトリを作成する
3. Imageディレクトリ配下に変換後の画像ファイルを配置する
　ファイル名はDiscord上の絵文字のエイリアス名から"_"または"__"を取り除いたもの
4. herokuにデプロイする

詳細な使い方は[note記事](https://note.com/yogox/n/nd7824a8fe950?magazine_key=m672d63b41a0e)を参照。
