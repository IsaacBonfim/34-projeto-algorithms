def study_schedule(permanence_period, target_time):
    count_student = 0

    try:
        for entry, exit in permanence_period:
            if (target_time >= entry and target_time <= exit):
                count_student += 1
    except TypeError:
        return None

    return count_student
