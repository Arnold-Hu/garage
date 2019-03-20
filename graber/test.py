# coding=utf-8
import requests
import time
import sys
import json
reload(sys)  #重新加载sys"
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数"


def parse(data, f):
    for line in data["result"]["rows"]:
        rcontent = []
        for i in line["rcontext"]:
            rcontent.append(i["orth_token"])
        lcontent = []
        for i in line["lcontext"]:
            lcontent.append(i["orth_token"])

        lcontent.append(line["orth_base"])
        lcontent.extend(rcontent)
        f.write("".join(lcontent))
        f.write("\n")

def scrabe_with_keyword(keyword):
    payload=dict()
    payload["retrievalMethod"]="文字列検索"
    payload["condDescription"]="検索フォームで検索"
    payload["queryString"]=keyword
    payload["searchFormOptions[resultUnitWord]"]="short"
    payload["searchFormOptions[keyDisplay]"]="0"
    payload["retrievalTarget[PN][core]"]="true"
    payload["retrievalTarget[PN][core]"]="false"
    payload["retrievalTarget[PM][core]"]="true"
    payload["retrievalTarget[PM][core]"]="false"
    payload["retrievalTarget[PB][core]"]="true"
    payload["retrievalTarget[PB][core]"]="false"
    payload["retrievalTarget[LB][core]"]="false"
    payload["retrievalTarget[OW][core]"]="true"
    payload["retrievalTarget[OW][core]"]="false"
    payload["retrievalTarget[OB][core]"]="false"
    payload["retrievalTarget[OC][core]"]="true"
    payload["retrievalTarget[OC][core]"]="false"
    payload["retrievalTarget[OY][core]"]="true"
    payload["retrievalTarget[OY][core]"]="false"
    payload["retrievalTarget[OL][core]"]="false"
    payload["retrievalTarget[OM][core]"]="false"
    payload["retrievalTarget[OP][core]"]="false"
    payload["retrievalTarget[OT][core]"]="false"
    payload["retrievalTarget[OV][core]"]="false"
    payload["retrievalTarget[PN][genreAll]"]="on"
    payload["retrievalTarget[PN][genre1]"]="全国紙"
    payload["retrievalTarget[PN][genre2]"]="全国紙/朝日新聞"
    payload["retrievalTarget[PN][genre2]"]="全国紙/読売新聞"
    payload["retrievalTarget[PN][genre2]"]="全国紙/毎日新聞"
    payload["retrievalTarget[PN][genre2]"]="全国紙/産経新聞"
    payload["retrievalTarget[PN][genre1]"]="ブロック紙"
    payload["retrievalTarget[PN][genre2]"]="ブロック紙/北海道新聞"
    payload["retrievalTarget[PN][genre2]"]="ブロック紙/中日新聞"
    payload["retrievalTarget[PN][genre2]"]="ブロック紙/西日本新聞"
    payload["retrievalTarget[PN][genre1]"]="地方紙"
    payload["retrievalTarget[PN][genre2]"]="地方紙/河北新報"
    payload["retrievalTarget[PN][genre2]"]="地方紙/新潟日報"
    payload["retrievalTarget[PN][genre2]"]="地方紙/京都新聞"
    payload["retrievalTarget[PN][genre2]"]="地方紙/神戸新聞"
    payload["retrievalTarget[PN][genre2]"]="地方紙/中国新聞"
    payload["retrievalTarget[PN][genre2]"]="地方紙/高知新聞"
    payload["retrievalTarget[PN][genre2]"]="地方紙/琉球新報"
    payload["retrievalTarget[PM][genreAll]"]="on"
    payload["retrievalTarget[PM][genre1]"]="総合"
    payload["retrievalTarget[PM][genre2]"]="総合/総記／マスコミ"
    payload["retrievalTarget[PM][genre2]"]="総合/一般"
    payload["retrievalTarget[PM][genre2]"]="総合/家庭／生活"
    payload["retrievalTarget[PM][genre2]"]="総合/児童"
    payload["retrievalTarget[PM][genre2]"]="総合/娯楽／芸能"
    payload["retrievalTarget[PM][genre2]"]="総合/レジャー／趣味"
    payload["retrievalTarget[PM][genre2]"]="総合/スポーツ"
    payload["retrievalTarget[PM][genre1]"]="教育・学芸"
    payload["retrievalTarget[PM][genre2]"]="教育・学芸/教育"
    payload["retrievalTarget[PM][genre2]"]="教育・学芸/学習／語学"
    payload["retrievalTarget[PM][genre2]"]="教育・学芸/文学／芸術"
    payload["retrievalTarget[PM][genre2]"]="教育・学芸/社会科学"
    payload["retrievalTarget[PM][genre2]"]="教育・学芸/自然科学"
    payload["retrievalTarget[PM][genre2]"]="教育・学芸/人文科学"
    payload["retrievalTarget[PM][genre1]"]="政治・経済・商業"
    payload["retrievalTarget[PM][genre2]"]="政治・経済・商業/政治／外交"
    payload["retrievalTarget[PM][genre2]"]="政治・経済・商業/経済／経営"
    payload["retrievalTarget[PM][genre2]"]="政治・経済・商業/金融／財政"
    payload["retrievalTarget[PM][genre2]"]="政治・経済・商業/商業／消費者"
    payload["retrievalTarget[PM][genre2]"]="政治・経済・商業/国勢／民力"
    payload["retrievalTarget[PM][genre1]"]="産業"
    payload["retrievalTarget[PM][genre2]"]="産業/農林水産"
    payload["retrievalTarget[PM][genre2]"]="産業/運輸／通信"
    payload["retrievalTarget[PM][genre1]"]="工業"
    payload["retrievalTarget[PM][genre2]"]="工業/機械"
    payload["retrievalTarget[PM][genre2]"]="工業/電気機／電子"
    payload["retrievalTarget[PM][genre1]"]="厚生・医療"
    payload["retrievalTarget[PM][genre2]"]="厚生・医療/厚生"
    payload["retrievalTarget[PM][genre2]"]="厚生・医療/医学"
    payload["retrievalTarget[PB][genreAll]"]="on"
    payload["retrievalTarget[PB][genre1]"]="0 総記"
    payload["retrievalTarget[PB][genre1]"]="1 哲学"
    payload["retrievalTarget[PB][genre1]"]="2 歴史"
    payload["retrievalTarget[PB][genre1]"]="3 社会科学"
    payload["retrievalTarget[PB][genre1]"]="4 自然科学"
    payload["retrievalTarget[PB][genre1]"]="5 技術・工学"
    payload["retrievalTarget[PB][genre1]"]="6 産業"
    payload["retrievalTarget[PB][genre1]"]="7 芸術・美術"
    payload["retrievalTarget[PB][genre1]"]="8 言語"
    payload["retrievalTarget[PB][genre1]"]="9 文学"
    payload["retrievalTarget[PB][genre1]"]="分類なし"
    payload["retrievalTarget[LB][genreAll]"]="on"
    payload["retrievalTarget[LB][genre1]"]="0 総記"
    payload["retrievalTarget[LB][genre1]"]="1 哲学"
    payload["retrievalTarget[LB][genre1]"]="2 歴史"
    payload["retrievalTarget[LB][genre1]"]="3 社会科学"
    payload["retrievalTarget[LB][genre1]"]="4 自然科学"
    payload["retrievalTarget[LB][genre1]"]="5 技術・工学"
    payload["retrievalTarget[LB][genre1]"]="6 産業"
    payload["retrievalTarget[LB][genre1]"]="7 芸術・美術"
    payload["retrievalTarget[LB][genre1]"]="8 言語"
    payload["retrievalTarget[LB][genre1]"]="9 文学"
    payload["retrievalTarget[LB][genre1]"]="分類なし"
    payload["retrievalTarget[OW][genreAll]"]="on"
    payload["retrievalTarget[OW][genre1]"]="国土交通"
    payload["retrievalTarget[OW][genre2]"]="国土交通/観光白書"
    payload["retrievalTarget[OW][genre2]"]="国土交通/国土交通白書（運輸白書，建設白書）"
    payload["retrievalTarget[OW][genre2]"]="国土交通/首都圏白書"
    payload["retrievalTarget[OW][genre2]"]="国土交通/土地白書（国土利用白書）"
    payload["retrievalTarget[OW][genre1]"]="外交"
    payload["retrievalTarget[OW][genre2]"]="外交/外交青書（わが外交の近況）"
    payload["retrievalTarget[OW][genre2]"]="外交/政府開発援助白書（我が国の政府開発援助）"
    payload["retrievalTarget[OW][genre1]"]="安全"
    payload["retrievalTarget[OW][genre2]"]="安全/警察白書"
    payload["retrievalTarget[OW][genre2]"]="安全/原子力安全白書"
    payload["retrievalTarget[OW][genre2]"]="安全/原子力白書"
    payload["retrievalTarget[OW][genre2]"]="安全/交通安全白書"
    payload["retrievalTarget[OW][genre2]"]="安全/公害紛争処理白書"
    payload["retrievalTarget[OW][genre2]"]="安全/消防白書"
    payload["retrievalTarget[OW][genre2]"]="安全/犯罪白書"
    payload["retrievalTarget[OW][genre2]"]="安全/防衛白書"
    payload["retrievalTarget[OW][genre2]"]="安全/防災白書"
    payload["retrievalTarget[OW][genre1]"]="教育"
    payload["retrievalTarget[OW][genre2]"]="教育/文部科学白書（我が国の文教施策）"
    payload["retrievalTarget[OW][genre1]"]="環境"
    payload["retrievalTarget[OW][genre2]"]="環境/環境白書"
    payload["retrievalTarget[OW][genre2]"]="環境/循環型社会白書"
    payload["retrievalTarget[OW][genre1]"]="福祉"
    payload["retrievalTarget[OW][genre2]"]="福祉/厚生労働白書（厚生白書）"
    payload["retrievalTarget[OW][genre2]"]="福祉/高齢社会白書"
    payload["retrievalTarget[OW][genre2]"]="福祉/国民生活白書"
    payload["retrievalTarget[OW][genre2]"]="福祉/少子化社会白書"
    payload["retrievalTarget[OW][genre2]"]="福祉/障害者白書"
    payload["retrievalTarget[OW][genre2]"]="福祉/人権教育・啓発白書"
    payload["retrievalTarget[OW][genre2]"]="福祉/青少年白書"
    payload["retrievalTarget[OW][genre2]"]="福祉/男女共同参画白書"
    payload["retrievalTarget[OW][genre1]"]="科学技術"
    payload["retrievalTarget[OW][genre2]"]="科学技術/科学技術白書"
    payload["retrievalTarget[OW][genre2]"]="科学技術/情報通信白書（通信白書）"
    payload["retrievalTarget[OW][genre1]"]="経済"
    payload["retrievalTarget[OW][genre2]"]="経済/エネルギー白書"
    payload["retrievalTarget[OW][genre2]"]="経済/ものづくり白書（製造基盤白書）"
    payload["retrievalTarget[OW][genre2]"]="経済/経済財政白書（経済白書）"
    payload["retrievalTarget[OW][genre2]"]="経済/公益法人白書"
    payload["retrievalTarget[OW][genre2]"]="経済/独占禁止白書（独占白書）"
    payload["retrievalTarget[OW][genre2]"]="経済/地方財政白書"
    payload["retrievalTarget[OW][genre2]"]="経済/中小企業白書"
    payload["retrievalTarget[OW][genre2]"]="経済/通商白書"
    payload["retrievalTarget[OW][genre2]"]="経済/労働経済白書（労働白書）"
    payload["retrievalTarget[OW][genre1]"]="農林水産"
    payload["retrievalTarget[OW][genre2]"]="農林水産/食料農業農村白書（農業白書）"
    payload["retrievalTarget[OW][genre2]"]="農林水産/森林・林業白書（林業白書）"
    payload["retrievalTarget[OW][genre2]"]="農林水産/水産白書（漁業白書）"
    payload["retrievalTarget[OB][genreAll]"]="on"
    payload["retrievalTarget[OB][genre1]"]="0 総記"
    payload["retrievalTarget[OB][genre1]"]="1 哲学"
    payload["retrievalTarget[OB][genre1]"]="2 歴史"
    payload["retrievalTarget[OB][genre1]"]="3 社会科学"
    payload["retrievalTarget[OB][genre1]"]="4 自然科学"
    payload["retrievalTarget[OB][genre1]"]="5 技術・工学"
    payload["retrievalTarget[OB][genre1]"]="6 産業"
    payload["retrievalTarget[OB][genre1]"]="7 芸術・美術"
    payload["retrievalTarget[OB][genre1]"]="8 言語"
    payload["retrievalTarget[OB][genre1]"]="9 文学"
    payload["retrievalTarget[OB][genre1]"]="分類なし"
    payload["retrievalTarget[OC][genreAll]"]="on"
    payload["retrievalTarget[OC][genre1]"]="エンターテインメントと趣味"
    payload["retrievalTarget[OC][genre2]"]="エンターテインメントと趣味/ゲーム"
    payload["retrievalTarget[OC][genre2]"]="エンターテインメントと趣味/テレビ、ラジオ"
    payload["retrievalTarget[OC][genre2]"]="エンターテインメントと趣味/映画"
    payload["retrievalTarget[OC][genre2]"]="エンターテインメントと趣味/音楽"
    payload["retrievalTarget[OC][genre2]"]="エンターテインメントと趣味/芸能人、タレント"
    payload["retrievalTarget[OC][genre2]"]="エンターテインメントと趣味/占い、超常現象"
    payload["retrievalTarget[OC][genre2]"]="エンターテインメントと趣味/本、雑誌、コミック"
    payload["retrievalTarget[OC][genre1]"]="インターネット、PCと家電"
    payload["retrievalTarget[OC][genre2]"]="インターネット、PCと家電/インターネット"
    payload["retrievalTarget[OC][genre2]"]="インターネット、PCと家電/パソコン、周辺機器"
    payload["retrievalTarget[OC][genre2]"]="インターネット、PCと家電/家電、AV機器"
    payload["retrievalTarget[OC][genre2]"]="インターネット、PCと家電/携帯電話、モバイル"
    payload["retrievalTarget[OC][genre1]"]="ビジネス、経済とお金"
    payload["retrievalTarget[OC][genre2]"]="ビジネス、経済とお金/家計、貯金"
    payload["retrievalTarget[OC][genre2]"]="ビジネス、経済とお金/株と経済"
    payload["retrievalTarget[OC][genre2]"]="ビジネス、経済とお金/企業と経営"
    payload["retrievalTarget[OC][genre2]"]="ビジネス、経済とお金/保険、税金、年金"
    payload["retrievalTarget[OC][genre1]"]="職業とキャリア"
    payload["retrievalTarget[OC][genre2]"]="職業とキャリア/資格、習い事"
    payload["retrievalTarget[OC][genre2]"]="職業とキャリア/就職、転職"
    payload["retrievalTarget[OC][genre2]"]="職業とキャリア/派遣、アルバイト、パート"
    payload["retrievalTarget[OC][genre2]"]="職業とキャリア/労働問題、働き方"
    payload["retrievalTarget[OC][genre1]"]="ニュース、政治、国際情勢"
    payload["retrievalTarget[OC][genre2]"]="ニュース、政治、国際情勢/ニュース、事件"
    payload["retrievalTarget[OC][genre2]"]="ニュース、政治、国際情勢/政治、社会問題"
    payload["retrievalTarget[OC][genre1]"]="スポーツ、アウトドア、車"
    payload["retrievalTarget[OC][genre2]"]="スポーツ、アウトドア、車/アウトドア"
    payload["retrievalTarget[OC][genre2]"]="スポーツ、アウトドア、車/スポーツ"
    payload["retrievalTarget[OC][genre2]"]="スポーツ、アウトドア、車/バイク"
    payload["retrievalTarget[OC][genre2]"]="スポーツ、アウトドア、車/自動車"
    payload["retrievalTarget[OC][genre1]"]="暮らしと生活ガイド"
    payload["retrievalTarget[OC][genre2]"]="暮らしと生活ガイド/ショッピング"
    payload["retrievalTarget[OC][genre2]"]="暮らしと生活ガイド/ボランティア、環境問題、国際協力"
    payload["retrievalTarget[OC][genre2]"]="暮らしと生活ガイド/家事、住宅"
    payload["retrievalTarget[OC][genre2]"]="暮らしと生活ガイド/公共施設、役所"
    payload["retrievalTarget[OC][genre2]"]="暮らしと生活ガイド/福祉、介護"
    payload["retrievalTarget[OC][genre2]"]="暮らしと生活ガイド/法律、消費者問題"
    payload["retrievalTarget[OC][genre2]"]="暮らしと生活ガイド/料理、グルメ、レシピ"
    payload["retrievalTarget[OC][genre1]"]="健康、美容とファッション"
    payload["retrievalTarget[OC][genre2]"]="健康、美容とファッション/コスメ、美容"
    payload["retrievalTarget[OC][genre2]"]="健康、美容とファッション/ファッション"
    payload["retrievalTarget[OC][genre2]"]="健康、美容とファッション/メンタルヘルス"
    payload["retrievalTarget[OC][genre2]"]="健康、美容とファッション/健康、病気、ダイエット"
    payload["retrievalTarget[OC][genre2]"]="健康、美容とファッション/恋愛相談、人間関係の悩み"
    payload["retrievalTarget[OC][genre1]"]="子育てと学校"
    payload["retrievalTarget[OC][genre2]"]="子育てと学校/子育て、出産"
    payload["retrievalTarget[OC][genre2]"]="子育てと学校/受験、進学"
    payload["retrievalTarget[OC][genre2]"]="子育てと学校/小・中学校、高校"
    payload["retrievalTarget[OC][genre2]"]="子育てと学校/大学、留学"
    payload["retrievalTarget[OC][genre2]"]="子育てと学校/幼児教育、幼稚園、保育園"
    payload["retrievalTarget[OC][genre1]"]="マナー、冠婚葬祭"
    payload["retrievalTarget[OC][genre2]"]="マナー、冠婚葬祭/マナー"
    payload["retrievalTarget[OC][genre2]"]="マナー、冠婚葬祭/冠婚葬祭"
    payload["retrievalTarget[OC][genre2]"]="マナー、冠婚葬祭/祭りと年中行事"
    payload["retrievalTarget[OC][genre1]"]="教養と学問、サイエンス"
    payload["retrievalTarget[OC][genre2]"]="教養と学問、サイエンス/一般教養"
    payload["retrievalTarget[OC][genre2]"]="教養と学問、サイエンス/芸術、文学、歴史"
    payload["retrievalTarget[OC][genre2]"]="教養と学問、サイエンス/言葉、語学"
    payload["retrievalTarget[OC][genre2]"]="教養と学問、サイエンス/数学、サイエンス"
    payload["retrievalTarget[OC][genre2]"]="教養と学問、サイエンス/天気、天文、宇宙"
    payload["retrievalTarget[OC][genre2]"]="教養と学問、サイエンス/動物、植物、ペット"
    payload["retrievalTarget[OC][genre1]"]="地域、旅行、お出かけ"
    payload["retrievalTarget[OC][genre2]"]="地域、旅行、お出かけ/海外"
    payload["retrievalTarget[OC][genre2]"]="地域、旅行、お出かけ/交通、地図"
    payload["retrievalTarget[OC][genre2]"]="地域、旅行、お出かけ/国内"
    payload["retrievalTarget[OC][genre1]"]="Yahoo! JAPAN"
    payload["retrievalTarget[OC][genre2]"]="Yahoo! JAPAN/Yahoo!オークション"
    payload["retrievalTarget[OC][genre2]"]="Yahoo! JAPAN/Yahoo!サービス"
    payload["retrievalTarget[OC][genre2]"]="Yahoo! JAPAN/Yahoo!知恵袋"
    payload["retrievalTarget[OC][genre1]"]="その他"
    payload["retrievalTarget[OC][genre2]"]="その他/アダルト"
    payload["retrievalTarget[OC][genre2]"]="その他/ギャンブル"
    payload["retrievalTarget[OY][genreAll]"]="on"
    payload["retrievalTarget[OY][genre1]"]="ビジネスと経済"
    payload["retrievalTarget[OY][genre2]"]="ビジネスと経済/ビジネス"
    payload["retrievalTarget[OY][genre2]"]="ビジネスと経済/金融と投資"
    payload["retrievalTarget[OY][genre2]"]="ビジネスと経済/経済"
    payload["retrievalTarget[OY][genre2]"]="ビジネスと経済/雇用"
    payload["retrievalTarget[OY][genre2]"]="ビジネスと経済/職種"
    payload["retrievalTarget[OY][genre1]"]="コンピュータとインターネット"
    payload["retrievalTarget[OY][genre2]"]="コンピュータとインターネット/インターネット"
    payload["retrievalTarget[OY][genre2]"]="コンピュータとインターネット/コンピュータ"
    payload["retrievalTarget[OY][genre1]"]="生活と文化"
    payload["retrievalTarget[OY][genre2]"]="生活と文化/グルメ、ドリンク"
    payload["retrievalTarget[OY][genre2]"]="生活と文化/環境問題"
    payload["retrievalTarget[OY][genre2]"]="生活と文化/季節"
    payload["retrievalTarget[OY][genre2]"]="生活と文化/災害"
    payload["retrievalTarget[OY][genre2]"]="生活と文化/事件・事故"
    payload["retrievalTarget[OY][genre2]"]="生活と文化/祝日、記念日、年中行事"
    payload["retrievalTarget[OY][genre2]"]="生活と文化/文化活動"
    payload["retrievalTarget[OY][genre1]"]="エンターテインメント"
    payload["retrievalTarget[OY][genre2]"]="エンターテインメント/テーマパーク"
    payload["retrievalTarget[OY][genre2]"]="エンターテインメント/テレビ"
    payload["retrievalTarget[OY][genre2]"]="エンターテインメント/映画"
    payload["retrievalTarget[OY][genre2]"]="エンターテインメント/音楽"
    payload["retrievalTarget[OY][genre2]"]="エンターテインメント/芸能人、タレント"
    payload["retrievalTarget[OY][genre2]"]="エンターテインメント/占い"
    payload["retrievalTarget[OY][genre2]"]="エンターテインメント/超常現象"
    payload["retrievalTarget[OY][genre1]"]="家庭と住まい"
    payload["retrievalTarget[OY][genre2]"]="家庭と住まい/ペット、動物"
    payload["retrievalTarget[OY][genre2]"]="家庭と住まい/家庭"
    payload["retrievalTarget[OY][genre2]"]="家庭と住まい/家庭電化製品"
    payload["retrievalTarget[OY][genre2]"]="家庭と住まい/住まい"
    payload["retrievalTarget[OY][genre1]"]="政治"
    payload["retrievalTarget[OY][genre2]"]="政治/国際情勢"
    payload["retrievalTarget[OY][genre2]"]="政治/政界と政治活動"
    payload["retrievalTarget[OY][genre1]"]="健康と医学"
    payload["retrievalTarget[OY][genre2]"]="健康と医学/美容と健康"
    payload["retrievalTarget[OY][genre2]"]="健康と医学/病気、症状"
    payload["retrievalTarget[OY][genre1]"]="学校と教育"
    payload["retrievalTarget[OY][genre2]"]="学校と教育/学校"
    payload["retrievalTarget[OY][genre2]"]="学校と教育/教育"
    payload["retrievalTarget[OY][genre1]"]="科学"
    payload["retrievalTarget[OY][genre2]"]="科学/自然科学"
    payload["retrievalTarget[OY][genre2]"]="科学/社会科学"
    payload["retrievalTarget[OY][genre1]"]="出会い"
    payload["retrievalTarget[OY][genre2]"]="出会い/結婚"
    payload["retrievalTarget[OY][genre2]"]="出会い/恋愛"
    payload["retrievalTarget[OY][genre1]"]="地域"
    payload["retrievalTarget[OY][genre2]"]="地域/世界の地方"
    payload["retrievalTarget[OY][genre2]"]="地域/日本"
    payload["retrievalTarget[OY][genre1]"]="特集"
    payload["retrievalTarget[OY][genre2]"]="特集/趣味とスポーツ"
    payload["retrievalTarget[OY][genre1]"]="芸術と人文"
    payload["retrievalTarget[OY][genre2]"]="芸術と人文/デザイン"
    payload["retrievalTarget[OY][genre2]"]="芸術と人文/芸術、アート"
    payload["retrievalTarget[OY][genre2]"]="芸術と人文/人文科学"
    payload["retrievalTarget[OY][genre2]"]="芸術と人文/舞台、演劇"
    payload["retrievalTarget[OY][genre2]"]="芸術と人文/文学"
    payload["retrievalTarget[OY][genre1]"]="Yahoo!サービス"
    payload["retrievalTarget[OY][genre2]"]="Yahoo!サービス/Yahoo!アバター"
    payload["retrievalTarget[OY][genre2]"]="Yahoo!サービス/Yahoo!オークション"
    payload["retrievalTarget[OY][genre2]"]="Yahoo!サービス/Yahoo!ゲーム"
    payload["retrievalTarget[OY][genre2]"]="Yahoo!サービス/Yahoo!ショッピング"
    payload["retrievalTarget[OY][genre2]"]="Yahoo!サービス/Yahoo!スポーツ"
    payload["retrievalTarget[OY][genre2]"]="Yahoo!サービス/Yahoo!ブログ"
    payload["retrievalTarget[OY][genre1]"]="趣味とスポーツ"
    payload["retrievalTarget[OY][genre2]"]="趣味とスポーツ/ギャンブル"
    payload["retrievalTarget[OY][genre2]"]="趣味とスポーツ/スポーツ"
    payload["retrievalTarget[OY][genre2]"]="趣味とスポーツ/レジャー"
    payload["retrievalTarget[OY][genre2]"]="趣味とスポーツ/趣味"
    payload["retrievalTarget[OY][genre2]"]="趣味とスポーツ/乗り物"
    payload["retrievalTarget[OL][genreAll]"]="on"
    payload["retrievalTarget[OL][genre1]"]="01 憲法"
    payload["retrievalTarget[OL][genre1]"]="02 国会"
    payload["retrievalTarget[OL][genre1]"]="03 行政組織"
    payload["retrievalTarget[OL][genre1]"]="04 国家公務員"
    payload["retrievalTarget[OL][genre1]"]="05 行政手続"
    payload["retrievalTarget[OL][genre1]"]="07 地方自治"
    payload["retrievalTarget[OL][genre1]"]="08 地方財政"
    payload["retrievalTarget[OL][genre1]"]="09 司法"
    payload["retrievalTarget[OL][genre1]"]="10 民事"
    payload["retrievalTarget[OL][genre1]"]="11 刑事"
    payload["retrievalTarget[OL][genre1]"]="12 警察"
    payload["retrievalTarget[OL][genre1]"]="14 国土開発"
    payload["retrievalTarget[OL][genre1]"]="15 土地"
    payload["retrievalTarget[OL][genre1]"]="16 都市計画"
    payload["retrievalTarget[OL][genre1]"]="17 道路"
    payload["retrievalTarget[OL][genre1]"]="19 災害対策"
    payload["retrievalTarget[OL][genre1]"]="20 建築・住宅"
    payload["retrievalTarget[OL][genre1]"]="21 財務通則"
    payload["retrievalTarget[OL][genre1]"]="23 国税"
    payload["retrievalTarget[OL][genre1]"]="24 専売・事業"
    payload["retrievalTarget[OL][genre1]"]="25 国債"
    payload["retrievalTarget[OL][genre1]"]="26 教育"
    payload["retrievalTarget[OL][genre1]"]="27 文化"
    payload["retrievalTarget[OL][genre1]"]="28 産業通則"
    payload["retrievalTarget[OL][genre1]"]="29 農業"
    payload["retrievalTarget[OL][genre1]"]="30 林業"
    payload["retrievalTarget[OL][genre1]"]="31 水産業"
    payload["retrievalTarget[OL][genre1]"]="32 鉱業"
    payload["retrievalTarget[OL][genre1]"]="33 工業"
    payload["retrievalTarget[OL][genre1]"]="34 商業"
    payload["retrievalTarget[OL][genre1]"]="35 金融・保険"
    payload["retrievalTarget[OL][genre1]"]="37 陸運"
    payload["retrievalTarget[OL][genre1]"]="38 海運"
    payload["retrievalTarget[OL][genre1]"]="39 航空"
    payload["retrievalTarget[OL][genre1]"]="40 貨物運送"
    payload["retrievalTarget[OL][genre1]"]="42 郵務"
    payload["retrievalTarget[OL][genre1]"]="43 電気通信"
    payload["retrievalTarget[OL][genre1]"]="44 労働"
    payload["retrievalTarget[OL][genre1]"]="45 環境保全"
    payload["retrievalTarget[OL][genre1]"]="46 厚生"
    payload["retrievalTarget[OL][genre1]"]="47 社会福祉"
    payload["retrievalTarget[OL][genre1]"]="49 防衛"
    payload["retrievalTarget[OL][genre1]"]="50 外事"
    payload["retrievalTarget[OM][genreAll]"]="on"
    payload["retrievalTarget[OM][genre1]"]="衆議院"
    payload["retrievalTarget[OM][genre2]"]="衆議院/本会議"
    payload["retrievalTarget[OM][genre2]"]="衆議院/常任委員会"
    payload["retrievalTarget[OM][genre2]"]="衆議院/特別委員会"
    payload["retrievalTarget[OM][genre2]"]="衆議院/その他"
    payload["retrievalTarget[OM][genre1]"]="参議院"
    payload["retrievalTarget[OM][genre2]"]="参議院/本会議"
    payload["retrievalTarget[OM][genre2]"]="参議院/常任委員会"
    payload["retrievalTarget[OM][genre2]"]="参議院/特別委員会"
    payload["retrievalTarget[OM][genre2]"]="参議院/その他"
    payload["retrievalTarget[OP][genreAll]"]="on"
    payload["retrievalTarget[OP][genre1]"]="北海道"
    payload["retrievalTarget[OP][genre2]"]="北海道/北海道"
    payload["retrievalTarget[OP][genre1]"]="東北地方"
    payload["retrievalTarget[OP][genre2]"]="東北地方/青森県"
    payload["retrievalTarget[OP][genre2]"]="東北地方/岩手県"
    payload["retrievalTarget[OP][genre2]"]="東北地方/宮城県"
    payload["retrievalTarget[OP][genre2]"]="東北地方/秋田県"
    payload["retrievalTarget[OP][genre2]"]="東北地方/山形県"
    payload["retrievalTarget[OP][genre2]"]="東北地方/福島県"
    payload["retrievalTarget[OP][genre1]"]="関東地方"
    payload["retrievalTarget[OP][genre2]"]="関東地方/茨城県"
    payload["retrievalTarget[OP][genre2]"]="関東地方/栃木県"
    payload["retrievalTarget[OP][genre2]"]="関東地方/群馬県"
    payload["retrievalTarget[OP][genre2]"]="関東地方/埼玉県"
    payload["retrievalTarget[OP][genre2]"]="関東地方/千葉県"
    payload["retrievalTarget[OP][genre2]"]="関東地方/東京都"
    payload["retrievalTarget[OP][genre2]"]="関東地方/神奈川県"
    payload["retrievalTarget[OP][genre1]"]="中部地方"
    payload["retrievalTarget[OP][genre2]"]="中部地方/新潟県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/富山県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/石川県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/福井県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/山梨県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/長野県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/岐阜県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/静岡県"
    payload["retrievalTarget[OP][genre2]"]="中部地方/愛知県"
    payload["retrievalTarget[OP][genre1]"]="近畿地方"
    payload["retrievalTarget[OP][genre2]"]="近畿地方/三重県"
    payload["retrievalTarget[OP][genre2]"]="近畿地方/滋賀県"
    payload["retrievalTarget[OP][genre2]"]="近畿地方/京都府"
    payload["retrievalTarget[OP][genre2]"]="近畿地方/大阪府"
    payload["retrievalTarget[OP][genre2]"]="近畿地方/兵庫県"
    payload["retrievalTarget[OP][genre2]"]="近畿地方/奈良県"
    payload["retrievalTarget[OP][genre2]"]="近畿地方/和歌山県"
    payload["retrievalTarget[OP][genre1]"]="中国地方"
    payload["retrievalTarget[OP][genre2]"]="中国地方/鳥取県"
    payload["retrievalTarget[OP][genre2]"]="中国地方/島根県"
    payload["retrievalTarget[OP][genre2]"]="中国地方/岡山県"
    payload["retrievalTarget[OP][genre2]"]="中国地方/広島県"
    payload["retrievalTarget[OP][genre2]"]="中国地方/山口県"
    payload["retrievalTarget[OP][genre1]"]="四国地方"
    payload["retrievalTarget[OP][genre2]"]="四国地方/徳島県"
    payload["retrievalTarget[OP][genre2]"]="四国地方/香川県"
    payload["retrievalTarget[OP][genre2]"]="四国地方/愛媛県"
    payload["retrievalTarget[OP][genre2]"]="四国地方/高知県"
    payload["retrievalTarget[OP][genre1]"]="九州・沖縄地方"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/福岡県"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/佐賀県"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/長崎県"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/熊本県"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/大分県"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/宮崎県"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/鹿児島県"
    payload["retrievalTarget[OP][genre2]"]="九州・沖縄地方/沖縄県"
    payload["retrievalTarget[OT][genreAll]"]="on"
    payload["retrievalTarget[OT][genre1]"]="国語"
    payload["retrievalTarget[OT][genre2]"]="国語/小"
    payload["retrievalTarget[OT][genre2]"]="国語/中"
    payload["retrievalTarget[OT][genre2]"]="国語/高"
    payload["retrievalTarget[OT][genre1]"]="数学"
    payload["retrievalTarget[OT][genre2]"]="数学/小"
    payload["retrievalTarget[OT][genre2]"]="数学/中"
    payload["retrievalTarget[OT][genre2]"]="数学/高"
    payload["retrievalTarget[OT][genre1]"]="理科"
    payload["retrievalTarget[OT][genre2]"]="理科/小"
    payload["retrievalTarget[OT][genre2]"]="理科/中"
    payload["retrievalTarget[OT][genre2]"]="理科/高"
    payload["retrievalTarget[OT][genre1]"]="社会"
    payload["retrievalTarget[OT][genre2]"]="社会/小"
    payload["retrievalTarget[OT][genre2]"]="社会/中"
    payload["retrievalTarget[OT][genre2]"]="社会/高"
    payload["retrievalTarget[OT][genre1]"]="外国語"
    payload["retrievalTarget[OT][genre2]"]="外国語/中"
    payload["retrievalTarget[OT][genre2]"]="外国語/高"
    payload["retrievalTarget[OT][genre1]"]="技術家庭"
    payload["retrievalTarget[OT][genre2]"]="技術家庭/小"
    payload["retrievalTarget[OT][genre2]"]="技術家庭/中"
    payload["retrievalTarget[OT][genre2]"]="技術家庭/高"
    payload["retrievalTarget[OT][genre1]"]="芸術"
    payload["retrievalTarget[OT][genre2]"]="芸術/小"
    payload["retrievalTarget[OT][genre2]"]="芸術/中"
    payload["retrievalTarget[OT][genre2]"]="芸術/高"
    payload["retrievalTarget[OT][genre1]"]="保健体育"
    payload["retrievalTarget[OT][genre2]"]="保健体育/高"
    payload["retrievalTarget[OT][genre1]"]="情報"
    payload["retrievalTarget[OT][genre2]"]="情報/高"
    payload["retrievalTarget[OT][genre1]"]="生活"
    payload["retrievalTarget[OT][genre2]"]="生活/小"
    payload["retrievalTarget[OV][genreAll]"]="on"
    payload["retrievalTarget[OV][genre1]"]="短歌"
    payload["retrievalTarget[OV][genre1]"]="俳句"
    payload["retrievalTarget[OV][genre1]"]="詩"
    payload["retrievalTarget[publishedYearAll]"]="on"
    payload["retrievalTarget[publishedYear]"]="1971"
    payload["retrievalTarget[publishedYear]"]="1972"
    payload["retrievalTarget[publishedYear]"]="1973"
    payload["retrievalTarget[publishedYear]"]="1974"
    payload["retrievalTarget[publishedYear]"]="1975"
    payload["retrievalTarget[publishedYear]"]="1976"
    payload["retrievalTarget[publishedYear]"]="1977"
    payload["retrievalTarget[publishedYear]"]="1978"
    payload["retrievalTarget[publishedYear]"]="1979"
    payload["retrievalTarget[publishedYear]"]="1980"
    payload["retrievalTarget[publishedYear]"]="1981"
    payload["retrievalTarget[publishedYear]"]="1982"
    payload["retrievalTarget[publishedYear]"]="1983"
    payload["retrievalTarget[publishedYear]"]="1984"
    payload["retrievalTarget[publishedYear]"]="1985"
    payload["retrievalTarget[publishedYear]"]="1986"
    payload["retrievalTarget[publishedYear]"]="1987"
    payload["retrievalTarget[publishedYear]"]="1988"
    payload["retrievalTarget[publishedYear]"]="1989"
    payload["retrievalTarget[publishedYear]"]="1990"
    payload["retrievalTarget[publishedYear]"]="1991"
    payload["retrievalTarget[publishedYear]"]="1992"
    payload["retrievalTarget[publishedYear]"]="1993"
    payload["retrievalTarget[publishedYear]"]="1994"
    payload["retrievalTarget[publishedYear]"]="1995"
    payload["retrievalTarget[publishedYear]"]="1996"
    payload["retrievalTarget[publishedYear]"]="1997"
    payload["retrievalTarget[publishedYear]"]="1998"
    payload["retrievalTarget[publishedYear]"]="1999"
    payload["retrievalTarget[publishedYear]"]="2000"
    payload["retrievalTarget[publishedYear]"]="2001"
    payload["retrievalTarget[publishedYear]"]="2002"
    payload["retrievalTarget[publishedYear]"]="2003"
    payload["retrievalTarget[publishedYear]"]="2004"
    payload["retrievalTarget[publishedYear]"]="2005"
    payload["retrievalTarget[publishedYear]"]="2006"
    payload["retrievalTarget[publishedYear]"]="2007"
    payload["retrievalTarget[publishedYear]"]="2008"
    payload["searchFormOptions.wordSep"]="|"
    payload["searchFormOptions.sentSep"]="#"
    payload["searchFormOptions[tglWords]"]="100"
    payload["downloadOptions[encoding]"]="UTF-16LE"
    payload["downloadOptions[endOfLine]"]="CRLF"
    payload["downloadOptions.notCompressedIfOneFile"]="on"
    payload["downloadOptions.splitDownloadFiles"]="on"


    headers=dict()
    headers["Accept"]="*/*"
    headers["Accept-Encoding"]="gzip, deflate, br"
    headers["Accept-Language"]="zh-CN,zh;q=0.8,en;q=0.6"
    headers["Connection"]="keep-alive"
    headers["Content-Length"]="49233"
    headers["Content-Type"]="application/x-www-form-urlencoded; charset=UTF-8"
    headers["Cookie"]="JSESSIONID=46162FE8CE2BBA7AB9524EC6A6D39801.bccwj02; JSESSIONID=D13C8A05202B7C853DF253614A942A44"
    headers["Host"]="chunagon.ninjal.ac.jp"
    headers["Origin"]="https://chunagon.ninjal.ac.jp"
    headers["Referer"]="https://chunagon.ninjal.ac.jp/bccwj-nt/search"
    headers["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers["X-Requested-With"]="XMLHttpRequest"


    startt = time.time()
    url = "https://chunagon.ninjal.ac.jp/bccwj-nt/search?search"
    rsp = requests.post(url, data=payload, headers=headers)
    time1 = time.time()
    print rsp.text

    d = json.loads(rsp.text)

    filename = "%s.txt" % keyword
    with open("tmp3.txt", "w+") as f:
        parse(d, f)

if __name__ == "__main__":
    scrabe_with_keyword("学芸")