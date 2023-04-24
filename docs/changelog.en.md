# Changelog
All notable changes to this project will be documented in this file. Version naming based on [Semantic Versioning](https://semver.org/) and [keep a changelog](https://keepachangelog.com/)

## [2.0.1] - 20220423
### Changed
- Morph
  - コートOFF
    - hide leftover part in coat 

## [2.0.0] - 20220302
### Changed
- Mesh
    - face
        - changed eye position, eyeball is now sphere-shaped, polished the profile and cheek, improved face texture, added nose shadow, redone eyelashes
    - hair
        - improved top-down view, also added details to the bang
- Material
    - hood_string　wrong name wrong vertices
    - protector_belt　wrong name wrong vertices
    - also moved UV of sunglasses (should look the same)
- Morph
    - eyes
        - redone

### Added

- Mesh
    - face
        - added transparent lens to the eyes
- Morph
    - eye
        - heart_eye
        - kirakira_eye
    - brow
        - UP
        - DOWN
    - mouth
        - 舌伸び longer tongue
    - etc
        - both coat_sleeves_shorten, left, right
            - please use it when the coat sleeve is penetrating when arm bended
- Display frame
    - I totally forgot this so I just added everything other than physics bones
- Physics
    - added physics to the earring

## [1.1.1] - 20221225
### Fixed
- コート物理　fixed by Huiyi_iii ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - Huiyi_iii helped to improve the physics for the coat physics again, and the splitted part of coat now move seperately!

## [1.1.0] - 20220822
### Added
- ❗❗「スフィアマップ」 by ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - added a few morph for turning off the sphere maps, **model may look different by default**, please check the readme for details

### Fixed
- ズボンのウェイト　reported by ([twitter@tadanemui1](https://twitter.com/tadanemui1)
  - pants would no longer stick out when you use center bone to crouch all the way
- コート物理　fixed by ([twitter@IiiHuiyi](https://twitter.com/IiiHuiyi))
  - new version is much softer and beautiful and less penetration now, thanks twitter@IiiHuiyi for the help!
- 「モーフ：コートなし」
  - なんか外すのをまた忘れたので外した

### Changed
 - 「モーフ：まばたき」
   - eyes should move with the lid when blinking

## [1.0.1] - 20220808
### Changed
- 「モーフ：コートなし」
  - 脫外套的時候忘記脫的護甲會脫掉了
  - the protector now remove with the coat

## [1.0.0] - 20220806
### Added
- First release

