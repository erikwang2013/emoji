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

![笑](pets/ads-php/smile.svg) `:ads-php-smile:` · ![欢乐](pets/ads-php/joy.svg) `:ads-php-joy:` · ![哭](pets/ads-php/cry.svg) `:ads-php-cry:` · ![沮丧](pets/ads-php/depressed.svg) `:ads-php-depressed:` · ![惊恐](pets/ads-php/terrified.svg) `:ads-php-terrified:` · ![愤怒](pets/ads-php/angry.svg) `:ads-php-angry:`

![撒娇](pets/ads-php/coquettish.svg) `:ads-php-coquettish:` · ![卖萌](pets/ads-php/cute.svg) `:ads-php-cute:` · ![讨好](pets/ads-php/pleasing.svg) `:ads-php-pleasing:` · ![敲打](pets/ads-php/knocking.svg) `:ads-php-knocking:` · ![捂脸](pets/ads-php/facepalm.svg) `:ads-php-facepalm:` · ![吐舌头](pets/ads-php/tongue.svg) `:ads-php-tongue:`

### 小约 · `appointment-php` · `:appointment-php-*:`

![笑](pets/appointment-php/smile.svg) `:appointment-php-smile:` · ![欢乐](pets/appointment-php/joy.svg) `:appointment-php-joy:` · ![哭](pets/appointment-php/cry.svg) `:appointment-php-cry:` · ![沮丧](pets/appointment-php/depressed.svg) `:appointment-php-depressed:` · ![惊恐](pets/appointment-php/terrified.svg) `:appointment-php-terrified:` · ![愤怒](pets/appointment-php/angry.svg) `:appointment-php-angry:`

![撒娇](pets/appointment-php/coquettish.svg) `:appointment-php-coquettish:` · ![卖萌](pets/appointment-php/cute.svg) `:appointment-php-cute:` · ![讨好](pets/appointment-php/pleasing.svg) `:appointment-php-pleasing:` · ![敲打](pets/appointment-php/knocking.svg) `:appointment-php-knocking:` · ![捂脸](pets/appointment-php/facepalm.svg) `:appointment-php-facepalm:` · ![吐舌头](pets/appointment-php/tongue.svg) `:appointment-php-tongue:`

### Rusty · `bee-rust` · `:bee-rust-*:`

![笑](pets/bee-rust/smile.svg) `:bee-rust-smile:` · ![欢乐](pets/bee-rust/joy.svg) `:bee-rust-joy:` · ![哭](pets/bee-rust/cry.svg) `:bee-rust-cry:` · ![沮丧](pets/bee-rust/depressed.svg) `:bee-rust-depressed:` · ![惊恐](pets/bee-rust/terrified.svg) `:bee-rust-terrified:` · ![愤怒](pets/bee-rust/angry.svg) `:bee-rust-angry:`

![撒娇](pets/bee-rust/coquettish.svg) `:bee-rust-coquettish:` · ![卖萌](pets/bee-rust/cute.svg) `:bee-rust-cute:` · ![讨好](pets/bee-rust/pleasing.svg) `:bee-rust-pleasing:` · ![敲打](pets/bee-rust/knocking.svg) `:bee-rust-knocking:` · ![捂脸](pets/bee-rust/facepalm.svg) `:bee-rust-facepalm:` · ![吐舌头](pets/bee-rust/tongue.svg) `:bee-rust-tongue:`

### 阿守 · `bee-rust-admin` · `:bee-rust-admin-*:`

![笑](pets/bee-rust-admin/smile.svg) `:bee-rust-admin-smile:` · ![欢乐](pets/bee-rust-admin/joy.svg) `:bee-rust-admin-joy:` · ![哭](pets/bee-rust-admin/cry.svg) `:bee-rust-admin-cry:` · ![沮丧](pets/bee-rust-admin/depressed.svg) `:bee-rust-admin-depressed:` · ![惊恐](pets/bee-rust-admin/terrified.svg) `:bee-rust-admin-terrified:` · ![愤怒](pets/bee-rust-admin/angry.svg) `:bee-rust-admin-angry:`

![撒娇](pets/bee-rust-admin/coquettish.svg) `:bee-rust-admin-coquettish:` · ![卖萌](pets/bee-rust-admin/cute.svg) `:bee-rust-admin-cute:` · ![讨好](pets/bee-rust-admin/pleasing.svg) `:bee-rust-admin-pleasing:` · ![敲打](pets/bee-rust-admin/knocking.svg) `:bee-rust-admin-knocking:` · ![捂脸](pets/bee-rust-admin/facepalm.svg) `:bee-rust-admin-facepalm:` · ![吐舌头](pets/bee-rust-admin/tongue.svg) `:bee-rust-admin-tongue:`

### 云团 · `cloud-php` · `:cloud-php-*:`

![笑](pets/cloud-php/smile.svg) `:cloud-php-smile:` · ![欢乐](pets/cloud-php/joy.svg) `:cloud-php-joy:` · ![哭](pets/cloud-php/cry.svg) `:cloud-php-cry:` · ![沮丧](pets/cloud-php/depressed.svg) `:cloud-php-depressed:` · ![惊恐](pets/cloud-php/terrified.svg) `:cloud-php-terrified:` · ![愤怒](pets/cloud-php/angry.svg) `:cloud-php-angry:`

![撒娇](pets/cloud-php/coquettish.svg) `:cloud-php-coquettish:` · ![卖萌](pets/cloud-php/cute.svg) `:cloud-php-cute:` · ![讨好](pets/cloud-php/pleasing.svg) `:cloud-php-pleasing:` · ![敲打](pets/cloud-php/knocking.svg) `:cloud-php-knocking:` · ![捂脸](pets/cloud-php/facepalm.svg) `:cloud-php-facepalm:` · ![吐舌头](pets/cloud-php/tongue.svg) `:cloud-php-tongue:`

### E-Cat · `e-cat` · `:e-cat-*:`

![笑](pets/e-cat/smile.svg) `:e-cat-smile:` · ![欢乐](pets/e-cat/joy.svg) `:e-cat-joy:` · ![哭](pets/e-cat/cry.svg) `:e-cat-cry:` · ![沮丧](pets/e-cat/depressed.svg) `:e-cat-depressed:` · ![惊恐](pets/e-cat/terrified.svg) `:e-cat-terrified:` · ![愤怒](pets/e-cat/angry.svg) `:e-cat-angry:`

![撒娇](pets/e-cat/coquettish.svg) `:e-cat-coquettish:` · ![卖萌](pets/e-cat/cute.svg) `:e-cat-cute:` · ![讨好](pets/e-cat/pleasing.svg) `:e-cat-pleasing:` · ![敲打](pets/e-cat/knocking.svg) `:e-cat-knocking:` · ![捂脸](pets/e-cat/facepalm.svg) `:e-cat-facepalm:` · ![吐舌头](pets/e-cat/tongue.svg) `:e-cat-tongue:`

### Lumi · `erik-talk` · `:erik-talk-*:`

![笑](pets/erik-talk/smile.svg) `:erik-talk-smile:` · ![欢乐](pets/erik-talk/joy.svg) `:erik-talk-joy:` · ![哭](pets/erik-talk/cry.svg) `:erik-talk-cry:` · ![沮丧](pets/erik-talk/depressed.svg) `:erik-talk-depressed:` · ![惊恐](pets/erik-talk/terrified.svg) `:erik-talk-terrified:` · ![愤怒](pets/erik-talk/angry.svg) `:erik-talk-angry:`

![撒娇](pets/erik-talk/coquettish.svg) `:erik-talk-coquettish:` · ![卖萌](pets/erik-talk/cute.svg) `:erik-talk-cute:` · ![讨好](pets/erik-talk/pleasing.svg) `:erik-talk-pleasing:` · ![敲打](pets/erik-talk/knocking.svg) `:erik-talk-knocking:` · ![捂脸](pets/erik-talk/facepalm.svg) `:erik-talk-facepalm:` · ![吐舌头](pets/erik-talk/tongue.svg) `:erik-talk-tongue:`

### 小八爪 · `erp-php` · `:erp-php-*:`

![笑](pets/erp-php/smile.svg) `:erp-php-smile:` · ![欢乐](pets/erp-php/joy.svg) `:erp-php-joy:` · ![哭](pets/erp-php/cry.svg) `:erp-php-cry:` · ![沮丧](pets/erp-php/depressed.svg) `:erp-php-depressed:` · ![惊恐](pets/erp-php/terrified.svg) `:erp-php-terrified:` · ![愤怒](pets/erp-php/angry.svg) `:erp-php-angry:`

![撒娇](pets/erp-php/coquettish.svg) `:erp-php-coquettish:` · ![卖萌](pets/erp-php/cute.svg) `:erp-php-cute:` · ![讨好](pets/erp-php/pleasing.svg) `:erp-php-pleasing:` · ![敲打](pets/erp-php/knocking.svg) `:erp-php-knocking:` · ![捂脸](pets/erp-php/facepalm.svg) `:erp-php-facepalm:` · ![吐舌头](pets/erp-php/tongue.svg) `:erp-php-tongue:`

### Dicey · `game-platform-php` · `:game-platform-php-*:`

![笑](pets/game-platform-php/smile.svg) `:game-platform-php-smile:` · ![欢乐](pets/game-platform-php/joy.svg) `:game-platform-php-joy:` · ![哭](pets/game-platform-php/cry.svg) `:game-platform-php-cry:` · ![沮丧](pets/game-platform-php/depressed.svg) `:game-platform-php-depressed:` · ![惊恐](pets/game-platform-php/terrified.svg) `:game-platform-php-terrified:` · ![愤怒](pets/game-platform-php/angry.svg) `:game-platform-php-angry:`

![撒娇](pets/game-platform-php/coquettish.svg) `:game-platform-php-coquettish:` · ![卖萌](pets/game-platform-php/cute.svg) `:game-platform-php-cute:` · ![讨好](pets/game-platform-php/pleasing.svg) `:game-platform-php-pleasing:` · ![敲打](pets/game-platform-php/knocking.svg) `:game-platform-php-knocking:` · ![捂脸](pets/game-platform-php/facepalm.svg) `:game-platform-php-facepalm:` · ![吐舌头](pets/game-platform-php/tongue.svg) `:game-platform-php-tongue:`

### 霜霜 · `insurance-service` · `:insurance-service-*:`

![笑](pets/insurance-service/smile.svg) `:insurance-service-smile:` · ![欢乐](pets/insurance-service/joy.svg) `:insurance-service-joy:` · ![哭](pets/insurance-service/cry.svg) `:insurance-service-cry:` · ![沮丧](pets/insurance-service/depressed.svg) `:insurance-service-depressed:` · ![惊恐](pets/insurance-service/terrified.svg) `:insurance-service-terrified:` · ![愤怒](pets/insurance-service/angry.svg) `:insurance-service-angry:`

![撒娇](pets/insurance-service/coquettish.svg) `:insurance-service-coquettish:` · ![卖萌](pets/insurance-service/cute.svg) `:insurance-service-cute:` · ![讨好](pets/insurance-service/pleasing.svg) `:insurance-service-pleasing:` · ![敲打](pets/insurance-service/knocking.svg) `:insurance-service-knocking:` · ![捂脸](pets/insurance-service/facepalm.svg) `:insurance-service-facepalm:` · ![吐舌头](pets/insurance-service/tongue.svg) `:insurance-service-tongue:`

### E-Cat · `integrated-global-logistics` · `:integrated-global-logistics-*:`

![笑](pets/integrated-global-logistics/smile.svg) `:integrated-global-logistics-smile:` · ![欢乐](pets/integrated-global-logistics/joy.svg) `:integrated-global-logistics-joy:` · ![哭](pets/integrated-global-logistics/cry.svg) `:integrated-global-logistics-cry:` · ![沮丧](pets/integrated-global-logistics/depressed.svg) `:integrated-global-logistics-depressed:` · ![惊恐](pets/integrated-global-logistics/terrified.svg) `:integrated-global-logistics-terrified:` · ![愤怒](pets/integrated-global-logistics/angry.svg) `:integrated-global-logistics-angry:`

![撒娇](pets/integrated-global-logistics/coquettish.svg) `:integrated-global-logistics-coquettish:` · ![卖萌](pets/integrated-global-logistics/cute.svg) `:integrated-global-logistics-cute:` · ![讨好](pets/integrated-global-logistics/pleasing.svg) `:integrated-global-logistics-pleasing:` · ![敲打](pets/integrated-global-logistics/knocking.svg) `:integrated-global-logistics-knocking:` · ![捂脸](pets/integrated-global-logistics/facepalm.svg) `:integrated-global-logistics-facepalm:` · ![吐舌头](pets/integrated-global-logistics/tongue.svg) `:integrated-global-logistics-tongue:`

### IoT Bot · `iot-platform` · `:iot-platform-*:`

![笑](pets/iot-platform/smile.svg) `:iot-platform-smile:` · ![欢乐](pets/iot-platform/joy.svg) `:iot-platform-joy:` · ![哭](pets/iot-platform/cry.svg) `:iot-platform-cry:` · ![沮丧](pets/iot-platform/depressed.svg) `:iot-platform-depressed:` · ![惊恐](pets/iot-platform/terrified.svg) `:iot-platform-terrified:` · ![愤怒](pets/iot-platform/angry.svg) `:iot-platform-angry:`

![撒娇](pets/iot-platform/coquettish.svg) `:iot-platform-coquettish:` · ![卖萌](pets/iot-platform/cute.svg) `:iot-platform-cute:` · ![讨好](pets/iot-platform/pleasing.svg) `:iot-platform-pleasing:` · ![敲打](pets/iot-platform/knocking.svg) `:iot-platform-knocking:` · ![捂脸](pets/iot-platform/facepalm.svg) `:iot-platform-facepalm:` · ![吐舌头](pets/iot-platform/tongue.svg) `:iot-platform-tongue:`

### 租租鼠 · `item-rental` · `:item-rental-*:`

![笑](pets/item-rental/smile.svg) `:item-rental-smile:` · ![欢乐](pets/item-rental/joy.svg) `:item-rental-joy:` · ![哭](pets/item-rental/cry.svg) `:item-rental-cry:` · ![沮丧](pets/item-rental/depressed.svg) `:item-rental-depressed:` · ![惊恐](pets/item-rental/terrified.svg) `:item-rental-terrified:` · ![愤怒](pets/item-rental/angry.svg) `:item-rental-angry:`

![撒娇](pets/item-rental/coquettish.svg) `:item-rental-coquettish:` · ![卖萌](pets/item-rental/cute.svg) `:item-rental-cute:` · ![讨好](pets/item-rental/pleasing.svg) `:item-rental-pleasing:` · ![敲打](pets/item-rental/knocking.svg) `:item-rental-knocking:` · ![捂脸](pets/item-rental/facepalm.svg) `:item-rental-facepalm:` · ![吐舌头](pets/item-rental/tongue.svg) `:item-rental-tongue:`

### 小音机 · `omb` · `:omb-*:`

![笑](pets/omb/smile.svg) `:omb-smile:` · ![欢乐](pets/omb/joy.svg) `:omb-joy:` · ![哭](pets/omb/cry.svg) `:omb-cry:` · ![沮丧](pets/omb/depressed.svg) `:omb-depressed:` · ![惊恐](pets/omb/terrified.svg) `:omb-terrified:` · ![愤怒](pets/omb/angry.svg) `:omb-angry:`

![撒娇](pets/omb/coquettish.svg) `:omb-coquettish:` · ![卖萌](pets/omb/cute.svg) `:omb-cute:` · ![讨好](pets/omb/pleasing.svg) `:omb-pleasing:` · ![敲打](pets/omb/knocking.svg) `:omb-knocking:` · ![捂脸](pets/omb/facepalm.svg) `:omb-facepalm:` · ![吐舌头](pets/omb/tongue.svg) `:omb-tongue:`

### 小安 · `open-admin` · `:open-admin-*:`

![笑](pets/open-admin/smile.svg) `:open-admin-smile:` · ![欢乐](pets/open-admin/joy.svg) `:open-admin-joy:` · ![哭](pets/open-admin/cry.svg) `:open-admin-cry:` · ![沮丧](pets/open-admin/depressed.svg) `:open-admin-depressed:` · ![惊恐](pets/open-admin/terrified.svg) `:open-admin-terrified:` · ![愤怒](pets/open-admin/angry.svg) `:open-admin-angry:`

![撒娇](pets/open-admin/coquettish.svg) `:open-admin-coquettish:` · ![卖萌](pets/open-admin/cute.svg) `:open-admin-cute:` · ![讨好](pets/open-admin/pleasing.svg) `:open-admin-pleasing:` · ![敲打](pets/open-admin/knocking.svg) `:open-admin-knocking:` · ![捂脸](pets/open-admin/facepalm.svg) `:open-admin-facepalm:` · ![吐舌头](pets/open-admin/tongue.svg) `:open-admin-tongue:`

### Novi · `open-novel` · `:open-novel-*:`

![笑](pets/open-novel/smile.svg) `:open-novel-smile:` · ![欢乐](pets/open-novel/joy.svg) `:open-novel-joy:` · ![哭](pets/open-novel/cry.svg) `:open-novel-cry:` · ![沮丧](pets/open-novel/depressed.svg) `:open-novel-depressed:` · ![惊恐](pets/open-novel/terrified.svg) `:open-novel-terrified:` · ![愤怒](pets/open-novel/angry.svg) `:open-novel-angry:`

![撒娇](pets/open-novel/coquettish.svg) `:open-novel-coquettish:` · ![卖萌](pets/open-novel/cute.svg) `:open-novel-cute:` · ![讨好](pets/open-novel/pleasing.svg) `:open-novel-pleasing:` · ![敲打](pets/open-novel/knocking.svg) `:open-novel-knocking:` · ![捂脸](pets/open-novel/facepalm.svg) `:open-novel-facepalm:` · ![吐舌头](pets/open-novel/tongue.svg) `:open-novel-tongue:`

### 南南 · `open-travel` · `:open-travel-*:`

![笑](pets/open-travel/smile.svg) `:open-travel-smile:` · ![欢乐](pets/open-travel/joy.svg) `:open-travel-joy:` · ![哭](pets/open-travel/cry.svg) `:open-travel-cry:` · ![沮丧](pets/open-travel/depressed.svg) `:open-travel-depressed:` · ![惊恐](pets/open-travel/terrified.svg) `:open-travel-terrified:` · ![愤怒](pets/open-travel/angry.svg) `:open-travel-angry:`

![撒娇](pets/open-travel/coquettish.svg) `:open-travel-coquettish:` · ![卖萌](pets/open-travel/cute.svg) `:open-travel-cute:` · ![讨好](pets/open-travel/pleasing.svg) `:open-travel-pleasing:` · ![敲打](pets/open-travel/knocking.svg) `:open-travel-knocking:` · ![捂脸](pets/open-travel/facepalm.svg) `:open-travel-facepalm:` · ![吐舌头](pets/open-travel/tongue.svg) `:open-travel-tongue:`

### 小筑 · `property-management-platform` · `:property-management-platform-*:`

![笑](pets/property-management-platform/smile.svg) `:property-management-platform-smile:` · ![欢乐](pets/property-management-platform/joy.svg) `:property-management-platform-joy:` · ![哭](pets/property-management-platform/cry.svg) `:property-management-platform-cry:` · ![沮丧](pets/property-management-platform/depressed.svg) `:property-management-platform-depressed:` · ![惊恐](pets/property-management-platform/terrified.svg) `:property-management-platform-terrified:` · ![愤怒](pets/property-management-platform/angry.svg) `:property-management-platform-angry:`

![撒娇](pets/property-management-platform/coquettish.svg) `:property-management-platform-coquettish:` · ![卖萌](pets/property-management-platform/cute.svg) `:property-management-platform-cute:` · ![讨好](pets/property-management-platform/pleasing.svg) `:property-management-platform-pleasing:` · ![敲打](pets/property-management-platform/knocking.svg) `:property-management-platform-knocking:` · ![捂脸](pets/property-management-platform/facepalm.svg) `:property-management-platform-facepalm:` · ![吐舌头](pets/property-management-platform/tongue.svg) `:property-management-platform-tongue:`

### 犇犇 · `quantitative-trading` · `:quantitative-trading-*:`

![笑](pets/quantitative-trading/smile.svg) `:quantitative-trading-smile:` · ![欢乐](pets/quantitative-trading/joy.svg) `:quantitative-trading-joy:` · ![哭](pets/quantitative-trading/cry.svg) `:quantitative-trading-cry:` · ![沮丧](pets/quantitative-trading/depressed.svg) `:quantitative-trading-depressed:` · ![惊恐](pets/quantitative-trading/terrified.svg) `:quantitative-trading-terrified:` · ![愤怒](pets/quantitative-trading/angry.svg) `:quantitative-trading-angry:`

![撒娇](pets/quantitative-trading/coquettish.svg) `:quantitative-trading-coquettish:` · ![卖萌](pets/quantitative-trading/cute.svg) `:quantitative-trading-cute:` · ![讨好](pets/quantitative-trading/pleasing.svg) `:quantitative-trading-pleasing:` · ![敲打](pets/quantitative-trading/knocking.svg) `:quantitative-trading-knocking:` · ![捂脸](pets/quantitative-trading/facepalm.svg) `:quantitative-trading-facepalm:` · ![吐舌头](pets/quantitative-trading/tongue.svg) `:quantitative-trading-tongue:`

### 雪球 Snowy · `shop-php` · `:shop-php-*:`

![笑](pets/shop-php/smile.svg) `:shop-php-smile:` · ![欢乐](pets/shop-php/joy.svg) `:shop-php-joy:` · ![哭](pets/shop-php/cry.svg) `:shop-php-cry:` · ![沮丧](pets/shop-php/depressed.svg) `:shop-php-depressed:` · ![惊恐](pets/shop-php/terrified.svg) `:shop-php-terrified:` · ![愤怒](pets/shop-php/angry.svg) `:shop-php-angry:`

![撒娇](pets/shop-php/coquettish.svg) `:shop-php-coquettish:` · ![卖萌](pets/shop-php/cute.svg) `:shop-php-cute:` · ![讨好](pets/shop-php/pleasing.svg) `:shop-php-pleasing:` · ![敲打](pets/shop-php/knocking.svg) `:shop-php-knocking:` · ![捂脸](pets/shop-php/facepalm.svg) `:shop-php-facepalm:` · ![吐舌头](pets/shop-php/tongue.svg) `:shop-php-tongue:`

### Bub · `social` · `:social-*:`

![笑](pets/social/smile.svg) `:social-smile:` · ![欢乐](pets/social/joy.svg) `:social-joy:` · ![哭](pets/social/cry.svg) `:social-cry:` · ![沮丧](pets/social/depressed.svg) `:social-depressed:` · ![惊恐](pets/social/terrified.svg) `:social-terrified:` · ![愤怒](pets/social/angry.svg) `:social-angry:`

![撒娇](pets/social/coquettish.svg) `:social-coquettish:` · ![卖萌](pets/social/cute.svg) `:social-cute:` · ![讨好](pets/social/pleasing.svg) `:social-pleasing:` · ![敲打](pets/social/knocking.svg) `:social-knocking:` · ![捂脸](pets/social/facepalm.svg) `:social-facepalm:` · ![吐舌头](pets/social/tongue.svg) `:social-tongue:`

### ssd · `ssd` · `:ssd-*:`

![笑](pets/ssd/smile.svg) `:ssd-smile:` · ![欢乐](pets/ssd/joy.svg) `:ssd-joy:` · ![哭](pets/ssd/cry.svg) `:ssd-cry:` · ![沮丧](pets/ssd/depressed.svg) `:ssd-depressed:` · ![惊恐](pets/ssd/terrified.svg) `:ssd-terrified:` · ![愤怒](pets/ssd/angry.svg) `:ssd-angry:`

![撒娇](pets/ssd/coquettish.svg) `:ssd-coquettish:` · ![卖萌](pets/ssd/cute.svg) `:ssd-cute:` · ![讨好](pets/ssd/pleasing.svg) `:ssd-pleasing:` · ![敲打](pets/ssd/knocking.svg) `:ssd-knocking:` · ![捂脸](pets/ssd/facepalm.svg) `:ssd-facepalm:` · ![吐舌头](pets/ssd/tongue.svg) `:ssd-tongue:`

### 超猫 SuperCat · `super-ops` · `:super-ops-*:`

![笑](pets/super-ops/smile.svg) `:super-ops-smile:` · ![欢乐](pets/super-ops/joy.svg) `:super-ops-joy:` · ![哭](pets/super-ops/cry.svg) `:super-ops-cry:` · ![沮丧](pets/super-ops/depressed.svg) `:super-ops-depressed:` · ![惊恐](pets/super-ops/terrified.svg) `:super-ops-terrified:` · ![愤怒](pets/super-ops/angry.svg) `:super-ops-angry:`

![撒娇](pets/super-ops/coquettish.svg) `:super-ops-coquettish:` · ![卖萌](pets/super-ops/cute.svg) `:super-ops-cute:` · ![讨好](pets/super-ops/pleasing.svg) `:super-ops-pleasing:` · ![敲打](pets/super-ops/knocking.svg) `:super-ops-knocking:` · ![捂脸](pets/super-ops/facepalm.svg) `:super-ops-facepalm:` · ![吐舌头](pets/super-ops/tongue.svg) `:super-ops-tongue:`

### 小运 · `bag/canal` · `:canal-*:`

![笑](pets/canal/smile.svg) `:canal-smile:` · ![欢乐](pets/canal/joy.svg) `:canal-joy:` · ![哭](pets/canal/cry.svg) `:canal-cry:` · ![沮丧](pets/canal/depressed.svg) `:canal-depressed:` · ![惊恐](pets/canal/terrified.svg) `:canal-terrified:` · ![愤怒](pets/canal/angry.svg) `:canal-angry:`

![撒娇](pets/canal/coquettish.svg) `:canal-coquettish:` · ![卖萌](pets/canal/cute.svg) `:canal-cute:` · ![讨好](pets/canal/pleasing.svg) `:canal-pleasing:` · ![敲打](pets/canal/knocking.svg) `:canal-knocking:` · ![捂脸](pets/canal/facepalm.svg) `:canal-facepalm:` · ![吐舌头](pets/canal/tongue.svg) `:canal-tongue:`

### 小德 · `bag/druid-rust` · `:druid-rust-*:`

![笑](pets/druid-rust/smile.svg) `:druid-rust-smile:` · ![欢乐](pets/druid-rust/joy.svg) `:druid-rust-joy:` · ![哭](pets/druid-rust/cry.svg) `:druid-rust-cry:` · ![沮丧](pets/druid-rust/depressed.svg) `:druid-rust-depressed:` · ![惊恐](pets/druid-rust/terrified.svg) `:druid-rust-terrified:` · ![愤怒](pets/druid-rust/angry.svg) `:druid-rust-angry:`

![撒娇](pets/druid-rust/coquettish.svg) `:druid-rust-coquettish:` · ![卖萌](pets/druid-rust/cute.svg) `:druid-rust-cute:` · ![讨好](pets/druid-rust/pleasing.svg) `:druid-rust-pleasing:` · ![敲打](pets/druid-rust/knocking.svg) `:druid-rust-knocking:` · ![捂脸](pets/druid-rust/facepalm.svg) `:druid-rust-facepalm:` · ![吐舌头](pets/druid-rust/tongue.svg) `:druid-rust-tongue:`

### Locky · `bag/encryption-rust` · `:encryption-rust-*:`

![笑](pets/encryption-rust/smile.svg) `:encryption-rust-smile:` · ![欢乐](pets/encryption-rust/joy.svg) `:encryption-rust-joy:` · ![哭](pets/encryption-rust/cry.svg) `:encryption-rust-cry:` · ![沮丧](pets/encryption-rust/depressed.svg) `:encryption-rust-depressed:` · ![惊恐](pets/encryption-rust/terrified.svg) `:encryption-rust-terrified:` · ![愤怒](pets/encryption-rust/angry.svg) `:encryption-rust-angry:`

![撒娇](pets/encryption-rust/coquettish.svg) `:encryption-rust-coquettish:` · ![卖萌](pets/encryption-rust/cute.svg) `:encryption-rust-cute:` · ![讨好](pets/encryption-rust/pleasing.svg) `:encryption-rust-pleasing:` · ![敲打](pets/encryption-rust/knocking.svg) `:encryption-rust-knocking:` · ![捂脸](pets/encryption-rust/facepalm.svg) `:encryption-rust-facepalm:` · ![吐舌头](pets/encryption-rust/tongue.svg) `:encryption-rust-tongue:`

### 小侦 Scouty · `bag/go-scout` · `:go-scout-*:`

![笑](pets/go-scout/smile.svg) `:go-scout-smile:` · ![欢乐](pets/go-scout/joy.svg) `:go-scout-joy:` · ![哭](pets/go-scout/cry.svg) `:go-scout-cry:` · ![沮丧](pets/go-scout/depressed.svg) `:go-scout-depressed:` · ![惊恐](pets/go-scout/terrified.svg) `:go-scout-terrified:` · ![愤怒](pets/go-scout/angry.svg) `:go-scout-angry:`

![撒娇](pets/go-scout/coquettish.svg) `:go-scout-coquettish:` · ![卖萌](pets/go-scout/cute.svg) `:go-scout-cute:` · ![讨好](pets/go-scout/pleasing.svg) `:go-scout-pleasing:` · ![敲打](pets/go-scout/knocking.svg) `:go-scout-knocking:` · ![捂脸](pets/go-scout/facepalm.svg) `:go-scout-facepalm:` · ![吐舌头](pets/go-scout/tongue.svg) `:go-scout-tongue:`

### Kee · 橘猫 · `bag/jwt-rust` · `:jwt-rust-*:`

![笑](pets/jwt-rust/smile.svg) `:jwt-rust-smile:` · ![欢乐](pets/jwt-rust/joy.svg) `:jwt-rust-joy:` · ![哭](pets/jwt-rust/cry.svg) `:jwt-rust-cry:` · ![沮丧](pets/jwt-rust/depressed.svg) `:jwt-rust-depressed:` · ![惊恐](pets/jwt-rust/terrified.svg) `:jwt-rust-terrified:` · ![愤怒](pets/jwt-rust/angry.svg) `:jwt-rust-angry:`

![撒娇](pets/jwt-rust/coquettish.svg) `:jwt-rust-coquettish:` · ![卖萌](pets/jwt-rust/cute.svg) `:jwt-rust-cute:` · ![讨好](pets/jwt-rust/pleasing.svg) `:jwt-rust-pleasing:` · ![敲打](pets/jwt-rust/knocking.svg) `:jwt-rust-knocking:` · ![捂脸](pets/jwt-rust/facepalm.svg) `:jwt-rust-facepalm:` · ![吐舌头](pets/jwt-rust/tongue.svg) `:jwt-rust-tongue:`

### Posty · `bag/poster-rust` · `:poster-rust-*:`

![笑](pets/poster-rust/smile.svg) `:poster-rust-smile:` · ![欢乐](pets/poster-rust/joy.svg) `:poster-rust-joy:` · ![哭](pets/poster-rust/cry.svg) `:poster-rust-cry:` · ![沮丧](pets/poster-rust/depressed.svg) `:poster-rust-depressed:` · ![惊恐](pets/poster-rust/terrified.svg) `:poster-rust-terrified:` · ![愤怒](pets/poster-rust/angry.svg) `:poster-rust-angry:`

![撒娇](pets/poster-rust/coquettish.svg) `:poster-rust-coquettish:` · ![卖萌](pets/poster-rust/cute.svg) `:poster-rust-cute:` · ![讨好](pets/poster-rust/pleasing.svg) `:poster-rust-pleasing:` · ![敲打](pets/poster-rust/knocking.svg) `:poster-rust-knocking:` · ![捂脸](pets/poster-rust/facepalm.svg) `:poster-rust-facepalm:` · ![吐舌头](pets/poster-rust/tongue.svg) `:poster-rust-tongue:`

### Scout · `bag/rust-scout` · `:rust-scout-*:`

![笑](pets/rust-scout/smile.svg) `:rust-scout-smile:` · ![欢乐](pets/rust-scout/joy.svg) `:rust-scout-joy:` · ![哭](pets/rust-scout/cry.svg) `:rust-scout-cry:` · ![沮丧](pets/rust-scout/depressed.svg) `:rust-scout-depressed:` · ![惊恐](pets/rust-scout/terrified.svg) `:rust-scout-terrified:` · ![愤怒](pets/rust-scout/angry.svg) `:rust-scout-angry:`

![撒娇](pets/rust-scout/coquettish.svg) `:rust-scout-coquettish:` · ![卖萌](pets/rust-scout/cute.svg) `:rust-scout-cute:` · ![讨好](pets/rust-scout/pleasing.svg) `:rust-scout-pleasing:` · ![敲打](pets/rust-scout/knocking.svg) `:rust-scout-knocking:` · ![捂脸](pets/rust-scout/facepalm.svg) `:rust-scout-facepalm:` · ![吐舌头](pets/rust-scout/tongue.svg) `:rust-scout-tongue:`

### 哨兵鼠 · `bag/security-go` · `:security-go-*:`

![笑](pets/security-go/smile.svg) `:security-go-smile:` · ![欢乐](pets/security-go/joy.svg) `:security-go-joy:` · ![哭](pets/security-go/cry.svg) `:security-go-cry:` · ![沮丧](pets/security-go/depressed.svg) `:security-go-depressed:` · ![惊恐](pets/security-go/terrified.svg) `:security-go-terrified:` · ![愤怒](pets/security-go/angry.svg) `:security-go-angry:`

![撒娇](pets/security-go/coquettish.svg) `:security-go-coquettish:` · ![卖萌](pets/security-go/cute.svg) `:security-go-cute:` · ![讨好](pets/security-go/pleasing.svg) `:security-go-pleasing:` · ![敲打](pets/security-go/knocking.svg) `:security-go-knocking:` · ![捂脸](pets/security-go/facepalm.svg) `:security-go-facepalm:` · ![吐舌头](pets/security-go/tongue.svg) `:security-go-tongue:`

### 甲哨 Sentri · `bag/security-rust` · `:security-rust-*:`

![笑](pets/security-rust/smile.svg) `:security-rust-smile:` · ![欢乐](pets/security-rust/joy.svg) `:security-rust-joy:` · ![哭](pets/security-rust/cry.svg) `:security-rust-cry:` · ![沮丧](pets/security-rust/depressed.svg) `:security-rust-depressed:` · ![惊恐](pets/security-rust/terrified.svg) `:security-rust-terrified:` · ![愤怒](pets/security-rust/angry.svg) `:security-rust-angry:`

![撒娇](pets/security-rust/coquettish.svg) `:security-rust-coquettish:` · ![卖萌](pets/security-rust/cute.svg) `:security-rust-cute:` · ![讨好](pets/security-rust/pleasing.svg) `:security-rust-pleasing:` · ![敲打](pets/security-rust/knocking.svg) `:security-rust-knocking:` · ![捂脸](pets/security-rust/facepalm.svg) `:security-rust-facepalm:` · ![吐舌头](pets/security-rust/tongue.svg) `:security-rust-tongue:`

### 以太兽 · `erikwang2013/aetherupload-webman` · `:aetherupload-webman-*:`

![笑](pets/aetherupload-webman/smile.svg) `:aetherupload-webman-smile:` · ![欢乐](pets/aetherupload-webman/joy.svg) `:aetherupload-webman-joy:` · ![哭](pets/aetherupload-webman/cry.svg) `:aetherupload-webman-cry:` · ![沮丧](pets/aetherupload-webman/depressed.svg) `:aetherupload-webman-depressed:` · ![惊恐](pets/aetherupload-webman/terrified.svg) `:aetherupload-webman-terrified:` · ![愤怒](pets/aetherupload-webman/angry.svg) `:aetherupload-webman-angry:`

![撒娇](pets/aetherupload-webman/coquettish.svg) `:aetherupload-webman-coquettish:` · ![卖萌](pets/aetherupload-webman/cute.svg) `:aetherupload-webman-cute:` · ![讨好](pets/aetherupload-webman/pleasing.svg) `:aetherupload-webman-pleasing:` · ![敲打](pets/aetherupload-webman/knocking.svg) `:aetherupload-webman-knocking:` · ![捂脸](pets/aetherupload-webman/facepalm.svg) `:aetherupload-webman-facepalm:` · ![吐舌头](pets/aetherupload-webman/tongue.svg) `:aetherupload-webman-tongue:`

### Apidoc · `erikwang2013/apidoc-php` · `:apidoc-php-*:`

![笑](pets/apidoc-php/smile.svg) `:apidoc-php-smile:` · ![欢乐](pets/apidoc-php/joy.svg) `:apidoc-php-joy:` · ![哭](pets/apidoc-php/cry.svg) `:apidoc-php-cry:` · ![沮丧](pets/apidoc-php/depressed.svg) `:apidoc-php-depressed:` · ![惊恐](pets/apidoc-php/terrified.svg) `:apidoc-php-terrified:` · ![愤怒](pets/apidoc-php/angry.svg) `:apidoc-php-angry:`

![撒娇](pets/apidoc-php/coquettish.svg) `:apidoc-php-coquettish:` · ![卖萌](pets/apidoc-php/cute.svg) `:apidoc-php-cute:` · ![讨好](pets/apidoc-php/pleasing.svg) `:apidoc-php-pleasing:` · ![敲打](pets/apidoc-php/knocking.svg) `:apidoc-php-knocking:` · ![捂脸](pets/apidoc-php/facepalm.svg) `:apidoc-php-facepalm:` · ![吐舌头](pets/apidoc-php/tongue.svg) `:apidoc-php-tongue:`

### ClickHouse 仓鼠 · `erikwang2013/clickhouse-php` · `:clickhouse-php-*:`

![笑](pets/clickhouse-php/smile.svg) `:clickhouse-php-smile:` · ![欢乐](pets/clickhouse-php/joy.svg) `:clickhouse-php-joy:` · ![哭](pets/clickhouse-php/cry.svg) `:clickhouse-php-cry:` · ![沮丧](pets/clickhouse-php/depressed.svg) `:clickhouse-php-depressed:` · ![惊恐](pets/clickhouse-php/terrified.svg) `:clickhouse-php-terrified:` · ![愤怒](pets/clickhouse-php/angry.svg) `:clickhouse-php-angry:`

![撒娇](pets/clickhouse-php/coquettish.svg) `:clickhouse-php-coquettish:` · ![卖萌](pets/clickhouse-php/cute.svg) `:clickhouse-php-cute:` · ![讨好](pets/clickhouse-php/pleasing.svg) `:clickhouse-php-pleasing:` · ![敲打](pets/clickhouse-php/knocking.svg) `:clickhouse-php-knocking:` · ![捂脸](pets/clickhouse-php/facepalm.svg) `:clickhouse-php-facepalm:` · ![吐舌头](pets/clickhouse-php/tongue.svg) `:clickhouse-php-tongue:`

### Consu · `erikwang2013/consul-php` · `:consul-php-*:`

![笑](pets/consul-php/smile.svg) `:consul-php-smile:` · ![欢乐](pets/consul-php/joy.svg) `:consul-php-joy:` · ![哭](pets/consul-php/cry.svg) `:consul-php-cry:` · ![沮丧](pets/consul-php/depressed.svg) `:consul-php-depressed:` · ![惊恐](pets/consul-php/terrified.svg) `:consul-php-terrified:` · ![愤怒](pets/consul-php/angry.svg) `:consul-php-angry:`

![撒娇](pets/consul-php/coquettish.svg) `:consul-php-coquettish:` · ![卖萌](pets/consul-php/cute.svg) `:consul-php-cute:` · ![讨好](pets/consul-php/pleasing.svg) `:consul-php-pleasing:` · ![敲打](pets/consul-php/knocking.svg) `:consul-php-knocking:` · ![捂脸](pets/consul-php/facepalm.svg) `:consul-php-facepalm:` · ![吐舌头](pets/consul-php/tongue.svg) `:consul-php-tongue:`

### Locky · `erikwang2013/encryptable` · `:encryptable-*:`

![笑](pets/encryptable/smile.svg) `:encryptable-smile:` · ![欢乐](pets/encryptable/joy.svg) `:encryptable-joy:` · ![哭](pets/encryptable/cry.svg) `:encryptable-cry:` · ![沮丧](pets/encryptable/depressed.svg) `:encryptable-depressed:` · ![惊恐](pets/encryptable/terrified.svg) `:encryptable-terrified:` · ![愤怒](pets/encryptable/angry.svg) `:encryptable-angry:`

![撒娇](pets/encryptable/coquettish.svg) `:encryptable-coquettish:` · ![卖萌](pets/encryptable/cute.svg) `:encryptable-cute:` · ![讨好](pets/encryptable/pleasing.svg) `:encryptable-pleasing:` · ![敲打](pets/encryptable/knocking.svg) `:encryptable-knocking:` · ![捂脸](pets/encryptable/facepalm.svg) `:encryptable-facepalm:` · ![吐舌头](pets/encryptable/tongue.svg) `:encryptable-tongue:`

### Locky · `erikwang2013/encryption` · `:encryption-*:`

![笑](pets/encryption/smile.svg) `:encryption-smile:` · ![欢乐](pets/encryption/joy.svg) `:encryption-joy:` · ![哭](pets/encryption/cry.svg) `:encryption-cry:` · ![沮丧](pets/encryption/depressed.svg) `:encryption-depressed:` · ![惊恐](pets/encryption/terrified.svg) `:encryption-terrified:` · ![愤怒](pets/encryption/angry.svg) `:encryption-angry:`

![撒娇](pets/encryption/coquettish.svg) `:encryption-coquettish:` · ![卖萌](pets/encryption/cute.svg) `:encryption-cute:` · ![讨好](pets/encryption/pleasing.svg) `:encryption-pleasing:` · ![敲打](pets/encryption/knocking.svg) `:encryption-knocking:` · ![捂脸](pets/encryption/facepalm.svg) `:encryption-facepalm:` · ![吐舌头](pets/encryption/tongue.svg) `:encryption-tongue:`

### Etchy · `erikwang2013/etcd` · `:etcd-*:`

![笑](pets/etcd/smile.svg) `:etcd-smile:` · ![欢乐](pets/etcd/joy.svg) `:etcd-joy:` · ![哭](pets/etcd/cry.svg) `:etcd-cry:` · ![沮丧](pets/etcd/depressed.svg) `:etcd-depressed:` · ![惊恐](pets/etcd/terrified.svg) `:etcd-terrified:` · ![愤怒](pets/etcd/angry.svg) `:etcd-angry:`

![撒娇](pets/etcd/coquettish.svg) `:etcd-coquettish:` · ![卖萌](pets/etcd/cute.svg) `:etcd-cute:` · ![讨好](pets/etcd/pleasing.svg) `:etcd-pleasing:` · ![敲打](pets/etcd/knocking.svg) `:etcd-knocking:` · ![捂脸](pets/etcd/facepalm.svg) `:etcd-facepalm:` · ![吐舌头](pets/etcd/tongue.svg) `:etcd-tongue:`

### 哈希迪 Hashy · `erikwang2013/hashids` · `:hashids-*:`

![笑](pets/hashids/smile.svg) `:hashids-smile:` · ![欢乐](pets/hashids/joy.svg) `:hashids-joy:` · ![哭](pets/hashids/cry.svg) `:hashids-cry:` · ![沮丧](pets/hashids/depressed.svg) `:hashids-depressed:` · ![惊恐](pets/hashids/terrified.svg) `:hashids-terrified:` · ![愤怒](pets/hashids/angry.svg) `:hashids-angry:`

![撒娇](pets/hashids/coquettish.svg) `:hashids-coquettish:` · ![卖萌](pets/hashids/cute.svg) `:hashids-cute:` · ![讨好](pets/hashids/pleasing.svg) `:hashids-pleasing:` · ![敲打](pets/hashids/knocking.svg) `:hashids-knocking:` · ![捂脸](pets/hashids/facepalm.svg) `:hashids-facepalm:` · ![吐舌头](pets/hashids/tongue.svg) `:hashids-tongue:`

### Kee · 柴犬门卫 · `erikwang2013/jwt-webman` · `:jwt-webman-*:`

![笑](pets/jwt-webman/smile.svg) `:jwt-webman-smile:` · ![欢乐](pets/jwt-webman/joy.svg) `:jwt-webman-joy:` · ![哭](pets/jwt-webman/cry.svg) `:jwt-webman-cry:` · ![沮丧](pets/jwt-webman/depressed.svg) `:jwt-webman-depressed:` · ![惊恐](pets/jwt-webman/terrified.svg) `:jwt-webman-terrified:` · ![愤怒](pets/jwt-webman/angry.svg) `:jwt-webman-angry:`

![撒娇](pets/jwt-webman/coquettish.svg) `:jwt-webman-coquettish:` · ![卖萌](pets/jwt-webman/cute.svg) `:jwt-webman-cute:` · ![讨好](pets/jwt-webman/pleasing.svg) `:jwt-webman-pleasing:` · ![敲打](pets/jwt-webman/knocking.svg) `:jwt-webman-knocking:` · ![捂脸](pets/jwt-webman/facepalm.svg) `:jwt-webman-facepalm:` · ![吐舌头](pets/jwt-webman/tongue.svg) `:jwt-webman-tongue:`

### Posty · `erikwang2013/poster-php` · `:poster-php-*:`

![笑](pets/poster-php/smile.svg) `:poster-php-smile:` · ![欢乐](pets/poster-php/joy.svg) `:poster-php-joy:` · ![哭](pets/poster-php/cry.svg) `:poster-php-cry:` · ![沮丧](pets/poster-php/depressed.svg) `:poster-php-depressed:` · ![惊恐](pets/poster-php/terrified.svg) `:poster-php-terrified:` · ![愤怒](pets/poster-php/angry.svg) `:poster-php-angry:`

![撒娇](pets/poster-php/coquettish.svg) `:poster-php-coquettish:` · ![卖萌](pets/poster-php/cute.svg) `:poster-php-cute:` · ![讨好](pets/poster-php/pleasing.svg) `:poster-php-pleasing:` · ![敲打](pets/poster-php/knocking.svg) `:poster-php-knocking:` · ![捂脸](pets/poster-php/facepalm.svg) `:poster-php-facepalm:` · ![吐舌头](pets/poster-php/tongue.svg) `:poster-php-tongue:`

### Seasony 季灵 · `erikwang2013/season` · `:season-*:`

![笑](pets/season/smile.svg) `:season-smile:` · ![欢乐](pets/season/joy.svg) `:season-joy:` · ![哭](pets/season/cry.svg) `:season-cry:` · ![沮丧](pets/season/depressed.svg) `:season-depressed:` · ![惊恐](pets/season/terrified.svg) `:season-terrified:` · ![愤怒](pets/season/angry.svg) `:season-angry:`

![撒娇](pets/season/coquettish.svg) `:season-coquettish:` · ![卖萌](pets/season/cute.svg) `:season-cute:` · ![讨好](pets/season/pleasing.svg) `:season-pleasing:` · ![敲打](pets/season/knocking.svg) `:season-knocking:` · ![捂脸](pets/season/facepalm.svg) `:season-facepalm:` · ![吐舌头](pets/season/tongue.svg) `:season-tongue:`

### 小盾 · `erikwang2013/security-php` · `:security-php-*:`

![笑](pets/security-php/smile.svg) `:security-php-smile:` · ![欢乐](pets/security-php/joy.svg) `:security-php-joy:` · ![哭](pets/security-php/cry.svg) `:security-php-cry:` · ![沮丧](pets/security-php/depressed.svg) `:security-php-depressed:` · ![惊恐](pets/security-php/terrified.svg) `:security-php-terrified:` · ![愤怒](pets/security-php/angry.svg) `:security-php-angry:`

![撒娇](pets/security-php/coquettish.svg) `:security-php-coquettish:` · ![卖萌](pets/security-php/cute.svg) `:security-php-cute:` · ![讨好](pets/security-php/pleasing.svg) `:security-php-pleasing:` · ![敲打](pets/security-php/knocking.svg) `:security-php-knocking:` · ![捂脸](pets/security-php/facepalm.svg) `:security-php-facepalm:` · ![吐舌头](pets/security-php/tongue.svg) `:security-php-tongue:`

### 雪花精灵 · `erikwang2013/snowflake-php` · `:snowflake-php-*:`

![笑](pets/snowflake-php/smile.svg) `:snowflake-php-smile:` · ![欢乐](pets/snowflake-php/joy.svg) `:snowflake-php-joy:` · ![哭](pets/snowflake-php/cry.svg) `:snowflake-php-cry:` · ![沮丧](pets/snowflake-php/depressed.svg) `:snowflake-php-depressed:` · ![惊恐](pets/snowflake-php/terrified.svg) `:snowflake-php-terrified:` · ![愤怒](pets/snowflake-php/angry.svg) `:snowflake-php-angry:`

![撒娇](pets/snowflake-php/coquettish.svg) `:snowflake-php-coquettish:` · ![卖萌](pets/snowflake-php/cute.svg) `:snowflake-php-cute:` · ![讨好](pets/snowflake-php/pleasing.svg) `:snowflake-php-pleasing:` · ![敲打](pets/snowflake-php/knocking.svg) `:snowflake-php-knocking:` · ![捂脸](pets/snowflake-php/facepalm.svg) `:snowflake-php-facepalm:` · ![吐舌头](pets/snowflake-php/tongue.svg) `:snowflake-php-tongue:`

### Sniffy · `erikwang2013/webman-scout` · `:webman-scout-*:`

![笑](pets/webman-scout/smile.svg) `:webman-scout-smile:` · ![欢乐](pets/webman-scout/joy.svg) `:webman-scout-joy:` · ![哭](pets/webman-scout/cry.svg) `:webman-scout-cry:` · ![沮丧](pets/webman-scout/depressed.svg) `:webman-scout-depressed:` · ![惊恐](pets/webman-scout/terrified.svg) `:webman-scout-terrified:` · ![愤怒](pets/webman-scout/angry.svg) `:webman-scout-angry:`

![撒娇](pets/webman-scout/coquettish.svg) `:webman-scout-coquettish:` · ![卖萌](pets/webman-scout/cute.svg) `:webman-scout-cute:` · ![讨好](pets/webman-scout/pleasing.svg) `:webman-scout-pleasing:` · ![敲打](pets/webman-scout/knocking.svg) `:webman-scout-knocking:` · ![捂脸](pets/webman-scout/facepalm.svg) `:webman-scout-facepalm:` · ![吐舌头](pets/webman-scout/tongue.svg) `:webman-scout-tongue:`

### Xhpy · `erikwang2013/xhprof` · `:xhprof-*:`

![笑](pets/xhprof/smile.svg) `:xhprof-smile:` · ![欢乐](pets/xhprof/joy.svg) `:xhprof-joy:` · ![哭](pets/xhprof/cry.svg) `:xhprof-cry:` · ![沮丧](pets/xhprof/depressed.svg) `:xhprof-depressed:` · ![惊恐](pets/xhprof/terrified.svg) `:xhprof-terrified:` · ![愤怒](pets/xhprof/angry.svg) `:xhprof-angry:`

![撒娇](pets/xhprof/coquettish.svg) `:xhprof-coquettish:` · ![卖萌](pets/xhprof/cute.svg) `:xhprof-cute:` · ![讨好](pets/xhprof/pleasing.svg) `:xhprof-pleasing:` · ![敲打](pets/xhprof/knocking.svg) `:xhprof-knocking:` · ![捂脸](pets/xhprof/facepalm.svg) `:xhprof-facepalm:` · ![吐舌头](pets/xhprof/tongue.svg) `:xhprof-tongue:`

### 焰焰 · `erikwang2013/xhprof-webman` · `:xhprof-webman-*:`

![笑](pets/xhprof-webman/smile.svg) `:xhprof-webman-smile:` · ![欢乐](pets/xhprof-webman/joy.svg) `:xhprof-webman-joy:` · ![哭](pets/xhprof-webman/cry.svg) `:xhprof-webman-cry:` · ![沮丧](pets/xhprof-webman/depressed.svg) `:xhprof-webman-depressed:` · ![惊恐](pets/xhprof-webman/terrified.svg) `:xhprof-webman-terrified:` · ![愤怒](pets/xhprof-webman/angry.svg) `:xhprof-webman-angry:`

![撒娇](pets/xhprof-webman/coquettish.svg) `:xhprof-webman-coquettish:` · ![卖萌](pets/xhprof-webman/cute.svg) `:xhprof-webman-cute:` · ![讨好](pets/xhprof-webman/pleasing.svg) `:xhprof-webman-pleasing:` · ![敲打](pets/xhprof-webman/knocking.svg) `:xhprof-webman-knocking:` · ![捂脸](pets/xhprof-webman/facepalm.svg) `:xhprof-webman-facepalm:` · ![吐舌头](pets/xhprof-webman/tongue.svg) `:xhprof-webman-tongue:`

### 吞吞 · `oss` · `:oss-*:`

![笑](pets/oss/smile.svg) `:oss-smile:` · ![欢乐](pets/oss/joy.svg) `:oss-joy:` · ![哭](pets/oss/cry.svg) `:oss-cry:` · ![沮丧](pets/oss/depressed.svg) `:oss-depressed:` · ![惊恐](pets/oss/terrified.svg) `:oss-terrified:` · ![愤怒](pets/oss/angry.svg) `:oss-angry:`

![撒娇](pets/oss/coquettish.svg) `:oss-coquettish:` · ![卖萌](pets/oss/cute.svg) `:oss-cute:` · ![讨好](pets/oss/pleasing.svg) `:oss-pleasing:` · ![敲打](pets/oss/knocking.svg) `:oss-knocking:` · ![捂脸](pets/oss/facepalm.svg) `:oss-facepalm:` · ![吐舌头](pets/oss/tongue.svg) `:oss-tongue:`

### Pax · `polypack` · `:polypack-*:`

![笑](pets/polypack/smile.svg) `:polypack-smile:` · ![欢乐](pets/polypack/joy.svg) `:polypack-joy:` · ![哭](pets/polypack/cry.svg) `:polypack-cry:` · ![沮丧](pets/polypack/depressed.svg) `:polypack-depressed:` · ![惊恐](pets/polypack/terrified.svg) `:polypack-terrified:` · ![愤怒](pets/polypack/angry.svg) `:polypack-angry:`

![撒娇](pets/polypack/coquettish.svg) `:polypack-coquettish:` · ![卖萌](pets/polypack/cute.svg) `:polypack-cute:` · ![讨好](pets/polypack/pleasing.svg) `:polypack-pleasing:` · ![敲打](pets/polypack/knocking.svg) `:polypack-knocking:` · ![捂脸](pets/polypack/facepalm.svg) `:polypack-facepalm:` · ![吐舌头](pets/polypack/tongue.svg) `:polypack-tongue:`

### 小欧 · `opi` · `:opi-*:`

![笑](pets/opi/smile.svg) `:opi-smile:` · ![欢乐](pets/opi/joy.svg) `:opi-joy:` · ![哭](pets/opi/cry.svg) `:opi-cry:` · ![沮丧](pets/opi/depressed.svg) `:opi-depressed:` · ![惊恐](pets/opi/terrified.svg) `:opi-terrified:` · ![愤怒](pets/opi/angry.svg) `:opi-angry:`

![撒娇](pets/opi/coquettish.svg) `:opi-coquettish:` · ![卖萌](pets/opi/cute.svg) `:opi-cute:` · ![讨好](pets/opi/pleasing.svg) `:opi-pleasing:` · ![敲打](pets/opi/knocking.svg) `:opi-knocking:` · ![捂脸](pets/opi/facepalm.svg) `:opi-facepalm:` · ![吐舌头](pets/opi/tongue.svg) `:opi-tongue:`

## 说明

- 图片源文件在 `pets/<项目>/<形态>.svg`，PNG 在 `png/<项目>/<形态>.png`。
- `preview.png` 是所有项目「笑」形态的总览。
- 已去除与其他项目重复的 7 个宠物入口：`aetherupload-rust`、`apidoc-go`、`apidoc-rust`、`apidoc-ui`、`encryptable-rust`、`hashids-rust`、`snowflake-rust`；保留对应的 PHP / Webman 版本。`jwt-rust` 已改为独立橘猫形象，重新纳入。
- 本项目代码与生成脚本仍遵循其原有许可；视觉资产适用 [ASSETS-LICENSE.md](ASSETS-LICENSE.md)。
