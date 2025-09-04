# 7-simulation: 시뮬레이션 모음

쉽게 이해할 수 있도록 간단한 규칙과 예시를 정리했습니다.

## 포함 알고리즘/유틸

- 방향/이동 유틸 (`directions.py`)
  - `DIRS_4`, `DIRS_8`: 4/8방향 벡터
  - `move(pos, dir_idx, dirs)`: 한 칸 이동
- 격자 명령 시뮬레이터 (`grid_sim.py`)
  - `simulate_grid_commands(n, m, start, commands)`
  - 명령: L(좌회전), R(우회전), F(전진), 격자 밖은 무시
- 게임 오브 라이프 (`game_of_life.py`)
  - `next_state(board)`: 다음 세대 보드 계산
- 이벤트 시뮬레이터 (`event_sim.py`)
  - `EventSimulator`: `schedule(time, callback)`, `run()`
- 몬테카를로 (`monte_carlo.py`)
  - `estimate_pi(num_samples)`: PI 추정

## 간단 예시

```python
from grid_sim import simulate_grid_commands
pos, dir_idx = simulate_grid_commands(5, 5, (2, 2), "FFRFFLFF")
print(pos, dir_idx)
```

```python
from game_of_life import next_state
board = [
  [0,1,0],
  [0,1,0],
  [0,1,0],
]
print(next_state(board))
```

```python
from event_sim import EventSimulator
sim = EventSimulator()
sim.schedule(5, lambda s: print("Hello at", s.time))
sim.schedule(1, lambda s: print("Start at", s.time))
sim.run()
```

```python
from monte_carlo import estimate_pi
print(estimate_pi(50000))
```

