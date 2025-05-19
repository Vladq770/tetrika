def merge_intervals(intervals: list[int]) -> list[tuple[int, int]]:
    """
    Схлопнуть пересекающиеся интервалы.

    Args:
        intervals: Интервалы, которые нужно обработать.

    Returns:
        Список обработанных интервалов, разбитых по парам.
    """
    pairs = list(zip(intervals[::2], intervals[1::2]))

    pairs.sort()

    merged = [pairs[0]]

    for current_start, current_end in pairs[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged


def appearance(intervals: dict[str, list[int]]) -> int:  # noqa
    """
    Вычислить общее время нахождения на уроке.

    Args:
        intervals: Словарь с интервалами, которые нужно обработать.

    Returns:
        Общее время.
    """
    lesson_start, lesson_end = intervals["lesson"]

    pupil_intervals = merge_intervals(intervals["pupil"])
    tutor_intervals = merge_intervals(intervals["tutor"])

    total_overlap = 0

    p_idx = 0
    t_idx = 0

    while p_idx < len(pupil_intervals) and t_idx < len(tutor_intervals):
        p_start, p_end = pupil_intervals[p_idx]
        t_start, t_end = tutor_intervals[t_idx]

        p_start = max(p_start, lesson_start)
        p_end = min(p_end, lesson_end)
        t_start = max(t_start, lesson_start)
        t_end = min(t_end, lesson_end)

        if p_end <= t_start:
            p_idx += 1
        elif t_end <= p_start:
            t_idx += 1
        else:
            overlap_start = max(p_start, t_start)
            overlap_end = min(p_end, t_end)
            if overlap_start < overlap_end:
                total_overlap += overlap_end - overlap_start

            if p_end < t_end:
                p_idx += 1
            else:
                t_idx += 1

    return total_overlap
