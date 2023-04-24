# Changelog
All notable changes to this project will be documented in this file. Version naming based on [Semantic Versioning](https://semver.org/) and [keep a changelog](https://keepachangelog.com/)

## [2.0.1] - 20220423
### Changed
- モーフ
  - コートOFF
    - コートオフするときちょっと忘れ物があるので修正した 

## [2.0.0] - 20220302
### Changed

- メッシュ
    - 顔
        - 目を寄り目に、眼球を丸に、横顔や頬、顔のテクスチャ、鼻の影など、まつげも全部作り直しました
    - 髪
        - ちょっと上から見る形整ったのと、前髪にちょっとディテール
- 材質
    - フード紐　名前間違えた
    - ベルトなど　名前間違えた
    - サングラスのUVをちょっと移動（外見影響なし）
- モーフ
    - 目
        - 全部作り直した

### Added

- メッシュ
    - 顔
        - 目に透明のレンズを追加した
- モーフ
    - 目
        - ハート目
        - 星目 
    - まゆ
        - 上
        - 下
    - 口
        - 舌伸び
    - 他
        - コート袖上げ、左、右
            - コート袖が貫通するとき使ってください
- 表示枠
    - なんか作るとき追加するのを完全に忘れたのでなんか物理以外全部入れた
- 物理
    - イヤリングに物理入れた

## [1.1.1] - 20221225
### Fixed
- コート物理　fixed by Huiyi_iii ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - Huiyi_iiiさんのお陰でコートの物理さらにきれいになり、コートのの裾部分の物理が左右別々に動くようになりました。ありがとうございます！

## [1.1.0] - 20220822
### Added
- ❗❗「スフィアマップ」 by ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - スフィアマップをオフできるモーフ作りました、**デフォルトの見た目が変わるので**詳しくはReadmeをチェックしてください

### Fixed
- ズボンのウェイト　reported by ([twitter@tadanemui1](https://twitter.com/tadanemui1)
  - センターボーンでしゃがむとき、ズボンの頂点が飛び出さないようになりました

- コート物理　fixed by ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - twitter@IiiHuiyのお陰でコートの物理が柔らかくてきれいになり、下半身の貫通なども直りました。ありがとうございます！
- 「モーフ：コートなし」
  - なんか外すのをまた忘れたので外した

### Changed
 - 「モーフ：まばたき」
   - まばたきなどをするとき目も一緒に動くようになりました


## [1.0.1] - 20220808
### Changed
- 「モーフ：コートなし」
  - コート外すときプロテクターも外すようになりました。

## [1.0.0] - 20220806
### Added
- 初配布

