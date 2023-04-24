# Changelog
All notable changes to this project will be documented in this file. Version naming based on [Semantic Versioning](https://semver.org/) and [keep a changelog](https://keepachangelog.com/)

## [2.0.1] - 20220423
### Changed
- モーフ
  - コートOFF
    - 修正了脫掉外套的時候不小心留下來的部分

## [2.0.0] - 20220302
### Changed

- Mesh
    - 顔
        - 眼睛稍微往中間靠攏、眼球變成球型、修正側臉和臉頰、臉的texture、鼻子的影子、另外重做了睫毛
    - 髪
        - 整理了鳥瞰的形狀、另在瀏海至追加一些細節
- 材質
    - フード紐　名字弄錯了
    - ベルト什麼的　名字弄錯了
    - 移動了眼鏡的UV（看起來應該沒有影響）
- モーフ
    - 目
        - 全部重做了

### Added

- Mesh
    - 顔
        - 眼睛追加了水晶體
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
            - 外套袖子貫通的時候請用這個調整
- 表示枠
    - 我完全忘記要把做的東西追加進去才看的到，所以就把物理以外的東西全部加進去了
- 物理
    - 耳環加了點物理進去

## [1.1.1] - 20221225
### Fixed
- コート物理　fixed by Huiyi_iii ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - Huiyi_iii桑幫忙修改了外套衣襬物理，下擺換成會左右分開了！


## [1.1.0] - 20220822
### Added
- ❗❗「スフィアマップ」 by ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - 加了幾個能開關Sphere map的morph，**預設的外表有變化**，請看readme的詳細說明

### Fixed
- ズボンのウェイト　reported by ([twitter@tadanemui1](https://twitter.com/tadanemui1)
  - 移動センター做出蹲下動作時褲子的頂點會飛出來一塊的問題解決了

- コート物理　fixed by ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - 新版本變得很軟很漂亮也不太會貫穿了，感謝twitter@IiiHuiyi的幫忙！


### Changed
 - 「モーフ：まばたき」
   - 眨眼睛的時候眼球也會一起動


## [1.0.1] - 20220808
### Changed
- 「モーフ：コートなし」
  - 脫外套的時候忘記脫的護甲會脫掉了

## [1.0.0] - 20220806
### Added
- 初配布
