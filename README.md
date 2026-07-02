# 📋 外贸开发 Skill — 客户背调报告生成器

**把海外客户背景调查变成一份专业的 HTML 报告**

输入客户公司名或域名，AI 自动执行 4 阶段深度背调，输出一份与高端 B2B 商务 UI 风格一致的 HTML 客户背调报告。

---

## 核心功能

### 🕵️ Phase 1 — 全景画像
公司基础档案 + 决策人挖掘（7大数据源）+ 中国办事处深挖 + 初版开发信

### 📡 Phase 2 — 渠道动态
销售渠道布局（ DTC / Amazon / eBay / B2B / Showroom）+ 参展记录 + 品牌类目 + 高管动态

### ⚔️ Phase 3 — 竞争环境
主要竞争对手分析 + 供应链结构与中国参与度 + 市场合规要求（CE / UL / SASO / REACH 等）

### 📧 Phase 4 — 开发信输出
2 封个性化开发信（Value-Based + Product-Match）+ 决策人联系表 + LinkedIn 触达话术 + 跟进节奏建议

---

## 特点

- ✅ **不依赖 LLM API 调用费用** — AI 自主执行调查，调用 WebSearch / WebFetch 等工具
- ✅ **每条信息标注来源 URL** — 可追溯可验证，拒绝编造
- ✅ **区分"已证实"与"预测/推断"** — 邮箱等信息标注 Actual / Predicted 状态
- ✅ **输出独立 HTML 文件** — 直接在浏览器打开，可分发给团队
- ✅ **高端 B2B 商务视觉风格** — 象牙白 + 墨绿 + 古铜金配色

---

## 适用场景

- 开发新海外客户前的基础背调
- 准备开发信前的客户痛点分析
- 生成可发送给团队的正式 B2B 背调报告
- 摸清目标客户的渠道布局与竞争环境

---

## 文件结构

```
foreign-trade-dev-skill/
├── SKILL.md       # Skill 定义文件
├── template.html  # HTML 报告模板
└── README.md      # 本文件
```

---

## 使用前提

本 skill 需要配合 AI Agent（如 Claude Code）使用，AI 通过 WebSearch / WebFetch 等工具自主执行调查，无需调用额外 LLM API。

---

## 触发方式

当用户出现以下意图时自动激活：
- "帮我背调这家公司" / "调查一下 leds24.com"
- "我要开发德国客户" / "给我写封开发信"
- "分析一下这个海外买家" / "这个公司有什么痛点"
- 提供公司名或 URL 并要求"深挖"、"背调"、"开发"

---

## 与 GCCS Trade Hunter 的区别

| 特性 | 本 Skill | GCCS Trade Hunter |
|------|----------|-------------------|
| 输出形式 | 独立 HTML 文件 | 独立 UI 应用 |
| LLM 调用 | 不依赖 | 需要 |
| 侧边栏 | 本厂画像卡片 | 交互式导航 |
| 交付物 | 可分发报告 | Web 应用 |

---

**GitHub**: https://github.com/hongjunte/foreign-trade-dev-skill