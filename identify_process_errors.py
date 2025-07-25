import pandas as pd

# Define the correct process order
CORRECT_ORDER = ['start', 'step_1', 'step_2', 'step_3', 'confirm']
STEP_RANKS = {step: idx for idx, step in enumerate(CORRECT_ORDER)}

def identify_process_errors(df):
    """
    Identifies errors in the process flow for each visit_id:
    1. Consecutive duplicate steps
    2. Out-of-sequence steps
    3. Invalid steps
    4. Premature reset to 'start' without 'confirm'
    5. Proper sequence validation
    """
    df = df.copy()
    df['date_time'] = pd.to_datetime(df['date_time'])
    df_sorted = df.sort_values(['visit_id', 'date_time'])
    df_sorted['error'] = False

    for (visit_id,), group in df_sorted.groupby(['visit_id']):
        previous_step = None
        current_rank = -1
        reached_confirm = False

        for idx, row in group.iterrows():
            step = row['process_step']

            # Case 1: Consecutive duplicate step
            if step == previous_step:
                df_sorted.at[idx, 'error'] = True
                continue

            # Case 2: Premature reset to start
            if step == 'start' and previous_step not in [None, 'confirm']:
                df_sorted.at[idx, 'error'] = True
                current_rank = 0
                previous_step = 'start'
                continue

            # Case 3: Valid start after confirm/None
            if step == 'start':
                current_rank = 0
                reached_confirm = False
                previous_step = 'start'
                continue

            # Case 4: Invalid step
            if step not in STEP_RANKS:
                df_sorted.at[idx, 'error'] = True
                previous_step = step
                continue

            step_rank = STEP_RANKS[step]

            # Case 5: Out of sequence
            if step_rank < current_rank:
                df_sorted.at[idx, 'error'] = True
            else:
                current_rank = step_rank
                if step == 'confirm':
                    reached_confirm = True

            previous_step = step

    return df_sorted.sort_index()