# 项目宠物 Emoji 图鉴 · Pet Emoji Atlas

**51 个项目 × 12 种形态 = 612 枚宠物表情 emoji。**
每一枚同时提供 **图片（SVG / PNG）+ 彩色字体（CBDT/CBLC TTF）+ 短码（shortcode）**。

> **授权 / License**：本项目中的项目宠物、图片、图标、表情及字体中的图形字形均为
> **非开源资产**，商业使用需取得商业授权。详见 [ASSETS-LICENSE.md](ASSETS-LICENSE.md)。

## 12 种形态

笑 / 欢乐 / 哭 / 沮丧 / 惊恐 / 愤怒 / 撒娇 / 卖萌 / 讨好 / 敲打 / 捂脸 / 吐舌头

## 用法

### 1. 图片

```markdown
![笑](pets/ads-php/smile.svg)
![笑](png/ads-php/smile.png)
```

### 2. 字体

引入 `font/emoji.css` 后，使用字体族 `Pet Emoji Atlas` 与码位 `U+E000` 显示对应字形；支持 `liga` 连字的编辑器也可直接输入短码。

```css
@import url("font/emoji.css");
```

字体为 CBDT/CBLC 彩色位图字体；支持彩色位图字体的环境会显示对应宠物表情，否则请使用图片。

### 3. 短码

```text
:ads-php-smile:
:emoji-ads-php-smile:
```

- 主短码：`:<项目>-<形态>:`
- 别名：`:emoji-<项目>-<形态>:`
- 字体码位：`U+E000..U+E263`
- 全量映射见 [shortcodes.json](shortcodes.json)；字体内置主短码 `:<项目>-<形态>:` 的 `liga` 连字。
- `:emoji-<项目>-<形态>:` 别名可用 `shortcodes.json` 映射为图片或对应码位；需要把短码渲染成图片时，查 `image` 字段。

## 项目总览

| # | 宠物 | 项目 | 短码前缀 | 形态 |
|---|---|---|---|---|
| 1 | 阿章 | `ads-php` | `:ads-php-*:` | 12 |
| 2 | 小约 | `appointment-php` | `:appointment-php-*:` | 12 |
| 3 | Rusty | `bee-rust` | `:bee-rust-*:` | 12 |
| 4 | 阿守 | `bee-rust-admin` | `:bee-rust-admin-*:` | 12 |
| 5 | 云团 | `cloud-php` | `:cloud-php-*:` | 12 |
| 6 | E-Cat | `e-cat` | `:e-cat-*:` | 12 |
| 7 | Lumi | `erik-talk` | `:erik-talk-*:` | 12 |
| 8 | 小八爪 | `erp-php` | `:erp-php-*:` | 12 |
| 9 | Dicey | `game-platform-php` | `:game-platform-php-*:` | 12 |
| 10 | 霜霜 | `insurance-service` | `:insurance-service-*:` | 12 |
| 11 | E-Cat | `integrated-global-logistics` | `:integrated-global-logistics-*:` | 12 |
| 12 | IoT Bot | `iot-platform` | `:iot-platform-*:` | 12 |
| 13 | 租租鼠 | `item-rental` | `:item-rental-*:` | 12 |
| 14 | 小音机 | `omb` | `:omb-*:` | 12 |
| 15 | 小安 | `open-admin` | `:open-admin-*:` | 12 |
| 16 | Novi | `open-novel` | `:open-novel-*:` | 12 |
| 17 | 南南 | `open-travel` | `:open-travel-*:` | 12 |
| 18 | 小筑 | `property-management-platform` | `:property-management-platform-*:` | 12 |
| 19 | 犇犇 | `quantitative-trading` | `:quantitative-trading-*:` | 12 |
| 20 | 雪球 Snowy | `shop-php` | `:shop-php-*:` | 12 |
| 21 | Bub | `social` | `:social-*:` | 12 |
| 22 | ssd | `ssd` | `:ssd-*:` | 12 |
| 23 | 超猫 SuperCat | `super-ops` | `:super-ops-*:` | 12 |
| 24 | 小运 | `bag/canal` | `:canal-*:` | 12 |
| 25 | 小德 | `bag/druid-rust` | `:druid-rust-*:` | 12 |
| 26 | Locky | `bag/encryption-rust` | `:encryption-rust-*:` | 12 |
| 27 | 小侦 Scouty | `bag/go-scout` | `:go-scout-*:` | 12 |
| 28 | Kee · 橘猫 | `bag/jwt-rust` | `:jwt-rust-*:` | 12 |
| 29 | Posty | `bag/poster-rust` | `:poster-rust-*:` | 12 |
| 30 | Scout | `bag/rust-scout` | `:rust-scout-*:` | 12 |
| 31 | 哨兵鼠 | `bag/security-go` | `:security-go-*:` | 12 |
| 32 | 甲哨 Sentri | `bag/security-rust` | `:security-rust-*:` | 12 |
| 33 | 以太兽 | `erikwang2013/aetherupload-webman` | `:aetherupload-webman-*:` | 12 |
| 34 | Apidoc | `erikwang2013/apidoc-php` | `:apidoc-php-*:` | 12 |
| 35 | ClickHouse 仓鼠 | `erikwang2013/clickhouse-php` | `:clickhouse-php-*:` | 12 |
| 36 | Consu | `erikwang2013/consul-php` | `:consul-php-*:` | 12 |
| 37 | Locky | `erikwang2013/encryptable` | `:encryptable-*:` | 12 |
| 38 | Locky | `erikwang2013/encryption` | `:encryption-*:` | 12 |
| 39 | Etchy | `erikwang2013/etcd` | `:etcd-*:` | 12 |
| 40 | 哈希迪 Hashy | `erikwang2013/hashids` | `:hashids-*:` | 12 |
| 41 | Kee · 柴犬门卫 | `erikwang2013/jwt-webman` | `:jwt-webman-*:` | 12 |
| 42 | Posty | `erikwang2013/poster-php` | `:poster-php-*:` | 12 |
| 43 | Seasony 季灵 | `erikwang2013/season` | `:season-*:` | 12 |
| 44 | 小盾 | `erikwang2013/security-php` | `:security-php-*:` | 12 |
| 45 | 雪花精灵 | `erikwang2013/snowflake-php` | `:snowflake-php-*:` | 12 |
| 46 | Sniffy | `erikwang2013/webman-scout` | `:webman-scout-*:` | 12 |
| 47 | Xhpy | `erikwang2013/xhprof` | `:xhprof-*:` | 12 |
| 48 | 焰焰 | `erikwang2013/xhprof-webman` | `:xhprof-webman-*:` | 12 |
| 49 | 吞吞 | `oss` | `:oss-*:` | 12 |
| 50 | Pax | `polypack` | `:polypack-*:` | 12 |
| 51 | 小欧 | `opi` | `:opi-*:` | 12 |

## 逐项目预览

### 阿章 · `ads-php` · `:ads-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/ads-php/smile.png) | ![欢乐](thumbs/ads-php/joy.png) | ![哭](thumbs/ads-php/cry.png) | ![沮丧](thumbs/ads-php/depressed.png) | ![惊恐](thumbs/ads-php/terrified.png) | ![愤怒](thumbs/ads-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/ads-php/coquettish.png) | ![卖萌](thumbs/ads-php/cute.png) | ![讨好](thumbs/ads-php/pleasing.png) | ![敲打](thumbs/ads-php/knocking.png) | ![捂脸](thumbs/ads-php/facepalm.png) | ![吐舌头](thumbs/ads-php/tongue.png) |

`:ads-php-smile:` · `:ads-php-joy:` · `:ads-php-cry:` · `:ads-php-depressed:` · `:ads-php-terrified:` · `:ads-php-angry:` · `:ads-php-coquettish:` · `:ads-php-cute:` · `:ads-php-pleasing:` · `:ads-php-knocking:` · `:ads-php-facepalm:` · `:ads-php-tongue:`

### 小约 · `appointment-php` · `:appointment-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/appointment-php/smile.png) | ![欢乐](thumbs/appointment-php/joy.png) | ![哭](thumbs/appointment-php/cry.png) | ![沮丧](thumbs/appointment-php/depressed.png) | ![惊恐](thumbs/appointment-php/terrified.png) | ![愤怒](thumbs/appointment-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/appointment-php/coquettish.png) | ![卖萌](thumbs/appointment-php/cute.png) | ![讨好](thumbs/appointment-php/pleasing.png) | ![敲打](thumbs/appointment-php/knocking.png) | ![捂脸](thumbs/appointment-php/facepalm.png) | ![吐舌头](thumbs/appointment-php/tongue.png) |

`:appointment-php-smile:` · `:appointment-php-joy:` · `:appointment-php-cry:` · `:appointment-php-depressed:` · `:appointment-php-terrified:` · `:appointment-php-angry:` · `:appointment-php-coquettish:` · `:appointment-php-cute:` · `:appointment-php-pleasing:` · `:appointment-php-knocking:` · `:appointment-php-facepalm:` · `:appointment-php-tongue:`

### Rusty · `bee-rust` · `:bee-rust-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/bee-rust/smile.png) | ![欢乐](thumbs/bee-rust/joy.png) | ![哭](thumbs/bee-rust/cry.png) | ![沮丧](thumbs/bee-rust/depressed.png) | ![惊恐](thumbs/bee-rust/terrified.png) | ![愤怒](thumbs/bee-rust/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/bee-rust/coquettish.png) | ![卖萌](thumbs/bee-rust/cute.png) | ![讨好](thumbs/bee-rust/pleasing.png) | ![敲打](thumbs/bee-rust/knocking.png) | ![捂脸](thumbs/bee-rust/facepalm.png) | ![吐舌头](thumbs/bee-rust/tongue.png) |

`:bee-rust-smile:` · `:bee-rust-joy:` · `:bee-rust-cry:` · `:bee-rust-depressed:` · `:bee-rust-terrified:` · `:bee-rust-angry:` · `:bee-rust-coquettish:` · `:bee-rust-cute:` · `:bee-rust-pleasing:` · `:bee-rust-knocking:` · `:bee-rust-facepalm:` · `:bee-rust-tongue:`

### 阿守 · `bee-rust-admin` · `:bee-rust-admin-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/bee-rust-admin/smile.png) | ![欢乐](thumbs/bee-rust-admin/joy.png) | ![哭](thumbs/bee-rust-admin/cry.png) | ![沮丧](thumbs/bee-rust-admin/depressed.png) | ![惊恐](thumbs/bee-rust-admin/terrified.png) | ![愤怒](thumbs/bee-rust-admin/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/bee-rust-admin/coquettish.png) | ![卖萌](thumbs/bee-rust-admin/cute.png) | ![讨好](thumbs/bee-rust-admin/pleasing.png) | ![敲打](thumbs/bee-rust-admin/knocking.png) | ![捂脸](thumbs/bee-rust-admin/facepalm.png) | ![吐舌头](thumbs/bee-rust-admin/tongue.png) |

`:bee-rust-admin-smile:` · `:bee-rust-admin-joy:` · `:bee-rust-admin-cry:` · `:bee-rust-admin-depressed:` · `:bee-rust-admin-terrified:` · `:bee-rust-admin-angry:` · `:bee-rust-admin-coquettish:` · `:bee-rust-admin-cute:` · `:bee-rust-admin-pleasing:` · `:bee-rust-admin-knocking:` · `:bee-rust-admin-facepalm:` · `:bee-rust-admin-tongue:`

### 云团 · `cloud-php` · `:cloud-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/cloud-php/smile.png) | ![欢乐](thumbs/cloud-php/joy.png) | ![哭](thumbs/cloud-php/cry.png) | ![沮丧](thumbs/cloud-php/depressed.png) | ![惊恐](thumbs/cloud-php/terrified.png) | ![愤怒](thumbs/cloud-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/cloud-php/coquettish.png) | ![卖萌](thumbs/cloud-php/cute.png) | ![讨好](thumbs/cloud-php/pleasing.png) | ![敲打](thumbs/cloud-php/knocking.png) | ![捂脸](thumbs/cloud-php/facepalm.png) | ![吐舌头](thumbs/cloud-php/tongue.png) |

`:cloud-php-smile:` · `:cloud-php-joy:` · `:cloud-php-cry:` · `:cloud-php-depressed:` · `:cloud-php-terrified:` · `:cloud-php-angry:` · `:cloud-php-coquettish:` · `:cloud-php-cute:` · `:cloud-php-pleasing:` · `:cloud-php-knocking:` · `:cloud-php-facepalm:` · `:cloud-php-tongue:`

### E-Cat · `e-cat` · `:e-cat-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/e-cat/smile.png) | ![欢乐](thumbs/e-cat/joy.png) | ![哭](thumbs/e-cat/cry.png) | ![沮丧](thumbs/e-cat/depressed.png) | ![惊恐](thumbs/e-cat/terrified.png) | ![愤怒](thumbs/e-cat/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/e-cat/coquettish.png) | ![卖萌](thumbs/e-cat/cute.png) | ![讨好](thumbs/e-cat/pleasing.png) | ![敲打](thumbs/e-cat/knocking.png) | ![捂脸](thumbs/e-cat/facepalm.png) | ![吐舌头](thumbs/e-cat/tongue.png) |

`:e-cat-smile:` · `:e-cat-joy:` · `:e-cat-cry:` · `:e-cat-depressed:` · `:e-cat-terrified:` · `:e-cat-angry:` · `:e-cat-coquettish:` · `:e-cat-cute:` · `:e-cat-pleasing:` · `:e-cat-knocking:` · `:e-cat-facepalm:` · `:e-cat-tongue:`

### Lumi · `erik-talk` · `:erik-talk-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/erik-talk/smile.png) | ![欢乐](thumbs/erik-talk/joy.png) | ![哭](thumbs/erik-talk/cry.png) | ![沮丧](thumbs/erik-talk/depressed.png) | ![惊恐](thumbs/erik-talk/terrified.png) | ![愤怒](thumbs/erik-talk/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/erik-talk/coquettish.png) | ![卖萌](thumbs/erik-talk/cute.png) | ![讨好](thumbs/erik-talk/pleasing.png) | ![敲打](thumbs/erik-talk/knocking.png) | ![捂脸](thumbs/erik-talk/facepalm.png) | ![吐舌头](thumbs/erik-talk/tongue.png) |

`:erik-talk-smile:` · `:erik-talk-joy:` · `:erik-talk-cry:` · `:erik-talk-depressed:` · `:erik-talk-terrified:` · `:erik-talk-angry:` · `:erik-talk-coquettish:` · `:erik-talk-cute:` · `:erik-talk-pleasing:` · `:erik-talk-knocking:` · `:erik-talk-facepalm:` · `:erik-talk-tongue:`

### 小八爪 · `erp-php` · `:erp-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/erp-php/smile.png) | ![欢乐](thumbs/erp-php/joy.png) | ![哭](thumbs/erp-php/cry.png) | ![沮丧](thumbs/erp-php/depressed.png) | ![惊恐](thumbs/erp-php/terrified.png) | ![愤怒](thumbs/erp-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/erp-php/coquettish.png) | ![卖萌](thumbs/erp-php/cute.png) | ![讨好](thumbs/erp-php/pleasing.png) | ![敲打](thumbs/erp-php/knocking.png) | ![捂脸](thumbs/erp-php/facepalm.png) | ![吐舌头](thumbs/erp-php/tongue.png) |

`:erp-php-smile:` · `:erp-php-joy:` · `:erp-php-cry:` · `:erp-php-depressed:` · `:erp-php-terrified:` · `:erp-php-angry:` · `:erp-php-coquettish:` · `:erp-php-cute:` · `:erp-php-pleasing:` · `:erp-php-knocking:` · `:erp-php-facepalm:` · `:erp-php-tongue:`

### Dicey · `game-platform-php` · `:game-platform-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/game-platform-php/smile.png) | ![欢乐](thumbs/game-platform-php/joy.png) | ![哭](thumbs/game-platform-php/cry.png) | ![沮丧](thumbs/game-platform-php/depressed.png) | ![惊恐](thumbs/game-platform-php/terrified.png) | ![愤怒](thumbs/game-platform-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/game-platform-php/coquettish.png) | ![卖萌](thumbs/game-platform-php/cute.png) | ![讨好](thumbs/game-platform-php/pleasing.png) | ![敲打](thumbs/game-platform-php/knocking.png) | ![捂脸](thumbs/game-platform-php/facepalm.png) | ![吐舌头](thumbs/game-platform-php/tongue.png) |

`:game-platform-php-smile:` · `:game-platform-php-joy:` · `:game-platform-php-cry:` · `:game-platform-php-depressed:` · `:game-platform-php-terrified:` · `:game-platform-php-angry:` · `:game-platform-php-coquettish:` · `:game-platform-php-cute:` · `:game-platform-php-pleasing:` · `:game-platform-php-knocking:` · `:game-platform-php-facepalm:` · `:game-platform-php-tongue:`

### 霜霜 · `insurance-service` · `:insurance-service-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/insurance-service/smile.png) | ![欢乐](thumbs/insurance-service/joy.png) | ![哭](thumbs/insurance-service/cry.png) | ![沮丧](thumbs/insurance-service/depressed.png) | ![惊恐](thumbs/insurance-service/terrified.png) | ![愤怒](thumbs/insurance-service/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/insurance-service/coquettish.png) | ![卖萌](thumbs/insurance-service/cute.png) | ![讨好](thumbs/insurance-service/pleasing.png) | ![敲打](thumbs/insurance-service/knocking.png) | ![捂脸](thumbs/insurance-service/facepalm.png) | ![吐舌头](thumbs/insurance-service/tongue.png) |

`:insurance-service-smile:` · `:insurance-service-joy:` · `:insurance-service-cry:` · `:insurance-service-depressed:` · `:insurance-service-terrified:` · `:insurance-service-angry:` · `:insurance-service-coquettish:` · `:insurance-service-cute:` · `:insurance-service-pleasing:` · `:insurance-service-knocking:` · `:insurance-service-facepalm:` · `:insurance-service-tongue:`

### E-Cat · `integrated-global-logistics` · `:integrated-global-logistics-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/integrated-global-logistics/smile.png) | ![欢乐](thumbs/integrated-global-logistics/joy.png) | ![哭](thumbs/integrated-global-logistics/cry.png) | ![沮丧](thumbs/integrated-global-logistics/depressed.png) | ![惊恐](thumbs/integrated-global-logistics/terrified.png) | ![愤怒](thumbs/integrated-global-logistics/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/integrated-global-logistics/coquettish.png) | ![卖萌](thumbs/integrated-global-logistics/cute.png) | ![讨好](thumbs/integrated-global-logistics/pleasing.png) | ![敲打](thumbs/integrated-global-logistics/knocking.png) | ![捂脸](thumbs/integrated-global-logistics/facepalm.png) | ![吐舌头](thumbs/integrated-global-logistics/tongue.png) |

`:integrated-global-logistics-smile:` · `:integrated-global-logistics-joy:` · `:integrated-global-logistics-cry:` · `:integrated-global-logistics-depressed:` · `:integrated-global-logistics-terrified:` · `:integrated-global-logistics-angry:` · `:integrated-global-logistics-coquettish:` · `:integrated-global-logistics-cute:` · `:integrated-global-logistics-pleasing:` · `:integrated-global-logistics-knocking:` · `:integrated-global-logistics-facepalm:` · `:integrated-global-logistics-tongue:`

### IoT Bot · `iot-platform` · `:iot-platform-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/iot-platform/smile.png) | ![欢乐](thumbs/iot-platform/joy.png) | ![哭](thumbs/iot-platform/cry.png) | ![沮丧](thumbs/iot-platform/depressed.png) | ![惊恐](thumbs/iot-platform/terrified.png) | ![愤怒](thumbs/iot-platform/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/iot-platform/coquettish.png) | ![卖萌](thumbs/iot-platform/cute.png) | ![讨好](thumbs/iot-platform/pleasing.png) | ![敲打](thumbs/iot-platform/knocking.png) | ![捂脸](thumbs/iot-platform/facepalm.png) | ![吐舌头](thumbs/iot-platform/tongue.png) |

`:iot-platform-smile:` · `:iot-platform-joy:` · `:iot-platform-cry:` · `:iot-platform-depressed:` · `:iot-platform-terrified:` · `:iot-platform-angry:` · `:iot-platform-coquettish:` · `:iot-platform-cute:` · `:iot-platform-pleasing:` · `:iot-platform-knocking:` · `:iot-platform-facepalm:` · `:iot-platform-tongue:`

### 租租鼠 · `item-rental` · `:item-rental-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/item-rental/smile.png) | ![欢乐](thumbs/item-rental/joy.png) | ![哭](thumbs/item-rental/cry.png) | ![沮丧](thumbs/item-rental/depressed.png) | ![惊恐](thumbs/item-rental/terrified.png) | ![愤怒](thumbs/item-rental/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/item-rental/coquettish.png) | ![卖萌](thumbs/item-rental/cute.png) | ![讨好](thumbs/item-rental/pleasing.png) | ![敲打](thumbs/item-rental/knocking.png) | ![捂脸](thumbs/item-rental/facepalm.png) | ![吐舌头](thumbs/item-rental/tongue.png) |

`:item-rental-smile:` · `:item-rental-joy:` · `:item-rental-cry:` · `:item-rental-depressed:` · `:item-rental-terrified:` · `:item-rental-angry:` · `:item-rental-coquettish:` · `:item-rental-cute:` · `:item-rental-pleasing:` · `:item-rental-knocking:` · `:item-rental-facepalm:` · `:item-rental-tongue:`

### 小音机 · `omb` · `:omb-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/omb/smile.png) | ![欢乐](thumbs/omb/joy.png) | ![哭](thumbs/omb/cry.png) | ![沮丧](thumbs/omb/depressed.png) | ![惊恐](thumbs/omb/terrified.png) | ![愤怒](thumbs/omb/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/omb/coquettish.png) | ![卖萌](thumbs/omb/cute.png) | ![讨好](thumbs/omb/pleasing.png) | ![敲打](thumbs/omb/knocking.png) | ![捂脸](thumbs/omb/facepalm.png) | ![吐舌头](thumbs/omb/tongue.png) |

`:omb-smile:` · `:omb-joy:` · `:omb-cry:` · `:omb-depressed:` · `:omb-terrified:` · `:omb-angry:` · `:omb-coquettish:` · `:omb-cute:` · `:omb-pleasing:` · `:omb-knocking:` · `:omb-facepalm:` · `:omb-tongue:`

### 小安 · `open-admin` · `:open-admin-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/open-admin/smile.png) | ![欢乐](thumbs/open-admin/joy.png) | ![哭](thumbs/open-admin/cry.png) | ![沮丧](thumbs/open-admin/depressed.png) | ![惊恐](thumbs/open-admin/terrified.png) | ![愤怒](thumbs/open-admin/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/open-admin/coquettish.png) | ![卖萌](thumbs/open-admin/cute.png) | ![讨好](thumbs/open-admin/pleasing.png) | ![敲打](thumbs/open-admin/knocking.png) | ![捂脸](thumbs/open-admin/facepalm.png) | ![吐舌头](thumbs/open-admin/tongue.png) |

`:open-admin-smile:` · `:open-admin-joy:` · `:open-admin-cry:` · `:open-admin-depressed:` · `:open-admin-terrified:` · `:open-admin-angry:` · `:open-admin-coquettish:` · `:open-admin-cute:` · `:open-admin-pleasing:` · `:open-admin-knocking:` · `:open-admin-facepalm:` · `:open-admin-tongue:`

### Novi · `open-novel` · `:open-novel-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/open-novel/smile.png) | ![欢乐](thumbs/open-novel/joy.png) | ![哭](thumbs/open-novel/cry.png) | ![沮丧](thumbs/open-novel/depressed.png) | ![惊恐](thumbs/open-novel/terrified.png) | ![愤怒](thumbs/open-novel/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/open-novel/coquettish.png) | ![卖萌](thumbs/open-novel/cute.png) | ![讨好](thumbs/open-novel/pleasing.png) | ![敲打](thumbs/open-novel/knocking.png) | ![捂脸](thumbs/open-novel/facepalm.png) | ![吐舌头](thumbs/open-novel/tongue.png) |

`:open-novel-smile:` · `:open-novel-joy:` · `:open-novel-cry:` · `:open-novel-depressed:` · `:open-novel-terrified:` · `:open-novel-angry:` · `:open-novel-coquettish:` · `:open-novel-cute:` · `:open-novel-pleasing:` · `:open-novel-knocking:` · `:open-novel-facepalm:` · `:open-novel-tongue:`

### 南南 · `open-travel` · `:open-travel-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/open-travel/smile.png) | ![欢乐](thumbs/open-travel/joy.png) | ![哭](thumbs/open-travel/cry.png) | ![沮丧](thumbs/open-travel/depressed.png) | ![惊恐](thumbs/open-travel/terrified.png) | ![愤怒](thumbs/open-travel/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/open-travel/coquettish.png) | ![卖萌](thumbs/open-travel/cute.png) | ![讨好](thumbs/open-travel/pleasing.png) | ![敲打](thumbs/open-travel/knocking.png) | ![捂脸](thumbs/open-travel/facepalm.png) | ![吐舌头](thumbs/open-travel/tongue.png) |

`:open-travel-smile:` · `:open-travel-joy:` · `:open-travel-cry:` · `:open-travel-depressed:` · `:open-travel-terrified:` · `:open-travel-angry:` · `:open-travel-coquettish:` · `:open-travel-cute:` · `:open-travel-pleasing:` · `:open-travel-knocking:` · `:open-travel-facepalm:` · `:open-travel-tongue:`

### 小筑 · `property-management-platform` · `:property-management-platform-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/property-management-platform/smile.png) | ![欢乐](thumbs/property-management-platform/joy.png) | ![哭](thumbs/property-management-platform/cry.png) | ![沮丧](thumbs/property-management-platform/depressed.png) | ![惊恐](thumbs/property-management-platform/terrified.png) | ![愤怒](thumbs/property-management-platform/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/property-management-platform/coquettish.png) | ![卖萌](thumbs/property-management-platform/cute.png) | ![讨好](thumbs/property-management-platform/pleasing.png) | ![敲打](thumbs/property-management-platform/knocking.png) | ![捂脸](thumbs/property-management-platform/facepalm.png) | ![吐舌头](thumbs/property-management-platform/tongue.png) |

`:property-management-platform-smile:` · `:property-management-platform-joy:` · `:property-management-platform-cry:` · `:property-management-platform-depressed:` · `:property-management-platform-terrified:` · `:property-management-platform-angry:` · `:property-management-platform-coquettish:` · `:property-management-platform-cute:` · `:property-management-platform-pleasing:` · `:property-management-platform-knocking:` · `:property-management-platform-facepalm:` · `:property-management-platform-tongue:`

### 犇犇 · `quantitative-trading` · `:quantitative-trading-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/quantitative-trading/smile.png) | ![欢乐](thumbs/quantitative-trading/joy.png) | ![哭](thumbs/quantitative-trading/cry.png) | ![沮丧](thumbs/quantitative-trading/depressed.png) | ![惊恐](thumbs/quantitative-trading/terrified.png) | ![愤怒](thumbs/quantitative-trading/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/quantitative-trading/coquettish.png) | ![卖萌](thumbs/quantitative-trading/cute.png) | ![讨好](thumbs/quantitative-trading/pleasing.png) | ![敲打](thumbs/quantitative-trading/knocking.png) | ![捂脸](thumbs/quantitative-trading/facepalm.png) | ![吐舌头](thumbs/quantitative-trading/tongue.png) |

`:quantitative-trading-smile:` · `:quantitative-trading-joy:` · `:quantitative-trading-cry:` · `:quantitative-trading-depressed:` · `:quantitative-trading-terrified:` · `:quantitative-trading-angry:` · `:quantitative-trading-coquettish:` · `:quantitative-trading-cute:` · `:quantitative-trading-pleasing:` · `:quantitative-trading-knocking:` · `:quantitative-trading-facepalm:` · `:quantitative-trading-tongue:`

### 雪球 Snowy · `shop-php` · `:shop-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/shop-php/smile.png) | ![欢乐](thumbs/shop-php/joy.png) | ![哭](thumbs/shop-php/cry.png) | ![沮丧](thumbs/shop-php/depressed.png) | ![惊恐](thumbs/shop-php/terrified.png) | ![愤怒](thumbs/shop-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/shop-php/coquettish.png) | ![卖萌](thumbs/shop-php/cute.png) | ![讨好](thumbs/shop-php/pleasing.png) | ![敲打](thumbs/shop-php/knocking.png) | ![捂脸](thumbs/shop-php/facepalm.png) | ![吐舌头](thumbs/shop-php/tongue.png) |

`:shop-php-smile:` · `:shop-php-joy:` · `:shop-php-cry:` · `:shop-php-depressed:` · `:shop-php-terrified:` · `:shop-php-angry:` · `:shop-php-coquettish:` · `:shop-php-cute:` · `:shop-php-pleasing:` · `:shop-php-knocking:` · `:shop-php-facepalm:` · `:shop-php-tongue:`

### Bub · `social` · `:social-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/social/smile.png) | ![欢乐](thumbs/social/joy.png) | ![哭](thumbs/social/cry.png) | ![沮丧](thumbs/social/depressed.png) | ![惊恐](thumbs/social/terrified.png) | ![愤怒](thumbs/social/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/social/coquettish.png) | ![卖萌](thumbs/social/cute.png) | ![讨好](thumbs/social/pleasing.png) | ![敲打](thumbs/social/knocking.png) | ![捂脸](thumbs/social/facepalm.png) | ![吐舌头](thumbs/social/tongue.png) |

`:social-smile:` · `:social-joy:` · `:social-cry:` · `:social-depressed:` · `:social-terrified:` · `:social-angry:` · `:social-coquettish:` · `:social-cute:` · `:social-pleasing:` · `:social-knocking:` · `:social-facepalm:` · `:social-tongue:`

### ssd · `ssd` · `:ssd-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/ssd/smile.png) | ![欢乐](thumbs/ssd/joy.png) | ![哭](thumbs/ssd/cry.png) | ![沮丧](thumbs/ssd/depressed.png) | ![惊恐](thumbs/ssd/terrified.png) | ![愤怒](thumbs/ssd/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/ssd/coquettish.png) | ![卖萌](thumbs/ssd/cute.png) | ![讨好](thumbs/ssd/pleasing.png) | ![敲打](thumbs/ssd/knocking.png) | ![捂脸](thumbs/ssd/facepalm.png) | ![吐舌头](thumbs/ssd/tongue.png) |

`:ssd-smile:` · `:ssd-joy:` · `:ssd-cry:` · `:ssd-depressed:` · `:ssd-terrified:` · `:ssd-angry:` · `:ssd-coquettish:` · `:ssd-cute:` · `:ssd-pleasing:` · `:ssd-knocking:` · `:ssd-facepalm:` · `:ssd-tongue:`

### 超猫 SuperCat · `super-ops` · `:super-ops-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/super-ops/smile.png) | ![欢乐](thumbs/super-ops/joy.png) | ![哭](thumbs/super-ops/cry.png) | ![沮丧](thumbs/super-ops/depressed.png) | ![惊恐](thumbs/super-ops/terrified.png) | ![愤怒](thumbs/super-ops/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/super-ops/coquettish.png) | ![卖萌](thumbs/super-ops/cute.png) | ![讨好](thumbs/super-ops/pleasing.png) | ![敲打](thumbs/super-ops/knocking.png) | ![捂脸](thumbs/super-ops/facepalm.png) | ![吐舌头](thumbs/super-ops/tongue.png) |

`:super-ops-smile:` · `:super-ops-joy:` · `:super-ops-cry:` · `:super-ops-depressed:` · `:super-ops-terrified:` · `:super-ops-angry:` · `:super-ops-coquettish:` · `:super-ops-cute:` · `:super-ops-pleasing:` · `:super-ops-knocking:` · `:super-ops-facepalm:` · `:super-ops-tongue:`

### 小运 · `bag/canal` · `:canal-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/canal/smile.png) | ![欢乐](thumbs/canal/joy.png) | ![哭](thumbs/canal/cry.png) | ![沮丧](thumbs/canal/depressed.png) | ![惊恐](thumbs/canal/terrified.png) | ![愤怒](thumbs/canal/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/canal/coquettish.png) | ![卖萌](thumbs/canal/cute.png) | ![讨好](thumbs/canal/pleasing.png) | ![敲打](thumbs/canal/knocking.png) | ![捂脸](thumbs/canal/facepalm.png) | ![吐舌头](thumbs/canal/tongue.png) |

`:canal-smile:` · `:canal-joy:` · `:canal-cry:` · `:canal-depressed:` · `:canal-terrified:` · `:canal-angry:` · `:canal-coquettish:` · `:canal-cute:` · `:canal-pleasing:` · `:canal-knocking:` · `:canal-facepalm:` · `:canal-tongue:`

### 小德 · `bag/druid-rust` · `:druid-rust-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/druid-rust/smile.png) | ![欢乐](thumbs/druid-rust/joy.png) | ![哭](thumbs/druid-rust/cry.png) | ![沮丧](thumbs/druid-rust/depressed.png) | ![惊恐](thumbs/druid-rust/terrified.png) | ![愤怒](thumbs/druid-rust/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/druid-rust/coquettish.png) | ![卖萌](thumbs/druid-rust/cute.png) | ![讨好](thumbs/druid-rust/pleasing.png) | ![敲打](thumbs/druid-rust/knocking.png) | ![捂脸](thumbs/druid-rust/facepalm.png) | ![吐舌头](thumbs/druid-rust/tongue.png) |

`:druid-rust-smile:` · `:druid-rust-joy:` · `:druid-rust-cry:` · `:druid-rust-depressed:` · `:druid-rust-terrified:` · `:druid-rust-angry:` · `:druid-rust-coquettish:` · `:druid-rust-cute:` · `:druid-rust-pleasing:` · `:druid-rust-knocking:` · `:druid-rust-facepalm:` · `:druid-rust-tongue:`

### Locky · `bag/encryption-rust` · `:encryption-rust-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/encryption-rust/smile.png) | ![欢乐](thumbs/encryption-rust/joy.png) | ![哭](thumbs/encryption-rust/cry.png) | ![沮丧](thumbs/encryption-rust/depressed.png) | ![惊恐](thumbs/encryption-rust/terrified.png) | ![愤怒](thumbs/encryption-rust/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/encryption-rust/coquettish.png) | ![卖萌](thumbs/encryption-rust/cute.png) | ![讨好](thumbs/encryption-rust/pleasing.png) | ![敲打](thumbs/encryption-rust/knocking.png) | ![捂脸](thumbs/encryption-rust/facepalm.png) | ![吐舌头](thumbs/encryption-rust/tongue.png) |

`:encryption-rust-smile:` · `:encryption-rust-joy:` · `:encryption-rust-cry:` · `:encryption-rust-depressed:` · `:encryption-rust-terrified:` · `:encryption-rust-angry:` · `:encryption-rust-coquettish:` · `:encryption-rust-cute:` · `:encryption-rust-pleasing:` · `:encryption-rust-knocking:` · `:encryption-rust-facepalm:` · `:encryption-rust-tongue:`

### 小侦 Scouty · `bag/go-scout` · `:go-scout-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/go-scout/smile.png) | ![欢乐](thumbs/go-scout/joy.png) | ![哭](thumbs/go-scout/cry.png) | ![沮丧](thumbs/go-scout/depressed.png) | ![惊恐](thumbs/go-scout/terrified.png) | ![愤怒](thumbs/go-scout/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/go-scout/coquettish.png) | ![卖萌](thumbs/go-scout/cute.png) | ![讨好](thumbs/go-scout/pleasing.png) | ![敲打](thumbs/go-scout/knocking.png) | ![捂脸](thumbs/go-scout/facepalm.png) | ![吐舌头](thumbs/go-scout/tongue.png) |

`:go-scout-smile:` · `:go-scout-joy:` · `:go-scout-cry:` · `:go-scout-depressed:` · `:go-scout-terrified:` · `:go-scout-angry:` · `:go-scout-coquettish:` · `:go-scout-cute:` · `:go-scout-pleasing:` · `:go-scout-knocking:` · `:go-scout-facepalm:` · `:go-scout-tongue:`

### Kee · 橘猫 · `bag/jwt-rust` · `:jwt-rust-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/jwt-rust/smile.png) | ![欢乐](thumbs/jwt-rust/joy.png) | ![哭](thumbs/jwt-rust/cry.png) | ![沮丧](thumbs/jwt-rust/depressed.png) | ![惊恐](thumbs/jwt-rust/terrified.png) | ![愤怒](thumbs/jwt-rust/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/jwt-rust/coquettish.png) | ![卖萌](thumbs/jwt-rust/cute.png) | ![讨好](thumbs/jwt-rust/pleasing.png) | ![敲打](thumbs/jwt-rust/knocking.png) | ![捂脸](thumbs/jwt-rust/facepalm.png) | ![吐舌头](thumbs/jwt-rust/tongue.png) |

`:jwt-rust-smile:` · `:jwt-rust-joy:` · `:jwt-rust-cry:` · `:jwt-rust-depressed:` · `:jwt-rust-terrified:` · `:jwt-rust-angry:` · `:jwt-rust-coquettish:` · `:jwt-rust-cute:` · `:jwt-rust-pleasing:` · `:jwt-rust-knocking:` · `:jwt-rust-facepalm:` · `:jwt-rust-tongue:`

### Posty · `bag/poster-rust` · `:poster-rust-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/poster-rust/smile.png) | ![欢乐](thumbs/poster-rust/joy.png) | ![哭](thumbs/poster-rust/cry.png) | ![沮丧](thumbs/poster-rust/depressed.png) | ![惊恐](thumbs/poster-rust/terrified.png) | ![愤怒](thumbs/poster-rust/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/poster-rust/coquettish.png) | ![卖萌](thumbs/poster-rust/cute.png) | ![讨好](thumbs/poster-rust/pleasing.png) | ![敲打](thumbs/poster-rust/knocking.png) | ![捂脸](thumbs/poster-rust/facepalm.png) | ![吐舌头](thumbs/poster-rust/tongue.png) |

`:poster-rust-smile:` · `:poster-rust-joy:` · `:poster-rust-cry:` · `:poster-rust-depressed:` · `:poster-rust-terrified:` · `:poster-rust-angry:` · `:poster-rust-coquettish:` · `:poster-rust-cute:` · `:poster-rust-pleasing:` · `:poster-rust-knocking:` · `:poster-rust-facepalm:` · `:poster-rust-tongue:`

### Scout · `bag/rust-scout` · `:rust-scout-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/rust-scout/smile.png) | ![欢乐](thumbs/rust-scout/joy.png) | ![哭](thumbs/rust-scout/cry.png) | ![沮丧](thumbs/rust-scout/depressed.png) | ![惊恐](thumbs/rust-scout/terrified.png) | ![愤怒](thumbs/rust-scout/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/rust-scout/coquettish.png) | ![卖萌](thumbs/rust-scout/cute.png) | ![讨好](thumbs/rust-scout/pleasing.png) | ![敲打](thumbs/rust-scout/knocking.png) | ![捂脸](thumbs/rust-scout/facepalm.png) | ![吐舌头](thumbs/rust-scout/tongue.png) |

`:rust-scout-smile:` · `:rust-scout-joy:` · `:rust-scout-cry:` · `:rust-scout-depressed:` · `:rust-scout-terrified:` · `:rust-scout-angry:` · `:rust-scout-coquettish:` · `:rust-scout-cute:` · `:rust-scout-pleasing:` · `:rust-scout-knocking:` · `:rust-scout-facepalm:` · `:rust-scout-tongue:`

### 哨兵鼠 · `bag/security-go` · `:security-go-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/security-go/smile.png) | ![欢乐](thumbs/security-go/joy.png) | ![哭](thumbs/security-go/cry.png) | ![沮丧](thumbs/security-go/depressed.png) | ![惊恐](thumbs/security-go/terrified.png) | ![愤怒](thumbs/security-go/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/security-go/coquettish.png) | ![卖萌](thumbs/security-go/cute.png) | ![讨好](thumbs/security-go/pleasing.png) | ![敲打](thumbs/security-go/knocking.png) | ![捂脸](thumbs/security-go/facepalm.png) | ![吐舌头](thumbs/security-go/tongue.png) |

`:security-go-smile:` · `:security-go-joy:` · `:security-go-cry:` · `:security-go-depressed:` · `:security-go-terrified:` · `:security-go-angry:` · `:security-go-coquettish:` · `:security-go-cute:` · `:security-go-pleasing:` · `:security-go-knocking:` · `:security-go-facepalm:` · `:security-go-tongue:`

### 甲哨 Sentri · `bag/security-rust` · `:security-rust-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/security-rust/smile.png) | ![欢乐](thumbs/security-rust/joy.png) | ![哭](thumbs/security-rust/cry.png) | ![沮丧](thumbs/security-rust/depressed.png) | ![惊恐](thumbs/security-rust/terrified.png) | ![愤怒](thumbs/security-rust/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/security-rust/coquettish.png) | ![卖萌](thumbs/security-rust/cute.png) | ![讨好](thumbs/security-rust/pleasing.png) | ![敲打](thumbs/security-rust/knocking.png) | ![捂脸](thumbs/security-rust/facepalm.png) | ![吐舌头](thumbs/security-rust/tongue.png) |

`:security-rust-smile:` · `:security-rust-joy:` · `:security-rust-cry:` · `:security-rust-depressed:` · `:security-rust-terrified:` · `:security-rust-angry:` · `:security-rust-coquettish:` · `:security-rust-cute:` · `:security-rust-pleasing:` · `:security-rust-knocking:` · `:security-rust-facepalm:` · `:security-rust-tongue:`

### 以太兽 · `erikwang2013/aetherupload-webman` · `:aetherupload-webman-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/aetherupload-webman/smile.png) | ![欢乐](thumbs/aetherupload-webman/joy.png) | ![哭](thumbs/aetherupload-webman/cry.png) | ![沮丧](thumbs/aetherupload-webman/depressed.png) | ![惊恐](thumbs/aetherupload-webman/terrified.png) | ![愤怒](thumbs/aetherupload-webman/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/aetherupload-webman/coquettish.png) | ![卖萌](thumbs/aetherupload-webman/cute.png) | ![讨好](thumbs/aetherupload-webman/pleasing.png) | ![敲打](thumbs/aetherupload-webman/knocking.png) | ![捂脸](thumbs/aetherupload-webman/facepalm.png) | ![吐舌头](thumbs/aetherupload-webman/tongue.png) |

`:aetherupload-webman-smile:` · `:aetherupload-webman-joy:` · `:aetherupload-webman-cry:` · `:aetherupload-webman-depressed:` · `:aetherupload-webman-terrified:` · `:aetherupload-webman-angry:` · `:aetherupload-webman-coquettish:` · `:aetherupload-webman-cute:` · `:aetherupload-webman-pleasing:` · `:aetherupload-webman-knocking:` · `:aetherupload-webman-facepalm:` · `:aetherupload-webman-tongue:`

### Apidoc · `erikwang2013/apidoc-php` · `:apidoc-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/apidoc-php/smile.png) | ![欢乐](thumbs/apidoc-php/joy.png) | ![哭](thumbs/apidoc-php/cry.png) | ![沮丧](thumbs/apidoc-php/depressed.png) | ![惊恐](thumbs/apidoc-php/terrified.png) | ![愤怒](thumbs/apidoc-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/apidoc-php/coquettish.png) | ![卖萌](thumbs/apidoc-php/cute.png) | ![讨好](thumbs/apidoc-php/pleasing.png) | ![敲打](thumbs/apidoc-php/knocking.png) | ![捂脸](thumbs/apidoc-php/facepalm.png) | ![吐舌头](thumbs/apidoc-php/tongue.png) |

`:apidoc-php-smile:` · `:apidoc-php-joy:` · `:apidoc-php-cry:` · `:apidoc-php-depressed:` · `:apidoc-php-terrified:` · `:apidoc-php-angry:` · `:apidoc-php-coquettish:` · `:apidoc-php-cute:` · `:apidoc-php-pleasing:` · `:apidoc-php-knocking:` · `:apidoc-php-facepalm:` · `:apidoc-php-tongue:`

### ClickHouse 仓鼠 · `erikwang2013/clickhouse-php` · `:clickhouse-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/clickhouse-php/smile.png) | ![欢乐](thumbs/clickhouse-php/joy.png) | ![哭](thumbs/clickhouse-php/cry.png) | ![沮丧](thumbs/clickhouse-php/depressed.png) | ![惊恐](thumbs/clickhouse-php/terrified.png) | ![愤怒](thumbs/clickhouse-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/clickhouse-php/coquettish.png) | ![卖萌](thumbs/clickhouse-php/cute.png) | ![讨好](thumbs/clickhouse-php/pleasing.png) | ![敲打](thumbs/clickhouse-php/knocking.png) | ![捂脸](thumbs/clickhouse-php/facepalm.png) | ![吐舌头](thumbs/clickhouse-php/tongue.png) |

`:clickhouse-php-smile:` · `:clickhouse-php-joy:` · `:clickhouse-php-cry:` · `:clickhouse-php-depressed:` · `:clickhouse-php-terrified:` · `:clickhouse-php-angry:` · `:clickhouse-php-coquettish:` · `:clickhouse-php-cute:` · `:clickhouse-php-pleasing:` · `:clickhouse-php-knocking:` · `:clickhouse-php-facepalm:` · `:clickhouse-php-tongue:`

### Consu · `erikwang2013/consul-php` · `:consul-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/consul-php/smile.png) | ![欢乐](thumbs/consul-php/joy.png) | ![哭](thumbs/consul-php/cry.png) | ![沮丧](thumbs/consul-php/depressed.png) | ![惊恐](thumbs/consul-php/terrified.png) | ![愤怒](thumbs/consul-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/consul-php/coquettish.png) | ![卖萌](thumbs/consul-php/cute.png) | ![讨好](thumbs/consul-php/pleasing.png) | ![敲打](thumbs/consul-php/knocking.png) | ![捂脸](thumbs/consul-php/facepalm.png) | ![吐舌头](thumbs/consul-php/tongue.png) |

`:consul-php-smile:` · `:consul-php-joy:` · `:consul-php-cry:` · `:consul-php-depressed:` · `:consul-php-terrified:` · `:consul-php-angry:` · `:consul-php-coquettish:` · `:consul-php-cute:` · `:consul-php-pleasing:` · `:consul-php-knocking:` · `:consul-php-facepalm:` · `:consul-php-tongue:`

### Locky · `erikwang2013/encryptable` · `:encryptable-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/encryptable/smile.png) | ![欢乐](thumbs/encryptable/joy.png) | ![哭](thumbs/encryptable/cry.png) | ![沮丧](thumbs/encryptable/depressed.png) | ![惊恐](thumbs/encryptable/terrified.png) | ![愤怒](thumbs/encryptable/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/encryptable/coquettish.png) | ![卖萌](thumbs/encryptable/cute.png) | ![讨好](thumbs/encryptable/pleasing.png) | ![敲打](thumbs/encryptable/knocking.png) | ![捂脸](thumbs/encryptable/facepalm.png) | ![吐舌头](thumbs/encryptable/tongue.png) |

`:encryptable-smile:` · `:encryptable-joy:` · `:encryptable-cry:` · `:encryptable-depressed:` · `:encryptable-terrified:` · `:encryptable-angry:` · `:encryptable-coquettish:` · `:encryptable-cute:` · `:encryptable-pleasing:` · `:encryptable-knocking:` · `:encryptable-facepalm:` · `:encryptable-tongue:`

### Locky · `erikwang2013/encryption` · `:encryption-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/encryption/smile.png) | ![欢乐](thumbs/encryption/joy.png) | ![哭](thumbs/encryption/cry.png) | ![沮丧](thumbs/encryption/depressed.png) | ![惊恐](thumbs/encryption/terrified.png) | ![愤怒](thumbs/encryption/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/encryption/coquettish.png) | ![卖萌](thumbs/encryption/cute.png) | ![讨好](thumbs/encryption/pleasing.png) | ![敲打](thumbs/encryption/knocking.png) | ![捂脸](thumbs/encryption/facepalm.png) | ![吐舌头](thumbs/encryption/tongue.png) |

`:encryption-smile:` · `:encryption-joy:` · `:encryption-cry:` · `:encryption-depressed:` · `:encryption-terrified:` · `:encryption-angry:` · `:encryption-coquettish:` · `:encryption-cute:` · `:encryption-pleasing:` · `:encryption-knocking:` · `:encryption-facepalm:` · `:encryption-tongue:`

### Etchy · `erikwang2013/etcd` · `:etcd-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/etcd/smile.png) | ![欢乐](thumbs/etcd/joy.png) | ![哭](thumbs/etcd/cry.png) | ![沮丧](thumbs/etcd/depressed.png) | ![惊恐](thumbs/etcd/terrified.png) | ![愤怒](thumbs/etcd/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/etcd/coquettish.png) | ![卖萌](thumbs/etcd/cute.png) | ![讨好](thumbs/etcd/pleasing.png) | ![敲打](thumbs/etcd/knocking.png) | ![捂脸](thumbs/etcd/facepalm.png) | ![吐舌头](thumbs/etcd/tongue.png) |

`:etcd-smile:` · `:etcd-joy:` · `:etcd-cry:` · `:etcd-depressed:` · `:etcd-terrified:` · `:etcd-angry:` · `:etcd-coquettish:` · `:etcd-cute:` · `:etcd-pleasing:` · `:etcd-knocking:` · `:etcd-facepalm:` · `:etcd-tongue:`

### 哈希迪 Hashy · `erikwang2013/hashids` · `:hashids-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/hashids/smile.png) | ![欢乐](thumbs/hashids/joy.png) | ![哭](thumbs/hashids/cry.png) | ![沮丧](thumbs/hashids/depressed.png) | ![惊恐](thumbs/hashids/terrified.png) | ![愤怒](thumbs/hashids/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/hashids/coquettish.png) | ![卖萌](thumbs/hashids/cute.png) | ![讨好](thumbs/hashids/pleasing.png) | ![敲打](thumbs/hashids/knocking.png) | ![捂脸](thumbs/hashids/facepalm.png) | ![吐舌头](thumbs/hashids/tongue.png) |

`:hashids-smile:` · `:hashids-joy:` · `:hashids-cry:` · `:hashids-depressed:` · `:hashids-terrified:` · `:hashids-angry:` · `:hashids-coquettish:` · `:hashids-cute:` · `:hashids-pleasing:` · `:hashids-knocking:` · `:hashids-facepalm:` · `:hashids-tongue:`

### Kee · 柴犬门卫 · `erikwang2013/jwt-webman` · `:jwt-webman-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/jwt-webman/smile.png) | ![欢乐](thumbs/jwt-webman/joy.png) | ![哭](thumbs/jwt-webman/cry.png) | ![沮丧](thumbs/jwt-webman/depressed.png) | ![惊恐](thumbs/jwt-webman/terrified.png) | ![愤怒](thumbs/jwt-webman/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/jwt-webman/coquettish.png) | ![卖萌](thumbs/jwt-webman/cute.png) | ![讨好](thumbs/jwt-webman/pleasing.png) | ![敲打](thumbs/jwt-webman/knocking.png) | ![捂脸](thumbs/jwt-webman/facepalm.png) | ![吐舌头](thumbs/jwt-webman/tongue.png) |

`:jwt-webman-smile:` · `:jwt-webman-joy:` · `:jwt-webman-cry:` · `:jwt-webman-depressed:` · `:jwt-webman-terrified:` · `:jwt-webman-angry:` · `:jwt-webman-coquettish:` · `:jwt-webman-cute:` · `:jwt-webman-pleasing:` · `:jwt-webman-knocking:` · `:jwt-webman-facepalm:` · `:jwt-webman-tongue:`

### Posty · `erikwang2013/poster-php` · `:poster-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/poster-php/smile.png) | ![欢乐](thumbs/poster-php/joy.png) | ![哭](thumbs/poster-php/cry.png) | ![沮丧](thumbs/poster-php/depressed.png) | ![惊恐](thumbs/poster-php/terrified.png) | ![愤怒](thumbs/poster-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/poster-php/coquettish.png) | ![卖萌](thumbs/poster-php/cute.png) | ![讨好](thumbs/poster-php/pleasing.png) | ![敲打](thumbs/poster-php/knocking.png) | ![捂脸](thumbs/poster-php/facepalm.png) | ![吐舌头](thumbs/poster-php/tongue.png) |

`:poster-php-smile:` · `:poster-php-joy:` · `:poster-php-cry:` · `:poster-php-depressed:` · `:poster-php-terrified:` · `:poster-php-angry:` · `:poster-php-coquettish:` · `:poster-php-cute:` · `:poster-php-pleasing:` · `:poster-php-knocking:` · `:poster-php-facepalm:` · `:poster-php-tongue:`

### Seasony 季灵 · `erikwang2013/season` · `:season-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/season/smile.png) | ![欢乐](thumbs/season/joy.png) | ![哭](thumbs/season/cry.png) | ![沮丧](thumbs/season/depressed.png) | ![惊恐](thumbs/season/terrified.png) | ![愤怒](thumbs/season/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/season/coquettish.png) | ![卖萌](thumbs/season/cute.png) | ![讨好](thumbs/season/pleasing.png) | ![敲打](thumbs/season/knocking.png) | ![捂脸](thumbs/season/facepalm.png) | ![吐舌头](thumbs/season/tongue.png) |

`:season-smile:` · `:season-joy:` · `:season-cry:` · `:season-depressed:` · `:season-terrified:` · `:season-angry:` · `:season-coquettish:` · `:season-cute:` · `:season-pleasing:` · `:season-knocking:` · `:season-facepalm:` · `:season-tongue:`

### 小盾 · `erikwang2013/security-php` · `:security-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/security-php/smile.png) | ![欢乐](thumbs/security-php/joy.png) | ![哭](thumbs/security-php/cry.png) | ![沮丧](thumbs/security-php/depressed.png) | ![惊恐](thumbs/security-php/terrified.png) | ![愤怒](thumbs/security-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/security-php/coquettish.png) | ![卖萌](thumbs/security-php/cute.png) | ![讨好](thumbs/security-php/pleasing.png) | ![敲打](thumbs/security-php/knocking.png) | ![捂脸](thumbs/security-php/facepalm.png) | ![吐舌头](thumbs/security-php/tongue.png) |

`:security-php-smile:` · `:security-php-joy:` · `:security-php-cry:` · `:security-php-depressed:` · `:security-php-terrified:` · `:security-php-angry:` · `:security-php-coquettish:` · `:security-php-cute:` · `:security-php-pleasing:` · `:security-php-knocking:` · `:security-php-facepalm:` · `:security-php-tongue:`

### 雪花精灵 · `erikwang2013/snowflake-php` · `:snowflake-php-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/snowflake-php/smile.png) | ![欢乐](thumbs/snowflake-php/joy.png) | ![哭](thumbs/snowflake-php/cry.png) | ![沮丧](thumbs/snowflake-php/depressed.png) | ![惊恐](thumbs/snowflake-php/terrified.png) | ![愤怒](thumbs/snowflake-php/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/snowflake-php/coquettish.png) | ![卖萌](thumbs/snowflake-php/cute.png) | ![讨好](thumbs/snowflake-php/pleasing.png) | ![敲打](thumbs/snowflake-php/knocking.png) | ![捂脸](thumbs/snowflake-php/facepalm.png) | ![吐舌头](thumbs/snowflake-php/tongue.png) |

`:snowflake-php-smile:` · `:snowflake-php-joy:` · `:snowflake-php-cry:` · `:snowflake-php-depressed:` · `:snowflake-php-terrified:` · `:snowflake-php-angry:` · `:snowflake-php-coquettish:` · `:snowflake-php-cute:` · `:snowflake-php-pleasing:` · `:snowflake-php-knocking:` · `:snowflake-php-facepalm:` · `:snowflake-php-tongue:`

### Sniffy · `erikwang2013/webman-scout` · `:webman-scout-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/webman-scout/smile.png) | ![欢乐](thumbs/webman-scout/joy.png) | ![哭](thumbs/webman-scout/cry.png) | ![沮丧](thumbs/webman-scout/depressed.png) | ![惊恐](thumbs/webman-scout/terrified.png) | ![愤怒](thumbs/webman-scout/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/webman-scout/coquettish.png) | ![卖萌](thumbs/webman-scout/cute.png) | ![讨好](thumbs/webman-scout/pleasing.png) | ![敲打](thumbs/webman-scout/knocking.png) | ![捂脸](thumbs/webman-scout/facepalm.png) | ![吐舌头](thumbs/webman-scout/tongue.png) |

`:webman-scout-smile:` · `:webman-scout-joy:` · `:webman-scout-cry:` · `:webman-scout-depressed:` · `:webman-scout-terrified:` · `:webman-scout-angry:` · `:webman-scout-coquettish:` · `:webman-scout-cute:` · `:webman-scout-pleasing:` · `:webman-scout-knocking:` · `:webman-scout-facepalm:` · `:webman-scout-tongue:`

### Xhpy · `erikwang2013/xhprof` · `:xhprof-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/xhprof/smile.png) | ![欢乐](thumbs/xhprof/joy.png) | ![哭](thumbs/xhprof/cry.png) | ![沮丧](thumbs/xhprof/depressed.png) | ![惊恐](thumbs/xhprof/terrified.png) | ![愤怒](thumbs/xhprof/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/xhprof/coquettish.png) | ![卖萌](thumbs/xhprof/cute.png) | ![讨好](thumbs/xhprof/pleasing.png) | ![敲打](thumbs/xhprof/knocking.png) | ![捂脸](thumbs/xhprof/facepalm.png) | ![吐舌头](thumbs/xhprof/tongue.png) |

`:xhprof-smile:` · `:xhprof-joy:` · `:xhprof-cry:` · `:xhprof-depressed:` · `:xhprof-terrified:` · `:xhprof-angry:` · `:xhprof-coquettish:` · `:xhprof-cute:` · `:xhprof-pleasing:` · `:xhprof-knocking:` · `:xhprof-facepalm:` · `:xhprof-tongue:`

### 焰焰 · `erikwang2013/xhprof-webman` · `:xhprof-webman-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/xhprof-webman/smile.png) | ![欢乐](thumbs/xhprof-webman/joy.png) | ![哭](thumbs/xhprof-webman/cry.png) | ![沮丧](thumbs/xhprof-webman/depressed.png) | ![惊恐](thumbs/xhprof-webman/terrified.png) | ![愤怒](thumbs/xhprof-webman/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/xhprof-webman/coquettish.png) | ![卖萌](thumbs/xhprof-webman/cute.png) | ![讨好](thumbs/xhprof-webman/pleasing.png) | ![敲打](thumbs/xhprof-webman/knocking.png) | ![捂脸](thumbs/xhprof-webman/facepalm.png) | ![吐舌头](thumbs/xhprof-webman/tongue.png) |

`:xhprof-webman-smile:` · `:xhprof-webman-joy:` · `:xhprof-webman-cry:` · `:xhprof-webman-depressed:` · `:xhprof-webman-terrified:` · `:xhprof-webman-angry:` · `:xhprof-webman-coquettish:` · `:xhprof-webman-cute:` · `:xhprof-webman-pleasing:` · `:xhprof-webman-knocking:` · `:xhprof-webman-facepalm:` · `:xhprof-webman-tongue:`

### 吞吞 · `oss` · `:oss-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/oss/smile.png) | ![欢乐](thumbs/oss/joy.png) | ![哭](thumbs/oss/cry.png) | ![沮丧](thumbs/oss/depressed.png) | ![惊恐](thumbs/oss/terrified.png) | ![愤怒](thumbs/oss/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/oss/coquettish.png) | ![卖萌](thumbs/oss/cute.png) | ![讨好](thumbs/oss/pleasing.png) | ![敲打](thumbs/oss/knocking.png) | ![捂脸](thumbs/oss/facepalm.png) | ![吐舌头](thumbs/oss/tongue.png) |

`:oss-smile:` · `:oss-joy:` · `:oss-cry:` · `:oss-depressed:` · `:oss-terrified:` · `:oss-angry:` · `:oss-coquettish:` · `:oss-cute:` · `:oss-pleasing:` · `:oss-knocking:` · `:oss-facepalm:` · `:oss-tongue:`

### Pax · `polypack` · `:polypack-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/polypack/smile.png) | ![欢乐](thumbs/polypack/joy.png) | ![哭](thumbs/polypack/cry.png) | ![沮丧](thumbs/polypack/depressed.png) | ![惊恐](thumbs/polypack/terrified.png) | ![愤怒](thumbs/polypack/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/polypack/coquettish.png) | ![卖萌](thumbs/polypack/cute.png) | ![讨好](thumbs/polypack/pleasing.png) | ![敲打](thumbs/polypack/knocking.png) | ![捂脸](thumbs/polypack/facepalm.png) | ![吐舌头](thumbs/polypack/tongue.png) |

`:polypack-smile:` · `:polypack-joy:` · `:polypack-cry:` · `:polypack-depressed:` · `:polypack-terrified:` · `:polypack-angry:` · `:polypack-coquettish:` · `:polypack-cute:` · `:polypack-pleasing:` · `:polypack-knocking:` · `:polypack-facepalm:` · `:polypack-tongue:`

### 小欧 · `opi` · `:opi-*:`

| 笑 | 欢乐 | 哭 | 沮丧 | 惊恐 | 愤怒 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![笑](thumbs/opi/smile.png) | ![欢乐](thumbs/opi/joy.png) | ![哭](thumbs/opi/cry.png) | ![沮丧](thumbs/opi/depressed.png) | ![惊恐](thumbs/opi/terrified.png) | ![愤怒](thumbs/opi/angry.png) |

| 撒娇 | 卖萌 | 讨好 | 敲打 | 捂脸 | 吐舌头 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| ![撒娇](thumbs/opi/coquettish.png) | ![卖萌](thumbs/opi/cute.png) | ![讨好](thumbs/opi/pleasing.png) | ![敲打](thumbs/opi/knocking.png) | ![捂脸](thumbs/opi/facepalm.png) | ![吐舌头](thumbs/opi/tongue.png) |

`:opi-smile:` · `:opi-joy:` · `:opi-cry:` · `:opi-depressed:` · `:opi-terrified:` · `:opi-angry:` · `:opi-coquettish:` · `:opi-cute:` · `:opi-pleasing:` · `:opi-knocking:` · `:opi-facepalm:` · `:opi-tongue:`

## 说明

- 图片源文件在 `pets/<项目>/<形态>.svg`，PNG 在 `png/<项目>/<形态>.png`，README 预览使用 `thumbs/<项目>/<形态>.png`（64×64）。
- `preview.png` 是所有项目「笑」形态的总览。
- 已去除与其他项目重复的 7 个宠物入口：`aetherupload-rust`、`apidoc-go`、`apidoc-rust`、`apidoc-ui`、`encryptable-rust`、`hashids-rust`、`snowflake-rust`；保留对应的 PHP / Webman 版本。`jwt-rust` 已改为独立橘猫形象，重新纳入。
- 本项目代码与生成脚本仍遵循其原有许可；视觉资产适用 [ASSETS-LICENSE.md](ASSETS-LICENSE.md)。
