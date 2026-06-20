# Data Model: 快艇骰子遊戲

## Entities

### Die（骰子）

```js
{
  value: number,   // 1–6，擲骰前為 null
  held: boolean    // true = 鎖定不重擲
}
```

**Validation**: `value` 必須是 1–6 的整數；`held` 只在至少擲過一次後才有意義。

---

### ScoringCategory（計分類別）

| id | 中文名稱 | 英文名稱 | 區域 | 計分規則 |
|----|---------|---------|------|---------|
| `ones` | 一點 | Aces | 上區 | 所有顯示 1 的骰子點數之和 |
| `twos` | 二點 | Twos | 上區 | 所有顯示 2 的骰子點數之和 |
| `threes` | 三點 | Threes | 上區 | 所有顯示 3 的骰子點數之和 |
| `fours` | 四點 | Fours | 上區 | 所有顯示 4 的骰子點數之和 |
| `fives` | 五點 | Fives | 上區 | 所有顯示 5 的骰子點數之和 |
| `sixes` | 六點 | Sixes | 上區 | 所有顯示 6 的骰子點數之和 |
| `threeOfAKind` | 三同 | Three of a Kind | 下區 | 若有 ≥3 個相同骰子 → 所有骰子之和；否則 0 |
| `fourOfAKind` | 四同 | Four of a Kind | 下區 | 若有 ≥4 個相同骰子 → 所有骰子之和；否則 0 |
| `fullHouse` | 葫蘆 | Full House | 下區 | 若有 3 個一樣 + 2 個一樣 → 25 分；否則 0 |
| `smallStraight` | 小順 | Small Straight | 下區 | 若有 4 個連續點數 → 30 分；否則 0 |
| `largeStraight` | 大順 | Large Straight | 下區 | 若有 5 個連續點數 → 40 分；否則 0 |
| `yacht` | 快艇 | Yacht | 下區 | 若 5 個骰子全同 → 50 分；否則 0 |
| `chance` | 機會 | Chance | 下區 | 所有骰子點數之和（無條件） |

**上區獎勵**: 上區 6 類合計 ≥ 63 → 自動加 35 分（顯示於計分板，不佔類別欄位）。

---

### Scorecard（計分板）

```js
{
  ones: null | number,
  twos: null | number,
  threes: null | number,
  fours: null | number,
  fives: null | number,
  sixes: null | number,
  threeOfAKind: null | number,
  fourOfAKind: null | number,
  fullHouse: null | number,
  smallStraight: null | number,
  largeStraight: null | number,
  yacht: null | number,
  chance: null | number
}
```

**State transitions**: `null` → `number`（不可逆；一旦填入不能修改）。

**Computed fields**（不存入狀態，每次 render 動態計算）:

- `upperSubtotal` = ones + twos + threes + fours + fives + sixes（已填入者）
- `upperBonus` = upperSubtotal ≥ 63 ? 35 : 0（僅在上區全部填完後顯示為確定值；進行中顯示進度）
- `lowerSubtotal` = threeOfAKind + fourOfAKind + fullHouse + smallStraight + largeStraight + yacht + chance
- `grandTotal` = upperSubtotal + upperBonus + lowerSubtotal

---

### Player（玩家）

```js
{
  name: string,      // '玩家一' | '玩家二' | 'CPU'
  scorecard: Scorecard,
  isCpu: boolean
}
```

---

### GameState（全局狀態）

```js
{
  phase: 'menu' | 'playing' | 'gameover',
  mode: '1p' | '2p',          // 選擇模式後設定
  players: Player[],           // length = 2
  currentPlayerIndex: 0 | 1,
  round: number,               // 1–13
  dice: Die[],                 // length = 5
  rollsLeft: number,           // 3 = 尚未擲骰, 2 = 擲過1次, 1 = 擲過2次, 0 = 擲過3次
  rollPhase: boolean           // true = 已擲過至少一次（可鎖骰子、可選分類）
}
```

**State transitions**:

```
menu → playing  (玩家選擇模式)
playing → playing  (每回合選完分類 → 換玩家 or 換回合)
playing → gameover  (round 13 最後一位玩家選完分類)
gameover → menu  (點「再玩一次」)
```

---

## Scoring Functions（偽碼）

```js
function score(categoryId, dice):
  values = dice.map(d => d.value)
  counts = tally(values)   // {1: n, 2: n, ...}

  switch categoryId:
    case 'ones'...'sixes':
      faceValue = 1..6
      return sum(values.filter(v => v === faceValue))

    case 'threeOfAKind':
      return max(counts.values()) >= 3 ? sum(values) : 0

    case 'fourOfAKind':
      return max(counts.values()) >= 4 ? sum(values) : 0

    case 'fullHouse':
      return (counts has entry 3) && (counts has entry 2) ? 25 : 0

    case 'smallStraight':
      unique_sorted = sorted(unique(values))
      return hasConsecutiveRun(unique_sorted, 4) ? 30 : 0

    case 'largeStraight':
      unique_sorted = sorted(unique(values))
      return unique_sorted.length === 5 && hasConsecutiveRun(unique_sorted, 5) ? 40 : 0

    case 'yacht':
      return max(counts.values()) === 5 ? 50 : 0

    case 'chance':
      return sum(values)
```

---

## CPU Strategy（Greedy）

```
cpuTurn():
  for reroll in [1, 2]:  // 最多再擲 2 次
    delay(400ms)
    bestCategory = argmax over available categories of score(cat, currentDice)
    targetDice = selectDiceToHold(bestCategory, currentDice)
    hold those dice, reroll rest
  delay(400ms)
  selectCategory(argmax over available categories of score(cat, currentDice))
```

`selectDiceToHold(category, dice)` 邏輯：
- 上區類別：保留對應面值的骰子
- threeOfAKind / fourOfAKind：保留出現最多的那個面值
- fullHouse：保留出現 ≥2 的面值
- straight：保留已形成連續段的骰子
- yacht：保留出現最多的面值
- chance：保留所有 ≥4 點的骰子
