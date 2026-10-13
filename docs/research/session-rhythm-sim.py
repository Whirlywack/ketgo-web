"""Design calculation for docs/research/session-rhythm.md (issue #17).

What it does: simulates a KETGO Program with the FSRS-6 default parameters and counts how many
Questions a learner answers per day. It is a workload estimate, not evidence about learning.

Run:  pip install fsrs==6.3.2 && python session-rhythm-sim.py

Assumptions (design guesses, all to be replaced by KETGO data):
- 250 Rules, one FSRS card per Rule (real KETGO keeps memory per Question and rolls up per Rule).
- 8 new Rules per Lesson; the Program ends 2 days before the Theory Exam (those days are review only).
- First answer after the Rule Explainer is correct with probability 0.75.
- Later answers are correct with probability = FSRS retrievability at that moment.
- Correct -> Good, wrong -> Again. Desired retention 0.9. Learning steps 1 min and 10 min,
  so a new Rule is asked about 2-3 times on its first day.
- All of a day's Lessons happen in one evening sitting (18:00). Reviews are never shown after the exam.
"""
import math
import random
import statistics
from datetime import datetime, timedelta, timezone

from fsrs import Card, Rating, Scheduler

N_RULES = 250
PER_LESSON = 8
TAIL_DAYS = 2
P_FIRST = 0.75
SEEDS = range(4)


def simulate(new_per_day, days, seed, sweep=False, stats=None):
    """new_per_day[d] = new Rules introduced on day d. Returns (new answers/day, review answers/day, mean exam-day R).

    sweep=True: on the last day, also ask every Rule whose predicted exam-day recall is below 0.9 once.
    stats (dict): filled with the share of Rules at R >= 0.9 on exam day.
    """
    rng = random.Random(seed)
    sch = Scheduler(desired_retention=0.9)
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    exam = start + timedelta(days=days, hours=9)
    cards, born, seen = [], [], set()
    new_ans, rev_ans = [], []
    for d in range(days):
        now = start + timedelta(days=d, hours=18)
        for _ in range(new_per_day[d] if d < len(new_per_day) else 0):
            cards.append(Card(card_id=len(cards) + 1, due=now))
            born.append(d)
        n_new = n_rev = 0
        swept = set()
        while True:
            due = [i for i, c in enumerate(cards) if c.due <= now]
            if sweep and d == days - 1 and not due:
                due = [i for i, c in enumerate(cards) if i not in swept
                       and sch.get_card_retrievability(c, exam) < 0.9]
                swept.update(due[:1])
            if not due:
                later = [c.due for c in cards if now < c.due <= now + timedelta(minutes=15)]
                if not later:
                    break
                now = min(later)
                continue
            i = due[0]
            p = P_FIRST if i not in seen else sch.get_card_retrievability(cards[i], now)
            seen.add(i)
            rating = Rating.Good if rng.random() < p else Rating.Again
            cards[i], _ = sch.review_card(cards[i], rating, now)
            if born[i] == d:
                n_new += 1
            else:
                n_rev += 1
            now += timedelta(seconds=30)
        new_ans.append(n_new)
        rev_ans.append(n_rev)
    rs = [sch.get_card_retrievability(c, exam) for c in cards]
    if stats is not None:
        stats["share_r90"] = sum(r >= 0.9 for r in rs) / len(rs)
    return new_ans, rev_ans, statistics.mean(rs)


def averaged(new_per_day, days):
    runs = [simulate(new_per_day, days, s) for s in SEEDS]
    new = [statistics.mean(r[0][d] for r in runs) for d in range(days)]
    rev = [statistics.mean(r[1][d] for r in runs) for d in range(days)]
    return new, rev, statistics.mean(r[2] for r in runs)


def lessons_per_day_table():
    n_lessons = math.ceil(N_RULES / PER_LESSON)
    print(f"A. {N_RULES} Rules, {PER_LESSON} new Rules per Lesson = {n_lessons} Lessons, then {TAIL_DAYS} review-only days")
    print("Lessons/day | days to exam | answers/day mean | peak | share of answers on new Rules (1st/2nd/3rd third of Program) | exam-day R")
    for per_day in (1, 2, 3, 4):
        prog_days = math.ceil(n_lessons / per_day)
        days = prog_days + TAIL_DAYS
        plan, left = [], N_RULES
        for _ in range(prog_days):
            plan.append(min(PER_LESSON * per_day, left))
            left -= plan[-1]
        new, rev, r = averaged(plan, days)
        tot = [a + b for a, b in zip(new, rev)]
        thirds = [slice(0, days // 3), slice(days // 3, 2 * days // 3), slice(2 * days // 3, days)]
        share = [round(sum(new[s]) / sum(tot[s]), 2) for s in thirds]
        print(f"{per_day} | {days} | {round(statistics.mean(tot))} | {round(max(tot))} | {share} | {round(r, 3)}")


def day_one_binge_table():
    days = 30
    print(f"\nB. Day-one binge, exam in {days} days, {N_RULES} Rules, new Rules end {TAIL_DAYS} days before the exam")
    print("new Rules on day 1 | answers on days 1-7 | peak | total answers | exam-day R")
    for d1 in (8, 40, 80, 150):
        rest_days = days - 1 - TAIL_DAYS
        rest = [(N_RULES - d1) // rest_days + (1 if i < (N_RULES - d1) % rest_days else 0) for i in range(rest_days)]
        new, rev, r = averaged([d1] + rest, days)
        tot = [a + b for a, b in zip(new, rev)]
        print(f"{d1} | {[round(x) for x in tot[:7]]} | {round(max(tot))} | {round(sum(tot))} | {round(r, 3)}")


def final_sweep_table():
    n_lessons = math.ceil(N_RULES / PER_LESSON)
    print("\nC. Last-day sweep: ask once more every Rule predicted below 90 % recall on exam day")
    print("Lessons/day | sweep | answers on last day | share of Rules at >= 90 % predicted recall on exam day")
    for per_day in (1, 2):
        prog_days = math.ceil(n_lessons / per_day)
        days = prog_days + TAIL_DAYS
        plan, left = [], N_RULES
        for _ in range(prog_days):
            plan.append(min(PER_LESSON * per_day, left))
            left -= plan[-1]
        for sweep in (False, True):
            last, share = [], []
            for s in SEEDS:
                st = {}
                new, rev, _ = simulate(plan, days, s, sweep=sweep, stats=st)
                last.append(new[-1] + rev[-1])
                share.append(st["share_r90"])
            print(f"{per_day} | {sweep} | {round(statistics.mean(last))} | {round(statistics.mean(share), 2)}")


if __name__ == "__main__":
    lessons_per_day_table()
    day_one_binge_table()
    final_sweep_table()
